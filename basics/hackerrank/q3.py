# Enter your code here. Read input from STDIN. Print output to STDOUT
N=int(input())
a=set()
if(N>0 and N<100):
   for i in range(N):
       string=input()
       a.add(string)
print(len(a))
    