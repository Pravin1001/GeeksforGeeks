#User function Template for python3

class Solution: 
    def maxIntersections(self, lines, N):
        # Code here
        c,r=0,0
        d={}
        for i in lines:
            x=i[0]
            y=i[1]+1
            if x in d:
                d[x]+=1
            else:
                d[x]=1
            if y in d:
                d[y]-=1
            else:
                d[y]=-1
        s=sorted(d.keys())
        for i in s:
            c+=d[i]
            r=max(r,c)
        return r
