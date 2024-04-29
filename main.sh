#!/bin/bash

echo "# hello world"
python -m unittest discover -s src
python src/main.py
