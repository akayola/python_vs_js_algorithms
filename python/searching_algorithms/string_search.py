"""
   Searching sub-string using nested loop.
   O(n**2) - quadratick runtime complexity (BAD SOLUTION!!!)
   Pseudocode:
   1. Loop over string
   2. Loop over pattern string
   3. If the charactes don't match, break out inner loop.
   4. If the characters match, keep going.
   5. If searching inner loop complete and foud match, increment cout.
   6. Return count.
"""

def string_search_nested_loop(long, pattern):
    count = 0

    for i in range(len(long) - 1):
        for j in range(len(pattern)):
            print(f'{long[i]}, {pattern[j]}, {i}, {j}')
            if pattern[j] != long[i+j]:
                print("BREAK!")
                break
            # Increment count if j is equal to pattern length.
            if j == len(pattern) - 1:
                print(f'found match, {j}')
                count += 1

    return count

print(string_search_nested_loop("create lollipop charts with pandas, matplotlib and lol", "lol"))
