def convert(C):
    F=(C*1.8)+ 32
    return F
C=int(input("Enter the temperature in celsius "))
F=convert(C)
print(f"The equivalent of the {C} degree in farenhit is {F}")