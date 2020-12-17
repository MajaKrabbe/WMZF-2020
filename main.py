'''
Maja Zdancewicz, Aleksandra Zając
Ruch punktu materialnego w polu grawitacyjnym
'''

import matplotlib.pyplot as plot
import numpy as np
import constants as const
import data_input as din
import data_init as ini
import movement as mv

def main():
    ini.dinit()
    data = din.data_input()

    if data['grav_type'] == 'centralne':
        if data['flag_rot'] == False:
            data['v_rot'] = 0

        dt = 0.02   # można by dodać dynamiczne zmienianie dt w zależności od wartości przyspieszenia,
                    # im większe przyspieszenie tym większe dt ?

        pos = []; pos.append(data['pos'])
        acc = mv.acceleration(data['pos'], data['mass'], data['v_lin'], data['v_rot'])
        vel = data['v_lin']

        i = 0;
        while mv.distance(pos[len(pos)-1]) >= data[radius]:
            i += 1
            pos.append(mv.position(dt, pos[i-1], vel, acc))
            vel = mv.velocity(dt, vel, acc)
            acc = mv.acceleration(pos[i], data['mass'], vel, data['v_rot'])

        t = i * dt  # czas całkowity

        #todo: wykres, przedstawienie danych

    elif data['grav_type'] == 'jednorodne':
        tmax = mv.timePlasz(data['surf_acc'], data['v_lin'], data['pos'])
        steps = 5000
        time = np.linspace(0, tmax, steps)

        pos = np.zeros(steps+1)
        #todo: zoptymalizować pętlę?
        for step in range(0, steps+1):
            pos[step] = mv.trajectoryPlasz(time[step], data['surf_acc'], data['v_lin'], data['pos'])

        h_max = mv.maxHeight(data['surf_acc'], data['v_lin'], data['pos'])
        h_max_test = pos[round(0.5*steps)]     # powinno być bliskie h_max

        reach = mv.reach(data['surf_acc'], data['v_lin'], data['pos'])

        # todo: wykres, przedstawienie danych

    return 0

if __name__ == '__main__':
    main()