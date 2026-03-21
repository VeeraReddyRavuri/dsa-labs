"""Given an integer array nums, return True if a value appears at least twice
 or else return False"""

def contains_duplicate(nums):
    #create a hash set to store every element we have seen
    seen = set()    

    #iterate through each num in the list
    for num in nums:    
        #if we found the number in the hash set, we return True and exit function.
        if num in seen:   
            return True  
        #if number is not in the hash set we add to the hash set for future reference
        seen.add(num)   
    #if loop exits with out returing then only unique elements remain and we return False.
    return False   

"""nums = [1, 2, 3, 8, 9, 10]
result = contains_duplicate(nums)
print(result)"""




"""
----- Leet code -----

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.

Example 2:

Input: nums = [1,2,3,4]

Output: false

Explanation:

All elements are distinct.

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]

Output: true

 class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


"""