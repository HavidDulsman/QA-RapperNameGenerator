#!/bin/bash
# source  ~/.bashrc
source /var/lib/jenkins/workspace/rapper-pipeline/venv/bin/activate
ansible-playbook -i inventory.cfg playbook.yml --start-at-task="install packages"