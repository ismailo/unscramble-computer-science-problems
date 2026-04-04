## Task0

Question: Retrieve the first record from texts and the last record from calls.

Approach: Direct index access using texts[0] and calls[-1].

Big O Notation: O(1)

Justification: Index access on a Python list is O(1) regardless of list size. No search or iteration occurs.

--------------------------------

## Task1

Question: Count all distinct telephone numbers across texts and calls.

Approach: Iterate through both lists adding each number to a set. Sets discard duplicates automatically.

Big O Notation: O(n + m)

Justification: One pass through texts (n records) and one pass through calls (m records). Set insertion is O(1) on average.

--------------------------------

## Task2

Question: Find the number with the most total time on the phone as either caller or receiver.

Approach: Build a dictionary of cumulative durations in one pass, then scan it once to find the maximum.

Big O Notation: O(m)

Justification: Both loops are linear in the size of calls (m records). Dictionary operations are O(1) on average.

--------------------------------

## Task3

Question: Find all area codes and mobile prefixes called from Bangalore (080) numbers, and the percentage of those calls that stayed within Bangalore.

Approach: Single pass through calls, extracting codes into a set and tracking counts. Sort the set for output.

Big O Notation: O(m + k log k)

Justification: The scan is O(m). Sorting k unique codes is O(k log k). Since k is much smaller than m, the dominant term is O(m).

--------------------------------

## Task4

Question: Identify numbers that only make outgoing calls and never send or receive texts or receive calls.

Approach: Build a set of outgoing callers and a set of disqualified numbers, then subtract. Sort the result.

Big O Notation: O(n + m + p log p)

Justification: Building both sets is O(n + m). Set difference is O(min of the two set sizes). Sorting p results is O(p log p).