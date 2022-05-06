from sklearn import svm, datasets

irisiflowers = datasets.load_iris()
Xdata = irisiflowers.data[:, :2]
Ydata = irisiflowers.target

print(Ydata)

ml = svm.SVC()
ml.fit(Xdata,Ydata)
p = ml.predict([[5.4,3.2]])
print(p)