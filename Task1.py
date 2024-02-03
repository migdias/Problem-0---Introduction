"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

telephone_numbers = set()

for from_number, to_number, _ in texts:
    telephone_numbers.add(from_number)
    telephone_numbers.add(to_number)

for from_number, to_number, _, _ in calls:
    telephone_numbers.add(from_number)
    telephone_numbers.add(to_number)

print(f'There are {len(telephone_numbers)} different telephone numbers in the records.')

## Time Analysis

## Reading in the data
# The necessary time to read the texts is O(n) where n is the number of texts in the file
# The necessary time to read the calls is O(m) where , is the number of calls in the file

## Solution
# 1. For the texts we have to go through all the texts which and add them to the dictionary. This is O(n) where n is the amount of texts
# 2. For the calls we have the same idea. This is O(m) where m is the amount of calls
# 3. To print out the unique telephone numbers its O(1) since we just need to printout the length of the set (which holds unique values).
# The solution has a time complexity of O(n) where n is the size of the biggest file.

## Overview
# The overall time complexity is 2O(n) + 2O(m) + O(1) which simplifies to O(n) where n is the number of lines of the biggest file.