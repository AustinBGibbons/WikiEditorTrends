#!/bin/bash

if [ -z "$1" ]; then
	echo "usage: $0 [mapreduce output suffix]"
	exit 
fi

if [ -d "parts/" ]; then
	rm -rf parts/
fi

echo "Sync directory"
mkdir parts
s3cmd sync "s3://pageview-output/output-$1/" parts/

echo "Assemble"
cat parts/* > "./dataset-$1.tsv"
rm -rf parts/
