class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mapping1 = {}
        mapping2 = {}
        for char in s:
            if char not in mapping1:
                mapping1[char] = 1
            else:
                mapping1[char] += 1
        for char in t:
            if char not in mapping2:
                mapping2[char] = 1
            else:
                mapping2[char] += 1  
        return mapping1 == mapping2 
