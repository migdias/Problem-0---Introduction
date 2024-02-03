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

texts_sent_received_and_calls_received = set()
for from_number, to_number, _ in texts:
    texts_sent_received_and_calls_received.add(from_number)
    texts_sent_received_and_calls_received.add(to_number)

# Complexity O(c) where c is the amount of calls
calls_sent_set = set()
for from_number, to_number, _, _ in calls:
    texts_sent_received_and_calls_received.add(to_number)
    calls_sent_set.add(from_number)
    

# Complexity of O(len(calls_sent_set))
telemarketers = calls_sent_set - texts_sent_received_and_calls_received

# complexity is sort + print = O(k log k) + O(k) -> O(k log k)
print('These numbers could be telemarketers: ')
for pn in sorted(list(telemarketers)):
    print(pn)


