'''


The idea is to reverse the given list, and then reverse elements in the range 0..k and in the range k..L. For example nums = [1,2,3,4,5,6,7], k = 3:

Reverse: nums = [7,6,5,4,3,2,1]
Reverse in the range 0..k: nums = [5,6,7,4,3,2,1]
Reverse in the range k..L: nums = [5,6,7,1,2,3,4]
Notice that k can be greater than L (length of the nums) because k is number of rotattion steps. If k is equal to L, elements do full rotation and nums is not changed. So for this case we can recalculate k as k%L.

Time: O(n) - for reverse and swaps
Space: O(1) - in-place



'''


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        L = len(nums)
        if L == k: return

        k = k%L # the case when k > L
        nums.reverse()

        for i in range(k//2):
            nums[i], nums[k-1-i] = nums[k-1-i], nums[i]

        for i in range(k, (L+k)//2):
            nums[i], nums[L-1-i+k] = nums[L-1-i+k], nums[i]
    
    
    
########################### Another solution #########################


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def inverse(i, j):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i, j = i + 1, j - 1
        
        n = len(nums)
        k = k % n
        inverse(0, n-1)
        inverse(0, k-1)
        inverse(k, n-1)
        return nums
      
      
      
      
      
      
      
      
'''

Classical 3-step array rotation:

1. reverse the first n - k elements
2. reverse the rest of them
3. reverse the entire array


'''

class Solution(object):
    def rotate(self, nums, k):
        if k is None or k <= 0:
            return
        k, end = k % len(nums), len(nums) - 1
        self.reverse(nums, 0, end - k)
        self.reverse(nums, end - k + 1, end)
        self.reverse(nums, 0, end)
        
    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start + 1, end - 1
