'''
Created on 7 oct 2021

@author: oscar
'''
from Ejercicio4 import ApartadoA

cuestionarios  = (datos1[0], datos2[0])

parciales = (datos1[1], datos2[1])

proyectos = (datos1[2], datos2[2])

if __name__ == '__main__':
    
    print("Introduzca los datos del primer cuatrimestre: ")
    datos1 = ApartadoA.entrada_datos()
    print("Introduzca los datos del segundo cuatrimestre: ")
    datos2 = ApartadoA.entrada_datos()
    
    
    
    

def calcula_nota_evaluacion_continua(cuestionarios, parciales, proyectos):
    
    nota1 = ApartadoA.calcula_nota_cuatrimestre(cuestionarios[0], parciales[0], proyectos[0])
    nota2 = ApartadoA.calcula_nota_cuatrimestre(cuestionarios[1], parciales[1], proyectos[1])
    
    notaEvalCont = (nota1 + nota2)/2
    
    if (nota1 < 4 or nota2 < 4) and notaEvalCont > 4:
        notaEvalCont = 4
    
    return notaEvalCont

print(calcula_nota_evaluacion_continua(cuestionarios, parciales, proyectos))