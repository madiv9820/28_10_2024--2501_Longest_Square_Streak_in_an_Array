- ## Using Set

    - ### Intuition
        - The goal is to find the longest sequence of numbers starting from a given number `num` where each subsequent number is the square of the previous one. The sequence can continue as long as the squared number exists in the input list of numbers and does not exceed `100,000`. The length of this sequence is termed a "streak." We want to find the longest streak for any starting number in the list.

    - ### Approach
        1. **Initialization**:
        - Create a variable `longest_Streak` to keep track of the longest streak found.
        - Convert the input list `nums` into a set `unique_Numbers` for O(1) average-time complexity lookups.

        2. **Iteration**:
        - For each number in the original list, initialize a counter `current_Streak` to track the length of the current streak.
        - Use a while loop to continue checking for the squared values as long as:
                - The current number is in the set of unique numbers.
                - The number does not exceed `100,000`.
                - The current streak is less than `5`.
        - Increment the `current_Streak` for each valid number and update `num` to its square for the next iteration.

        3. **Update Longest Streak**:
            - After processing each number, compare `current_Streak` with `longest_Streak` and update it if necessary.

        4. **Return Result**:
            - If `longest_Streak` is less than `2`, return `-1` (indicating no valid streak was found). Otherwise, return `longest_Streak`.

    - ### Time Complexity
        - The overall time complexity is **O(n * k)**, where:
            - `n` is the number of elements in `nums`.
            - `k` is the maximum length of a streak that can be formed, which is limited by how many times you can square a number before exceeding `100,000` (in practice, it’s generally small).

    - ### Space Complexity
        - The space complexity is **O(n)** for storing the unique numbers in a set.
    
    - ### Code
        ```python3 []
        class Solution:
            def longestSquareStreak(self, nums: List[int]) -> int:
                # Initialize the longest streak to 0 (no streak found yet)
                longest_Streak = 0
                
                # Create a set of unique numbers for quick lookup
                unique_Numbers = set(nums)

                # Iterate through each number in the original list
                for num in nums:
                    current_Streak = 0  # Initialize the current streak counter

                    # Continue while the current number is present in the set of unique numbers
                    while num in unique_Numbers:
                        # Break the loop if the number exceeds 100,000 or the streak reaches 5
                        if num > 10**5 or current_Streak == 5:
                            break

                        # Increment the current streak for a valid number
                        current_Streak += 1
                        # Update the current number to its square for the next iteration
                        num **= 2

                    # Update the longest streak found so far
                    longest_Streak = max(longest_Streak, current_Streak)

                # Return -1 if no valid streak is found (less than 2), otherwise return the longest streak
                return -1 if longest_Streak < 2 else longest_Streak
        ```