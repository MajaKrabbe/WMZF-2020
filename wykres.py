# -*- coding: utf-8 -*-
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

def wykresCentr(poz:float, r:int, *args):
    ax = plt.axes(projection='3d')

    argx = poz[:,0]
    argy = poz[:,1]
    argz = poz[:,2]
    
#    x = np.linspace(argx, r)
#    y = np.linspace(argy, r)
#    z = np.linspace(argz, r)
    
    ax.plot3D(argx, argy, argz, 'r')

    # wyrównanie skali osi x,y
    #ax.set_box_aspect([1,1,1])
    lmin = max(argx[0], argy[0], argz[0])
    lmax = max(argx[len(argx)-1], argy[len(argy)-1], argz[len(argz)-1])
    lmin, lmax, lmin, lmax= plt.axis()

    data = ('Całkowity czas ruchu [s]: ' + str(round(args[0],2))
            + '\nMaksymalna wysokość nad powierzchnią [m]: ' + str(round(args[1],2))
            + '\nOdległość przebyta względem powierzchni [m]: ' + str(round(args[2],2)))
    #plt.text(10,10,data)
    #plt.Axes.text(ax,50,0.25,data)
    plt.title(data, fontsize=11)

    plt.show()
    return 0

def wykresPlaszcz(poz:np.ndarray, *args):
    ax = plt.axes(projection='3d')

    argx = poz[:,0]
    argy = poz[:,1]
    argz = poz[:,2]

    ax.plot3D(argx, argy, argz, 'r')

    # wyrównanie skali osi x,y
    # ax.set_box_aspect([1,1,1])
    lmin = max(argx[0], argy[0], argz[0])
    lmax = max(argx[len(argx) - 1], argy[len(argy) - 1], argz[len(argz) - 1])
    lmin, lmax, lmin, lmax = plt.axis()

    data = ('Całkowity czas ruchu [s]: ' + str(round(args[0],2))
            + '\nMaksymalna wysokość nad powierzchnią [m]: ' + str(round(args[1],2))
            + '\nZasięg rzutu [m]: ' + str(round(args[2],2)))
    plt.title(data, fontsize=11)

    plt.show()

    return 0

