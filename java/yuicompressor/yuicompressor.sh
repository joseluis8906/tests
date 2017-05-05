#!/bin/sh
fullfile=$(basename "$1")
filepath=$(dirname "$1")
filename="${fullfile%.*}"
extension="${fullfile##*.}"

#mkdir -p $filepath/build

java -jar /usr/local/bin/yuicompressor.jar $filepath/$fullfile -o $filepath/$filename.min.$extension
