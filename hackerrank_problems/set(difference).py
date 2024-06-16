# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
m=input()
k=m.split()
a=set()
for i in k:
    a.add(int(i))
#print(a)
n=int(input())
m=input()
k=m.split()
b=set()
for i in k:
    b.add(int(i))
#print(a)
print(len(a.difference(b)))
