# YCEP2025-Challenge-Repo

Challenge files for NP YCEP 2025

## To Do

- Update LionExchange 2 have a dependancy on LionExchange 1
- Add double tag for ConsumerFolder 3 (web, forensics)

## If everything breaks

In the case where my script breaks, heres a quick fix

1. Stop all kube containers
2. Stop kube
3. Run this

```bash
sed -i 's/\\/\//g' compose.yml # BUG in the current version of ctfa
docker compose up -d # rebuild the containers, ports should stay the same
```
