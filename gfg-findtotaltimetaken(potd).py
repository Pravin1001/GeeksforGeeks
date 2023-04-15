from typing import List


class Solution:
    def totalTime(self, n : int, arr : List[int], time : List[int]) -> int:
        # code here
        d={arr[0]:1}
        c=0
        for i in range(1,n):
            if arr[i] in d:
                c+=time[arr[i]-1]
            else:
                c+=1
                d[arr[i]]=1
        return c
