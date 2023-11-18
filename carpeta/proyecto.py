from collections import deque
import re

from Tabla_Simbolos import Tabla_Simbolos
from Utiles import Utilidades

operadores = {
    '+': 'Suma',
    '=': 'igual',
    '-': 'Resta',
    '*': 'Multiplicación',
    '/': 'División',
    '%': 'Módulo',
    '==': 'Igual a',
    '!=': 'Diferente de',
    '<': 'Menor que',
    '>': 'Mayor que',
    '<=': 'Menor o igual que',
    '>=': 'Mayor o igual que',
    '|': 'OR ',
    '<<': 'Desplazamiento izquierdo',
    '>>': 'Desplazamiento derecho'
}
tipos_de_datos = {'int':'Entero', 'float':'flotante', 'string':'cadena', 'void':'void'}
palabras_reservadas = {
    'if': 'if',
    'while': 'bucle while',
}


operadores_llave=operadores.keys()
tipos_de_datos_llave=tipos_de_datos.keys()
palabras_reservadas_llave=palabras_reservadas.keys()
#-----------------------------------------------------------------






class AnalizadorSemantico:

    def __init__(self):
        self.tabla_de_simbolos = Tabla_Simbolos()  # Asumo que TablaDeSimbolos es la clase que estás utilizando
        self.utiles=Utilidades()

    def leer_archivo_texto(self, nombre_archivo):
        try:
            with open(nombre_archivo, "r", encoding="utf-8") as archivo:
                contenido = archivo.read()
            return contenido
        except FileNotFoundError:
            print(f"Error: El archivo '{nombre_archivo}' no se encuentra.")
            return None
        except Exception as e:
            print(f"Error inesperado al leer el archivo: {str(e)}")
            return None

    def analizar_codigo(self, codigo):
     
        lineas = codigo.split('\n')

        for numero_linea, linea in enumerate(lineas, start=1):
        
            
            self.analizar_linea(linea, numero_linea)


    def analizar_linea(self, linea, numero_linea):
        palabras = self.utiles.corte_palabras(linea.strip())
        conta = len(palabras)

        for posicion in range(conta):
         
            palabra_actual = palabras[posicion].strip()


            if palabra_actual in tipos_de_datos_llave and "=" in palabras:
                
                if posicion+1<conta and posicion+2<conta:
                    if palabras[posicion+2]=="=" :
                        k= palabras[posicion+3]


                      #  print(self.tabla_de_simbolos.buscar_simbolo(k))
                        if palabra_actual == "int" and ( self.utiles.es_numero(k) or self.tabla_de_simbolos.obtener_tipo(k)=="int"):
                           
                            pos = posicion + 4

                            if pos<conta:
                                for cont in range(pos, len(palabras)):
                                    if palabras[cont] in operadores_llave:
                                        if  ( self.utiles.es_numero(palabras[cont+1]) or self.tabla_de_simbolos.obtener_tipo(palabras[cont+1])=="int"):
                                             
                                            self.tabla_de_simbolos.agregar_simbolo(palabras[posicion+1],palabras[posicion],palabras[cont+1])
                                            print(self.tabla_de_simbolos.obtener_valor( palabras[posicion+1]))

                                    
                                        else:
                                            print(f"Error - Línea {numero_linea}: asignacion de tipo de dato   incorrecta")
                            else:
                                self.tabla_de_simbolos.agregar_simbolo(palabras[posicion+1],palabras[posicion],palabras[posicion+3])
         

                        elif palabra_actual == "string" and  self.utiles.es_numero(k)==False  and k!="":
                                    
                                pos = posicion + 6
                                total=True

                                if pos<conta:
                                    for cont in range(pos, len(palabras)):
                                        if palabras[cont] in operadores_llave:
                                            
                                            if  ( self.utiles.es_numero(palabras[cont+1]) or self.tabla_de_simbolos.obtener_tipo(palabras[cont+1])!="String"):
                                                  total=False
                                               
                                            

                                    if total:
                                        self.tabla_de_simbolos.agregar_simbolo(palabras[posicion+1],palabras[posicion],palabras[cont+1])
                                    else:
                                      print(f"Error - Línea {numero_linea}: asignacion de tipo de dato   incorrecta")     

                                elif  palabras[posicion+1] in self.tabla_de_simbolos.obtener_nombres():
                                    print(f"Error - Línea {numero_linea}: asignacion de tipo de dato   incorrecta")   
                                
                                else:
                                    self.tabla_de_simbolos.agregar_simbolo(palabras[posicion+1],palabras[posicion],palabras[posicion+4])

                                    
                                  ##  self.tabla_de_simbolos.agregar_simbolo(palabras[1],palabras[0],palabras[4])
                                    ##print ( self.tabla_de_simbolos.obtener_simbolos())

                        elif palabra_actual == "float" and  self.utiles.es_numero(k) :
                                    self.tabla_de_simbolos.agregar_simbolo(palabras[1],palabras[0],palabras[3])
                        
                        elif palabra_actual == "void" and  self.utiles.es_numero(k)==False  and k!="" or self.utiles.es_numero(k)==True and '(' is not palabras:
                                    print(f"Error - Línea {numero_linea}: tipo de dato '{palabras[posicion].strip()}'  incorrecta")

                        else:
                          
                            print(f"Error - Línea {numero_linea}: tipo de dato '{palabras[posicion].strip()}'  incorrecta")
                                    
                    



               # print(self.tabla_de_simbolos.obtener_simbolos())
       



    



        


if __name__ == "__main__":
    a = AnalizadorSemantico()

   
    nombre_archivo = "m.txt"

    contenido_codigo = a.leer_archivo_texto(nombre_archivo)

    if contenido_codigo:
        a.analizar_codigo(contenido_codigo)
    else:
        print("No se pudo analizar el código debido a errores en la lectura del archivo.")