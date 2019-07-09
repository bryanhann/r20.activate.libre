import os
import sys

CURRENT_LIBRE_FIELDS = [
    'ID', 
    'Time', 
    'Record Type', 
    'Historic Glucose (mmol/L)', 
    'Scan Glucose (mmol/L)', 
    'Non-numeric Rapid-Acting Insulin', 
    'Rapid-Acting Insulin (units)', 
    'Non-numeric Food', 
    'Carbohydrates (grams)', 
    'Non-numeric Long-Acting Insulin', 
    'Long-Acting Insulin (units)', 
    'Notes', 
    'Strip Glucose (mmol/L)', 
    'Ketone (mmol/L)', 
    'Meal Insulin (units)', 
    'Correction Insulin (units)', 
    'User Change Insulin (units)', 
    'Previous Time', 
    'Updated Time'
]


def usage(x=None):
    name = sys.argv[0]
    if x: 
        print( "\n%s: error: %s. (Try '%s --help'" % (name, x, name))
    else:
        print ( """usage: %s FNAME\n\n\tFNAME is the path to the libre output file to be parsed""" % name )
    exit()

def parse_arguments():
    if '--help' in sys.argv: usage()
    if '-h' in sys.argv: usage()
    if len(sys.argv)<2: usage('arg missing')
    if len(sys.argv)>2: usage('too many args')
    file = sys.argv[1]
    if not os.path.isfile(file): usage("cannot open file '%s'" %file )
    return file

def fixtime(timestamp):
    ymd, hm = timestamp.split(' ')
    ymd = ''.join(ymd.split('/'))
    hm = ''.join(hm.split(':'))
    ymdhms = '%sT%s00' % (ymd,hm)
    return ymdhms

def confirm_fields(fields):
    for a,b in zip(fields, CURRENT_LIBRE_FIELDS):
        assert a==b or 'N/A' in (a,b)

def chop(line):
    while line and line[-1] in '\n\r':
        line=line[:-1]
    return line

def main():
    filename = parse_arguments()

    with open(filename) as f:
        lines = f.readlines()

    lines = [ chop(line) for line in lines ] 
    rows  = [ line.split('\t') for line in lines ]
    owner = rows.pop(0)
    fields = rows.pop(0)
    confirm_fields(fields)

    while rows:
        row = rows.pop(0)
        clean_row = [ item.strip() for item in row ]
        timestamp = fixtime( clean_row[1] )
        aa = list( zip(CURRENT_LIBRE_FIELDS, clean_row) )
        bb = [ item for item in aa if item[1] ]
        cc = [ '='.join(x) for x in bb ]
        dd = ' | '.join(cc)
        print( '%s [libre] %s' % (timestamp, dd) )


if __name__=='__main__':
    main()
