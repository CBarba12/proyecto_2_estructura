from collections import deque
import re


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
#-----------------------------------------------------------------

class Tabla_Simbolos:
    def __init__(self):
        self.simbolos = {}

    def agregar_simbolo(self, nombre, tipo, valor=None):
        self.simbolos[nombre] = {'tipo': tipo, 'valor': valor}

    def buscar_simbolo(self, nombre):
        return self.simbolos.get(nombre, {'tipo': None, 'valor': None})


    def obtener_simbolos(self):
        return list(self.simbolos.keys())   
def leer_archivo_texto(nombre_archivo):
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
    

def corte_palabras(fuente):

     # Utilizamos una expresión regular para dividir la cadena en partes de caracteres y letras
    coincidencias = re.split(r'(\W+)', fuente)  # '\W+' coincide con uno o más caracteres no alfabéticos

    # Filtramos las partes para excluir espacios en blanco
    coincidencias = [coincidencias for coincidencias in coincidencias if not coincidencias.isspace()]

    return coincidencias

operadores_key=operadores.keys()

palabras_reservadas_key=palabras_reservadas.keys()


def analizar_codigo(nombre_archivo):
    a = leer_archivo_texto(nombre_archivo)
    tabla = Tabla_Simbolos()
    in_funcion = False
    tipo_funcion = None

    program=a.split('\n')
    count=0
    count_2=0

    pila = deque()
    pila.append("(")
    pila.append("(")
    pila.pop()
    pila.pop()
 
     
    print(" ")
    print(" ")
       
    for line in program: #inicio de cada linea
     #   print(f"Error - Línea {count}: Variable '{palabras[posicion-1].strip()}' NO ESTA DECLARADO")

        count+=1
        tokens = line.split(' ')  # Separar la línea en tokens
        contador = len(tokens)  # Calcular la cantidad de tokens
        palabras = corte_palabras(line)
        conta=len(palabras)


        for posicion in range(conta):
#----------------------------asignacion de una variable-----------------------------------------------------------------
            if palabras[posicion].strip() in tipos_de_datos and "=" in line:
                
                tabla.agregar_simbolo(palabras[posicion+1],palabras[posicion],palabras[posicion+3])

                print(tabla.buscar_simbolo(palabras[posicion+1]))


            elif palabras[posicion].strip() in tabla.obtener_simbolos():
                print("la variable esta definida")

            elif palabras[posicion].strip() is not tipos_de_datos  and "=" in line and palabras[posicion].strip() !="":
                  
                  

                  if range(conta) >posicion+3:
                    print(f"Error - Línea {count}: Variable '{palabras[posicion].strip()}' NO ESTA DECLARADO") 
           
                 
  





from collections import deque

tipos_de_datos = {'void', 'int', 'float', 'string'}


    


def analizar_codigo(nombre_archivo):
    programa = leer_archivo_texto(nombre_archivo).split('\n')
    tabla = Tabla_Simbolos()
    
    in_funcion = False
    tipo_funcion = None
    alcance_actual = "global"
    errores = []

    for numero_linea, line in enumerate(programa, start=1):
        
        pal=line.strip();
        
        palabras = corte_palabras(pal)
        conta = len(palabras)
        
        if palabras[numero_linea] !="":  # si encue  x=56
            if palabras[0] is not tipos_de_datos and "="  in palabras:
                if palabras[0]!=tipos_de_datos and line[0] is not tabla:
                    print(f"Error - Línea {numero_linea}: '{palabras[0]}' error de declaracion")
            
        
        

        for posicion in range(conta):
            
            palabra_actual = palabras[posicion].strip()

            if palabra_actual in tipos_de_datos and "=" in line:
                if alcance_actual == "global":
                    tabla.agregar_simbolo(palabras[posicion + 1], palabra_actual, alcance_actual)
                else:
                    errores.append(f"Error - Línea {numero_linea}: '{palabras[posicion + 1]}' no puede ser declarado en una función")

            elif palabra_actual == "{":
                print("se abre una funcion")

            elif palabra_actual == "}":
               print("se cierra una funcion")

            elif palabra_actual == "if" or palabra_actual == "while":
                print("se cierra una funcion")

            elif palabra_actual == "return":
                if tipo_funcion and tipo_funcion != tipos_de_datos.index(palabras[posicion + 1].strip()):
                    errores.append(f"Error - Línea {numero_linea}: Valor de retorno no coincide con la declaración de la función")
            
            elif palabra_actual == "void":
                in_funcion = True
                tipo_funcion = None
                if palabra_actual != palabras[posicion + 1].strip():
                    errores.append(f"Error - Línea {numero_linea}: Declaración de función incorrecta")
                elif "(" not in palabras[posicion + 2]:
                    errores.append(f"Error - Línea {numero_linea}: Sintaxis incorrecta de declaración de función")

            elif palabra_actual in tipos_de_datos and in_funcion:
                tipo_funcion = tipos_de_datos.index(palabra_actual)

        if "}" in palabras:
            in_funcion = False
            tipo_funcion = None



    if errores:
        for error in errores:
            print(error)
    else:
        print("El código fuente es correcto.")
        
        
        



        

if __name__ == "__main__":
    analizar_codigo("m.txt")