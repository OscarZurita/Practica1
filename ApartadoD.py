from Ejercicio4 import ApartadoC
from Ejercicio4 import ApartadoB

def lee_nota(mensaje):
    mensajeDividido = ApartadoC.lee_real(mensaje)
    string = mensajeDividido[0]
    real = mensajeDividido[1]
    
    if(string[0] == 'C' or string[0] == 'c'):
        if(real == 1):
            print(ApartadoB.cuestionarios[0][0])
        elif(real == 2):
            print(ApartadoB.cuestionarios[0][1])
        elif(real == 3):
            print(ApartadoB.cuestionarios[0][2])
        elif(real == 4):
            print(ApartadoB.cuestionarios[1][0])
        elif(real == 5):
            print(ApartadoB.cuestionarios[1][1])
        elif(real == 6):
            print(ApartadoB.cuestionarios[1][2])
    elif(string[1] == 'a'):
        print(ApartadoB.parciales[real-1])
    elif(string[1] == 'r'):
        print(ApartadoB.proyectos[real-1])
    
    return

mensaje = input("Introduzca la nota que quiera buscar, ya sea de cuestrionarios, parciales o de  proyectos, indicando, tras un espacio, el numero correspondiente")
lee_nota(mensaje)