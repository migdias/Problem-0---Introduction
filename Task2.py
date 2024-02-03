"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

phonenumber_dict = {}

for from_number, to_number, datetime, seconds in calls:
    seconds = int(seconds)
    # Add from number
    if from_number not in phonenumber_dict.keys():
        phonenumber_dict[from_number] = seconds
    else:
        phonenumber_dict[from_number] += seconds

    # to number also increases
    if to_number not in phonenumber_dict.keys():
        phonenumber_dict[to_number] = seconds
    else:
        phonenumber_dict[to_number] += seconds

_max = 0
_max_phone = None

for phone_number, amount_spent_on_phone in phonenumber_dict.items():
    if amount_spent_on_phone > _max:
        _max = amount_spent_on_phone
        _max_phone = phone_number

print(f'{_max_phone} spent the longest time, {_max} seconds, on the phone during September 2016.')

## Time Analysis

## Reading in the data
# The necessary time to read the calls is O(m) where , is the number of calls in the file

## Solution
# 1. We only go through the calls one by one so the time complexity is O(n) where n is the amount of calls in the file. There are some O(1) operations, but everything simplifies to O(n)
# 2. To get the maximum, we go through  the whole dictionary, which is complexity of O(k) where k is the unique phone numbers within the calls file.
# Therefore the solution is O(n) + O(k) -> O(n), since k will always be smaller than n.

## Overview
# The overall time complexity is 2O(m) + O(k) which simplifies to O(m) where n is the number of lines of the calls.