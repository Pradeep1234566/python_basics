S=set()
S.add(20)
S.add(20.0)
S.add("20")
print(S)#20 and 20.0 are considered as one and the same
print(len(S))