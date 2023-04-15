from typing import List


class Solution:
    def finLength(self, N : int, color : List[int], radius : List[int]) -> int:
        # code here
        l=[]
        for i in range(N):
            if len(l)==0:
                l.append([color[i],radius[i]])
            elif l[-1][0]==color[i] and l[-1][1]==radius[i]:
                l.pop()
            else:
                l.append([color[i],radius[i]])
        return len(l)
            
        
