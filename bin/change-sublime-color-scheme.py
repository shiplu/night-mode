#!/usr/bin/env python3
import os
import sys
import json
import argparse


filename = os.path.expanduser("~/.config/sublime-text-3/Packages/User/Preferences.sublime-settings")

argp = argparse.ArgumentParser()
argp.add_argument('mode', help='The color mode. dark or light', choices=['dark', 'light'])
args = argp.parse_args()
theme = "ayu-{}.sublime-theme".format(args.mode)
color_scheme = "Packages/ayu/ayu-{}.sublime-color-scheme".format(args.mode)
with open(filename, "r+") as f:
    d = json.load(f)
    f.seek(0)
    f.truncate()
    d['color_scheme'] = color_scheme
    d['theme'] = theme 
    json.dump(d, f, indent=4)



