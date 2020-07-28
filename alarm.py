import sys
import string
from time import sleep
import time
    
tm = time.asctime()
var = tm.split()    
print var


try:
    #minutes = int(raw_input("Enter the number of minutes?? "))
    minutes = int(raw_input("Enter the number of minutes "))
except ValueError:
    print "Invalid numeric value (%s) for minutes" % minutes
    print "Should be an integer >= 0"
    sys.exit(1)

if minutes < 0:
    print "Invalid value for minutes, should be >= 0"
    sys.exit(1)

seconds = minutes * 60

if minutes == 1:
    unit_word = " minute"
else:
    unit_word = " minutes"

try:
    if minutes > 0:
        print "Sleeping for " + str(minutes) + unit_word
        sleep(seconds)
    print "Wake up"
    for i in range(5):
        print chr(7),
        sleep(1)
except KeyboardInterrupt:
    print "Interrupted by user"
    sys.exit(1)