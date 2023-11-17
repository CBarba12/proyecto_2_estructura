from collections import deque
import re

from Tabla_Simbolos import Tabla_Simbolos

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



def es_numero(palabra):
    try:
        float(palabra)
        return True
    except ValueError:
        return False  

#def corte_palabras(fuente):

     # Utilizamos una expresión regular para dividir la cadena en partes de caracteres y letras
  #  coincidencias = re.split(r'(\W+)', fuente)  # '\W+' coincide con uno o más caracteres no alfabéticos

    # Filtramos las partes para excluir espacios en blanco
   # coincidencias = [coincidencias for coincidencias in coincidencias if not coincidencias.isspace()]

    #return coincidencias


def corte_palabras(oracion):
    palabras_y_simbolos = re.findall(r'\b\w+\b|\S', oracion)
    return palabras_y_simbolos    
    





 

class AnalizadorSemantico:

    def __init__(self):
        self.tabla_de_simbolos = Tabla_Simbolos()  # Asumo que TablaDeSimbolos es la clase que estás utilizando

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
        palabras = corte_palabras(linea.strip())
        conta = len(palabras)



    



        


if __name__ == "__main__":
    a = AnalizadorSemantico()

   
    nombre_archivo = "m.txt"

    contenido_codigo = a.leer_archivo_texto(nombre_archivo)

    if contenido_codigo:
        a.analizar_codigo(contenido_codigo)
    else:
        print("No se pudo analizar el código debido a errores en la lectura del archivo.")