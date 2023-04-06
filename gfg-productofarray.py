def product(arr,n,mod):
    # your code here
    c=1
    for i in arr:
        c*=i
    res=c%mod
    return res
