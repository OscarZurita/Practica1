# -*- coding: utf-8 -*-

'''
C1 --->  CUESTIONARIO1
C2 ---> CUESTIONARIO2
C3 ---> CUESTIONARIO3
C4 ---> CUESTIONARIO4
C5 ---> CUESTIONARIO5
C6 ---> CUESTIONARIO6
P1 ---> PARCIAL1
P2 ---> PARCIAL2
PRY1 ---> PROYECTO1
PRY2 ---> PROYECTO2

'''

def entrada_datos():
    C1 = input("Introduzca la nota del primer cuestionario ")
    C2 = input("Introduzca la nota del segundo cuestionario ")
    C3 = input("Introduzca la nota del tercer cuestionario ")
    C1 = int(C1)
    C2 = int(C2)
    C3 = int(C3)
        
    Cuestionarios = (C1,C2,C3)
    
    P1 = input("Introduzca la nota del parcial ")
    P1 = int(P1)
        
    PRY1 = input("Introduzca la nota del proyecto ")
    PRY1 = int(PRY1)
    
    return Cuestionarios, P1, PRY1


def calcula_nota_cuatrimestre(Cuestionarios,P1,PRY1):
    
    notaCuatrimestre = 0.13*(Cuestionarios[0]+Cuestionarios[1]+Cuestionarios[2]) + 0.5 * P1 + 0.1 * PRY1
    
    if(PRY1<5 and notaCuatrimestre >5):
        notaCuatrimestre = 3
    
    return notaCuatrimestre


if __name__ == '__main__':
    
    datos = entrada_datos()
    notaCuatrimestre = float(calcula_nota_cuatrimestre(datos[0], datos[1], datos[2]))
    print(notaCuatrimestre)

