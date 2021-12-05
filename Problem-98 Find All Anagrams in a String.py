# 438. Find All Anagrams in a String
# https://leetcode.com/problems/find-all-anagrams-in-a-string/

# Logic: Make a count hashmap of p. Iterate over s. 
# Reduce count in hashmap if the current element is 
# in hashmap. If the count goes to zero, increase 
# match. When match equals the length of hashmap 
# append correct idx in the result.

# Time Complexity: O(n)
# Space Complexity: O(len{p}) [for hashmap]

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        hashmap = dict()
        res = list()
        
        # Make count hashmap for p
        for i in p:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i] += 1
        
        match = 0
        # iterate over s
        for idx, i in enumerate(s):
            if i in hashmap:
                hashmap[i] -= 1
                if hashmap[i] == 0:
                    match += 1
            
            if idx >= len(p):
                if s[idx-len(p)] in hashmap:
                    if hashmap[s[idx-len(p)]] == 0:
                        match -= 1
                    hashmap[s[idx-len(p)]] += 1
            
            if match == len(hashmap):
                res.append(idx-len(p)+1)
        return res