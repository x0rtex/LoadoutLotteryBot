#!/bin/bash

basedir=$(realpath `dirname "$0"`)
/usr/bin/tmux new -d -c $basedir -s Tarkov "./venv/bin/python -O main.py"
exit 0
