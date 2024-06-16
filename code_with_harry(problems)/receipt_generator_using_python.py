sum = 0
dict1 = {}
print(type(dict1))
print("If the shopping is completed, press 0 or enter none in the item name ")

while True:
    item = input("Enter the item: ")
    n = int(input("Enter the price of the item: "))
    
    if (n != 0 or item!='none'):

        sum += n
        dict1[item] = n
    else:
        break

print("\nShopping List:")
for item, value in dict1.items():
    print(f"{item}: {value}")

print(f"TOTAL : {sum}")
