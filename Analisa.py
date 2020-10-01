import numpy as np 
import pandas as pd 

#masukan data ke python

dataset = pd.read_csv('Data.csv')
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values

#memproses data yang hilang(missing)

from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_value= np.nan, strategy='mean')
imputer = imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])

#encoding data kategori dan variable independent
from sklearn.preprocessing import LaberEncoder, OnehotEncoder
from sklearn.compose import ColumnTransformer
labelencoder_x.fit_transform(X[:, 0])
transformer = ColumnTransformer(
	[('Negara', OnehotEncoder(), [0])],
	remainder='passthrouhg')
X = np.array(transform.fit_transform(x), dtype=np.float)

#encoding Depandent variable
labelencoder_y = labelencoder()
y = labelencoder_y.fit_transform(y)
