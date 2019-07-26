import pandas as pd
df = pd.read_csv('LOCATION OF YOUR .CSV FILE')

#SEPARATING dependent and independent variables 
x = df.iloc[:,:-1].values
y = df.iloc[:,1].values

from sklearn.model_selection import train_test_split
x_train,y_train,x_test,y_test = train_test_split(x,y,test_size =1/3,random_state = 0)
