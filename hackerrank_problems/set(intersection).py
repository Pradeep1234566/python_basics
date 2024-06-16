# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
k=input()
a=k.split()
p=set()
for i in a:
    p.add(int(i))
m=int(input())
k=input()
a=k.split()
q=set()
for i in a:
    q.add(int(i))
m=q.intersection(p)
print(len(m))
