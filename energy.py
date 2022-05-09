from numpy import dtype
from sklearn  import svm, datasets
import pandas as pd
from matplotlib import pyplot
from pandas.plotting import scatter_matrix

df = pd.read_excel("data.xlsx", sheet_name="Steam,(101-E-202)")


#print(df.shape)

#df.hist()
#pyplot.show()

#Scatter plot

df.iloc[1] = df.iloc[1].convert_dtypes("float32")
df.iloc[2] = df.iloc[2].convert_dtypes("float32")
df.iloc[3] = df.iloc[3].convert_dtypes("float32")
df.iloc[4] = df.iloc[4].convert_dtypes("float32")
df.iloc[5] = df.iloc[5].convert_dtypes("float32")


print(df.dtypes)

dl = svm.SVC()
X = df.values[2:, 1:2]
y = df.values[2:, 2:5]
#y = y.astype("float32")
print(y)
#dl.fit(y,X)
for xx in y:
    if type(xx) == "object":
        print(xx)

#res = dl.predict([[145.85,90.5,133.09,7.55]])
#print(res)

