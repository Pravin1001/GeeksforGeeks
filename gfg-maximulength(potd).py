#User function Template for python3
class Solution():
    def solve(self, a, b, c):
        #your code goes here
        freq=[a,b,c]
        freq.sort(reverse=True)
        if freq[0]>(freq[1]+freq[2])*2+2:
            return -1
        else:
            return a+b+c
        
