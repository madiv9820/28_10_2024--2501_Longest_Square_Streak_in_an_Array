from typing import List

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        
        # Helper function to perform binary search
        def binary_Search(X: int) -> bool:
            left_Most_Index, right_Most_Index = 0, len(nums) - 1  # Initialize left and right pointers

            # Binary search loop
            while left_Most_Index <= right_Most_Index:
                mid_Index = (left_Most_Index + right_Most_Index) // 2  # Find the middle index
                
                if nums[mid_Index] == X:  # If the middle element is the target
                    return True
                elif nums[mid_Index] > X:  # If the middle element is greater than the target
                    right_Most_Index = mid_Index - 1  # Search in the left half
                else:  # If the middle element is less than the target
                    left_Most_Index = mid_Index + 1  # Search in the right half
            
            return False  # Target not found

        # Initialize the longest streak to -1 (indicating no streak found yet)
        longest_Streak = -1
        # Sort the input list for binary search
        nums.sort()
        # Set to keep track of processed numbers
        processed_Numbers = set()  

        # Iterate through each number in the sorted list
        for num in nums:
            # Skip if the number has already been processed
            if num in processed_Numbers:  
                continue

            # Initialize current streak with the current number
            current_Streak = 1  
            
            while True:
                # Break the loop if the square exceeds 100,000, the streak reaches 5, or the square is not found
                if num ** 2 > 10**5 or current_Streak == 5 or not binary_Search(X=num ** 2):
                    break
                else:
                    # Increment the streak for each valid square found
                    current_Streak += 1
                    processed_Numbers.add(num)  # Mark the number as processed
                    num **= 2  # Update the current number to its square
            
            # Update the longest streak found so far
            longest_Streak = max(longest_Streak, current_Streak)
        
        # Return -1 if no valid streak is found (less than 2), otherwise return the longest streak
        return -1 if longest_Streak < 2 else longest_Streak