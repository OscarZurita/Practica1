# -*- coding: utf-8 -*-

'''
Created on 5 oct 2021

@author: oscar
'''

def calculo_nota(aciertos, errores, totalRespuestas):
    
    nota = (aciertos*10/totalRespuestas)-(errores*10-(50-totalRespuestas))
    return max(0, nota)

def entrada_datos():
    aciertos = int(input("Introduzca el número de aciertos "))
    errores = int(input("Introduzca el numero de errores "))
    totalRespuestas = int(input("Introduzca el total de repuestas "))
    return aciertos, errores, totalRespuestas
