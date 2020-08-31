#!/bin/bash

cd "$(dirname "$0")"
FILENAME=playlist.m3u
LINECOUNT=$(wc -l < "$FILENAME")
COUNTER=0
echo "ਵਾਹਿਗੁਰੂਜੀਕਾਖ਼ਾਲਸਾਵਾਹਿਗੁਰੂਜੀਕੀਫ਼ਤਿਹ॥ Welcome to gv-downloader. This script will download files to the folder printed above."
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
