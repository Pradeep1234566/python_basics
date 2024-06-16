#Sets prints only non repeated values

a={1,2,3,4,5}
#print(type(a))
#print(a)
#b={1,1,1,2,3,4,5}
#print(b)
#c={1,1,1,1,1}
#print(c)


d={}#This doesnt yield to a empty set rather it yields to a empty dictionary
print(type(d))

#To create an empty set 
e=set()#This creates and empty set
print(type(e))

#To add values to an empty set
e.add(1)
e.add(1)
e.add(2)
e.add(3)
e.add(4)
e.add((4,5,6)) #YOU CAN ADD ONLY ELEMENTS THAT ARENT HASHABLE 
#e.add([4,5,6]) # YOU CANT ADD A LIST TO AN SET
print(e)
#print(len(e))#The entire tulip is considered as one element
#e.remove((4,5,6))#It removes the element present inside the brackets
#print(e)
#e.pop()#It pops the topmost element from the set
#print(e)
#e.pop()
#print(e)
#e.pop()
#print(e)
f={10,11,12,1}
b=a.intersection(f)
print(b)
