class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        output = []
        for i in nums:
            if i not in hashmap.keys():
                hashmap[i] = 1
            else:
                hashmap[i] += 1
        listing = list(hashmap.keys())
        listing.sort()
        for i in range(0, k):
            output.append(listing[i])
        return(output)