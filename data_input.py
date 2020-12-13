import numpy as np
import constants as const

def data_conv(tup:tuple):
    '''
    Konwertuje dane na słownik. TYLKO DO UŻYCIA W FUNKCJI data_init()
    '''

    # konwersja położenia ze współrzędnych sferycznych na kartezjańskie
    pos = np.zeros(3)
    pos_r = tup[3] + tup[0]['radius']
    pos[0] = pos_r * np.sin(tup[2][1]) * np.cos(tup[2][0])
    pos[1] = pos_r * np.sin(tup[2][1]) * np.sin(tup[2][0])
    pos[2] = pos_r * np.cos(tup[2][1])

    # konwerssja prędkości na współrzędne kartezjańskie
    vel = np.zeros(3)
    if tup[4][0] == 1:      # kartezjańskie
        vel[0] = tup[4][1]
        vel[1] = tup[4][2]
        vel[2] = tup[4][3]
    elif tup[4][0] == 2:    # cylindryczne
        vel[0] = tup[4][2] * np.cos(tup[4][1])
        vel[1] = tup[4][2] * np.sin(tup[4][1])
        vel[2] = tup[4][3]
    elif tup[4][0] == 3:    # sferyczne
        vel[0] = tup[4][3] * np.sin(tup[4][2]) * np.cos(tup[4][1])
        vel[1] = tup[4][3] * np.sin(tup[4][2]) * np.sin(tup[4][1])
        vel[2] = tup[4][3] * np.cos(tup[4][2])

    env = {
        'name': tup[0]['name'],
        'grav_type': tup[0]['gravfieldtype'],
        'surf_acc': tup[0]['surfacegrav'],
        'radius': tup[0]['radius'],
        'v_rot': tup[0]['rotation'],
        'mass': tup[0]['mass'],
        'flag_rot': tup[1],
        'pos': pos,
        'v_lin': vel
    }

    return env

def data_input():
    '''
    Przyjmuje dane od użytkownika, a następnie konwertuje je na format przyjazny obliczeniom.

    Zwraca słownik zawierający elementy:
        - name
        - grav_type
        - surf_acc
        - radius
        - v_rot
        - mass
        - flag_rot
        - pos
        - v_lin
    '''
    # '''
    # Wczytuje dane i konwertuje je na bardziej przyjazne obliczeniom.
    # Zwraca krotkę o następujących elementach:
    # [0] - environment, słownik - zawiera elementy: name, gravfieldtype, surfacegrav, radius, rotation, mass \n
    # [1] - flagCoriolis, boolean - czy uwzględnione jest występowanie siły Coriolisa \n
    # [2] - location, ndarray - postaci [a,b], zawiera położenie początkowe w postaci współrzędnych sferycznych azymutalnej i zenitalnej \n
    # [3] - height, float - odległość od powierzchni ziemi \n
    # [4] - velocity, ndarray - postaci [t,x1,x2,x3], gdzie t - typ współrzędnych (1-kartezjańskie, 2-cylindryczne, 3-sferyczne),
    # x1,x2,x3 - kolejne współrzędne prędkości
    #
    # :return: krotka zawierająca informacje o środowisku ruchu, występowaniu siły Coriolisa,
    #          położeniu geograficznym, wysokości nad powierzchnią ziemi, prędkości początkowej
    # '''

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
        print(element['name'], end='\t')
    environment = input('\nWybierz środowisko ruchu:')
    environment = environment.lower()
    if environment == 'księżyc' or environment == 'księzyc' or environment == 'ksieżyc':
        environment = 'ksiezyc'
    if environment == 'płaszczyzna':
        environment = 'plaszczyzna'
    #todo: inne warunki dla polskich znaków?
    for env in envs:
        if env['name'].lower() == environment:
            environment = env
            break

    # czy uzwględniamy siłę Coriolisa
    while True:
        if environment['gravfieldtype'] == 'centralne':
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
        else:
            flagCoriolis = False
            break

    # współrzędne geograficzne położenia początkowego
    location = np.zeros(2)
    if flagCoriolis == True:
        geolength = input('Podaj długość geograficzną położenia startowego w stopniach. Wielkości dodatnie - długość geograficzna wschodnia (E), ujemna - zachodnia (W):')
        geowidth = input('Podaj szerokość geograficzną położenia startowego w stopniach. Wielkości dodatnie - szerokość geograficzna północna (N), ujemne - południowa (S):')
        while True:
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
    while True:
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
    while True:
        temp = input('Podaj typ współrzędnych prędkości (1-kartezjańskie, 2-cylindryczne, 3-sferyczne):')
        try:
            velocity[0] = float(temp)
            if not (velocity[0] == 1 or velocity[0] == 2 or velocity[0] == 3):
                raise ValueError
        except:
            continue
        else:
            break
    while True:
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
            if velocity[0] == 2 or velocity[0] == 3:
                if temp1.endswith(('pi', 'PI', 'Pi')):
                    if temp1[0:len(temp1) - 2] == '-':
                        temp1 = temp1.replace('-', '-1')
                    elif temp1[0:len(temp1) - 2] == '':
                        temp1 = '0' + temp1
                    temp1 = float(temp1[0:len(temp1)-2]) * const.PI
                else:
                    temp1 = float(temp1)
                while temp1 >= 2*const.PI:
                    temp1 -= 2 * const.PI
                while temp1 < 0:
                    temp1 += 2 * const.PI
            if velocity[0] == 3:
                if temp2.endswith(('pi', 'PI', 'Pi')):
                    if temp2[0:len(temp2) - 2] == '-':
                        temp2 = temp2.replace('-', '-1')
                    elif temp2[0:len(temp2) - 2] == '':
                        temp2 = '0' + temp2
                    temp2 = float(temp2[0:len(temp2) - 2]) * const.PI
                else:
                    temp2 = float(temp2)
                #konwersja z nachylenia do poziomu na odchylenie od osi pionowej
                temp2 += 0.5*const.PI
                if temp2 < 0:
                    temp2 *= (-1)
                if temp2 > const.PI:
                    temp2 = 2*const.PI - temp2
            velocity[1] = float(temp1)
            velocity[2] = float(temp2)
            velocity[3] = float(temp3)
        except:
            print('Podano niepoprawne współrzędne.')
            continue
        else:
            break

    final =  (environment, flagCoriolis, location, height, velocity)
    return data_conv(final)

