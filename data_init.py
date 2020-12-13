#name, graVtype, surfaceGravAcceleration, radius, radialVelocity

def dinit():
#    data = '''Plaszczyzna jednorodne 9.81 -1 0
#Ziemia centralne 9.81 6371*(10**3) 2.33*3.1415*(10**(-5))
#Mars centralne 3.7 3389.5*(10**3) 8.33*3.1415*(10**(-7))
#Ksiezyc centralne 1,62 1737.1*(10**3) 2.25*3.1415*(10**(-5))'''

    data = (
'''Plaszczyzna jednorodne -9.81 -1 0
Ziemia centralne 9.81 6.371e+6 7.32e-5
Mars centralne 3.7 3.3895e+6 2.617e-6
Ksiezyc centralne 1.62 1.7371e+6 7.07e-5''')

    file = open('environments.dat', 'w+')
    file.write(data)
    file.close()