#!/bin/sh

MYDIR=$(cd `dirname $0`; pwd)

ROOTDIR=`dirname $MYDIR`

sudo pip3 install -r $MYDIR/requirements.txt
