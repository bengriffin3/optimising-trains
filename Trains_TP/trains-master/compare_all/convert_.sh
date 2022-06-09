#! /bin/bash

filename=$1
name="${filename%.*}"

inkscape --file="$name.svg" --export-area-drawing --without-gui --export-pdf="$name.pdf"
rm $1
