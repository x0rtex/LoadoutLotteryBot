#!/bin/bash

basedir=$(realpath `dirname "$0"`)
/usr/bin/tmux new -d -c $basedir -s Tarkov "uv run main.py"
exit 0
