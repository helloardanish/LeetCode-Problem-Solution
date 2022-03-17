class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        l=len(A)+len(B)
        return self.findKth(A,B,l//2) if l%2==1 else (self.findKth(A,B,l//2-1)+self.findKth(A,B,l//2))/2.0
            
            
    def findKth(self,A,B,k):
        if len(A)>len(B):
            A,B=B,A
        if not A:
            return B[k]
        if k==len(A)+len(B)-1:
            return max(A[-1],B[-1])
        i=len(A)//2
        j=k-i
        if A[i]>B[j]:
            #Here I assume it is O(1) to get A[:i] and B[j:]. In python, it's not but in cpp it is.
            return self.findKth(A[:i],B[j:],i)
        else:
            return self.findKth(A[i:],B[:j],j)
            
            
            
########################## Another solution   #################################


class Solution:
    def findMedianSortedArrays(self, arr1: List[int], arr2: List[int]) -> float:
        x=len(arr1)
        y=len(arr2)
        if x>y:
            return self.findMedianSortedArrays(arr2,arr1)
        low=0
        high=x
        while(low<=high):
            #print(low)
            partitionX=int((low+high)/2)

            partitionY=int(((x+y+1)//2 )-partitionX)
            maxLeftX= float('-inf') if partitionX==0 else arr1[partitionX-1]
            minRightX=float('inf') if partitionX==x else arr1[partitionX]
            maxLeftY = float('-inf') if partitionY == 0 else arr2[partitionY - 1]
            minRightY =  float('inf') if partitionY == y else arr2[partitionY]
            if maxLeftX<=minRightY and maxLeftY<=minRightX:
                if (x+y) %2 ==0:
                    return (max(maxLeftX,maxLeftY) + min(minRightX,minRightY))/2
                else:
                    return max(maxLeftY,maxLeftX)
            elif(maxLeftX>minRightY):
                high=partitionX-1
            else:
                low=partitionX+1

