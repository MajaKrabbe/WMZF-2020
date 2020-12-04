import numpy as np
import constants as const


def gravityAcceleration(radius, x, y, z, surfaceGravAcceleration):
    # r odległość w prostej linii punktu od powierzchni
    r = (((radius - x) ** 2 + (radius - y) ** 2 + (radius - z) ** 2) ** (1 / 2))

    #G = 6.67430 * (10 ** (-11))
    M = surfaceGravAcceleration * (radius ** 2) / const.GRAV_CONST

    a = const.GRAV_CONST * M / (radius + r) ** 2
    # To samo generalnie:
    # g = (surfaceGravAcceleration/(1+(r/radius))**2)

    return a

