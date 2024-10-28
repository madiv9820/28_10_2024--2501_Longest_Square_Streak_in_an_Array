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