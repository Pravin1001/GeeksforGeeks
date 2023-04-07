class Solution:
    def addMinChar (self, str1):
        # code here
        l=len(str1)-1
        i,j=0,l
        while i<j:
            if str1[i]==str1[j]:
                i+=1
            else:
                j,i=l,0
                l-=1
            j-=1
        return len(str1)-l-1
