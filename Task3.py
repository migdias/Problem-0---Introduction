"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import re

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

# Part A
# O(n) where n is the amount of calls
codes = set()
for from_number, to_number, _, _ in calls:
    if from_number.startswith('(080)'):
        # Fixes lines starting with (0..) OR mobile no parenthesis but space in the middle OR starts with "140"
        if to_number.startswith('(0'):
            codes.add(re.search(r'\((.*?)\)', to_number).group(1))
        elif (' ' in to_number and int(to_number[0]) >= 7):
            codes.add(to_number[:4])
        elif to_number.startswith('140'):
            codes.add('140')

print('The numbers called by people in Bangalore have codes:')
# O(k) where k is the number of phone numbers found
for phonenumber in sorted(list(codes)):
    print(phonenumber)

# The overall complexity of Part A is O(n) + O(k) -> O(n) [k is always smaller or equal than n] where n is the amount of calls and k is the amount of phone numbers found.

# Part B

total_length = len(calls)
bangalore2bangalore = 0
for from_number, to_number, _, _ in calls:
    if from_number.startswith('(080)') and to_number.startswith('(080)'):
        bangalore2bangalore += 1


print(f'{round((bangalore2bangalore/total_length) * 100, 2)} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.')