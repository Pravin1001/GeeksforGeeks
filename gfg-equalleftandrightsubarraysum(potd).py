class Solution:
    # Complete this function
    
    #Function to find equilibrium point in the array.
    def equalSum(self,A, N):
        # Your code here
        s=sum(A)
        ls=0
        for i in range(N):
            if ls==s-ls-A[i]:
                return i+1
            ls+=A[i]
        return -1
