for _ in range(int(input())):
    n,m=map(int,input().split())
    a=[int(i) for i in input().split()]
    b=[int(i) for i in input().split()]
    d={}
    d=dict(d)
    for i in a:
        d[i]=0
    for i in range(len(a)):
        d[a[i]]+=b[i]
    print(min(d.values()))
