import random
import math
import matplotlib.pyplot as plt

rangeValue = float(input(" Enter the max range of random values"))
seedNumber = float(input(" Enter the seed value to obtain the random series"))
maxNumber = float(input("Enter no. random numbers to be generated"))
i = 0;
randomNumbers = []
while(i < maxNumber):
    randomNumbers.append(round((((seedNumber * random.randint(1,356) + random.randint(4,523)) % rangeValue)/rangeValue),4))
    #print(randomNumbers[i])
    i = i+1
    f2= open('randGeo.txt','w')

len = 0
for x in randomNumbers:
    len+=len+1
randomNumbers.sort()
propabilityValue = float(input("Enter the probability value"))
def geometricDistribution():
    y=[]
    f = open('Geometric.txt', 'w')
    i=0
    while(i < maxNumber):
        y.append(round(1 - math.pow(1 - randomNumbers[i],maxNumber-1),4))
        f.write(str(y[i]) + "\n")
        f2.write(str(randomNumbers[i])+"\n")

        i=i+1
    f.close()
def geoDrawGraph():
    yAxis = []
    f = open('Geometric.txt','r')
    for line in f.readlines():
        yAxis.append(line.replace('\n',''))
    print(randomNumbers)
    print(yAxis)
    #plt.plot(yAxis,randomNumbers, 'o')
    plt.plot(randomNumbers,yAxis)
    plt.show()
    f.close()
geometricDistribution()
#geoDrawGraph()

def geoInverse():
    inverse = []
    i = 0
    while(i< maxNumber):
        inverse.append(round(math.log(1 - randomNumbers[i])/math.log(1- propabilityValue),4))
        i=i+1
    plt.plot(inverse,randomNumbers)
    fig1 = plt.gcf()
    plt.show()
    plt.draw()


    fig1.savefig('Geo.png', dpi=100)


#exponentialDistribution()
#drawGraph()
geoInverse()