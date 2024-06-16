m1=int(input("Enter subject 1 marks "))
m2=int(input("Enter subject 2 marks "))
m3=int(input("Enter subject 3 marks "))
if(m1>33 or m2>33 or m3>33):
    if(m1+m2+m3>40):   
        print("Pass")
    else:
        print("fail")
else:
    print("FAIL")