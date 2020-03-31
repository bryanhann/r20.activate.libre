import argparse
import sys
import os
import glob
import string
from os.path import dirname, realpath

FORMAT0 = '%Y/%m/%d %H:%M'
FORMAT1 = '%Y%m%dt%H%M%S'
IGNORE_KEYS = ['Tim', 'ID', 'Type']

GLOBSTRING = '%s/keylists/*.keys' % dirname( realpath( sys.argv[0] ))
KEEP = lambda item: item[1] and not item[0] in IGNORE_KEYS

def lines4file(fname):
    with open(fname) as fd:
        return fd.readlines()

def pair( aList ):
    assert len(aList)==2
    return tuple(aList)

def unique( aList ):
    assert len(aList)==1
    return aList[0]



car       = lambda x : x[0]
cdar      = lambda x : x[1]
item4line = lambda line : pair(map(string.strip, line.split('|')))
list4file = lambda file : map(item4line, lines4file( file ) )
keys4book = lambda book : map(car,book)

KEYBOOKS = map(list4file, glob.glob(GLOBSTRING))

