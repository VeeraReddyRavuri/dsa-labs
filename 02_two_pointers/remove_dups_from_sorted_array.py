def remove_dups(nums):
    slow = 1
    for fast in range(1, len(nums)):
        if nums[fast] != nums[fast-1]:
            nums[slow] = nums[fast]
            slow += 1
    return slow