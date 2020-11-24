'''
Maja Zdancewicz, Aleksandra Zając
Ruch punktu materialnego w polu grawitacyjnym
'''

import matplotlib.pyplot as plot
import numpy as np

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

    print('Wybierz środowisko ruchu. Dostępne środowiska:')
    #todo: wyświetlanie środowisk

    environment = input()
    #todo: normalizacja nazwy do małych liter i bez polskich znaków. dopasowanie do jednego z istniejących środowisk
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

    #todo: polożenie geograficzne dla flagCoriolis == True, dla False - ustawić opłożenie na biegun północny bo i tak to będzie bez znaczenia

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

    velocity = np.ndarray()
    while true:
        velocity[0] = input('Podaj typ współrzędnych prędkości (1-kartezjańskie, 2-cylindryczne, 3-sferyczne):')
        try:
            velocity[0] = int(velocity[0])
            if not (velocity[0] == 1 or velocity[0] == 2 or velocity[0] == 3):
                raise ValueError
        except:
            continue
        else:
            break
    while true:
        if velocity[0] == 1:
            print('Układ współrzędnych kartezjańskich; x, y - współrzędne poziome, z - współrzędna pionowa. Podaj współrzędną x prędkości [m/s]:')
            velocity[1] = input()
            velocity[2] = input('Podaj współrzędną y prędkości [m/s]:')
            velocity[3] = input('Podaj współrzędną z prędkości [m/s]:')
        elif velocity[0] == 2:
            print('Układ współrzędnych cylindrycznych. Podaj kierunek w radianach:')
            velocity[1] = input()
            velocity[2] = input('Podaj współrzędną poziomą prędkości [m/s]:')
            velocity[3] = input('Podaj współrzędną pionową prędkości [m/s]:')
        elif velocity[0] == 3:
            print('Układ współrzędnych sferycznych. Podaj azymut w radianach:')
            velocity[1] = input()
            velocity[2] = input('Podaj nachylenie do poziomu w radianach:')
            velocity[3] = input('Podaj szybkość [m/s]:')
        try:
            0 == 0
            #todo: konwersja na floaty, kąty znormalizować bo obsługujemy tylko wartości [0,2pi) dla azymutu i [0.5pi,-0.5pi] dla nachylenia
            #      dla radianów sprawdzić czy format jest 0.0 czy raczej 0.0pi / 0.0 pi -> wtedy trzeba konwertować na liczbę postaci 0.0*pi
            #      konwertować nachylenie od poziomu na nachylenie od osi pionowej; wtedy kąt powinien być jest [0,pi]
        except:
            print('Podano niepoprawne współrzędne.')
            continue
        else:
            break
    return (environment, flagCoriolis, height, velocity)









def main():
    return 0

if __name__ == '__main__':
    main()