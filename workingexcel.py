import pandas as pd
#pip install xlsxwriter and openpyxl for writing and reading excel files

data = {
    "Name": ["Javad","Ali","Mohammad","Ati","Abbas","Meysam","Sina"],
    "Age" : [37,7,9,36,38,39,33]
}

df = pd.DataFrame(data=data,columns=["Name","Age"])


#to export to excel file
writer = pd.ExcelWriter("emp.xlsx", engine="xlsxwriter")
df.to_excel(writer,sheet_name="Sheet1",index=False)
writer.save()

df2 = pd.read_excel("emp.xlsx", sheet_name="Sheet1")
print(df2)

#Useful AI frameworks
# Scikit-Learn:
#NLTK
#TensorFlow (Google)
#Keras
#OpenCV
#OpenAI, H2O, PyTorch(Facebook), DeepMind

#Machine learning are categorized into four categories:
#Unsupervised learning (Clustering and association based on sets of features K-Means)
#SuperVised learning (Classification and regression based on labeled features, naive bayes, nenural nets, k-nearest)
#Semisupervised learning (Clusering and then classify )
#Reinforcement learning (learn through trial and error)
#https://scikit-learn.org/stable/datasets.html

