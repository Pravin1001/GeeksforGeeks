class Solution:
    
    #Function to reverse words in a given string.
    def reverseWords(self,S):
        # code here 
        l=list(S.split('.'))
        l.reverse()
        a='.'.join(l)
        return a
