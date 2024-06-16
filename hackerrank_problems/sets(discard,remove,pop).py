n = int(input())
a=set()
element=input()
#print(element)
k=element.split()
for i in k:
    a.add(int(i))
reversed_list = list(a)[::-1]  
a = set(reversed_list) 
m=int(input())
for i in range(m):
    m=input()
    p=m.split()
    if(p[0]=='pop'):
        a.pop()
    elif(p[0]=='remove'):
        if(int(p[1]) in a):
            a.remove(int(p[1]))
    elif(p[0]=='discard'):
            a.discard(int(p[1]))

print(sum(a))
    