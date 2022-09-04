import numpy as np
from sklearn import linear_model
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression
from sklearn.metrics import matthews_corrcoef
import matplotlib.pyplot as plt
import pandas as pd

mydata = pd.read_csv("final_prod_rb_stats.csv")
data2 = pd.read_csv("finprodypc.csv")
regr_att = linear_model.LinearRegression()
regr_yds = linear_model.LinearRegression()

player = input("enter a player: ")
years = []
for i in range(0, mydata["name"].size):
    if mydata["name"][i] == player and mydata["year"][i] not in years:
        years.append(mydata["year"][i])
# years.append(2022)
year_chosen = input(f"pick a year {years}: ")

temp_data = mydata[(mydata["name"] == player) & (mydata["year"] == int(year_chosen))]
weeks = list(temp_data["week"].unique())
week_chosen = input(f"pick a week {weeks}: ")

player_atts = []
player_snapP = []
index = 0

for i in range(0, mydata["name"].size):
    # if mydata["name"][i] == player:
    #     player_atts.append(mydata["attempts"][i])
    #     player_snapP.append(mydata["run"][i])
    if mydata["week"][i] == int(week_chosen) and mydata["year"][i] == int(year_chosen) and mydata["name"][i] == player:
        index = i
count = mydata["game"][index]
temp_count = 0
if count >= 15:
    temp_count = index-14
else:
    temp_count = index-(count-1)

for i in range(temp_count,index):
    player_atts.append(mydata["attempts"][i])
    player_snapP.append(mydata["run"][i])
x = np.array(player_snapP).reshape(-1,1)
y = np.array(player_atts)
regr_att.fit(x,y)

print("coef:", regr_att.coef_, "intercept:",regr_att.intercept_)
pred_att = (mydata["run"][index]*regr_att.coef_)+regr_att.intercept_
print(f"pred attempts : {pred_att}\n actual attempts: {mydata['attempts'][index]}")

# ypc = []
# for i in range(temp_count,index):
#     opp = mydata["opponent"][i]
#     for i in range(0,data2["yr"].size):
#         if data2["team"][i] == opp and data2["yr"][i] == 2018:
#             ypc.append(data2["ypc"][i])
#
# x = np.array(ypc).reshape(-1,1)
# regr_att.fit(x,y)
#
# opp_main = mydata["opponent"][index]
# ypc_t = 0
# for i in range(0,data2["team"].size):
#     if data2["team"][i] == opp_main and data2["yr"][i] == 2018:
#         ypc_t = data2["ypc"][i]
#
# print("coef:", regr_att.coef_, "intercept:",regr_att.intercept_)
# pred_att = (ypc_t*regr_att.coef_)+regr_att.intercept_
# print(f"pred attempts : {pred_att}\n actual attempts: {mydata['attempts'][index]}")

#yards prediction
print("-------------------------------")
player_yds = []

for i in range(temp_count,index):
    player_yds.append(mydata["yds"][i])

x = np.array(player_atts).reshape(-1,1)
y= np.array(player_yds)
regr_yds.fit(x,y)

print("coef:", regr_yds.coef_, "intercept:",regr_yds.intercept_)
pred_yds = (pred_att*regr_yds.coef_)+regr_yds.intercept_
print(f"pred yds : {pred_yds}\n actual yds: {mydata['yds'][index]}")