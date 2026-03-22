from collections import defaultdict

"""
The Problem: Group Anagrams

You are given an array of strings called strs.
Group the anagrams together. You can return the answer in any order.

Example:

    Input: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

    Output: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
"""

def group_anagrams(strs):
    # Initialize our master dictionary where every value defaults to an empty list
    anagram_map = defaultdict(list)

    for word in strs:
        # Sort the word to create the universal signature.
        # sorted() returns a list like ['a', 'e', 't'], so we join it back into a string "aet"
        sorted_word = "".join(sorted(word))

        # Append the ORIGINAL word to the list belonging to that sorted key
        anagram_map[sorted_word].append(word)
    
    # We only need to return the groups (the values), we don't need the keys anymore
    return list(anagram_map.values())

"""
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = group_anagrams(strs)
print(result)
"""

"""
Given an array of strings strs, group the together. You can return the answer in any order.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

    There is no string in strs that can be rearranged to form "bat".
    The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
    The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]


from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)

        for word in strs:
            sorted_word = "".join(sorted(word))
            hash_map[sorted_word].append(word)
        return list(hash_map.values())

"""