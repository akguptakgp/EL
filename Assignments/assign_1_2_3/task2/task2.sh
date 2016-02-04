#!/bin/sh
#
if [ $# -lt 1 ]; then
    echo "usage: $0 inputtextfile"
    exit 1;
fi
stanford-parser-full-2015-12-09/lexparser.sh $1 > output_task2_PARSE.txt
if [ $# -eq 2 ]; then
    python task2.py > $2
    exit 1;
else
	python task2.py
fi
