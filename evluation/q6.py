import numpy as np
import pandas as pd
k=pd.read_excel("Book1.xlsx")
a=k['c1']
m1=sum(a)/len(a)
sum1=0
for i in range(len(a)):
    sum1=sum1+(a[i]-m1)*(a[i]-m1)
var1=sum1/len(a)
b=k['c2']
m2=sum(b)/len(b)
sum1=0
for i in range(len(a)):
    sum1=sum1+(b[i]-m1)*(b[i]-m1)
var2=sum1/len(b)
c=k['c3']
m3=sum(c)/len(c)
sum1=0
for i in range(len(c)):
    sum1=sum1+(c[i]-m1)*(c[i]-m1)
var3=sum1/len(c)
print(f"The mean and variance of the first column is {m1} and {var1}")
print(f"The mean and varince of the second column is {m2} and {var2}")
print(f"The mean and variance of  the third column is {m3} and {var3}")
