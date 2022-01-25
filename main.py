import plotly.figure_factory as ff 
import plotly.graph_objects as pg
import statistics 
import pandas as pd
import csv
import random

file=pd.read_csv("studentMarks.csv")
data=file["Math_score"].tolist()
fig=ff.create_distplot([data],["Math Score"],show_hist=False)
fig.show()

mean=statistics.mean(data)
std=statistics.stdev(data)
print(mean)
print(std)