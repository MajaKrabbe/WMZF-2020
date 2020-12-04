'''
Maja Zdancewicz, Aleksandra Zając
Ruch punktu materialnego w polu grawitacyjnym
'''

import matplotlib.pyplot as plot
import numpy as np
import constants as const
import data_input as din
import data_init as ini

#todo: plik .dat z danymi dostępnych środowisk, wczytywanie go w temp_input().
# format środowisk widzę tak:
# name, gravfieldtype, surfacegrav, radius, rotation
# name - bez polskich znaków
# gravfieldtype - pole jednorodne czy centralne
# surfacegrav - przyspieszenie graw. na powierzchni. z tego i promienia można policzyć masę ciała, kiedy jest ona potrzebna
# radius - promień kuli, -1 dla pola jednorodnego (płaszczyzna)
# rotation - prędkość kątowa obrotu środowiska. środowisko w wykresach chyba powinno być niezmienne, i wtedy pojawi się ten Coriolis

def main():
    ini.dinit()

    return 0

if __name__ == '__main__':
    main()