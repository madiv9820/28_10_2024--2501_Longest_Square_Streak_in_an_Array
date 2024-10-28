- ## Using Dictionary/Maps

    - ### Intuition
        - The goal is to find the longest sequence of numbers in the list where each number is a perfect square of its predecessor. For example, if a number is `4`, the previous number in the sequence could be `2`, since \(2^2 = 4\). We aim to identify these relationships and count the lengths of the resulting sequences, ultimately returning the length of the longest sequence found.

    - ### Approach
        1. **Initialization**:
            - Create a dictionary `streak_Lengths` to store the length of the streak for each number.
            - Sort the input list `nums` to ensure we process numbers in ascending order.

        2. **Iteration**:
            - For each number in the sorted list:
                - Calculate its integer square root.
                - Check if the current number is a perfect square (i.e., if the square of the square root equals the number) and if the square root exists in the `streak_Lengths` dictionary.
                - If both conditions are true, set the streak length of the current number to one more than the streak length of its square root.
                - If not, initialize the streak length of the current number to `1`.

        3. **Finding the Longest Streak**:
            - Use the `max()` function to find the longest streak length from the values in the `streak_Lengths` dictionary, with a default of `0` to handle empty cases.

        4. **Return Result**:
            - If the longest streak is less than `2`, return `-1` (indicating no valid streak was found). Otherwise, return the length of the longest streak.

    - ### Time Complexity
        - The overall time complexity is **O(n log n)** due to the sorting step, where `n` is the number of elements in `nums`. The iteration through the list is **O(n)**, making the sorting step the dominant factor.

    - ### Space Complexity
        - The space complexity is **O(n)** for storing the streak lengths in the `streak_Lengths` dictionary.
    
    - ### Code
        ```python3 []
        class Solution:
            def longestSquareStreak(self, nums: List[int]) -> int:
                # Dictionary to store the length of streaks for each number
                streak_Lengths = {}
                
                # Sort the input list to process numbers in increasing order
                nums.sort()

                # Iterate through each number in the sorted list
                for num in nums:
                    # Calculate the integer square root of the current number
                    sq_root = int(num ** 0.5)
                    
                    # Check if the current number is a perfect square and if its square root exists in streak_Lengths
                    if sq_root * sq_root == num and sq_root in streak_Lengths.keys():
                        # If so, the streak length for the current number is the streak length of its square root plus one
                        streak_Lengths[num] = streak_Lengths[sq_root] + 1
                    else:
                        # If not, initialize the streak length for the current number to 1
                        streak_Lengths[num] = 1

                # Find the maximum streak length from the streak_Lengths dictionary
                longest_Streak = max(streak_Lengths.values(), default = 0)
                
                # Return -1 if no valid streak is found (less than 2), otherwise return the longest streak
                return -1 if longest_Streak < 2 else longest_Streak
        ```