import random
import math
import numpy as np
import matplotlib.pyplot as plt

rangeValue = int(input(" Enter the max range of random values"))
seedNumber = int(input(" Enter the seed value to obtain the random series"))
maxNumber = int(input("Enter no. random numbers to be generated"))
i = 0;

randomNumbers = []
while(i < maxNumber):
    randomNumbers.append(round((((seedNumber * random.randint(1,356) + random.randint(4,523)) % rangeValue)/rangeValue),4))
    #print(randomNumbers[i])
    i = i+1

len = 0
for x in randomNumbers:
    len+=len+1
randomNumbers.sort()
lambdaValue = float(input("Enter the lambda value"))
def exponentialDistribution():
    y=[]
    f = open('Exponential.txt', 'w')
    f2= open('randomnum.txt','w')
    i=0

    while(i < maxNumber):
        y.append(round(math.exp(-lambdaValue*randomNumbers[i]),4))
        #1 - math.log(1 - 0.8)/lambdaValue
        #print(y)
        f.write(str(y[i]) + "\n")
        f2.write(str(randomNumbers[i])+"\n")
        i=i+1
    f.close()
    f2.close()
def drawGraph():
    yAxis = []
    f = open('Exponential.txt','r')
    for line in f.readlines():
        yAxis.append(line.replace('\n',''))
    print(randomNumbers)
    print(yAxis)
    plt.plot(yAxis,randomNumbers, 'o')
    plt.show()
    f.close()
def exponentialInverse():
    inverse = []
    i = 0
    while(i< maxNumber):
        inverse.append(lambdaValue * math.exp(lambdaValue * randomNumbers[i]))
        i=i+1
 #Save the figure before you show
        fig1 = plt.gcf()

    plt.plot(inverse,randomNumbers)
    plt.show()

    plt.draw()

   #Save the figure as a .png file
    fig1.savefig('ExpCGF.png', dpi=100)
    #####




exponentialDistribution()
#drawGraph()
exponentialInverse()
