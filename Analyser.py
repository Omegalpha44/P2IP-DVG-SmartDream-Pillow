import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from icecream import ic
import os
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as pio

liste = []
for i in range(23):
    for j in range(2):
        user = "user_" + str(i+1)
        try : 
            liste.append(pd.read_csv("updated_data\\" + user + "_sleep_" + str(j) + ".csv", sep = ",", header = 0))
        except :
            pass
#normalisation des données

for elem in liste :
    elem["HR"] = (elem["HR"] - elem["HR"].mean()) / elem["HR"].std()


Reveil_souhaité  = input("Quand voulez-vous vous réveiller ? (hh:mm)")
heure = int(Reveil_souhaité.split(":")[0])
minute = int(Reveil_souhaité.split(":")[1])
born_sup = heure * 60 + minute + 60
if born_sup // 60 < 10 :
    born_sup_str = "0" + str(born_sup // 60) + ":" + str(born_sup % 60) + ":00"
else : born_sup_str = str(born_sup // 60) + ":" + str(born_sup % 60) + ":00"
born_inf = heure * 60 + minute - 60
if born_inf // 60 < 10 :
    born_inf_str = "0" + str(born_inf // 60) + ":" + str(born_inf % 60) + ":00"
else : born_inf_str = str(born_inf // 60) + ":" + str(born_inf % 60) + ":00"
scope = [born_inf_str, born_sup_str]
compatible_hours = []
for elem in liste:
    elem = elem[elem["time"] >= scope[0]]
    elem = elem[elem["time"] <= scope[1]]
    compatible_hours.append(elem[elem["HR"] > 0])

best_hours = []
for elem in compatible_hours:
    #create a list containing the hours where the HR is the highest
    best_hours.append(elem[elem["HR"] == elem["HR"].max()]["time"])

best_hours = pd.concat(best_hours)
best_hours = best_hours.reset_index()
res = 0
for elem in best_hours["time"]:
    res += int(elem.split(":")[0]) * 3600 + int(elem.split(":")[1]) * 60 + int(elem.split(":")[2])
res = res / len(best_hours["time"])

best = str(int(res // 3600)) + ":" + str(int(res % 3600 // 60)) + ":" + str(int(res % 3600 % 60))

print("Vous devriez vous réveiller à " + best)