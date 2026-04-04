"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

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

time_spent = {}

for record in calls:
    caller   = record[0]
    receiver = record[1]
    duration = int(record[3])

    if caller not in time_spent:
        time_spent[caller] = 0
    time_spent[caller] += duration

    if receiver not in time_spent:
        time_spent[receiver] = 0
    time_spent[receiver] += duration

longest_number = None
longest_time   = 0

for number, total in time_spent.items():
    if total > longest_time:
        longest_time   = total
        longest_number = number

print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(
    longest_number, longest_time))