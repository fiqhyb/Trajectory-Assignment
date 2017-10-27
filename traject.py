import matplotlib.pyplot as plt
import random

if __name__ == '__main__':
    #Coordinates and Equations
    numx = list(range(0,26))#range is 26 for display purpose
    numy = [((x**2)-(3*x)+4) for x in numx]
    ranx = list(random.randint(0,25)  for p in range(4000))
    rany = list(random.randint(0,600) for q in range(4000))
    poin = []
    #create point and count as one below the curve
    for i in range(4000):
        if rany[i] <= numy[ranx[i]]:
            poin.append(1)
    cal  = 25*600*(sum(poin)/4000)#Calculate the area

    #sets the graph's axis
    plt.axis([-1,26,-30,630])#given offsides to axis for display purpose
    #Title and Axis' name
    plt.title("Area Calculator\nArea ={0}".format(cal))
    plt.xlabel("X-Coordinate")
    plt.ylabel("Y-Coordinate")

    #Draws and displays graph
    plt.scatter(ranx,rany,c=rany)
    plt.scatter(numx,numy,c="red")
    plt.show()