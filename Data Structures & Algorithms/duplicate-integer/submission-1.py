class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #make a hashmap
        hashmap={}
        for item in nums:
            if item in hashmap:
                return True
            else:
                hashmap[item]=1
        return False
