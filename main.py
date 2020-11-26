'''
Maja Zdancewicz, Aleksandra Zając
Ruch punktu materialnego w polu grawitacyjnym
'''

import matplotlib.pyplot as plot
import numpy as np
import constants as const

#todo: plik .dat z danymi dostępnych środowisk, wczytywanie go w temp_input().
# format środowisk widzę tak:
# name, gravfieldtype, surfacegrav, radius, rotation
# name - duh
# gravfieldtype - pole jednorodne czy centralne
# surfacegrav - przyspieszenie graw. na powierzchni. z tego i promienia można policzyć masę ciała, kiedy jest ona potrzebna
# radius - promień kuli, -1 dla pola jednorodnego (płaszczyzna)
# rotation - prędkość kątowa obrotu środowiska. środowisko w wykresach chyba powinno być niezmienne, i wtedy pojawi się ten Coriolis

def temp_input():
    '''tymaczasowo, zawartość funkcji pewnie się do czegoś przyda ale na nie wiem czy chcemy to w takiej postaci'''

    # wybór układu ruchu
    file = open("environments.dat", 'r')
    # envs = np.ndarray()
    envs = []
    for line in file:
        (name, gravfieldtype, surfacegrav, radius, rotation) = line.split()
        mass = float(surfacegrav) * float(radius)**2 / const.GRAV_CONST
        dct = {'name':name, 'gravfieldtype':gravfieldtype, 'surfacegrav':float(surfacegrav), 'radius':float(radius), 'rotation':float(rotation), 'mass':mass}
        # envs = np.append(envs, dct)
        envs.append(dct)
    file.close()
    print('Dostępne środowiska:')
    for element in envs:
        print(element[name], end='\t')
    environment = input('\nWybierz środowisko ruchu:')
    #todo: normalizacja nazwy do małych liter i bez polskich znaków. dopasowanie do jednego z istniejących środowisk

    # czy uzwględniamy siłę Coriolisa
    while true:
        if environment[gravfieldtype] == 'centralne':
            flagCoriolis = input('Czy uwzględnić wpływ rotacji ciała na trajektorię? Y/N')
            try:
                if flagCoriolis.lower() == 'n':
                    flagCoriolis = False
                    break
                elif flagCoriolis.lower() == 'y':
                    flagCoriolis = True
                    break
                else:
                    continue
            except:
                continue

    # współrzędne geograficzne położenia początkowego
    location = np.zeros(2)
    if flagCoriolis == True:
        geolength = input('Podaj długość geograficzną położenia startowego w stopniach. Wielkości dodatnie - długość geograficzna wschodnia (E), ujemna - zachodnia (W):')
        geowidth = input('Podaj szerokość geograficzną położenia startowego w stopniach. Wielkości dodatnie - szerokość geograficzna północna (N), ujemne - południowa (S):')
        while true:
            try:
                if location[0] > 180 or location[0] < -180 or location[1] > 90 or location[1] < -90:
                    raise ValueError
                location[0] = float(geolength) / const.DEG_PER_RAD
                location[1] = float(geowidth) / const.DEG_PER_RAD
            except ValueError:
                print('Podaj poprawne współrzędne geograficzne.')
                continue
            except:
                print('Podaj wartości liczbowe.')
                continue
            else:
                break
        # konwersja długości geograficznej na współrzędne sferyczne
        if location[0] < 0:
            location[0] += 2*const.PI
        # konwersja szerokości geograficznej na współrzędne sferyczne
        location[1] *= (-1)
        location[1] += 0.5*const.PI

    # położenie początkowe nad powierzchnią ziemi
    while true:
        height = input('Podaj wysokość (w metrach) nad powierzchnią ziemi w chwili początkowej:')
        try:
            height = float(height)
            if height < 0:
                raise ValueError
        except:
            print('Wprowadź liczbę rzeczywistą nieujemną.')
            continue
        else:
            break

    # prędkość w jednym z typów układów współrzędnych
    velocity = np.zeros(4)
    while true:
        temp = input('Podaj typ współrzędnych prędkości (1-kartezjańskie, 2-cylindryczne, 3-sferyczne):')
        try:
            velocity[0] = float(temp)
            if not (velocity[0] == 1 or velocity[0] == 2 or velocity[0] == 3):
                raise ValueError
        except:
            continue
        else:
            break
    while true:
        if velocity[0] == 1:
            print('Układ współrzędnych kartezjańskich; x, y - współrzędne poziome, z - współrzędna pionowa. Podaj współrzędną x prędkości [m/s]:')
            temp1 = input()
            temp2 = input('Podaj współrzędną y prędkości [m/s]:')
            temp3 = input('Podaj współrzędną z prędkości [m/s]:')
        elif velocity[0] == 2:
            print('Układ współrzędnych cylindrycznych. Podaj kierunek w radianach:')
            temp1 = input()
            temp2 = input('Podaj współrzędną poziomą prędkości [m/s]:')
            temp3 = input('Podaj współrzędną pionową prędkości [m/s]:')
        elif velocity[0] == 3:
            print('Układ współrzędnych sferycznych. Podaj azymut w radianach:')
            temp1 = input()
            temp2 = input('Podaj nachylenie do poziomu w radianach:')
            temp3 = input('Podaj szybkość [m/s]:')
        try:
            #todo: konwersja na floaty, kąty znormalizować bo obsługujemy tylko wartości [0,2pi) dla azymutu i [0.5pi,-0.5pi] dla nachylenia
            #      dla radianów sprawdzić czy format jest 0.0 czy raczej 0.0pi / 0.0 pi -> wtedy trzeba konwertować na liczbę postaci 0.0*pi
            #      konwertować nachylenie od poziomu na nachylenie od osi pionowej; wtedy kąt powinien być jest [0,pi]




        except:
            print('Podano niepoprawne współrzędne.')
            continue
        else:
            break

    return (environment, flagCoriolis, location, height, velocity)
    #todo: UPEWNIĆ SIĘ ŻE WSZYSTKIE POTRZEBNE INFORMACJE SĄ ZWRACANE PO DOKOŃCZENIU KODU FUNKCJI









def main():
    return 0

if __name__ == '__main__':
    main()