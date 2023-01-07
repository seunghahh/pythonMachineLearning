import pandas
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
scale = StandardScaler()

df = pandas.read_csv("/Users/seungha/Desktop/KHU/pythonMachineLearning/dataDistribution/data.csv")

x = df[['Weight', 'Volume']]
y = df['CO2']

scaledX = scale.fit_transform(x)

regr = linear_model.LinearRegression()
regr.fit(scaledX, y)

scaled = scale.transform([[2300, 1300]])

predictedCO2 = regr.predict([scaled[0]])
print(predictedCO2)