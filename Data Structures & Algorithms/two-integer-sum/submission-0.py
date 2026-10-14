class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        summap={}
        for i,num in enumerate(nums):
            need=target-num

            if need in summap:
                return [summap[need],i]
            summap[num]=i
        