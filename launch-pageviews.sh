#!/bin/bash

if [ -z "$1" ]; then
	echo "Usage: $0 [job name] [num instances total] [mapper] [reducer]"
	exit
fi

if [ -z "$2" ]; then
	echo "Usage: $0 [job name] [num instances total] [mapper] [reducer]"
	exit
fi

if [ -z "$3" ]; then
	echo "Usage: $0 [job name] [num instances total] [mapper] [reducer]"
	exit
fi

if [ -z "$4" ]; then
	echo "Usage: $0 [job name] [num instances total] [mapper] [reducer]"
	exit
fi

echo "push files to s3"
s3cmd put *.py s3://mr-code-wiki/

echo "launch emr job"
/home/ubuntu/emr/elastic-mapreduce --create --name "user-$1" --stream --input s3://pageviews-wiki/ --output "s3://language-output/output-$1/" --mapper s3://mr-code-wiki/$3 --reducer s3://mr-code-wiki/$4 --cache "s3://language-output/dataset-names.tsv#revision-tuples" --num-instances "$2" --master-instance-type "c1.medium"  --slave-instance-type "m1.xlarge" --enable-debugging

