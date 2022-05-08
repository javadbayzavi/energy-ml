from sklearn  import svm, datasets
import pandas as pd
from matplotlib import pyplot
from pandas.plotting import scatter_matrix

df = pd.read_excel("data.xlsx", sheet_name="Steam,(101-E-202)")


#print(df.shape)

#df.hist()
#pyplot.show()

#Scatter plot

#pyplot.show()

dl = svm.SVC()
dl.predict
