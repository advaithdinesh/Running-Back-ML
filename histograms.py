from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

mydata = pd.read_csv("rbstatsCORRECT.csv")
data2 = pd.read_csv("finprodypc.csv")

att = np.array(mydata[["attempts"]])
yd = np.array(mydata[["yds"]])
run = np.array(mydata[["run"]])
ypc = np.array(data2[["ypc"]])

fig, ax = plt.subplots(figsize =(10, 7))
# ax.hist(att, bins = [0, 10, 20, 30, 40])
# ax.hist(yd, bins = [0, 40, 80, 120, 160, 200, 240, 280, 320])
# ax.hist(run, bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
ax.hist(ypc, bins = [1,1.5,2,2.5,3,3.5,4,4.5,5,5.5,6])
plt.show()