#!/usr/local/bin/python2.7

from pandas import DataFrame as df
import csv
from datetime import datetime as dt
import datetime
import time
import json

lookuptable={}

# defining some functions for the reader and for parsing date times items
def records(path):
    with open(path) as f:
        contents = f.read()
        return (record for record in contents.split('\t\n'))
def parser(item):
    try:
        x=time.strptime(item,'%H:%M:%S')
        seconds=datetime.timedelta(hours=x.tm_hour,minutes=x.tm_min,seconds=x.tm_sec).total_seconds()
        return seconds
    except:
        return 0

def convert():

    csvfile=csv.reader(records('waittimes0804'),delimiter='|')

    for row in csvfile: 
        try:
            if row[0] not in lookuptable:
                lookuptable[row[0]]={}
                lookuptable[row[0]][row[1]]={}
                lookuptable[row[0]][row[1]]['mintimes'] = []
                lookuptable[row[0]][row[1]]['maxtimes'] = []
            else:
                if row[1] not in lookuptable[row[0]]:
                    lookuptable[row[0]][row[1]]={}
                    lookuptable[row[0]][row[1]]['mintimes'] = []
                    lookuptable[row[0]][row[1]]['maxtimes'] = []
            # append the minimum wait times 
            xlist=row[2].strip().split(',')
            xlist=map(parser,xlist)
            lookuptable[row[0]][row[1]]['mintimes'] = xlist
            # append the maximum wait times 
            xlist=row[3].strip().split(',')
            xlist=map(parser,xlist)
            lookuptable[row[0]][row[1]]['maxtimes'] = xlist
        except:
            pass

    with open('stop_id.json','w') as f:
        json.dump(lookuptable, f)



def startLoop():

    with open('last_updated.log') as f:
        timestamp = f.readline().strip().split('|')[1]    
   
    while True:
        with open('last_updated.log') as f:
            current_timestamp = f.readline().strip().split('|')[1]    
        if timestamp == current_timestamp:
            pass
        else:
            print 'converting....   '+ str(dt.now())
            convert()
            timestamp = current_timestamp
            print 'converted finished  '+ str(dt.now())

        time.sleep(10)

if __name__ == '__main__':
    startLoop()
