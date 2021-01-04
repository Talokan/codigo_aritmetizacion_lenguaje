# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 13:14:44 2019

@author: fernando
"""

def RecibirLista(): #Recibe la lista que se va a verificar
    lista = []
    salida = 0
    while(salida!=-1):
        salida = int(input("Introduzca el símbolo de la fórmula o bien teclee -1 para salir: "))
        lista.append(salida)
    del lista[-1]
    return lista  

def verificacionSimbolosAdecuados(lista):
    for elemento in lista:
        i = elemento
        if(i%2==0 or i<3): #Verificamos que los elementos de la lista sean mayores o iguales que 3 e impares
            return False
    return True    

def obtenerAridadesTerminosYUnaRelacion(lista): #Obtiene aridades de los terminos y de una sola relación
    listaSinRepeticiones = []
    aridades = []
    if(verificacionSimbolosAdecuados(lista)):
        for elemento in lista:
            if(not(elemento in listaSinRepeticiones)):
                listaSinRepeticiones.append(elemento)
        for elemento in listaSinRepeticiones:
            i = elemento
            if(funcionalTermino(i)):
                j = int(input("Introduzca la aridad del término %d: " %((i-27)/8)))
                aridades.append([0,int((i-27)/8),j])
            elif(relacionalTermino(i)):
                j = int(input("Introduzca la aridad de la relación %d: " %((i-25)/8)))
                aridades.append([1,int((i-29)/8),j])
    return aridades    
                
def variableTermino(num: int): #Función que verifica si un número corresponde a un símbolo variable, tipo de retorno bool
    if((num-23)>=0 and (num-23)%8==0):
        return True
    else:
        return False
    
def constanteTermino(num: int): #Función que verifica si un número corresponde a un símbolo constante, tipo de retorno bool
    if((num-25)>=0 and (num-25)%8==0):
        return True
    else:
        return False    
    
def funcionalTermino(num: int): #Función que verifica si un número corresponde a un símbolo funcional, tipo de retorno bool
    if((num-27)>=0 and (num-27)%8==0):
        return True
    else:
        return False  

def relacionalTermino(num: int): #Función que verifica si un número corresponde a un símbolo relacional, tipo de retorno bool
    if((num-29)>=0 and (num-29)%8==0):
        return True
    else:
        return False        
    
def copiarArregloAPartirDeIndiceDado(lista, posicion: int): #Esta función copia lo que se encuentra entre paréntesis a partir de una posición dada en un arreglo dado (la posición supondremos que se trata de la posición del paréntesis más a la derecha)
     copia = [] #Inicia una lista vacía
     j = 0
     k = 0 #Contador que se mueve entre paréntesis y que respecto a éste indice se añaden elementos significativos a la copia
     while(lista[posicion]!=3): #Se va a identificar el primer paréntesis
         posicion  = posicion - 1
     posicion = posicion + 1 #Se coloca adelante de dicho paréntesis
     while(lista[posicion]!=5): 
         if(lista[posicion]==-1 and lista[posicion+1]==-2): #Si se verifica que en la lista hay un -1 y después un -2 entonces está ante una estructura de tipo funcional/cancelado y paréntesis
             while True:
                 posicion = posicion + 1
                 if(lista[posicion]==-1 and lista[posicion+1]!=-2 and j==0): #Cuando haya verificado la funcional/cancelado y paréntesis ... paréntesis se termina
                     break
                 elif(lista[posicion]==-1 and lista[posicion+1]==-2): #Cuando encuentre una estructura funcional/cancelado y paréntesis suma uno al contador de dichas estructuras
                     j = j + 1
                 elif(lista[posicion]==-1 and lista[posicion+1]!=-2 and j>0): #Cuando encuentre una estructura paréntesis resta uno al contador de dichas estructuras
                     j = j - 1
         copia.insert(k,lista[posicion])  #Si encuentra un -1 (asterisco) lo copia ya que es un elemento que está reconocido como término). En otro caso si se trata de cualquier otro símbolo lo copia
         k = k + 1 #Se mueve una posición a la derecha sobre la lista "copia" y busca más elementos significativos
         posicion = posicion + 1
     return copia # Regresa todo los que se encuentra entre dos paréntesis de la lista original haciendo la cancelación de términos verificados colocando un único -1

def verificarArregloEsTermino(lista, aridad: int): #Esta función verifica que todo lo que se encuentra entre dos paréntesis corresponde en efecto a un término
    k = 0 #Es un contador que va verificando sobre los elementos del arreglo si son como deben ser
    comas = 0 #Contador de comas
    if(len(lista)>0 and len(lista)%2==1): #Verifica si la lista original tiene al menos un elemento, en caso contrario se regresa 0 y también que exista un número impar de dichos elementos pues por cada término debe haber una coma y un término al final
        if(len(lista)==1): #Se verifica el caso especial en el que sólo existe un elemento
            if((variableTermino(lista[0]) or constanteTermino(lista[0]) or lista[0]==-1) and aridad==1): #Debe corresponder a un término, variable o constante
                return True #Regresa 1 si es el caso
            else:
                print("O bien lo que está dentro de los paréntesis no es una variable o constante o un término o bien debería haber más de éstos.")
                return False #Si no regresa 0
        else:
            while(k<=len(lista)-1): #En caso de que existan más elementos dado que hay una cantidad impar va verificando que exista el par término-coma y al final verifica que exista un término
                if(variableTermino(lista[k]) or constanteTermino(lista[k]) or lista[k]==-1): #Verifica que se trate de un término
                    if(k<len(lista)-1): #Si no se trata del último elemento veriica el par término-coma
                        k = k + 1
                        if(lista[k]!=7): #Verfica si después del término hay una coma
                            print("No hay una coma después del término.")
                            return False #Si no regresa 0
                        else:
                            comas = comas + 1 #Cuenta una coma
                            k = k + 1 #Si hay una coma pasa al siguiente número
                    else:
                        k = k + 1 #Si se trata del último número la verificación de que se trata de un término ya se realizó
                else:
                    print("Lo que fue copiado no es una variable, constante o un término cancelado.")
                    return False #Si en algún paso no se trata de un término, termina y regresa 0
            if(comas==aridad-1): #Si cumple todo el ciclo anterior y se trata de un término bien formado, verifica que el número de comas coincida con la aridad menos uno es decir que en efecto hay tantos términos como la aridad
                return True #Regresa verdadero si esto es así
            else:
                print("El número de comas no coincide con la aridad, por lo tanto no se satisface la aridad del funcional o relacional en cuestión.")
                return False #Falso si no se cumple con la aridad
    else:
        print("Lo que se encuentra entre paréntesis es o bien vacío o hay una cantidad par de estos elementos.")
        return False #Si tiene una cantidad par de elementos o la lista tiene 0 elementos regresa 0

def verificacionQueListaEsLFormulaAtomica(lista, aridades):
    print(lista)
    j = 0
    k = 0
    contadorAridades = []
    if(len(lista)>0):
        if(relacionalTermino(lista[0]) and lista[-1]==5):
            k = k + 1
            if(lista[k]==3):
                for elemento in aridades:
                    if(elemento[1]==int((lista[k-1]-29)/8) and elemento[0]==1):
                        contadorAridades.append(elemento[2])
                        break
                k = k + 1
            else:
                print("No hay un paréntesis derecho después del número:", lista[k-1] , "cuyo relacional es de número:", int((lista[k-1]-29)/8))
                return False
            if(k<=len(lista)-2):  #Tiene que haber al menos otros dos excluye los casos en los que unicamente hay 2 o 3 elementos en la lista
                while True:
                    if(funcionalTermino(lista[k])):
                        k = k + 1
                        if(lista[k]==3):
                            for elemento in aridades:
                                if(elemento[1]==int((lista[k-1]-27)/8) and elemento[0]==0):
                                    contadorAridades.append(elemento[2])
                                    break
                            k = k + 1
                        else:
                            print("No hay un paréntesis derecho después del número: ", int((lista[k-1]-27)/8), " cuyo funcional es de número: ", lista[k-1])
                            return False
                    elif(lista[k]==5):
                        copia = copiarArregloAPartirDeIndiceDado(lista,k)
                        print("Contador aridades", contadorAridades)
                        print("Lista", lista)
                        print("Copia", copia)
                        if(verificarArregloEsTermino(copia, contadorAridades[-1])):
                            lista[k] = -1
                            while(lista[k]!=3):
                                k = k - 1
                            lista[k] = -2
                            k = k - 1
                            lista[k] = -1
                            del contadorAridades[-1]
                            print("Lista después del borrado: ", lista)
                            print("Contador aridades", contadorAridades)
                        else:
                            print("Fallo la verificación de un término.")
                            return False
                    elif(lista[k]==-1 and lista[k+1]==-2):
                        while True:
                            k = k + 1 
                            if(lista[k]==-1 and lista[k+1]==-2):
                                j = j + 1
                            elif(lista[k]==-1 and lista[k+1]!=-2 and j>0):
                                j = j - 1
                            if(lista[k]==-1 and lista[k+1]!=-2 and j==0):
                                break
                        k = k + 1    
                    else:
                        k = k + 1
                    if(contadorAridades==[] and lista[-1]==-1):
                        return True
                    elif(contadorAridades!=[] and k>=len(lista)-1 and lista[-1]!=5): #Si no se cancela el contadorAridades inicial y ya nos encontramos en el último elemento o mayor y el último no es un paréntesis derecho y ya se termino la lista entonces regresar false
                        print("Fallo que el último símbolo no fuera paréntesis derecho y todos los contadorAridades se cancelaran en ese último.")
                        return False
                    elif(contadorAridades==[] and lista[-1]!=-1):
                        print("Fallo ya que aunque contadorAridades es vacío aún quedan elementos en la lista que son parétesis derechos.")
                        return False
            else:
                print("No hay espacio suficiente para una fórmula de verdad.")
                return False
        else:
            print("El primer símbolo no es relacional o bien el último símbolo no es un paréntesis derecho.")
            return False
    else: 
        print("La lista inicial es vacía.")
        return False 
    
lista = RecibirLista()  
aridades = obtenerAridadesTerminosYUnaRelacion(lista) 
if(verificacionSimbolosAdecuados):
    print(verificacionQueListaEsLFormulaAtomica(lista, aridades))
else:
    print("No son los símbolos que corresponden. Deben ser impares mayores o iguales a 3.")
    print(False)
    
    
    
    
    
    
    
    
    
    
    
    
