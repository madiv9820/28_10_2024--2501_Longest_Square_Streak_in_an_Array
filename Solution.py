from typing import List

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