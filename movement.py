import numpy as np
import constants as const

# todo: funkcje na ruch w polu jednorodnym

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
