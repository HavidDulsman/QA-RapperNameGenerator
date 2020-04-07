#!/bin/bash
source /var/lib/jenkins/workspace/"rapper-pipeline"/venv/bin/activate
sudo docker stack deploy --compose-file docker-compose.yml rapperstack 