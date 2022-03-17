class Solution:
    def search(self, nums: List[int], target: int) -> int:
        found = False;
        i=0;
        for num in nums:
            if num==target:
                found=True;
                break;
            i+=1;
        if(found):
            return i;
        else:
            return -1;
        
        
