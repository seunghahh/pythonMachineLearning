import pandas
from sklearn import linear_model
import matplotlib.pyplot as plt

df = pandas.read_csv("/Users/seungha/Desktop/KHU/pythonMachineLearning/dataDistribution/data.csv")

x = df[['Weight', 'Volume']]
y = df['CO2']

regr = linear_model.LinearRegression()
regr.fit(x, y)
print(regr.coef_)

pridictedCO2 = regr.predict([[2300, 1300]])
print(pridictedCO2)