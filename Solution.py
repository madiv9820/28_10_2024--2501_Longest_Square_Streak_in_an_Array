from typing import List

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