class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge_sort(arr):
            
            if len(arr) <= 1:
                return arr
            
            pivot=int(len(arr)/2)
            
            left=merge_sort(arr[0:pivot])
            right=merge_sort(arr[pivot:])
            
            return merge(left,right)
        
        def merge(arr1,arr2):
            
            leftbound=rightbound=0
            ret=[]
            
            while leftbound < len(arr1) and rightbound < len(arr2):
                if arr1[leftbound]<arr2[rightbound]:
                    ret.append(arr1[leftbound])
                    leftbound+=1
                else:
                    ret.append(arr2[rightbound])
                    rightbound+=1
                
            ret.extend(arr1[leftbound:])
            ret.extend(arr2[rightbound:])
            
            return ret
        
        return merge_sort(nums)
        
