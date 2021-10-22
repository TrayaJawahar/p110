import csv 
import pandas as pd 
import statistics 
import plotly.figure_factory as ff
import random
import plotly.graph_objects as go

df = pd.read_csv("medium_data.csv")
data=df["reading_time"].tolist()
population_mean = statistics.mean(data)
print(population_mean)

dataset=[]

def set1(counter):
    dataset=[]
    for i in range(0,counter) :
        random_index1= random.randint(0,len(data)-1)
        value = data[random_index1]
        dataset.append(value)
    mean1=statistics.mean(dataset)
    return mean1

def show_fig(mean_list):
    df=mean_list
    fig=ff.create_distplot([df], ["reading_time"] , show_hist=False)
    fig.show()

def setup():
    mean_list=[]
    for i in range(1,1000):
        sd=set1(30)
        mean_list.append(sd)
    show_fig(mean_list)

setup()