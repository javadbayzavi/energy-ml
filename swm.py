from operator import index
from sklearn import svm
import pandas  as pd
#Each sample [Height(cm), Weight(kg), Shoesize(UK)]
dataX = [[170,70,10],[180,80,12],[170,65,8],[160,55,7]]
#Each sample [0=Male, 1=Female]
dataY = ["Male","Male","Female","Female"]
#dataY = [0,0,1,1]

clf = svm.SVC()
clf.fit(dataX,dataY)

prediction = clf.predict([[172,77,9]])
print (prediction)

def print1(x) :
    return "%" + str(x) + "%"
pp = pd.Series([1,2,3], index = ["a","b","c"])
#map function do the input operation on each element of the series
p = pp.map(print1)


print(pp)
print(p)

data = pd.Series([[60,40,50],[70,30,50],[90,10,50]], index = ["end","start","avg"])

datap = data.ev
