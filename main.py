'''
Maja Zdancewicz, Aleksandra Zając
Ruch punktu materialnego w polu grawitacyjnym
'''
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np
import constants as const
import data_input as din
import data_init as ini
import movement as mv
import wykres as wyk

def main():
    ini.dinit()
    data = din.data_input()
    if data['name'] == 'error':
        return 1

    if data['grav_type'] == 'centralne':
        if data['flag_rot'] == False:
            data['v_rot'] = 0

        dt = 0.2
        matrix = np.zeros((0,3), dtype = float)
        pos = []
        pos.append(data['pos'])
        posx = pos[0][0]
        posy = pos[0][1]
        posz = pos[0][2]
        matrix = np.append(matrix,[[posx,posy,posz]],axis=0)
        acc = mv.acceleration(data['pos'], data['mass'], data['v_lin'], data['v_rot'])
        vel = data['v_lin']

        i = 0              
        while mv.distance(pos[len(pos)-1]) >= data['radius']:
            i += 1
            dPos = mv.position(dt, pos[i-1], vel, acc)          
            matrix = np.append(matrix,[[dPos[0],dPos[1],dPos[2]]],axis=0)      
            pos.append(dPos)
            vel = mv.velocity(dt, vel, acc)
            acc = mv.acceleration(pos[i], data['mass'], vel, data['v_rot'])
          
        
        t = i * dt  # czas całkowity
        R = data['radius']
        
        wyk.wykresCentr(matrix, R)
        #todo: wykres, przedstawienie danych

    elif data['grav_type'] == 'jednorodne':
        tmax = mv.timePlasz(data['surf_acc'], data['v_lin'], data['pos'])
        steps = 5000
        time = np.linspace(0, tmax, steps)

        pos = np.zeros((steps, 3), dtype = float)

        for step in range(0, steps):
            x,y,z = mv.trajectoryPlasz(time[step], data['surf_acc'], data['v_lin'], data['pos'])
            pos[step][0] = x 
            pos[step][1] = y
            pos[step][2] = z

        h_max = mv.maxHeight(data['surf_acc'], data['v_lin'], data['pos'])
        h_max_test = pos[round(0.5*steps)]     # powinno być bliskie h_max

        reach = mv.reach(data['surf_acc'], data['v_lin'], data['pos'])
        
        wyk.wykresPlaszcz(pos)
        
        # todo: wykres, przedstawienie danych

    return 0

if __name__ == '__main__':
    main()