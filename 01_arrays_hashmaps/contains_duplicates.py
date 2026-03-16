"""Given an integer array nums, return True if a value appears at least twice
 or else return False"""

def contains_duplicate(nums):
    seen = set()    #create a hash set to store every element we have seen

    for num in nums:    #iterate through each num in the list
        if num in seen:   #if we found the number in the hash set, we return True and exit function.
            return True     #this triggers instant lookup O(1)     
        seen.add(num)   #if number is not in the hash set we add to the hash set for future reference

    return False    #if loop exits with out returing then only unique elements remain and we return False.

"""nums = [1, 2, 3, 8, 9, 10]
result = contains_duplicate(nums)
print(result)"""