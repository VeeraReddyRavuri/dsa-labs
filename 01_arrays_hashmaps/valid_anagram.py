"""
Valid Anagram: You are given two strings, s and t. 
Return True if t is an anagram of s, and False otherwise. 
An Anagram is a word formed by rearranging the letters of a different word, 
using all the original letters exactly once.
"""

def valid_anagram(s, t):
    #if length is not equal it cannot be an anagram
    if len(s) != len(t):
        return False
    
    sd = {}
    td = {}
    #loop throgh the length of characters
    for i in range(len(s)):
        #if its not is sd or td, the below line add the key and set its value to 1.
        #if its present it will increment its value
        sd[s[i]] = sd.get(s[i], 0) + 1
        td[t[i]] = td.get(t[i], 0) + 1
    
    return sd == td

"""
result = valid_anagram("anagram", "nagaram")
print(result)
"""



"""
----- Leet code -----

Given two strings s and t, return true if t is an of s, and false otherwise.

 

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_hash_map = {}
        t_hash_map = {}

        for i in range(len(s)):
            s_hash_map[s[i]] = s_hash_map.get(s[i], 0) + 1
            t_hash_map[t[i]] = t_hash_map.get(t[i], 0) + 1

"""