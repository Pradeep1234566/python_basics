import random
import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd
AB=pd.read_excel('/content/drive/MyDrive/mean.xlsx')
k=pd.DataFrame(AB)
m=k['c1'].median()
n=k['c2'].median()
o=k['c3'].median()
print(f"The median of the first colum is {m}")
print(f"The median of the second colum is {n}")
print(f"The median of the thir colum is {o}")
m=k['c1'].mode()
n=k['c2'].mode()
o=k['c3'].mode()
print(f"The mode of the first colum is {m}")
print(f"The mode of the second colum is {n}")
print(f"The mode of the thir colum is {o}")
m=k['c1'].mean()
n=k['c2'].mean()
o=k['c3'].mean()
print(f"The mean of the first colum is {m}")
print(f"The mean of the second colum is {n}")
print(f"The mean of the thir colum is {o}")
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('/content/e1.csv')
print(df)
axs=df.plot.bar(figsize=(10,10))
plt.show()