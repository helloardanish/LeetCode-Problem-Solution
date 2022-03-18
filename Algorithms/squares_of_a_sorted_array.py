############ simple solution #####################

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        org_lst=[]
        for num in nums:
            temp=num*num
            org_lst.append(temp)
        return sorted(org_lst)
        
        
        
######## But we have to use two pointers to solve this problem



def sortedSquares(self, A):
    answer = collections.deque()
    l, r = 0, len(A) - 1
    while l <= r:
        left, right = abs(A[l]), abs(A[r])
        if left > right:
            answer.appendleft(left * left)
            l += 1
        else:
            answer.appendleft(right * right)
            r -= 1
    return list(answer)
  
######## Same approach ################################
  
  
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        result = [None for _ in A]
        left, right = 0, len(A) - 1
        for index in range(len(A)-1, -1, -1):
            if abs(A[left]) > abs(A[right]):
                result[index] = A[left] ** 2
                left += 1
            else:
                result[index] = A[right] ** 2
                right -= 1
        return result
      
