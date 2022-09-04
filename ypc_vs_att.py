import numpy as np
from sklearn import linear_model
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression
from sklearn.metrics import matthews_corrcoef
import matplotlib.pyplot as plt
import pandas as pd

mydata = pd.read_csv("rbstatsCORRECT.csv")
data2 = pd.read_csv("finprodypc.csv")
mydata = mydata[["year","opponent","attempts"]]
data2 = data2[["yr","team","ypc"]]
print(mydata)


year_list = (list)(data2["yr"])
ypc = []
att = []
# y = []

#
for i in range(0,len(mydata["year"])):
    y = mydata["year"][i]
    opp = mydata["opponent"][i]
    for x in range(0,len(data2["yr"])):
        if data2["yr"][x] == y-1 and data2["team"][x] == opp:
            ypc.append(data2["ypc"][x])
            att.append(mydata["attempts"][i])


#
plt.scatter(ypc, att)
plt.title("ypc vs atts")
plt.show()
#
# plt.scatter(wk, y)
# plt.title("wks vs yds")
# plt.show()
#
