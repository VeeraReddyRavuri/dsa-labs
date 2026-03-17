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