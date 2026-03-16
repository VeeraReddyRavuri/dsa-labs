"""
You are given an array of integers nums and an integer target. 
Return the indices (the position numbers) of the two numbers that add up to the target. 
You may assume that each input would have exactly one solution, 
and you may not use the same element twice.
"""

def two_sum(nums, target):
    diff = {}

    for i in range(len(nums)):
        #What number do we need to hit the target?
        complement = target - nums[i]

        if complement in diff:
            # Return [past_index, current_index]
            return [diff[complement], i]
        # If we didn't find it, store the current number and its index for the future
        diff[nums[i]] = i