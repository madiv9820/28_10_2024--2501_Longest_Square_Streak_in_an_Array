- ## Optimized Brute Force Implementation (Using Set or Dictionaries / Maps)

    - ### Intuition
        - The problem aims to find the longest sequence of numbers in which each number is the square of the previous one. By starting from each number and repeatedly squaring it, we can explore how many valid squares exist in the input list. Using a set for quick lookups allows us to efficiently check for the presence of squares.

    - ### Approach
        1. **Set for Fast Lookup**: Create a dictionary to store the presence of numbers for quick lookups.
        
        2. **Sort the List**: Sort the input list to process the numbers in increasing order.

        3. **Iterate Through Each Number**: For each number in the sorted list:
            - Initialize a streak counter. If a valid square is found, start counting.
            - While the square of the current number exists in the set, keep squaring the number and incrementing the streak counter.
        
        4. **Update Longest Streak**: After processing each number, compare the current streak with the longest streak found so far.

        5. **Return the Result**: Finally, return the longest streak found. If no streak is found, return -1.

    - ### Time Complexity
        
        - __Sorting:__ The sorting operation takes __O(nlogn)__, where __n__ is the number of elements in the list.

        - __Iteration and Searching:__ For each element, we may need to search for its square in the set, which can take __O(n)__ in the worst case. Since this search occurs for each element, the overall complexity becomes __O(n<sup>2</sup>)__.

    - ### Space Complexity
        - The primary space usage comes from storing the set of numbers, leading to a space complexity of __O(n)__. The auxiliary space for variables remains constant, __O(1)__.

    - ### Code
        ```python3 []
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
        ```