import pandas as pd
data = {
    "Name": ["Javad","Ali","Mohammad","Ati","Abbas","Meysam","Sina"],
    "Age" : [37,7,9,37,38,39,33]
}

df = pd.DataFrame(data=data,columns=["Name","Age"])
df.to_csv('emp.csv', index=False)

df2 = pd.read_csv("emp.csv")

#df3 = df2.groupby(["Age"])
for v, grou in df2.groupby("Age"):
     print(v)
     print(grou)