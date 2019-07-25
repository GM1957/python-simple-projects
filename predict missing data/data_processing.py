import pandas as pd

#to read .csv(excel) file
dataset = pd.read_csv("LOCATION OF YOUR .CSV FILE ")

# ":-1" means we are eliminating the last column because in my case it is a dependent varibable and store the other part in x
x = dataset.iloc[:, :-1].values

#here we store the dependent part in y
y = dataset.iloc[:, 3].values

from sklearn.preprocessing import Imputer

#here we finding and predict the missing data
imputer = Imputer(missing_values="NaN" , strategy = 'mean' , axis =0 )

#fit and print the data
imputer = imputer.fit(x[:,1:3])
x[:,1:3] = imputer.transform(x[:,1:3])
