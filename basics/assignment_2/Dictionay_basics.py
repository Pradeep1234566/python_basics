dictionary={"kaun" : "who",
            "mai"  : "Me",
            "kyun" : "Why"
 }
print("THese are the options avaliable")
print(dictionary.keys())
k=input("Enter the word that you want to search ")
print("The meaning of your word : ",dictionary.get(k))