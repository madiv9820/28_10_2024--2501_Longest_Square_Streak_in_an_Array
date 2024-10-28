# 2501. Longest Square Streak in an Array

__Type:__ Medium <br>
__Companies:__ Amazon <br>
__Type:__ Array, Hash Table, Binary Search, Dynamic Programming, Sorting <br>
__LeetCode Link:__ [Longest Square Streak in an Array](https://leetcode.com/problems/longest-square-streak-in-an-array) <br>
<hr>

You are given an integer array `nums`. A subsequence of `nums` is called a __square streak__ if:
- The length of the subsequence is at least `2`, and
- __after__ sorting the subsequence, each element (except the first element) is the __square__ of the previous number.

Return the length of the __longest square streak__ in `nums`, or return `-1` if there is no __square streak__.

A __subsequence__ is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.
<hr>

### Examples

- __Example 1:__<br>
    __Input:__ nums = [4,3,6,16,8,2]<br>
    __Output:__ 3<br>
    __Explanation:__ Choose the subsequence [4,16,2]. After sorting it, it becomes [2,4,16].<br>- 4 = 2 * 2.<br>- 16 = 4 * 4.<br>
    Therefore, [4,16,2] is a square streak.<br>
    It can be shown that every subsequence of length 4 is not a square streak.

- __Example 2:__ <br>
    __Input:__ nums = [2,3,5,6,7] <br>
    __Output:__ -1 <br>
    __Explanation:__ There is no square streak in nums so return -1.
<hr>

### Constraints:
- <code>2 <= nums.length <= 10<sup>5</sup></code>
- <code>2 <= nums[i] <= 10<sup>5</sup></code>
<hr>

### Hints:
- With the constraints, the length of the longest square streak possible is 5.
- Store the elements of nums in a set to quickly check if it exists.