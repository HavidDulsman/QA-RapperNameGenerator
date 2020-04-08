#!/bin/bash
source /var/lib/jenkins/workspace/"rapper-pipeline"/venv/bin/activate
source ~/.bashrc
sudo docker stack deploy --compose-file docker-compose.yml rapperstack 