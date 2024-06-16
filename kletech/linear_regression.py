import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
x=np.array([1,5,13,25,33,46]).reshape((-1,1))
y=np.array([3,6,9,12,15,18])
plt.scatter(x,y)
plt.xlabel("IV")
plt.ylabel("Dv")
plt.show()
from sklearn.linear_model import LinearRegression
slr=LinearRegression()
slr.fit(x,y)
pred=slr.predict(x)
from sklearn.metrics import mean_squared_error
msr=mean_squared_error(y,pred)
plt.plot(x,pred,color='Red',marker='*')
print("mse",msr)
print("intercept",slr.intercept_)
print("Slope",slr.coef_)