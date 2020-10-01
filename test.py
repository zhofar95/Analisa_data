import pandas as pd 

dataset = pd.read_csv('Data.csv')

ds = dataset['Usia'].mean() #mencari niali mean untuk dimasukan kedalam data yang kosong
ds2 = dataset['Usia'].isna() #melihat data yang kosong
#memasukan nilai mean ke dalam data yang kosong
dataset['Usia'] = dataset['Usia'].fillna(dataset['Usia'].mean())

ds3 = dataset['Gaji'].mean()
dataset['Gaji'] = dataset['Gaji'].fillna(dataset['Gaji'].mean()) 


print(dataset)