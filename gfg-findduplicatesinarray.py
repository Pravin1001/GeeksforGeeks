    def duplicates(self, arr, n): 
    	# code here
    	d={}
    	l=[]
        for i in arr:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i in d:
            if d[i]>1:
                l.append(i)
        if not l:
            l.append(-1)
        l.sort()
        return l
