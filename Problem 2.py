import pandas as pd
a = pd.read_csv('cars.csv')
#display the first five rows with odd-numbered columns
o = a.iloc[0:5,0::2]

#display the row that contains the "Model" of "Mazda RX4"
RowMoMazda = a.loc[[0]]

#no. of cylinders that the Camaro Z28 has
Camaro_cyl = a.loc[[23],['Model','cyl']]

#no. of cylinders and gear type of Mazda RX4 Wag, Ford Pantera L, and Honda Civic
cng = a.loc[[1,28,18],['Model','cyl','gear']]