# Longest Square Streak in an Array (All Approaches)

- ## Brute Force Implementation (Time Limit Exceeded)

    - ### Intuition
        - The goal of this problem is to find the longest sequence of numbers where each number is the square of the previous one. To achieve this, we leverage the properties of squares and the relationship between the numbers. By starting with each number and repeatedly squaring it, we can determine how many valid squares exist in the list.

    - ### Approach
        1. **Sort the List**: We begin by sorting the input list. Sorting helps in efficiently checking for the presence of squares in the list.
        
        2. **Iterate Through Each Number**: For each number in the sorted list:
            - Initialize a streak counter. If we find a valid square, we start counting.
            - While the square of the current number exists in the list, we keep squaring the number and incrementing the streak counter.
        
        3. **Update Longest Streak**: After processing each number, we compare the current streak with the longest streak found so far.

        4. **Return the Result**: Finally, return the longest streak found. If no streak is found, return -1.

    - ### Time Complexity
        - **Sorting:** The sorting operation takes __O(nlogn)__, where __n__ is the number of elements in the list.

        - **Iteration and Searching:** For each element, we may need to search for its square in the list, which can take __O(n)__ in the worst case. Since we do this for each element, the overall complexity becomes __O(n<sup>2</sup>)__.

    - ### Space Complexity
        - The primary space usage comes from storing the sorted list, leading to a space complexity of __O(n)__. Additionally, the auxiliary space for variables remains constant, __O(1)__.

    - ### Code
        ``` python3[]
        class Solution:
            def longestSquareStreak(self, nums: List[int]) -> int:
                # Initialize the longest streak to -1 (indicating no streak found yet)
                longest_Streak = -1
                
                # Sort the list of numbers
                nums.sort()

                # Iterate through each number in the sorted list
                for index in range(len(nums)):
                    current_Element = nums[index]  # Current number to check for square streak
                    current_Streak = -1  # Initialize current streak for this element
                    
                    # Continue while the square of the current element is in the list
                    while current_Element ** 2 in nums:
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