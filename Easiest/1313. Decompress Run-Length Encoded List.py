class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        l = []
        for i in range(0,len(nums),2):
            k = nums[i]
            for j in range(k):
                l.append(nums[i+1])
        
        return l
