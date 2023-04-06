    def leaders(self, A, N):
        #Code here
        m=A[-1]
        l=[]
        for i in range(N-1,-1,-1):
            if A[i]>=m:
                l.append(A[i])
                m=A[i]
        l.reverse()
        return l
