import pandas as pd
#Load the corresponding .csv file
a = pd.read_csv('cars.csv')

#display the first five and last five rows
b = a.iloc[0:5]
c = a.iloc[27:32]
cars = pd.concat([b,c])
