#!/bin/sh
#

if [ $# -lt 1 ]; then
    echo "usage: $0 inputtextfile"
    exit 1;
fi

java -mx300m -cp 'stanford-postagger.jar:' edu.stanford.nlp.tagger.maxent.MaxentTagger -model english-bidirectional-distsim.tagger -textFile $1 > output_task1_POS.txt
if [ $# -eq 2 ]; then
    python task1.py > $2
    exit 1;
else
	python task1.py
fi	