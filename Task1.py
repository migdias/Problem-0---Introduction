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