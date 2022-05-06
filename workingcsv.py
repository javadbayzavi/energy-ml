import pandas as pd

data = {
    "Name": ["Javad","Ali","Mohammad","Ati","Abbas","Meysam","Sina"],
    "Age" : [37,7,9,36,38,39,33]
}

df = pd.DataFrame(data=data,columns=["Name","Age"])
print(df)
df.to_csv('emp.csv', index=False)

df2 = pd.read_csv("emp.csv")
print(df2)

