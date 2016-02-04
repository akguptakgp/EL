#!/bin/sh
#
# usage: ./stanford-postagger.sh model textFile
#  e.g., ./stanford-postagger.sh models/english-left3words-distsim.tagger sample-input.txt

if [ $# -lt 1 ]; then
    echo "usage: $0 inputtextfile"
    exit 1;
fi
java -mx300m -cp '/home/a/Downloads/stanford-postagger-full-2015-04-20/stanford-postagger.jar:' edu.stanford.nlp.tagger.maxent.MaxentTagger -model /home/a/Downloads/stanford-postagger-full-2015-04-20/models/english-bidirectional-distsim.tagger -textFile $2
python task1.py	