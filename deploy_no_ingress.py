#!/usr/bin/env python3
import os
import toml
import subprocess
import yaml
import random

BASE_DIR = "./challenges"
K8S_DEPLOYMENTS_DIR = "./k8s_deployments"

USE_DOCKER_HUB = False 
DOCKER_HUB_USERNAME = "your_dockerhub_username"

BLOCKED_CHALLENGES = ["lion"]
PORT_MAPPING_FILE = "port_mapping.yaml" 


os.makedirs(K8S_DEPLOYMENTS_DIR, exist_ok=True)


def load_port_mapping(file_path=PORT_MAPPING_FILE):
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            data = yaml.safe_load(f)
        return data.get("mapping", {})
    else:
        print(f"[WARN] Port mapping file {file_path} not found. No mappings will be used.")
        return {}

PORT_MAPPING = load_port_mapping()

def find_challenges(base_dir):

    challenges = []
    for root, _, files in os.walk(base_dir):
        if "chall.toml" in files:
            if any(blocked in root.lower() for blocked in BLOCKED_CHALLENGES):
                print(f"[SKIP] Blocking challenge: {root}")
                continue  # Skip this challenge
            challenges.append(os.path.join(root, "chall.toml"))
    return challenges


def parse_toml(file_path):
    with open(file_path, "r") as f:
        data = toml.load(f)

    challenge_data = data.get("challenge", {})
    services = challenge_data.get("services", [])
    service_data = None
    if services:
        service_data = services[0]
        if "name" not in service_data:
            service_data["name"] = challenge_data.get("name", "unknown").replace(" ", "-").lower()
        if "path" not in service_data:
            service_data["path"] = "service"

    return {
        "name": challenge_data.get("name", "unknown").replace(" ", "-").lower(),
        "folder_name" : challenge_data.get("folder_name", "unknown").replace(" ", "-").lower(),
        "category": challenge_data.get("category", "misc").replace(" ", "-").lower(),
        "description": challenge_data.get("description", ""),
        "author": challenge_data.get("author", ""),
        "flag": challenge_data.get("flags", [{}])[0].get("flag", "FLAG{DEFAULT}"),
        "service": service_data,
        "challenge_path": os.path.dirname(file_path)
    }


#########################################
# SINGLE-SERVICE FUNCTIONS (Dockerfile)
#########################################

def generate_k8s_yaml(challenge, docker_image):
    """Generate Deployment and Service YAML for a single-service challenge."""
    challenge_name = challenge["name"]
    service = challenge["service"]

    if not service or "ports" not in service:
        print(f"[SKIP] {challenge_name}: No valid service configuration found.")
        return None, None, None

    service_port = service["ports"][0]
    mapping_key = f"{challenge['category']}-{challenge['folder_name']}-{service['name']}"
    print(f"[DEBUG] Generated mapping key: {mapping_key}")
    print(f"[DEBUG] Available mapping keys: {list(PORT_MAPPING.keys())}")
    mapping_list = PORT_MAPPING.get(mapping_key)
    if mapping_list:
        mapping_item = next((m for m in mapping_list if m.get("from_port") == service_port), None)
        if mapping_item:
            node_port = mapping_item.get("to_port")
        else:
            print(f"[WARN] No mapping found for port {service_port} in {mapping_key}. Using a random node port.")
            node_port = random.randint(30000, 32767)
    else:
        print(f"[WARN] No port mapping for key {mapping_key}. Using a random node port.")
        node_port = random.randint(30000, 32767)

    deployment_yaml = {
        "apiVersion": "apps/v1",
        "kind": "Deployment",
        "metadata": {"name": challenge_name},
        "spec": {
            "replicas": 1,
            "selector": {"matchLabels": {"app": challenge_name}},
            "template": {
                "metadata": {"labels": {"app": challenge_name}},
                "spec": {
                    "containers": [
                        {
                            "name": challenge_name,
                            "image": docker_image,
                            "imagePullPolicy": "Always",
                            "ports": [{"containerPort": service_port}],
                            "env": [{"name": "FLAG", "value": challenge["flag"]}]  # FLAG IS THE ENV VARIABLE
                        }
                    ]
                }
            }
        }
    }

    service_yaml = {
        "apiVersion": "v1",
        "kind": "Service",
        "metadata": {"name": challenge_name},
        "spec": {
            "selector": {"app": challenge_name},
            "ports": [
                {
                    "protocol": "TCP",
                    "port": service_port,
                    "targetPort": service_port,
                    "nodePort": node_port
                }
            ],
            "type": "NodePort"
        }
    }

    deployment_file = os.path.join(K8S_DEPLOYMENTS_DIR, f"{challenge_name}-deployment.yaml")
    service_file = os.path.join(K8S_DEPLOYMENTS_DIR, f"{challenge_name}-service.yaml")
    with open(deployment_file, "w") as f:
        yaml.dump(deployment_yaml, f)
    with open(service_file, "w") as f:
        yaml.dump(service_yaml, f)

    return deployment_file, service_file, node_port


