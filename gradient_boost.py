import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, ensemble
import pandas as pd


mydata = pd.read_csv("final_prod_rb_stats.csv")
data2 = pd.read_csv("finprodypc.csv")


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


params = {
    "n_estimators": 500,
    "max_depth": 4,
    "min_samples_split": 5,
    "learning_rate": 0.01,
    "loss": "squared_error",
}
reg = ensemble.GradientBoostingRegressor(**params)
reg.fit(x, y)
