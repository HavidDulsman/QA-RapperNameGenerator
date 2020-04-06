#!/bin/bash
#run ansible!
sudo ansible-playbook -i inventory.cfg playbook.yml
#check if service is running

#if it is destroy it

#then rn this command

docker stack deploy --compose-file ../services/docker-compose.yml rappperstack

