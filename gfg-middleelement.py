class Solution:
    def middle(self,A,B,C):
        #code here
        l=[]
        l.append(A)
        l.append(B)
        l.append(C)
        l.sort()
        return l[1]
