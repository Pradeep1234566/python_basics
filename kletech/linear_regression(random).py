import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
tp=[]
for i in range(10):
  a=random.random()
  tp.append(a)
x=np.array(tp).reshape((-1,1))
k=[]
for i in range(10):
  a=random.random()
  k.append(a)
y=np.array(k)
plt.scatter(x,y)
plt.xlabel("IV")
plt.ylabel("Dv")
plt.show()
from sklearn.linear_model import LinearRegression
lr=LinearRegression()
lr.fit(x,y)
pre=lr.predict(x)
from sklearn.metrics import mean_squared_error
msr=mean_squared_error(y,pre)
plt.plot(x,pre,color='Red',marker='*')
print("mse",msr)
print("intercept",lr.intercept_)
print("Slope",lr.coef_)