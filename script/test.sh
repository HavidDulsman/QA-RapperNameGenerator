#!/bin/bash
source ~/.bashrc
source /var/lib/jenkins/workspace/rapper-pipeline/venv/bin/activate
pip install coverage
python3 -m coverage run -m pytest testing/test.py
python3 -m coverage report -m