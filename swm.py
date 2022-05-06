from sklearn import svm
#Each sample [Height(cm), Weight(kg), Shoesize(UK)]
dataX = [[170,70,10],[180,80,12],[170,65,8],[160,55,7]]
#Each sample [0=Male, 1=Female]
dataY = ["Male","Male","Female","Female"]
#dataY = [0,0,1,1]

clf = svm.SVC()
clf.fit(dataX,dataY)

prediction = clf.predict([[172,77,9]])
print (prediction)

