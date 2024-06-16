import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
t= pd.read_excel('/content/drive/MyDrive/Colab Notebooks/linear_regression.xlsx')
k=pd.DataFrame(t)
m=len(k['x'])
x=np.array(k['x']).reshape((-1,1))
y=np.array(k['y'])
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