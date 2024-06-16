a=int(input("Enter the number whose factorial you want to calculate "))
fact=1

for i in range(1,a+1):
    fact=fact*i
print("THe factorial of " + str(a) + " is" ,fact)