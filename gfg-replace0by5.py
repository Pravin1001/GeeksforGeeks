def convertFive(n):
    # Code here
    l=[]
    for i in str(n):
        l.append(i)
    for i in range(len(l)):
        if l[i]=='0':
            l[i]='5'
    ns=''.join(l)
    return int(ns)
