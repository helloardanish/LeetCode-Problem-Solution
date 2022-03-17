############## O(n) Solution ################

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        for i in range(len(nums)):
            if target <= nums[i]:
                return i;
        return len(nums)
        
        
        
################## Another O(n) solution ################################

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        nums = [x for x in nums if x < target]
        return len(nums)
        
        
############################## Binary Approach #########################

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, u = 0, len(nums)-1
        while l<=u:
            mid = l + (u- l)//2
            if nums[mid]>target :
                u = mid - 1
            elif nums[mid]<target:
                l = mid + 1
            else:
                return mid     
        return l
        
        
