class Solution:    
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
       
        if N==1:
            return [0,1,2,3,4,5,6,7,8,9]
        answer=[]
            
        def backtrack(buf):
            
            if len(buf)==N:
                answer.append(int(buf))
                return
            
            curr=buf[-1]

            if int(curr)+K <= 9:
                backtrack(buf+str(int(curr)+K))

            if int(curr)-K >= 0 and K>0:
                backtrack(buf+str(int(curr)-K))
                
        for digit in range(1,10):
            buf=str(digit)
            backtrack(buf)
            
        return answer    
