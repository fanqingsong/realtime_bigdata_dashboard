#!/bin/sh

MYDIR=$(cd `dirname $0`; pwd)

ROOTDIR=`dirname $MYDIR`

/usr/local/spark/bin/spark-submit $ROOTDIR/backend/wordCounter.py CN-00015440.ericsson.se:2181 1 rawContent 1
