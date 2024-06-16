mail=input("Enter the mail name ")
if("make a lot of money" in mail):
    a=1
elif("buy now" in mail):
    a=1
elif("Subscribe this" in mail):
    a=1
elif("click this" in mail):
    a=1
else:
    a=0
if(a==1):
    print("THe given mail is a spam")
else:
    print("The given mail isnt a spam")
    