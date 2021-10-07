'''
Created on 7 oct 2021

@author: oscar
'''


def lee_real(mensaje):
    
    string, real = mensaje.split(' ')
    real = int(real)
    
        
    return string, real

if __name__ == '__main__':
    mensaje = input("Introduzca una palabra y un numero separados por espacios ")
    print(lee_real(mensaje))
    
    