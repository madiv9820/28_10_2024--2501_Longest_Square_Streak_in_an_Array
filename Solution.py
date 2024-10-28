from typing import List

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        # Initialize the longest streak to -1 (indicating no streak found yet)
        longest_Streak = -1
        
        # Create a set for quick lookup of numbers in the list
        is_num_Present = {num: True for num in nums}
        
        # Sort the list of numbers
        nums.sort()

        # Iterate through each number in the sorted list
        for index in range(len(nums)):
            current_Element = nums[index]  # Current number to check for square streak
            current_Streak = -1  # Initialize current streak for this element
            
            # Continue while the square of the current element is present in the set
            while current_Element ** 2 in is_num_Present.keys():
                # If this is the first square found, start the streak at 2
                if current_Streak == -1:
                    current_Streak = 2  # Streak of at least 2 (the number and its square)
                else:
                    # Increment the streak for each subsequent square found
                    current_Streak += 1
                
                # Update the current element to its square for the next iteration
                current_Element **= 2
            
            # Update the longest streak found so far
            longest_Streak = max(longest_Streak, current_Streak)

        # Return the longest square streak found, or -1 if none exists
        return longest_Streak