import numpy as np
k=np.empty((2,2))
for i in range(2):
    for j in range(2):
        n=int(input())
        k[i][j]=n
accuracy=(k[0][0] + k[1][1])/(k[0][0] + k[1][1] + k[0][1] + k[1][0])
precision=(k[0][0])/(k[0][0]+k[1][0])
recall=(k[0][0] )/(k[0][0] +  k[0][1])
f1_score=2*((precision * recall) / (precision + recall))
print(k)
print("The accuracy is ",accuracy)
print("The recall is ",recall)
print("The precision is ",precision)
print("The f1_score is ",f1_score)
    