# -*- coding: utf-8 -*-
import numpy as np

def distance(pos_1, pos_2 = np.array([0,0,0])):
    '''
    Parameters
    ----------
    pos_1 : tablica, współżędne punktu wyrażone jako (x,y,z).
    pos_2 : tablica, The default is np.array([0,0,0]).

    Returns
    -------
    dist : float, odległosć między punktami.
    '''
    squares = 0
    vect = pos_1 - pos_2
    for i in vect:
        squares += i**2
    dist = float(squares**(1/2))
    return dist

def trajectoryPlasz(dt:float, acc:float, vel:np.array([]), 
               pos = np.array([0, 0, 0])):
    '''
    Parameters
    ----------
    dt : float, czas.
    acc : float, przyspieszenie grawitacyjne.
    vel : np.array([]), prędkosć początkowa.
    pos : np.array([]), pozycja początkowa. The default is np.array([0, 0, 0]).

    Returns
    -------
    r : np.array, położenie chwilowe.
    '''
    rx = vel[0]*dt + pos[0]
    ry = vel[1]*dt + pos[1]
    rz = vel[2]*dt + pos[2] + 0.5*dt**2*acc
   
    r = np.array([rx, ry, rz])
    return r

def velocityPlasz(dt:float, acc:float, 
                  vel = np.array([])):
    '''
    Parameters
    ----------
    dt : float, czas.
    acc : float, przyspieszenie grawitacyjne.
    vel : np.array([]), prędkosć początkowa.

    Returns
    -------
    v : np.array([]), prędkosć chwilowa.
    '''
    vx = vel[0]
    vy = vel[1]
    vz = dt*acc + vel[2]
    
    v = np.array([vx, vy, vz])
    return v

def timePlasz(acc:float, vel:np.array([]), 
              pos = np.array([0, 0, 0])):
    '''
    Parameters
    ----------
    acc : float, przyspieszenie grawitacyjne.
    vel : np.array([]), prędkosć początkowa.
    pos : np.array([]), pozycja początkowa. The default is np.array([0, 0, 0]).

    Returns
    -------
    t : float, czas całkowity.
    '''
    delta = (-vel[2])**2 - 2*(-acc)*pos[2]
    t = float((vel[2] - delta**(1/2))/-acc)
    # t = czas całkowity ruchu
    return t

def maxHeight(acc:float, vel:np.array([]), 
              pos = np.array([0, 0, 0])):
    '''
    Parameters
    ----------
    acc : float, przyspieszenie grawitacyjne.
    vel : np.array([]), prędkosć początkowa.
    pos : np.array([]), pozycja początkowa. The default is np.array([0, 0, 0]).

    Returns
    -------
    h : float, maksymalna wysokosć.
    '''
    h = vel[2]**2/2**acc + pos[2]
    return h

# Nie do końca wiem co tutaj poniżej

def reach(acc:float, t:float, vel:np.array([]), 
          pos = np.array([0, 0, 0])):
    '''
    Parameters
    ----------
    acc : float, przyspieszenie grawitacyjne.
    vel : np.array([]), prędkosć początkowa.
    pos : np.array([]), pozycja początkowa. The default is np.array([0, 0, 0]).
    t : float, czas całkowity ruchu.

    Returns
    -------
    z : float, zasięg.
    '''
    v = (vel[0]**2-vel[1]**2)**(1/2)
    z = v*t
    
    return z
