# Michael Angelo C. Adraincem
# MCA655 11208422
# This file handles RMSE and ERR computational analysis

import math


# err
# Parameter: answer/guess, target
# Returns: err value
def err(guess, target):
    return guess/target


# rmse
# Parameter: list of Err, tototal num/ N
# Returns: rmse of a test
def rmse(errlist, num):
    totalsqaurederr = 0.0
    tosquareroot = 0
    for x in errlist:
        totalsqaurederr += x*x
    tosquareroot = totalsqaurederr/num
    return math.sqrt(tosquareroot)
