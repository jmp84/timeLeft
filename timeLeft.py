#!/usr/bin/python

## How much time you have left to live.
## Prints out the number of weeks you have left to live.
## We assume you'll die 1 January 2083.

from datetime import *

finalDate = date(2083, 1, 1) #  1 January 2083
currentDate = date.today() # current date
dateDifference = finalDate - currentDate # date difference

print "If you die on the", finalDate, "you have", dateDifference.days / 7, "weeks to live."
