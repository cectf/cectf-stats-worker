#!/bin/sh

python3 -m venv venv
source venv/bin/activate

pip install -e .
pip install -r test_requirements.txt
