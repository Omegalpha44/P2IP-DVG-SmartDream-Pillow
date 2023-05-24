#permet de visualiser les courbes de l'ensemble des données 

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

data1 = pd.read_csv("updated_data\\user_1_sleep_1.csv", sep = ",", header = 0)

fig = px.line(data1, x = 'time', y = 'HR', color = 'day', title = 'user 1 sleep 0')
fig.show()