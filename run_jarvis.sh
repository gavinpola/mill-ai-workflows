#!/bin/bash
# Run Jarvis from anywhere
cd "$(dirname "$0")"
python3 jarvis/tui.py "$@"
