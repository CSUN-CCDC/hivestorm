#!/bin/bash
#Quick and dirty hack to find various filetypes we don't like
#Not exhaustive nor-accurate
find ./ -type f \( -iname \*.jpg -o -iname \*.png -o -iname \*.mp4 -o -iname \*.mp3 -o -iname \*.exe \)
