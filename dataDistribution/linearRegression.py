import matplotlib.pyplot as plt
from scipy import stats

x = [5,7,8,7,2,17,2,9,4,11,12,9,6] #ages of car
y = [99,86,87,88,111,86,103,87,94,78,77,85,86] #speeds of car

slope, intercept, r, p, std_err = stats.linregress(x, y)
print(r) # r : correlation coefficient
"""
if the data have bad relationship(ex. r is almost 0),
the data is not suitable for linear regression.
"""
def myfunc(x):
    return slope * x + intercept

mymodel = list(map(myfunc, x))

speed = myfunc(10) # predict future values
print(speed)

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()