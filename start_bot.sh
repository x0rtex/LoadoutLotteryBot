#!/bin/bash

basedir=$(realpath `dirname "$0"`)
/usr/bin/tmux new -d -c $basedir -s LoadoutLotteryBot "uv run main.py"
exit 0
