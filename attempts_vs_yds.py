import numpy as np
from sklearn import linear_model
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression
from sklearn.metrics import matthews_corrcoef
import matplotlib.pyplot as plt
import pandas as pd

mydata = pd.read_csv("rbstatsCORRECT.csv")
# data2 = pd.read_csv("finprodypc.csv")
mydata = mydata[["attempts","yds"]]
print(mydata)
plt.scatter(mydata["attempts"], mydata["yds"])
plt.show()

def make_pred(input, intercept, slope):
    return (input*slope + intercept)


train = mydata[:(int((len(mydata)*.8)))]
test = mydata[(int((len(mydata)*.8))):]

regr = linear_model.LinearRegression()
train_x = np.array(train[["attempts"]])
train_y = np.array(train[["yds"]])
regr.fit(train_x,train_y)

print("y = ", regr.intercept_, " + ", regr.coef_,"x")

test_x = np.array(test[["attempts"]])
test_y = np.array(test["yds"])
test_y1 = regr.predict(test_x)

print(make_pred(90, regr.intercept_, regr.coef_))
print("mean abs error: ", np.mean(np.absolute(test_y1-test_y)))
print("r score: ", ((r2_score(test_y1,test_y)))**(.5))


print("---------------------------------------------------------")