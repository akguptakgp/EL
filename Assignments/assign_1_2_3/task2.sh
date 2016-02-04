#!/bin/sh
#
# usage: ./stanford-postagger.sh model textFile
#  e.g., ./stanford-postagger.sh models/english-left3words-distsim.tagger sample-input.txt

if [ $# -lt 1 ]; then
    echo "usage: $0 inputtextfile"
    exit 1;
fi
/home/a/Downloads/stanford-parser-full-2015-04-20/lexparser.sh $1 > out_task2.txt
