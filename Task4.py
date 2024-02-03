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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

# For this problem we can create two sets. One of phone numbers for calls and on with phone numbers of texts and subtract the sets.
# Eg. calls_set - texts_set will result in all phone numbers that make calls but do not make tests.

# Complexity O(t) where t is the amount of texts
texts_set = set([x[0] for x in texts])

# Complexity O(c) where c is the amount of calls
calls_set = set([x[0] for x in calls])

# Complexity of O(len(calls_set)), which is smaller than O(c)
calls_but_no_texts = calls_set - texts_set

# Complexity is O(len(calls_set))
print('These numbers could be telemarketers: ')
for pn in calls_but_no_texts:
    print(pn)

# Overall complexity is O(t) + O(c) + 2O(len(calls_set)) -> O(c)
