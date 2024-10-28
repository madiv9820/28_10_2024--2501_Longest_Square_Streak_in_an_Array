- ## Binary Search

    - ### Intuition
        - The problem seeks to find the longest sequence of numbers where each number is the square of the previous one. By iterating through the list of numbers and using a binary search to check for the existence of squares, we can efficiently track how many valid squares exist in the input. The algorithm also uses a set to keep track of processed numbers, preventing duplicate calculations.

    - ### Approach
        1. **Binary Search**: Implement a binary search function to efficiently check if the square of a number exists in the sorted list.

        2. **Sort the List**: Sort the input list to enable binary search.

        3. **Process Each Number**: For each number in the list:
            - If the number has already been processed, skip it.
            - Initialize a streak counter.
            - Continuously check for the square of the current number:
                - If the square exists and does not exceed (10<sup>5</sup>), increment the streak.
                - Mark the number as processed and update the current number to its square.
                - Break the loop if the square is not found, exceeds (10<sup>5</sup>), or if the streak reaches 5.

        4. **Update Longest Streak**: After processing each number, update the longest streak found.

        5. **Return the Result**: Finally, return the longest streak found, or -1 if no valid streak exists.

    - ### Time Complexity
        - __Sorting:__ The sorting operation takes __O(nlogn)__, where n is the number of elements in the list.
        - __Binary Search:__ Each binary search operation takes __O(logn)__.
        - __Main Loop:__ In the worst case, we may process each element and check its squares repeatedly, resulting in a time complexity of __O(nlogn)__ overall due to the combination of sorting and binary searching.

    - ### Space Complexity
        - The primary space usage comes from the set of processed numbers and the sorted list, leading to a space complexity of __O(n)__. The auxiliary space for variables remains constant, __O(1)__.

    - ### Code
        ```python3 []
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

                processed_Numbers = set()  # Set to keep track of processed numbers

                # Iterate through each number in the sorted list
                for num in nums:
                    if num in processed_Numbers:  # Skip if the number has already been processed
                        continue

                    current_Streak = 1  # Initialize current streak with the current number
                    
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
        ```