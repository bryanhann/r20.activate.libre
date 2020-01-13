import sys
import datetime

from lib.libre.constants import KEYLISTS, IGNORE_KEYS

SCRIPT = sys.argv[0]
ARGS = sys.argv[1:]
USAGE="""\
%s -- catenate a processes version of an exported libre file.
usage:
    %s PATH
PATH is path to file.
""" % (SCRIPT, SCRIPT)

def main():
    if not ARGS or '-h' in ARGS or '--help' in ARGS:
        print USAGE
        exit(1)
    LIBRE = ARGS[0]
    name = name4file(LIBRE)
    keys = keys4file(LIBRE)
    dict4line = lambda line : dict4line4keys(line,keys)
    lines = lines4file(LIBRE)
    dicts = map(dict4line, lines)
    map(IOprint4dict, dicts)

def name4file(pth):
    with open(pth) as fd:
        name = fd.readline().strip()
        assert not '\t' in name
        return name

def keys4file(pth):
    with open(pth) as fd:
        fd.readline()
        keys = fd.readline().strip().split('\t')
        for long, short in KEYLISTS:
            if keys == long:
                return short
        sys.stderr.write( 'fatal error on file %s: unknown keys' % pth)
        exit(1)

def lines4file(pth):
    with open(pth) as fd:
        fd.readline()  # skip the first line which contains libre user's name
        fd.readline()  # skip the secondline which contains keylist
        return fd.readlines()

def sorted(aList):
    assert type(aList)==type([])
    x = aList[:]
    x.sort()
    return x

def IOprint4dict( _dict ):
    format0 = '%Y/%m/%d %H:%M'
    format1 = '%Y%m%dt%H%M%S'
    stamp0 = _dict['Time']
    stamp1 = datetime.datetime.strptime(stamp0, format0).strftime(format1)
    for key,val in _dict.items():
        if not val:
            del _dict[key]
    items = sorted( _dict.items() )
    print stamp1 + ':libre:' + repr(items)

def dict4line4keys(line,keys):
    fields = line.strip().split('\t')
    return dict(zip(keys,fields))

if __name__=='__main__':
    main()

