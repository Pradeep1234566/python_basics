a = int(input("Enter the number that you want to check "))
k=2
prime=True
while k<a:
    if(a%k==0):
        prime=False
        break
    else:
        k=k+1
if prime:
    print("The given number is a prime number")
else:
    print("The given number is not a prime number")