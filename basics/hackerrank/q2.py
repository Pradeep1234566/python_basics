def solve(s):
    (s[0])=int(s[0]-32)
    a=len(s)
    for i in range(a):
        if(s[i]==' ' and i+1<a):
            s[i+1]=s[i+1]-32
    print(s)
s=input("ENter the string ")
solve(s)