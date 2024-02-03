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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

print(f'The first record of texts, {texts[0][0]} texts {texts[0][1]} at time {texts[0][2]}')
print(f'The last record of calls, {calls[0][0]} calls {calls[0][1]} at time {calls[0][2]}, lasting {calls[0][3]} seconds')


## Time Analysis

## Reading in the data
# The necessary time to read the texts is O(n) where n is the number of texts in the file
# The necessary time to read the calls is O(m) where , is the number of calls in the file

## Solution
## To print out the solution the time necessary for both is O(1) since we can just quickly get the first and last index. This simplifies to O(1).

## Overview
## The overall time complexity is O(n) + O(m) + O(1) + O(1) which simplifies to O(n) where n is the number of lines of the biggest file.