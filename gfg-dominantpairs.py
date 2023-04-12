from typing import List


class Solution:
    def dominantPairs(self, n : int, arr : List[int]) -> int:
        # code here
        t=n//2
        arrl=sorted(arr[:t])
        arrr=sorted(arr[t:])
        for i in range(len(arrr)):
            arrr[i]=arrr[i]*5
        c=i=j=0
        while i<t and j<t:
            if arrl[i]>=arrr[j]:
                c+=t-i
                j+=1
            else:
                i+=1
        return c
