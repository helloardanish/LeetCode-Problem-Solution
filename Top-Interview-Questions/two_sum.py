##### Simplest approach #############
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            findval = target - nums[i];
            for j in range(len(nums)):
                #if nums[i]==nums[j]: // because index shouldn't be same but their  value can be
                if i==j:
                  continue;
                if nums[j]==findval:
                    return [i,j]
                  
                  
## But time compelexity O(n^2)


##################### Complex approach ################################

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            if target-nums[i] in nums[i+1:]:
                first=nums[i]
                nums[i]=-1000000001
                return i,nums.index(target-first)
        return -1
      
########## O(n) #################


############## Using dictionary-hashmap ####################33


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, n in enumerate(nums):
            m = target - n
            if m in d:
                return [d[m], i]
            else:
                d[n] = i
                
                
############## To understand easily ################3


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rev_table = dict()
        for i in range(len(nums)):
        	second_addend = target - nums[i]
        	if second_addend in rev_table:
        		return [rev_table[second_addend], i]
        	else:
        		rev_table[nums[i]] = i
                
                
###############    Both O(n) Solution #######################
