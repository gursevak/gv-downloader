#!/bin/bash

FILENAME=playlist.m3u
LINECOUNT=$(wc -l < "$FILENAME")
local -i COUNTER=0
echo "There are $LINECOUNT audio tracks in this playlist."
read -p "Are you sure you want to download them all? [Y/n]" -n 1 -r
echo

if [[ $REPLY =~ ^[Yy]$ ]]
then
	cat $FILENAME | while read LINE; do
		curl -O $LINE
		echo $COUNTER
		sed -i '' $COUNTER'd' $FILENAME
		COUNTER=$((COUNTER + 1))
	done
fi