###################### simple solution ##################



class Solution:
    def moveZeroes(self, nums: list) -> None:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0 and nums[slow] == 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]

            # wait while we find a non-zero element to
            # swap with you
            if nums[slow] != 0:
                slow += 1
                
                
                
##################

'''
Main idea
We usei to keep track of position of the first zero in the list (which changes as we go).
We usejto keep track of the first non-zero value after the first zero (which is pointed by i).
Each time we havei correctly points to a zero and j correctly points to the first non-zero after i, we swap the values that store at i and j.
By doing this, we move zeros towards the end of the list gradually until j reaches the end.
And when it does, we are done.

Remarks
No return value needed, since we are doing in-place modification.
We usenums[i], nums[j] = nums[j], nums[i] to achieve the in-place modification because Python allows you to swaps values in a list using syntax: x, y = y, x.

'''

class Solution:
    def moveZeroes(self, nums):
        n = len(nums)
        i = 0
        for j in range(n):
            if (nums[j] != 0):
                nums[i], nums[j] = nums[j], nums[i]
                i += 1

        
        
        
########### Another solution ##############


        
class Solution(object):
    def moveZeroes(self, nums):
        if len(nums) > 0:
            count = nums.count(0)
            nums[:] = (value for value in nums if value != 0)
            nums.extend([0] * count)
