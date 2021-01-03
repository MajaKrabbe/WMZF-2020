import numpy as np
import constants as const

def mass(sgrav:float, radius:float):
    '''
    Oblicza masę ciała przy założeniu, że jest ono jednorodną kulą

    :param sgrav: przyspieszenie grawitacyjne przy powierzchni ciała
    :param radius: promień ciała
    :returns: masa
    '''
    return sgrav * (radius**2) / const.GRAV_CONST

def vector_value(v:np.ndarray):
    '''
    Oblicza długość danego wektora.

    :param v: wektor
    :return: długość wektora v
    '''
    val = 0.0
    for crd in v:
        val += float(crd)**2
    val = val**0.5
    return val

def gravityAcceleration(radius, x, y, z, surfaceGravAcceleration):
    '''
    obsolete ?
    '''
    # r odległość w prostej linii punktu od powierzchni
    r = (((radius - x) ** 2 + (radius - y) ** 2 + (radius - z) ** 2) ** (1 / 2))
    #M = surfaceGravAcceleration * (radius ** 2) / const.GRAV_CONST
    M = mass(surfaceGravAcceleration, radius)

    a = const.GRAV_CONST * M / (radius + r) ** 2
    # To samo generalnie:
    # g = (surfaceGravAcceleration/(1+(r/radius))**2)

    return a

def grav_acc(pos:np.ndarray, M:float):
    '''
    Oblicza współrzędne przyspieszenia chwilowego w zależności od wektora położenia względem masy M

    :param pos: wektor położenia obiektu
    :param M: masa ciała przyciągającego obiekt, umieszczona w położeniu (0,0,0)
    :return: acc - wektor przyspieszenia chwilowego
    '''
    try:
        acc = pos * (-1) * const.GRAV_CONST * M / (vector_value(pos)**3)
    except ZeroDivisionError:
        acc = 0
    return acc

def velocity(dt:float, vel:np.ndarray = np.asarray([0,0,0]), acc:np.ndarray = np.asarray([0,0,0])):
    '''
    Oblicza prędkość obiektu poddanego przyspieszeniu w przedziale czasie dt

    :param dt: czas zmiany prędkości
    :param acc: wektor przyspieszenia chwilowego
    :param vel: prędkość początkowa
    :return: nowa prędkość
    '''
    dv = dt * acc
    return np.add(dv, vel)

def position(dt:float, pos:np.ndarray = np.asarray([0,0,0]), vel:np.ndarray = np.asarray([0,0,0]), acc:np.ndarray = np.asarray([0,0,0])):
    '''
    Oblicza pozycję obiektu po upływie czasu dt

    :param dt: przedział czasu, w którym następuje przemieszczenie
    :param acc: przyspieszenie chwilowe
    :param vel: prędkość chwilowa
    :param pos: położenie początkowe obiektu
    :return: Nowa pozycja obiektu
    '''
    dr = 0.5 * (dt**2) * acc + dt * vel
    return np.add(dr, pos)

def coriolis_acc(v_linear:np.ndarray, v_radial:float):
    '''
    Zwraca przyspieszenie pozorne obiektu związane z ruchem obrotowym układu odniesienia wokół osi pionowej OZ

    :param v_linear: wektor prędkości liniowej obiektu
    :param v_radial: wartość prędkości kątowej układu odniesienia
    :return: wektor przyspieszenia Coriolisa
    '''
    ax = 2 * v_radial * v_linear[1]
    ay = -2 * v_radial * v_linear[0]
    return np.asarray([ax,ay,0])

def acceleration(pos:np.ndarray, M:float, v_linear:np.ndarray = np.asarray([0,0,0]), v_radial:float = 0):
    '''
    Zwraca wektor przyspieszenia wypadkowego obiektu poruszającego się w układzie odniesienia obracającym sie wokół osi OZ

    :param pos:
    :param M:
    :param v_linear:
    :param v_radial:
    :return:
    '''
    acc = np.add( grav_acc(pos, M), coriolis_acc(v_linear, v_radial) )
    return acc

def distance(pos_1:np.ndarray, pos_2:np.ndarray = np.array([0,0,0])):
    '''
    Parameters
    ----------
    pos_1 : tablica, współrzędne punktu wyrażone jako (x,y,z).
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

def trajectoryPlasz(dt:float, acc:float, vel:np.ndarray,
               pos:np.ndarray = np.array([0, 0, 0])):
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
    rz = vel[2]*dt + pos[2] + 0.5*(dt**2)*acc
   

    return rx, ry, rz

def velocityPlasz(dt:float, acc:float, 
                  vel:np.ndarray = np.array([])):
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

def timePlasz(acc:float, vel:np.ndarray,
              pos:np.ndarray = np.array([0, 0, 0])):
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
    delta = (-vel[2])**2 - 2*acc*pos[2]
    #t = float( (vel[2] - delta**(1/2)) / (-acc) )
    t = 1/acc; t *= -1
    t *= vel[2] - delta**(1/2)
    return t

def maxHeight(acc:float, vel:np.ndarray,
              pos:np.ndarray = np.array([0, 0, 0])):
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
    t = 0.5 * timePlasz(acc, vel, pos)
    h = pos[2] + vel[2] * t + 0.5 * acc * (t**2)
    return h

def reach(acc:float, vel:np.ndarray,
          pos:np.ndarray = np.array([0, 0, 0])):
    '''
    Parameters
    ----------
    acc : float, przyspieszenie grawitacyjne.
    vel : np.array([]), prędkosć początkowa.
    pos : np.array([]), pozycja początkowa. The default is np.array([0, 0, 0]).

    Returns
    -------
    z : float, zasięg.
    '''

    # oblicza całkowity czas ruchu, następnie położenie po zakończeniu ruchu i odległość w której się wtedy znajduje
    t = timePlasz(acc, vel, pos)
    z = distance(trajectoryPlasz(t, acc, vel, pos))
    
    return z
