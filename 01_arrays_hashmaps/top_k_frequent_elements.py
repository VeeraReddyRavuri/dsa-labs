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
