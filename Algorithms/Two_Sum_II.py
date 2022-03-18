######## Binary approach #################


class Solution:
    def twoSum(self, numbers, target):
        for i in range(len(numbers)):
            l, r = i+1, len(numbers)-1
            tmp = target - numbers[i]
            while l <= r:
                mid = l + (r-l)//2
                if numbers[mid] == tmp:
                    return [i+1, mid+1]
                elif numbers[mid] < tmp:
                    l = mid+1
                else:
                    r = mid-1


## O(nlogn) time and O(1) space


######### Using dictionary #################


class Solution:
    def twoSum(self, numbers, target):
        dic = {}
        for i, num in enumerate(numbers):
            if target-num in dic:
                return [dic[target-num]+1, i+1]
            dic[num] = i

            
## O(n) time and O(n) space


######## Using two pointer #################


'''

Explanation:
The array is sorted in increasing order.
So, incresing left index gives bigger number and decresing right index gives smaller number.
We start with left index as the 1st index and right index as the last index of the array.
Calculate the sum of the two elements at the two indices.
If it is greater than the target, that means we have to decrese the sum. So, we decrement the right index.
If it is lesser than the target, that means we have to increse the sum. So, we inrement the left index.
Continue this process untill the sum is equal to the target.


'''



class Solution:
    def twoSum(self, numbers, target):
        l, r = 0, len(numbers)-1
        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l+1, r+1]
            elif s < target:
                l += 1
            else:
                r -= 1
                
                
## Reducing the code length

class Solution:
    def twoSum(self, nums, target):
        l, r = 0, len(nums) - 1
        while l < r:
            if nums[l] + nums[r] == target: return (l + 1,  r + 1)
            if nums[l] + nums[r] > target: r -= 1
            else: l += 1
                
## O(n) time and O(1) space



################## Another solution ################


class Solution:
    def twoSum(self, numbers, target):
        f, l = 0, len(numbers)-1;
        while numbers[f]+numbers[l] != target:
            if numbers[f]+numbers[l] > target:
                l -= 1;
            else:
                f +=1;
        return [f+1,l+1]
      
      
      
      