def build_and_push_docker_image(challenge, docker_path):
    """Build and push the Docker image for a single-service challenge."""
    challenge_name = challenge["name"]
    if USE_DOCKER_HUB:
        image_name = f"{DOCKER_HUB_USERNAME}/{challenge_name}:latest"
    else:
        image_name = f"localhost:5000/{challenge_name}:latest"

    print(f"[BUILD] Building Docker image for {challenge_name} ...")
    subprocess.run(["docker", "build", "-t", image_name, docker_path], check=True)

    if not USE_DOCKER_HUB:
        print(f"[PUSH] Pushing image to local registry: {image_name}")
        subprocess.run(["docker", "push", image_name], check=True)

    return image_name


def deploy_to_kubernetes(deployment_yaml, service_yaml, deploy_name, node_port):
    """Deploy resources to Kubernetes and report access details."""
    if not deployment_yaml or not service_yaml:
        return

    print(f"[DEPLOY] Deploying {deploy_name} ...")
    subprocess.run(["kubectl", "delete", "-f", deployment_yaml, "-f", service_yaml, "--ignore-not-found"], check=False)
    subprocess.run(["kubectl", "apply", "-f", deployment_yaml], check=True)
    subprocess.run(["kubectl", "apply", "-f", service_yaml], check=True)

    print(f"[OK] {deploy_name} deployed.")
    if node_port:
        print(f"    Accessible externally at: http://{get_external_ip()}:{node_port}")
    else:
        print("    Internal service (ClusterIP), not exposed externally.")


def get_external_ip():
    """Get the external IP address of the host."""
    result = subprocess.run(["curl", "-s", "https://ifconfig.me"], capture_output=True, text=True)
    return result.stdout.strip()


#########################
# MAIN DEPLOYMENT LOGIC
#########################
def main():
    chall_files = find_challenges(BASE_DIR)
    if not chall_files:
        print("[INFO] No challenges found.")
        return

    for chall_path in chall_files:
        challenge = parse_toml(chall_path)

        if not challenge.get("service"):
            print(f"[SKIP] {challenge['name']}: No service configuration defined.")
            continue

        service_dir = challenge["service"].get("path", "service")
        service_path = os.path.join(challenge["challenge_path"], service_dir)
        service_path = service_path.replace("\\", "/")

        if not os.path.exists(service_path):
            print(f"[SKIP] {challenge['name']}: Service path does not exist - {service_path}")
            continue
        
        dockerfile_path = os.path.join(service_path, "Dockerfile")
        if os.path.exists(dockerfile_path):
            docker_image = build_and_push_docker_image(challenge, service_path)
        else:
            print(f"[SKIP] {challenge['name']}: No Dockerfile found in {service_path}")
            continue

        deployment_yaml, service_yaml, node_port = generate_k8s_yaml(challenge, docker_image)
        deploy_to_kubernetes(deployment_yaml, service_yaml, challenge["name"], node_port)


if __name__ == "__main__":
    main()
