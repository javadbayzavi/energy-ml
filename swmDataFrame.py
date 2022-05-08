from sklearn  import svm, datasets
import pandas as pd
from matplotlib import pyplot
from pandas.plotting import scatter_matrix

#df = pd.read_csv("")
irisiflowers = datasets.load_iris()
df = irisiflowers

#Give info about the DataFrame
print(df.shape())

#Give n first rows of data
print(df.head(10))

#Give n last rows of data
print(df.tail(10))

#Give detailed description of DataFrame
print(df.describe())

#Give the total number of Not A Number features
print(df.isna().sum().sum())

#Drop NaN values
df = df.dropna()

#Give the number of classes
print(df.groupby("species").size())

#Histogram
df.hist()
pyplot.show()

#Scatter plot
scatter_matrix(df)
pyplot.show()

#learn and prediction
X = df.values[:, :2]
s = df["species"]
d = dict([(y,x) for x,y in enumerate(sorted(set(s)))])
y = [d[x] for x in s]

ml = svm.SVC()
ml.fit(X,y)
prediction = ml.predict([[5.4,3,2]])