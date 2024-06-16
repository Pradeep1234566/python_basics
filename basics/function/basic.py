def percentage(marks):
    sum=0
    wt=int(input("Enter the weight of the subjects "))
    for item in marks:
        sum=sum+item
    per=(sum/(len(marks)*wt))*100
    return per
marks1=[10,20,30,40]
print(percentage(marks1))

def sum(num1,num2):
    return num1+num2
a=2
b=10
k=sum(a,b)
print(k)