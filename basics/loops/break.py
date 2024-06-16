for i in range(10):
    print(i)
    if i==5:
        break
else:print("The loop has been executed completly")#When we use else it indicates that the else part is printed only when the for loop is executed successfully 
for i in range(10):
    if(i==5):
        continue # When we use continue statement then when i becomes 5 it doesnt execute the next statement it directly goes back to loop
    print(i)

