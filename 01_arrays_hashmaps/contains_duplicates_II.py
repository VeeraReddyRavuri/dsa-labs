"""
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
"""

def contains_duplicates_II(nums, k):
    seen = {}

    for i in range(len(nums)):
        current_num = nums[i]

        if current_num in seen:
            distance = i - seen[current_num]

            if distance <= k:
                return True
        seen[current_num] = i
    return False

nums = [1,2,3,1,2,3]
k = 2
print(contains_duplicates_II(nums, k))