"""
You are given an integer array nums and an integer k.
Return the k most frequent elements. You may return the answer in any order.

Example:

    nums = [1, 1, 1, 2, 2, 3]

    k = 2

    Output: [1, 2] (Because 1 appears three times, and 2 appears twice. They are the top 2 most frequent).
"""

def top_k(nums, k):
    kd = {}
    for num in nums:
        kd[num] = kd.get(num, 0) + 1
    
    # Sort by frequency (the value) in descending order
    sorted_kd = sorted(kd.items(), key=lambda x: x[1], reverse=True)

    # Slice the first 'k' elements, and extract just the key (item[0])
    return [item[0] for item in sorted_kd[:k]]
    
nums = [1, 1, 1, 2, 2, 3]
k = 2
result = top_k(nums, k)
print(result)


"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2

Output: [1,2]

Example 2:

Input: nums = [1], k = 1

Output: [1]

Example 3:

Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2

Output: [1,2]

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}

        for num in nums:
            hash_map[num] = hash_map.get(num, 0) + 1
        sorted_hash_map = sorted(hash_map.items(), key=lambda x:x[1], reverse=True)
        return [item[0] for item in sorted_hash_map[:k]]
"""
