def recursive(n):
    if(n==1 or n==0):
        return 1
    return n*recursive(n-1)
a=int(input("Enteer the input number "))
k=recursive(a)
print(k)