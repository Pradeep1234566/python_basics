def remove(string,word):
    newstr=string.replace(word,"")
    return newstr.strip()
string=input("Enter the string ")
print(f"The given string is {string} ")
word=input("Enter the word you want to remove in the string ")
newstr=remove(string,word)
print(f"The string after deletion is {newstr}")