#En este segundo ejercicios tendréis que crear un script que nos diga si es la hora de ir a casa. Tendréis que hacer uso del modulo time. 
#Necesitaréis la fecha del sistema y poder comprobar la hora.
#En el caso de que sean más de las 7, se mostrará un mensaje y en caso contrario, haréis una operación para calcular el tiempo que queda de trabajo.

import time

def main():
    hora_actual = time.strftime('%H')
    if int(hora_actual)>19 or int(hora_actual)<8:
        print('Es hora de estar en casa')
    else:
        falta = 19-int(time.strftime('%H'))
        print('Falta ', falta, 'para estar en casa')


if __name__ == '__main__':
    main()
