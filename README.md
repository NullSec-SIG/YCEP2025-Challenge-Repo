# YCEP2025 Challenge Repo

Welcome to the official GitHub repository for NP YCEP 2025, proudly organised by the NullSec SIG!

## Table of Contents
- **.github/workflows** (GitHub Actions scripts we use to keep challenge statistics up to date automatically)
- **challenges** (The main folder used to store all the challenges)
   - crypto
   - forensics
   - misc
   - osint
   - pwn
   - web
- **.gitattributes** (File used to configure Git LFS to facilitate the upload of ABC's Had Enough's massive dist file)
- **compose.yml** (Configuration file used to deploy pwn/web challenges on our infra via Docker/Kubernetes)
- **ctf_config.toml** (Configuration file for CTF-Architect)
- **deploy_no_ingress.py** (Script used for chall1 and chall2 machines to automatically deploy all challenges)
- **port_mapping.yml** (Configuration file used to deploy pwn/web challenges on our infra via Docker/Kubernetes)

## Challenge Folders
Each challenge is organised into folders based on their respective categories. They are organised like the following:
- **dist** (Folder containing **dist**ribution files, aka any files we want participants to download)
- **service** (Folder containing any Docker containers/server side stuff needed to be run for the challenge)
- **solution** (Folder containing writeups on how to solve the challenge)
- **chall.toml** (Configuration file used by CTF-Architect to determine the challenge parameters for CTFd)

## Contributors
Special thanks to everyone who made YCEP 2025 possible!

### NullSec AY24/25 EXCO
- Kairos (President)
- Bowen (Vice-President)
- Galen (Head of Tech)
- Tech team
- Dhava (Head of SecOps)
- SecOps team
- Yong Xin (Head of Publicity)
- Publicity team

### NullSec AY24/25 EXCO Interns
**Challenge Creators**
- Daksh (Handled most infra-related matters and all the infra scripts)
- Jun Wei (Created the most number of challenges)
- Chin Ray
- Damian
- Ravin
- Ryan Low
- Caeden
- Ryan Tan (SecOps team, created OSINT - Touch Grass)

#### SecOps Team
Thanks for handling the administrative matters of the event!
- Ryan Tan
- Quan Yu
- Ray THS

#### Publicity Team
Thanks for handling the photo-taking, design and other publicity related work!
- Rui Min
- Vicky
- Aloysius
