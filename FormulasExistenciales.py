# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 13:14:44 2019

@author: fernando
"""

def RecibirLista():
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
        if(i%2==0 or i<3):
            return False
    return True    

def obtenerAridadesTerminos(lista):
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
                aridades.append([int((i-27)/8),j])
    return aridades    

def obtenerAridadesTerminosYUnaRelacion(lista):
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
                j = int(input("Introduzca la aridad de la relación %d: " %((i-29)/8)))
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
    
#Verificar posibles impresiciones con este algoitmo
def copiarArregloAPartirDeIndiceDado(lista, posicion: int): #Esta función copia lo que se encuentra entre paréntesis a partir de una posición dada en un arreglo dado (la posición supondremos que se trata de la posición del paréntesis más a la derecha)
     copia = [] #Inicia una lista vacía
     j = 0
     k = 0 #Contador que se mueve entre paréntesis y que respecto a éste indice se añaden elementos significativos a la copia
     while(lista[posicion]!=3): #Se va a idenificar el primer paréntesis
         posicion  = posicion - 1
         
     posicion = posicion + 1 #Se coloca adelante de dicho paréntesis
     while(lista[posicion]!=5): 
         if(lista[posicion]==-1 and lista[posicion+1]==-2):
             while True:
                 posicion = posicion + 1
                 if(lista[posicion]==-1 and lista[posicion+1]!=-2 and j==0):
                     break
                 elif(lista[posicion]==-1 and lista[posicion+1]==-2):
                     j = j + 1
                 elif(lista[posicion]==-1 and lista[posicion+1]!=-2 and j>0):
                     j = j - 1
         copia.insert(k,lista[posicion])  #Si encuentra un -1 (asterisco) lo copia ya que es un elemento que está reconocido como término). En otro caso si se trata de cualquier otro símbolo lo copia
         k = k + 1 #Se mueve una posición a la derecha sobre la lista "copia" y busca más elementos significativos
         posicion = posicion + 1
     return copia # Regresa la todo los que se encuentra entre dos paaréntesis de la lista original

def verificarArregloEsTermino(lista, aridad: int): #Esta función verifica que todo lo que se encuentra  entre dos paréntesis corresponde en efecto a un término
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
                print("No hay un paréntesis derecho después del número:", lista[k-1] , "cuyo relacional es de número:", int((lista[k-1]-25)/8))
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
    
def verificacionListaEstructuraFormula(lista):
    if(len(lista)==1 or len(lista)==2 or len(lista)==3):
        if(len(lista)==1 and (lista[0]==-3) or (lista[0]==-1)):
            return True
        if(len(lista)==2):
            if((lista[0]==9 and lista[1]==-3) or (lista[0]==9 and lista[1]==-1)):
                return True
            else:
                print("No es la negación de una fórmula bien formada.")
                return False
        else:
            if((lista[0]==-3 and lista[1]==11 and lista[2]==-3) or (lista[0]==-3 and lista[1]==11 and lista[2]==-1) or 
            (lista[0]==-1 and lista[1]==11 and lista[2]==-3) or (lista[0]==-1 and lista[1]==11 and lista[2]==-1) or
            
            (lista[0]==-3 and lista[1]==13 and lista[2]==-3) or (lista[0]==-3 and lista[1]==13 and lista[2]==-1) or 
            (lista[0]==-1 and lista[1]==13 and lista[2]==-3) or (lista[0]==-1 and lista[1]==13 and lista[2]==-1) or
            
            (lista[0]==-3 and lista[1]==15 and lista[2]==-3) or (lista[0]==-3 and lista[1]==15 and lista[2]==-1) or 
            (lista[0]==-1 and lista[1]==15 and lista[2]==-3) or (lista[0]==-1 and lista[1]==15 and lista[2]==-1) or
            
            (lista[0]==-3 and lista[1]==17 and lista[2]==-3) or (lista[0]==-3 and lista[1]==17 and lista[2]==-1) or 
            (lista[0]==-1 and lista[1]==17 and lista[2]==-3) or (lista[0]==-1 and lista[1]==17 and lista[2]==-1)):
                return True
            else:
                print("No respeta la construcción por conectivos de fórmula bien formada.")
                return False
    else:
        print("La lista inicial es vacía.")
        return False
 

def verificacionQueListaEsFormulaSinCuantificar(lista, aridades):
    k = 0
    j = 0
    contadorParentesis = 0
    listaComprobacionFormulaAtomica = []
    listaComprobacionFormulaAbreviada = []
    listaComprobacionEstructura = []
    if(len(lista)>=4 and lista[-1]==5):
        while(k<=len(lista)-1): #Primer paso de simplificación y copiado
            contadorParentesis = 0
            listaComprobacionFormulaAtomica = []
            if(relacionalTermino(lista[k])):
                j = k
                j = j + 1 
                if(lista[j]==3):
                    contadorParentesis = contadorParentesis + 1
                    j = j + 1
                else:
                    return False
                if(j<len(lista)-1): #No es posible que siga un paréntesis derecho inmediato a uno izquierdo
                    listaComprobacionFormulaAtomica.append(lista[j-2])
                    listaComprobacionFormulaAtomica.append(lista[j-1])
                    while(contadorParentesis!=0 and j<=len(lista)-1):
                        if(j<len(lista)-1):
                            listaComprobacionFormulaAtomica.append(lista[j])
                            if((funcionalTermino(lista[j]) or relacionalTermino(lista[j])) and lista[j+1]==3):
                                contadorParentesis = contadorParentesis + 1
                            elif(lista[j] == 5 and contadorParentesis==1):
                                contadorParentesis = contadorParentesis - 1
                                break
                            elif(lista[j] == 5 and contadorParentesis>1):
                                contadorParentesis = contadorParentesis - 1
                        elif(j==len(lista)-1):
                            contadorParentesis = contadorParentesis - 1
                            listaComprobacionFormulaAtomica.append(lista[j])
                            break
                        j = j + 1
                    print("ListaComproFormAtomica: ", listaComprobacionFormulaAtomica)
                    if(verificacionQueListaEsLFormulaAtomica(listaComprobacionFormulaAtomica, aridades)):
                        print("ListaComproFormAtomica: ", listaComprobacionFormulaAtomica)
                        lista[k] = -3
                        k = j
                        lista[k] = -3
                        print("Lista: ", lista)
                        listaComprobacionFormulaAbreviada.append(-3)
                        k = k + 1
                        print("ListaComproFormAbre: ", listaComprobacionFormulaAbreviada)
                    else:
                        return False 
                else:
                    return False
            else:
                listaComprobacionFormulaAbreviada.append(lista[k])
                k = k + 1
        contadorParentesis = 0
        k = 0
        contadorSalto = 0
        checador = True
        for elemento in listaComprobacionFormulaAbreviada:
            if((elemento%2==1 and elemento>=19) or elemento==7):
                checador = False
                break
        if(len(listaComprobacionFormulaAbreviada)>=1 and checador):
            if(len(listaComprobacionFormulaAbreviada)==1 and listaComprobacionFormulaAbreviada[0]==-3):
                return True
            elif(listaComprobacionFormulaAbreviada[0]==3 and listaComprobacionFormulaAbreviada[-1]==5):
                while True:
                    print("Este paso ocurre")
                    print(contadorParentesis)
                    print(listaComprobacionFormulaAbreviada)
                    contadorSalto = 0
                    listaComprobacionEstructura = []
                    if(listaComprobacionFormulaAbreviada[k]==3):
                        contadorParentesis = contadorParentesis + 1
                        k = k + 1
                    elif(listaComprobacionFormulaAbreviada[k]==5):
                        while True:
                            k = k - 1
                            if(listaComprobacionFormulaAbreviada[k]==3):
                                break
                        listaComprobacionFormulaAbreviada[k] = -1
                        k = k + 1
                        while(listaComprobacionFormulaAbreviada[k]!=5):
                            if(listaComprobacionFormulaAbreviada[k]==-1):
                                contadorSalto = contadorSalto + 1
                                k = k + 1
                                while(contadorSalto!=0):
                                    if(k>len(listaComprobacionFormulaAbreviada)-1 and contadorSalto>0):
                                        print("Hubo un error.")
                                        return False
                                    elif(listaComprobacionFormulaAbreviada[k]==-1):
                                        contadorSalto = contadorSalto + 1
                                    elif(listaComprobacionFormulaAbreviada[k]==-4):
                                        contadorSalto = contadorSalto - 1
                                    k = k + 1
                                listaComprobacionEstructura.append(-1)
                            else: 
                                listaComprobacionEstructura.append(listaComprobacionFormulaAbreviada[k])
                                k = k + 1
                            print("ListaComproEstruct: ", listaComprobacionEstructura)
                        if(verificacionListaEstructuraFormula(listaComprobacionEstructura)):
                            listaComprobacionFormulaAbreviada[k] = -4
                            k = k + 1
                            contadorParentesis = contadorParentesis - 1
                        else:
                            print("No es fórmula bien formada.")
                            return False
                    else:
                        k = k + 1
                    if(contadorParentesis==0 and listaComprobacionFormulaAbreviada[-1]==-4):
                        return True
                    elif(contadorParentesis!=0 and k>=len(listaComprobacionFormulaAbreviada)-1 and listaComprobacionFormulaAbreviada[k]!=5):
                        print("No se pudieron cancelar todos los paréntesis.")
                        return False
                    elif(contadorParentesis==0 and listaComprobacionFormulaAbreviada[-1]==5):
                        print("Aún existen paréntesis derechos.")
                        return False
            else:
                print("No se trata de una fórmula bien formada ya que faltan paréntesis exteriores.")
                return False
        else:
            print("Lo copiado es nulo o bien hay términos, variables o funcionales que se colaron y sólo debe haber los símbolos 3, 5, -3 y los conectivos.")
            return False
    else:  
        print("No hay suficientes elementos para ser una fórmula ")
        return False
    
def verificacionQueListaEsFormulaExistencial(lista,aridades):
    k = 0
    j = 0 
    contadorParentesis = 0
    contadorSalto = 0
    copiaAuxFormulaSinCuantificar =  []
    listaComprobacionFormulaTotal = []
    listaComprobacionFormulaTotalFinal = []
    if(len(lista)>=10 and lista[0]==3 and lista[-1]==5): #Simplificación de fórmulas y posteriormente simplificación de existenciales y finalmente verificación de toda la fórmula
        print(lista)
        while(k<=len(lista)-1):
            contadorParentesis = 0
            copiaAuxFormulaSinCuantificar = []
            if(lista[k]==21 and k<=len(lista)-9): #La menor cantidad de elementos que puede haber después de un existencial
                listaComprobacionFormulaTotal.append(lista[k])
                k = k + 1
                if(variableTermino(lista[k]) and lista[k+1]==3):
                    listaComprobacionFormulaTotal.append(lista[k])
                    listaComprobacionFormulaTotal.append(lista[k+1])
                    k = k + 2
                    while(k<=len(lista)-1):
                        if(lista[k]==21 and k<=len(lista)-9):
                            listaComprobacionFormulaTotal.append(lista[k])
                            k = k + 1
                            if(variableTermino(lista[k]) and lista[k+1]==3):
                                listaComprobacionFormulaTotal.append(lista[k])
                                listaComprobacionFormulaTotal.append(lista[k+1])
                                k = k + 2
                            else:
                                print("Posterior a un existencial no sigue o bien una variable o bien un paréntesis izquierdo después de esta variable, fijarse en posición ", k)
                                return False
                        elif(lista[k] == 3 or relacionalTermino(lista[k])):
                            j = k
                            contadorParentesis = contadorParentesis + 1
                            while(j<=len(lista)-1):
                                if(lista[j]==3):
                                    contadorParentesis = contadorParentesis + 1
                                elif(lista[j] == 5 and contadorParentesis>1 and j<len(lista)-1):
                                    contadorParentesis = contadorParentesis - 1
                                elif(contadorParentesis==1 and lista[j]==5):
                                    contadorParentesis = contadorParentesis - 1
                                    break
                                elif(j==len(lista)-1 and contadorParentesis>1):
                                    print("Hubo un error")
                                    return False
                                j = j + 1
                            j = j - 1 
                            while(k<=j):
                                copiaAuxFormulaSinCuantificar.append(lista[k])
                                k = k + 1
                            k = k - 1
                            if(verificacionQueListaEsFormulaSinCuantificar(copiaAuxFormulaSinCuantificar,aridades)):
                                listaComprobacionFormulaTotal.append(-1)
                                k = k + 1
                                break
                            else:
                                print("Existe algo que no es una fórmula bien formada fijarse en la locación ", k)
                                return False
                        else:
                            print("En la parte de los existenciales está mal construido, fijarse en la posición ", k)
                            return False
                else:
                    print("Posterior a un existencial no sigue o bien una variable o bien un paréntesis izquierdo después de esta variable, fijarse en posición ", k)
                    return False
            else:
                listaComprobacionFormulaTotal.append(lista[k])
                k = k + 1
        k = 0
        contadorParentesis = 0
        checador = True
        print("listaComprobacionFormulaTotal: ", listaComprobacionFormulaTotal)
        for elemento in listaComprobacionFormulaTotal:
            if((elemento%2==1 and (elemento==19 or ((elemento-23)%8!=0 and elemento>=23) or elemento==7)) or listaComprobacionFormulaTotal[0]!=3 or listaComprobacionFormulaTotal[-1]!=5):
                print("Algo anda mal con la listaComproFormTotal ", listaComprobacionFormulaTotal)
                print(elemento)
                return False
        if(len(listaComprobacionFormulaTotal)>=7):
            while(k<=len(listaComprobacionFormulaTotal)-1):
                contadorParentesis = 0
                checador = True
                if(listaComprobacionFormulaTotal[k]==3):
                    k = k + 1
                    if(listaComprobacionFormulaTotal[k]==21):
                        contadorParentesis = contadorParentesis + 1
                        k = k + 2
                        while(k<=len(listaComprobacionFormulaTotal)-1 and checador):
                            if(listaComprobacionFormulaTotal[k]==3):
                                contadorParentesis = contadorParentesis + 1
                                k = k + 1
                            elif(listaComprobacionFormulaTotal[k]==-1):
                                k = k + 1
                                while(k<=len(listaComprobacionFormulaTotal)-1):
                                    if(listaComprobacionFormulaTotal[k]==5 and contadorParentesis==1):
                                        contadorParentesis = contadorParentesis - 1
                                        checador = False
                                        listaComprobacionFormulaTotalFinal.append(-3)
                                        k = k + 1
                                        break
                                    elif(listaComprobacionFormulaTotal[k]==5 and contadorParentesis>1 and k<len(listaComprobacionFormulaTotal)-1):
                                        contadorParentesis = contadorParentesis - 1
                                        k = k + 1
                                    elif(listaComprobacionFormulaTotal[k]==5 and contadorParentesis>1 and k==len(listaComprobacionFormulaTotal)-1):
                                        print("Algo falló. Faltan paréntesis derechos.")
                                        return False
                                    elif(listaComprobacionFormulaTotal[k]!=5):
                                        print("Se está colando algo que no es paréntesis derecho en la posición ", k)
                                        return False
                            else:
                                k = k + 1
                    else:
                        listaComprobacionFormulaTotalFinal.append(3)
                else:
                    listaComprobacionFormulaTotalFinal.append(listaComprobacionFormulaTotal[k])
                    k = k + 1
        else:
            print("No hay suficientes elementos para una fórmula.")
            return False
        print("ListaTotalFinal: ", listaComprobacionFormulaTotalFinal)
        for elemento in listaComprobacionFormulaTotalFinal:
            if(elemento%2==1 and (elemento == 19 or elemento>=23 or elemento == 7)):
                print("Hay términos, variables o funcionales que se colaron y sólo debe haber los símbolos 3, 5, -3 y los conectivos.")
                return False
        k = 0
        contadorParentesis = 0
        if(len(listaComprobacionFormulaTotalFinal)>=1):
            if(len(listaComprobacionFormulaTotalFinal)==1 and listaComprobacionFormulaTotalFinal[0]==-3):
                return True
            elif(listaComprobacionFormulaTotalFinal[0]==3 and listaComprobacionFormulaTotalFinal[-1]==5):
                while True:
                    print("Este paso ocurre")
                    print(contadorParentesis)
                    print(listaComprobacionFormulaTotalFinal)
                    contadorSalto = 0
                    listaComprobacionEstructura = []
                    if(listaComprobacionFormulaTotalFinal[k]==3):
                        contadorParentesis = contadorParentesis + 1
                        k = k + 1
                    elif(listaComprobacionFormulaTotalFinal[k]==5):
                        while True:
                            k = k - 1
                            if(listaComprobacionFormulaTotalFinal[k]==3):
                                break
                        listaComprobacionFormulaTotalFinal[k] = -1
                        k = k + 1
                        while(listaComprobacionFormulaTotalFinal[k]!=5):
                            if(listaComprobacionFormulaTotalFinal[k]==-1):
                                contadorSalto = contadorSalto + 1
                                k = k + 1
                                while(contadorSalto!=0):
                                    if(k>len(listaComprobacionFormulaTotalFinal)-1 and contadorSalto>0):
                                        print("Hubo un error.")
                                        return False
                                    elif(listaComprobacionFormulaTotalFinal[k]==-1):
                                        contadorSalto = contadorSalto + 1
                                    elif(listaComprobacionFormulaTotalFinal[k]==-4):
                                        contadorSalto = contadorSalto - 1
                                    k = k + 1
                                listaComprobacionEstructura.append(-1)
                            else: 
                                listaComprobacionEstructura.append(listaComprobacionFormulaTotalFinal[k])
                                k = k + 1
                            print("ListaComproEstruct: ", listaComprobacionEstructura)
                        if(verificacionListaEstructuraFormula(listaComprobacionEstructura)):
                            listaComprobacionFormulaTotalFinal[k] = -4
                            k = k + 1
                            contadorParentesis = contadorParentesis - 1
                        else:
                            print("No es fórmula bien formada.")
                            return False
                    else:
                        k = k + 1
                    if(contadorParentesis==0 and listaComprobacionFormulaTotalFinal[-1]==-4):
                        return True
                    elif(contadorParentesis!=0 and k>=len(listaComprobacionFormulaTotalFinal)-1 and listaComprobacionFormulaTotalFinal[k]!=5):
                        print("No se pudieron cancelar todos los paréntesis.")
                        return False
                    elif(contadorParentesis==0 and listaComprobacionFormulaTotalFinal[-1]==5):
                        print("Aún existen paréntesis derechos.")
                        return False
            else:
                print("No se trata de una fórmula bien formada ya que faltan paréntesis exteriores.")
                return False
        else:
            print("Lo copiado es nulo.")
            return False
    else:
        print("O bien faltan elementos para una fórmula existencial o bien el primer o último símbolo no corresponde con un paréntesis izquierdo/derecho respectivamente.")
        return False

lista = RecibirLista()
aridades = obtenerAridadesTerminosYUnaRelacion(lista)
if(verificacionSimbolosAdecuados(lista)):
    print(verificacionQueListaEsFormulaExistencial(lista,aridades))
else:
    print("Los números deben ser impares mayores o iguales a 3.")
    


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    