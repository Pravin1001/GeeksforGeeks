class Solution:
    def commonElements (self,A, B, C, n1, n2, n3):
        # your code here
        sa,sb,sc=set(A),set(B),set(C)
        sd=sa.intersection(sb,sc)
        l=list(sd)
        l.sort()
        return l
