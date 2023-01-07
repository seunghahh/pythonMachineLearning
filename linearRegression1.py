import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression

dataset = pd.read_csv('/Users/seungha/Desktop/KHU/pythonMachineLearning/PythonMLWorkspace(LightWeight)/ScikitLearn/LinearRegressionData.csv')

X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

reg = LinearRegression()
reg.fit(X, y) # 학습, 모델 생성

y_pred = reg.predict(X)
print(y_pred)

print(reg.predict([[9]])) #9시간 공부했을 때 예상 점수
print(reg.coef_) # 기울기
print(reg.intercept_) # y 절편

plt.scatter(X, y)
plt.plot(X, y_pred, color = 'green')
plt.show()