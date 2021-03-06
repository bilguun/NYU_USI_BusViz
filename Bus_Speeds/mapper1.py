#!/usr/bin/env python

###############################################################################
## mapper1.py
## mapper for calculating bus speed (naive method)
## contact: drp354@nyu.edu
###############################################################################

import sys
from datetime import datetime


def parseInput():
    for line in sys.stdin:
        line = line.strip('\n')
        values = line.split('\t')
        if values[0] != 'latitude':
            yield values

def main():
    for row in parseInput():
        time_stamp = row[2]
        busid = row[3]        
        direction = row[5]
        route = row[7]
        stop = row[10]
        print '%s|%s|%s|%s\t%s' % (busid,direction,route,time_stamp, stop)

if __name__ == "__main__":
    main()
