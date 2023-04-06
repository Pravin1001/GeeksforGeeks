from typing import List


class Solution:
    def minimumInteger(self, N : int, A : List[int]) -> int:
        # code here
        sums=sum(A)
        l=[]
        for i in A:
            if sums<=N*i:
                l.append(i)
        return min(l)
