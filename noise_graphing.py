import perlin
import random
import matplotlib.pyplot as plt
newgraph = 1
intensity = 0
manipulate = 0
global words
words = []

def wordinit():
    f = open('nouns.txt', 'r')
    words.append((f.readline()).split(' '))

def graph(intensity):
    noise=perlin.Perlin(intensity)

    time=[i for i in range(100)]
    values=[noise.valueAt(i) for i in time]
    titlestring = "Average discrimination against "+words[0][random.randint(0,len(words[0]))]+" by age in the UK"
    plt.title(titlestring)
    plt.xlabel("Age")
    plt.ylabel("Size")
    plt.plot(time, values)
    plt.show()

wordinit()

while newgraph == 1:
    manipulate = int(input("Would you like to manipulate the graph, or let the true data be pulled from the deepest and darkest corners of the internet? 1/0: "))
    if manipulate == 1:
        intensity = int(input("How erratic do you want the graph to be?: "))
    else:
        intensity = random.randint(0,15)
    graph(intensity)
    newgraph = int(input("Do you want to generate another graph? 1/0: "))



