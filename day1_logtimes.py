#%%
from datetime import datetime
import os
import urllib.request
import re

SHUTDOWN_EVENT = 'Shutdown initiated'

# prep: read in the logfile
tmp = os.getenv("TMP", "/tmp")
logfile = os.path.join(tmp, 'log')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/messages.log',
    logfile
)

with open(logfile) as f:
    loglines = f.readlines()


# for you to code:

def convert_to_datetime(line):
    """TODO 1:
       Extract timestamp from logline and convert it to a datetime object.
       For example calling the function with:
       INFO 2014-07-03T23:27:51 supybot Shutdown complete.
       returns:
       datetime(2014, 7, 3, 23, 27, 51)
    """
    for eachline in line:
        print(eachline)
        


def time_between_shutdowns(loglines):
    """TODO 2:
       Extract shutdown events ("Shutdown initiated") from loglines and
       calculate the timedelta between the first and last one.
       Return this datetime.timedelta object.
    """
    pass

test = convert_to_datetime(loglines)

line1 = 'ERROR 2014-07-03T23:24:31 supybot Invalid user dictionary file, resetting to empty'
#line1_obj = datetime(int(line1))

#print(line1)
#print(line1_obj.date)

print([int(s) for s in line1.split('-') if s.isdigit()])

print(re.findall(line1))
# %%
