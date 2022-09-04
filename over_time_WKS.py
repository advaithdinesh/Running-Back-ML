import numpy as np
from sklearn import linear_model
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression
from sklearn.metrics import matthews_corrcoef
import matplotlib.pyplot as plt
import pandas as pd

mydata = pd.read_csv("rbstatsCORRECT.csv")
# data2 = pd.read_csv("finprodypc.csv")
mydata = mydata[["name","week","attempts","yds"]]
print(mydata)

x = (list)(mydata["name"])
wk = []
att = []
y = []
inp = input("name: ")
ind = x.index(inp)
g = ind

while x[ind] == inp:
    wk.append(ind-(g-1))
    att.append(mydata["attempts"][ind])
    y.append(mydata["yds"][ind])
    ind += 1


plt.scatter(wk, att)
plt.title("wks vs atts")
plt.show()

plt.scatter(wk, y)
plt.title("wks vs yds")
plt.show()

