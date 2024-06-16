def count(Num):
    if(Num==0):
        return 0
    sum=Num+count(Num-1)
    return sum
Num=int(input("Enter the numbers whose sum you want "))
total=count(Num)
print(f"The sum of {Num} natural numbers is {total}")
