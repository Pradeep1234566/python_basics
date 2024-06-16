def conversion(inch):
    return inch*2.54
inch=int(input("Enter the number of inches "))
cm=conversion(inch)
print(f"The equvalent of {inch} inch in cm is {cm}")