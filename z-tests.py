import csv
import statistics
import pandas as pd 
import plotly.figure_factory as ff 
import random
import plotly.graph_objects as go 

df = pd.read_csv("studentMarks.csv")

data = df["Math_score"].tolist()
print(data)

datadeviation  = statistics.stdev(data)
print(datadeviation)

average = statistics.mean(data)
print(average)

def random_set_of_mean(counter):
    dataset = []
    for i in range(0,counter):
        randomindex = random.randint(0,len(data)-1)
        value = data[randomindex]
        dataset.append(value)

    mean = statistics.mean(dataset)
    return mean 

def show_fig(mean_list):
    df = mean_list
    mean = statistics.mean(df)
    fig = ff.create_distplot([df],["Mathscore"],show_hist=False)
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],name="Mean"))
    fig.show()

def setup():
    mean_list = []
    for i in range(0,1000):
        sets_of_means = random_set_of_mean(100)
        mean_list.append(sets_of_means)
    show_fig(mean_list)

    mean = statistics.mean(mean_list)
    print("Mean of sampling distrbution :-",mean)

setup()


marks = statistics.mean(data)
print("Mean of marks:-",marks)


def standard_deviation():
    mean_list = []
    for i in range(0,1000):
        sets_of_means = random_set_of_mean(100)
        mean_list.append(sets_of_means)


    std_deviation = statistics.stdev(mean_list)
    print("Standard deviation of sampling distrubution:-",std_deviation)

standard_deviation()