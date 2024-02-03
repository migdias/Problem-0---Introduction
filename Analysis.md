# Task 1

## Time Analysis

- Reading in the data
The necessary time to read the texts is O(n) where n is the number of texts in the file 
The necessary time to read the calls is O(m) where , is the number of calls in the file

- Solution
To print out the solution the time necessary for both is O(1) since we can just quickly get the first and last index. This simplifies to O(1).

- Overview
The overall time complexity is O(n) + O(m) + O(1) + O(1) which simplifies to O(n) where n is the number of lines of the biggest file.

# Task 2

## Time Analysis

- Reading in the data
The necessary time to read the calls is O(m) where , is the number of calls in the file

- Solution
1. We only go through the calls one by one so the time complexity is O(n) where n is the amount of calls in the file. There are some O(1) operations, but everything simplifies to O(n)
2. To get the maximum, we go through  the whole dictionary, which is complexity of O(k) where k is the unique phone numbers within the calls file.

Therefore the solution is O(n) + O(k) -> O(n), since k will always be smaller than n.

- Overview
The overall time complexity is 2O(m) + O(k) which simplifies to O(m) where n is the number of lines of the calls.

# Task 3

## Part A
O(n) where n is the amount of calls
O(k log k) is the time complexity of the sorting, where k is the number of phones found
O(k) where k is the number of phone numbers found

The overall complexity of Part A is O(n) + O(k log k) + O(k) -> O(n) + O(k log k) [k is always smaller or equal than n] where n is the amount of calls and k is the amount of phone numbers found. 

## Part B

The complexity of Part B is O(c) where c is the amount of calls.

The overall complexity is O(n) + O(n) + O(k) + O(k), which simplifies to O(n)


# Task 4

For this problem we can create two sets. One of phone numbers for calls and on with phone numbers of texts and subtract the sets.
Eg. calls_sent_set - texts_sent_received_and_calls_received will result in all phone numbers that make calls but do not make texts not receive texts or calls.

1. Complexity O(t) where t is the amount of texts
2. Complexity O(c) where c is the amount of calls
3. Complexity of O(len(telemarketers)), which is smaller than O(c)
4. Complexity is O(len(telemarketers))
5. Complexity of sorting is O(n log n)
5. Overall complexity is O(t) + O(c) + O(k log k) + O(k) -> O(t) + O(c) + O(k log k) where t is the number of texts, c in the number of calls and k is the number of telemarketers. 

PS: Reading the files in is ignored because in this case it will anyway simplify to O(c)