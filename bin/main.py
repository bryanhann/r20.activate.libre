#!/usr/bin/python

assert __name__ == '__main__'

import argparse
from datetime import datetime as DT
from misc import KEYBOOKS, cdar, unique, car, FORMAT0, FORMAT1 , KEEP

parser = argparse.ArgumentParser(description = 'catenate a processed version of an exported libre file.' )
parser.add_argument( '--test', action='store_true' )
parser.add_argument( 'filename' )
args = parser.parse_args()
if True:
    target = args.filename
    with open( target ) as fd:
        _owner = fd.readline().strip()
        _keys = fd.readline().strip().split('\t')
        _agree = lambda book : _keys == map(car,book)
        keys = map(cdar,unique(filter(_agree,KEYBOOKS)))
        for line in fd.readlines():
            vals  = line.strip().split('\t')
            items = zip(keys,vals)
            items.sort()
            stamp = DT.strptime(dict(items)['Time'], FORMAT0).strftime(FORMAT1)
            print(  stamp + ':libre:' + repr(filter(KEEP,items)))

