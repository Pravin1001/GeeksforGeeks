from typing import List

class Solution:
    def makeBeautiful(self, arr: List[int]) -> List[int]:
        # code here
        l=[]
        for i in arr:
            if len(l)==0:
                l.append(i)
            else:
                if(l[-1]<0 and i>=0) or (l[-1]>=0 and i<0):
                    l.pop()
                else:
                    l.append(i)
        return l
