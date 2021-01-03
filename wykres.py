# -*- coding: utf-8 -*-
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

def wykresCentr(poz:float, r:int):
    ax = plt.axes(projection='3d')

    argx = poz[:,0]
    argy = poz[:,1]
    argz = poz[:,2]
    
    #TODO: dorobić zatrzymywanie na powierzchni
    
#    x = np.linspace(argx, r)
#    y = np.linspace(argy, r)
#    z = np.linspace(argz, r)
    
    ax.plot3D(argx, argy, argz, 'r')

    # wyrównanie skali osi x,y
    #ax.set_box_aspect([1,1,1])
    lmin = max(argx[0], argy[0], argz[0])
    lmax = max(argx[len(argx)-1], argy[len(argy)-1], argz[len(argz)-1])
    lmin, lmax, lmin, lmax= plt.axis()

    plt.show()
    return 0

def wykresPlaszcz(poz:np.ndarray):
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

    plt.show()

    return 0

