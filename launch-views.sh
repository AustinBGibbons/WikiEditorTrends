#!/bin/bash

if [ -z "$1" ]; then
	echo "Usage: $0 [job name] [num instances total]"
	exit
fi

if [ -z "$2" ]; then
	echo "Usage: $0 [job name] [num instances total]"
	exit
fi

echo "push files to s3"
s3cmd put *.py s3://mr-code-wiki/

echo "launch emr job"
/home/ubuntu/emr/elastic-mapreduce --create --name "user-$1" --stream --input s3://pageviews-wiki/ --output "s3://pageview-output/output-$1/" --mapper s3://mr-code-wiki/pageview_mapper.py --reducer s3://mr-code-wiki/pageview_reducer.py --num-instances "$2" --master-instance-type "c1.medium"  --slave-instance-type "m1.xlarge" --enable-debugging --cache s3://pageviews-wiki/en_created_cats.tab#cats

#/home/ubuntu/emr/elastic-mapreduce --create --name "user-$1" --stream --input s3://pageview-test-bucket/ --output "s3://pageview-output/output-$1/" --mapper s3://mr-code-wiki/pageview_mapper.py --reducer s3://mr-code-wiki/pageview_reducer.py --num-instances "$2" --master-instance-type "c1.medium"  --slave-instance-type "m1.xlarge" --enable-debugging --cache s3://pageviews-wiki/en_created_cats.tab#cats

