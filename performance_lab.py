# 🔍 Problem 1: Find Most Frequent Element
# Given a list of integers, return the value that appears most frequently.
# If there's a tie, return any of the most frequent.
#
# Example:
# Input: [1, 3, 2, 3, 4, 1, 3]
# Output: 3

def most_frequent(numbers):
    # Your code here
    if not numbers:
        return None

    counts = {}
    for num in numbers:
        counts[num] = counts.get(num, 0) + 1

    return max(counts, key=counts.get)

# Test Cases
print(most_frequent([1, 3, 2, 3, 4, 1, 3]))  # Output: 3
print(most_frequent([]))  # Output: None
print(most_frequent([5,5,6,6]))  # Output: 5 or 6
print(most_frequent([7]))  # Output: 7
"""
Time and Space Analysis for problem 1:
- Best-case: O(n) has to go through every number 
- Worst-case: O(n) has to go through every number 
- Average-case: O(n) has to go through every number 
- Space complexity: O(n) has to go through every number 
- Why this approach? Counting with a dictionary structure is simple and efficient
- Could it be optimized? No because you have to go through every number no matter what.
"""


# 🔍 Problem 2: Remove Duplicates While Preserving Order
# Write a function that returns a list with duplicates removed but preserves order.
#
# Example:
# Input: [4, 5, 4, 6, 5, 7]
# Output: [4, 5, 6, 7]

def remove_duplicates(nums):
    # Your code here
    seen = set()
    result = []
    for num in nums:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result

# Test Cases
print(remove_duplicates([4, 5, 4, 6, 5, 7]))  # Output: [4, 5, 6, 7]
print(remove_duplicates([]))  # Output: []
print(remove_duplicates([1, 1, 1, 1]))  # Output: [1]
print(remove_duplicates([9,8,7]))  # Output: [9, 8, 7]

"""
Time and Space Analysis for problem 2:
- Best-case: O(n) has to go through every number 
- Worst-case: O(n) has to go through every number 
- Average-case: O(n) has to go through every number 
- Space complexity: O(n) because of storing the seen numbers and the result list
- Why this approach? Sets make checking duplicates really easy
- Could it be optimized? No
"""


# 🔍 Problem 3: Return All Pairs That Sum to Target
# Write a function that returns all unique pairs of numbers in the list that sum to a target.
# Order of output does not matter. Assume input list has no duplicates.
#
# Example:
# Input: ([1, 2, 3, 4], target=5)
# Output: [(1, 4), (2, 3)]

def find_pairs(nums, target):
    # Your code here
    seen = set()
    pairs = []

    for num in nums:
        needed = target - num
        if needed in seen:
            pairs.append((needed, num))
        seen.add(num)

    return pairs

# Test Cases
print(find_pairs([1, 2, 3, 4], 5))  # Output: [(1, 4), (2, 3)]
print(find_pairs([], 10))  # Output: []
print(find_pairs([10], 10))  # Output: []
print(find_pairs([2,4,6,8], 12))  # Output: [(4, 8)]
"""
Time and Space Analysis for problem 3:
- Best-case: O(n) only loop once through the list
- Worst-case: O(n) only loop once through the list
- Average-case: O(n) only loop once through the list
- Space complexity: O(n) because of storing the numbers in a set
- Why this approach? Sets avoid nested loops, also it keeps it simple
- Could it be optimized? No
"""


# 🔍 Problem 4: Simulate List Resizing (Amortized Cost)
# Create a function that adds n elements to a list that has a fixed initial capacity.
# When the list reaches capacity, simulate doubling its size by creating a new list
# and copying all values over (simulate this with print statements).
#
# Example:
# add_n_items(6) → should print when resizing happens.

def add_n_items(n):
    # Your code here
    capacity = 2
    items = []
    print(f"Starting capacity: {capacity}")

    for i in range(n):
        if len(items) == capacity:
            print(f"Resizing from {capacity} to {capacity * 2}")
            capacity *= 2
        items.append(i)

    return items

# Test Cases
add_n_items(6) 
add_n_items(1)
add_n_items(10)
"""
Time and Space Analysis for problem 4:
- When do resizes happen? When the list reaches its current capacity
- What is the worst-case for a single append? O(n) due to copying
- What is the amortized time per append overall? O(1)
- Space complexity: O(n) for storing the items
- Why does doubling reduce the cost overall? It makes resizing less frequent
"""


# 🔍 Problem 5: Compute Running Totals
# Write a function that takes a list of numbers and returns a new list
# where each element is the sum of all elements up to that index.
#
# Example:
# Input: [1, 2, 3, 4]
# Output: [1, 3, 6, 10]
# Because: [1, 1+2, 1+2+3, 1+2+3+4]

def running_total(nums):
    # Your code here
    total = 0
    result = []

    for num in nums:
        total += num
        result.append(total)

    return result

# Test Cases
print(running_total([1, 2, 3, 4]))  # Output: [1, 3, 6, 10]
print(running_total([]))  # Output: []
print(running_total([5]))  # Output: [5]
print(running_total([10, -5, 2]))  # Output: [10, 5, 7]

"""
Time and Space Analysis for problem 5:
- Best-case: O(n) has to go through every number
- Worst-case: O(n) has to go through every number
- Average-case: O(n) has to go through every number
- Space complexity: O(n) for storing the running totals
- Why this approach? It's simple and efficient, and works for any list
- Could it be optimized? No
"""

# Refactoring Problem 2
def remove_duplicates_refactored(nums):
    seen = {}
    result = []

    for num in nums:
        if num not in seen:
            seen[num] = True
            result.append(num)

    return result

"""
Explanation: The reason I changed to a dictionary is that a lookup is very fast
and lets me store the seen values and their marker in one place. This keeps the logic the same
but is more effiecient.
"""