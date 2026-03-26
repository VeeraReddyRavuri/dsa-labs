"""
You are given an integer array nums sorted in non-decreasing order.
 Remove the duplicates in-place (meaning O(1) extra memory) such that 
 each unique element appears only once. 
 The relative order of the elements should be kept the same. 
 Return k, which is the number of unique elements.
"""

def remove_dups(nums):
    slow = 1
    for fast in range(1, len(nums)):
        if nums[fast] != nums[fast-1]:
            nums[slow] = nums[fast]
            slow += 1
    return slow