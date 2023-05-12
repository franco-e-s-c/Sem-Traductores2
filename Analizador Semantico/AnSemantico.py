from tabulate import tabulate
from anytree import Node, RenderTree, PreOrderIter

data = []
data2 = []
pila = list()
pilaNodo = list()
pilaS = ""
lexList = list()
sinList = list()
fila = 0
columna = 0
accion = 0
elim = 6
archivo = open('compilador.lr','r')
lines = archivo.readlines()
reglas = list()
reg = 0
num = 0
tlr1 = list()
flagR = 0
objetoL = list()
root = Node("Arbol")
root2 = Node("Lex")
globals()['VarFlag']=0
globals()['ambito']=''
globals()['CallFlag']=0
globals()['tiporetorno'] =""
globals()['printV']=''
globals()['PrintFlag']=0
globals()['callFunc']=0

class Regla:
    def __init__(self, num, num2, elem, fuente):
        self.num = num
        self.num2 = num2
        self.elem = elem
        self.fuente = fuente

class ElementoPila:
    def __init__(self, fuente):
        self.fuente = fuente

class Terminal(ElementoPila):
    def __init__(self, fuente, tipo):
        super().__init__(fuente)
        self.tipo = tipo

class NoTerminal(ElementoPila):
    def __init__(self, fuente):
        super().__init__(fuente)

class Estado(ElementoPila):
    def __init__(self, fuente):
        super().__init__(fuente)

class Programa:
    def __init__(self, definiciones, nodo):
        self.definiciones =  definiciones
        self.fuente = 'Programa'
        self.nodo = nodo
class Variables:
    def __init__(self, cad, contexto):
        self.cad = cad
        self.contexto = contexto
    def __repr__(self):
        aux = ("Variable: "+str(self.cad)+" contexto: "+str(self.context))
        return aux
class Definiciones3:
    def __init__(self, definicion, definiciones, nodo):
        self.definicion = definicion
        self.definiciones =  definiciones
        self.fuente = 'Definiciones'
        self.nodo = nodo

class Definicion:
    def __init__(self, defi, nodo):
        self.defi = defi
        self.fuente = 'Definicion'
        self.nodo = nodo

class DefVar:
    def __init__(self, tipo, identificador, listaVar, puntoyComa, nodo):
        self.tipo = tipo
        self.identificador =  identificador
        self.listaVar = listaVar
        self.puntoyComa = puntoyComa
        self.fuente = 'DefVar'
        self.nodo = nodo

class ListaVar8:
    def __init__(self, identificador, listaVar, nodo):
        self.identificador = identificador
        self.listaVar =  listaVar
        self.fuente = 'ListaVar'
        self.nodo = nodo

class DefFunc:
    def __init__(self, tipo, identificador, parA, parametros, parC, bloqFunc, nodo):
        self.tipo = tipo
        self.identificador = identificador
        self.parA = parA
        self.parametros = parametros
        self.parC = parC
        self.bloqFunc = bloqFunc
        self.fuente = 'DefFunc'
        self.nodo = nodo

class Parametros:
    def __init__(self, tipo, identificador, listaParam, nodo):
        self.tipo = tipo
        self.identificador =  identificador
        self.listaParam = listaParam
        self.fuente = 'Parametros'
        self.nodo = nodo

class ParametrosCon:
    def __init__(self, tipo, identificador, contexto, nodo):
        self.tipo = tipo
        self.identificador =  identificador
        self.contexto = contexto
        self.fuente = 'Parametros'
        self.nodo = nodo


class ListaParam:
    def __init__(self, tipo, identificador, listaParam, nodo):
        self.tipo = tipo
        self.identificador =  identificador
        self.listaParam = listaParam
        self.fuente = 'ListaParam'
        self.nodo = nodo

class BloqFunc:
    def __init__(self, parA, defLocales, parC, nodo):
        self.parA = parA
        self.defLocales =  defLocales
        self.parC = parC
        self.fuente = 'BloqFunc'
        self.nodo = nodo

class DefLocales16:
    def __init__(self, defLocal, defLoclales, nodo):
        self.defLocal = defLocal
        self.defLocales = defLoclales
        self.fuente = 'DefLocales'
        self.nodo = nodo

class DefLocal:
    def __init__(self, defSent, nodo):
        self.defSent = defSent
        self.fuente = 'DefLocal'
        self.nodo = nodo

class Sentencias20:
    def __init__(self, sentencia, sentencias, nodo):
        self.sentencia = sentencia
        self.sentencias = sentencias
        self.fuente = 'Sentencias'
        self.nodo = nodo


class Sentencia21:
    def __init__(self, identificador, op, expresion, puntoyComa, nodo):
        self.identificador = identificador
        self.op = op
        self.expresion = expresion
        self.puntoyComa = puntoyComa
        self.fuente = 'Sentencia'
        self.nodo = nodo
        self.listateraux = list()

class Sentencia22:
    def __init__(self, ifV, parA, expresion, parC, sentenciaB, otro, nodo):
        self.ifV = ifV
        self.parA = parA
        self.expresion = expresion
        self.parC = parC
        self.sentenciaB = sentenciaB
        self.otro = otro
        self.fuente = 'Sentencia'
        self.nodo = nodo

class Sentencia23:
    def __init__(self, whileV, parA, expresion, parC, bloque, nodo):
        self.whileV = whileV
        self.parA = parA
        self.expresion = expresion
        self.parC = parC
        self.bloque = bloque
        self.fuente = 'Sentencia'
        self.nodo = nodo

class Sentencia24:
    def __init__(self, returnV, valorR, puntoyComa, nodo):
        self.returnV = returnV
        self.valorR = valorR
        self.puntoyComa = puntoyComa
        self.fuente = 'Sentencia'
        self.nodo = nodo

class Sentencia25:
    def __init__(self, llamadaF, puntoyComa, nodo):
        self.llamadaF = llamadaF
        self.puntoyComa = puntoyComa
        self.fuente = 'Sentencia'
        self.nodo = nodo

class Otro27:
    def __init__(self, elseV, sentenciaB, nodo):
        self.elseV = elseV
        self.sentenciaB = sentenciaB
        self.fuente = 'Otro'
        self.nodo = nodo

class Bloque:
    def __init__(self, parA, sentencias, parC, nodo):
        self.parA = parA
        self.sentencias = sentencias
        self.parC = parC
        self.fuente = 'Bloque'
        self.nodo = nodo

class ValorRegresa:
    def __init__(self, expresion, nodo):
        self.expresion = expresion
        self.fuente = 'Valor Regresa'
        self.nodo = nodo

class Argumentos:
    def __init__(self, expresion, listaA, nodo):
        self.expresion = expresion
        self.listaA = listaA
        self.fuente = 'Argumentos'
        self.nodo = nodo

class ListaArgumentos:
    def __init__(self, comaV, expresion, listaA, nodo):
        self.comaV = comaV
        self.expresion = expresion
        self.listaA = listaA
        self.fuente = 'Lista Argumentos'
        self.nodo = nodo

class Termino35:
    def __init__(self, llamadaFunc, nodo):
        self.llamadaFunc = llamadaFunc
        self.fuente = 'Termino'
        self.nodo = nodo

class Termino:
    def __init__(self, dato, nodo):
        self.dato = dato
        self.fuente = 'Termino'
        self.nodo = nodo

class LlamadaFunc:
    def __init__(self, identificador, parA, argumentos, parC, nodo):
        self.identificador = identificador
        self.parA = parA
        self.argumentos = argumentos
        self.parC = parC
        self.fuente = 'Llamada Funcion'
        self.nodo = nodo

class SentenciaBloque:
    def __init__(self, senBlo, nodo):
        self.senBlo = senBlo
        self.fuente = 'Sentencia Bloque'
        self.nodo = nodo


class Expresion43:
    def __init__(self, parenA, expresion, parenC, nodo):
        self.parenA = parenA
        self.expresion = expresion
        self.parenC = parenC
        self.fuente = 'Expresion'
        self.nodo = nodo

class Expresion44:
    def __init__(self, op, expresion, nodo):
        self.op = op
        self.expresion = expresion
        self.fuente = 'Expresion'
        self.nodo = nodo

class Expresion46:
    def __init__(self, expresion1, op, expresion2, nodo):
        self.expresion1 = expresion1
        self.op = op
        self.expresion2 = expresion2
        self.fuente = 'Expresion'
        self.nodo = nodo

class Expresion52:
    def __init__(self, termino, nodo):
        self.termino = termino
        self.fuente = 'Expresion'
        self.nodo = nodo

class NoElim:
    def __init__(self, nume, fuente, nodo):
        self.nume = nume
        self.fuente = fuente
        self.nodo = nodo

for line in lines:
    line = line.rstrip()
    line = line.split("\t")
    if (reg == 1):
        tlr1.append(line)
        for i in range(len(tlr1)):
            for j in range(len(tlr1[i])):
                tlr1[i][j] = int(tlr1[i][j])
    if (line[0]=='52'):
        continue
    if (line[0]=='95'):
        reg = 1
    if (reg == 0):
        num += 1
        obj = Regla(num, int(line[0]), int(line[1]), line[2])
        reglas.append(obj)
pila.append(Terminal("$", 100))
pila.append(Estado(0))
class Lexico:
    def __init__(self, cadena):
        self.cadena = cadena + '$'
        self.edo = -1

    def check(self, cad):
        reservadas = ["if","while", "return", "else"]
        tipoR = ["19","20", "21", "22"]
        if (cad in reservadas):
            it = 0
            for it in range(0, len(reservadas)):
                if cad == reservadas[it]:
                    tipoS = tipoR[it]
                    obj = Terminal(cad, int(tipoS))
                    lexList.append(obj)
                    it= it+1 
                    cad = ""
        else:
            obj = Terminal(cad, 0)
            lexList.append(obj)
            cad = ""
            

    def analizar(self):
        cad = ""
        identificador = ""
        numero = ""
        real = ""
        entero = ""
        cadenaS = ""
        i=0
        n=0
        skip = False
        tipo = ["int", "void", "float"]
        simbolos = [";", ",", "(", ")", "{", "}", "$"]
        tipoA = ["12", "13", "14", "15", "16", "17", "23"]
        relac = ""
        orV = ""
        reservadas = ["if","while", "return", "else"]
        tipoR = ["19", "20", "21", "22"]
        for caracter in self.cadena:
            asCarac = ord(caracter)
            if (caracter == '$'):
                obj = Terminal(caracter, 23)
                lexList.append(obj)
                break

            elif(skip==True):
                if(n != cont-1):
                    n=n+1
                    continue
                else:
                    skip=False
            elif (asCarac > 64 and asCarac < 91) or (asCarac>96 and asCarac<123): #Comprobamos si el caracter es una letra
                if(len(real)!=0):
                    obj = Terminal(real, 2)
                    lexList.append(obj)
                    print("Real Tipo 2: ", real)
                    real=""
                    identificador=""
                    numero=""
                    identificador += caracter
                elif(len(numero)!=0):
                    obj = Terminal(numero, 1)
                    lexList.append(obj)
                    print("Entero Tipo 1: ", numero)
                    real=""
                    identificador=""
                    numero=""
                    identificador += caracter
                elif(len(cadenaS)!=0):
                    obj = Terminal(cadenaS, 3)
                    lexList.append(obj)
                    print("Cadena Tipo 3: ", cadenaS)
                    real=""
                    identificador=""
                    numero=""
                    cadenaS=""
                    identificador += caracter
                else:
                    identificador += caracter

            elif (asCarac > 47 and asCarac < 58):
                if(len(identificador)!=0):
                    identificador += caracter
                    if(identificador in tipo):
                        obj = Terminal(identificador, 4)
                        lexList.append(obj)
                        print("TipoDato Tipo 4: ", identificador)
                        identificador=""

                    elif (identificador in reservadas):
                        it = 0
                        for it in range(0, len(reservadas)):
                            if identificador == reservadas[it]:
                                tipoS = tipoR[it]
                            it= it+1 
                        obj = Terminal(identificador, int(tipoS))
                        lexList.append(obj)
                        print("Reservada Tipo "+ tipoS + ":", identificador)
                        identificador=""
                elif(len(cadenaS)!=0):
                    obj = Terminal(cadenaS, 2)
                    lexList.append(obj)
                    print("Cadena Tipo 3: ", cadenaS)
                    real=""
                    identificador=""
                    numero=""
                    cadenaS=""
                    identificador += caracter
                else:
                    #entero +=caracter
                    numero += caracter
                    if(len(real)!=0):
                        real+=caracter
                       
            elif (caracter == "."):
                if(len(real)==0):
                    real += numero + caracter
                else:
                    print("ERROR")
            
            elif (caracter == " "):
                if(len(identificador)!=0):
                    if(identificador in tipo):
                        obj = Terminal(identificador, 4)
                        lexList.append(obj)
                        print("TipoDato Tipo 4: ", identificador)
                        identificador=""

                    elif (identificador in reservadas):
                        it = 0
                        for it in range(0, len(reservadas)):
                            if identificador == reservadas[it]:
                                tipoS = tipoR[it]
                            it= it+1 
                        obj = Terminal(identificador, int(tipoS))
                        lexList.append(obj)
                        print("Reservada Tipo "+ tipoS + ":", identificador)
                        identificador=""
                    else:
                        obj = Terminal(identificador, 0)
                        lexList.append(obj)
                        print("Identificador Tipo 0: ", identificador)
                        real=""
                        identificador=""
                        numero=""
                elif(len(real)!=0):
                    obj = Terminal(real, 2)
                    lexList.append(obj)
                    print("Real Tipo 2: ", real)
                    real=""
                    identificador=""
                    numero=""
                elif(len(numero)!=0):
                    obj = Terminal(entero, 1)
                    lexList.append(obj)
                    print("Entero Tipo 1: ", numero)
                    real=""
                    identificador=""
                    numero=""
                elif(len(cadenaS)!=0):
                    obj = Terminal(cadenaS, 3)
                    lexList.append(obj)
                    print("Cadena Tipo 3: ", cadenaS)
                    real=""
                    identificador=""
                    numero=""
                    cadenaS=""
                    
            
            elif (caracter =="'") or (caracter == '"'):
                c=i+1
                cont = 0
                if(len(identificador)!=0):
                    if(identificador in tipo):
                        obj = Terminal(identificador, 4)
                        lexList.append(obj)
                        print("TipoDato Tipo 4: ", identificador)
                        identificador=""

                    elif (identificador in reservadas):
                        it = 0
                        for it in range(0, len(reservadas)):
                            if identificador == reservadas[it]:
                                tipoS = tipoR[it]
                            it= it+1 
                        obj = Terminal(identificador, int(tipoS))
                        lexList.append(obj)
                        print("Reservada Tipo "+ tipoS + ":", identificador)
                        identificador=""
                    else:
                        obj = Terminal(identificador, 0)
                        lexList.append(obj)
                        print("Identificador Tipo 0: ", identificador)
                        real=""
                        identificador=""
                        numero=""
                elif(len(real)!=0):
                    obj = Terminal(real, 2)
                    lexList.append(obj)
                    print("Real Tipo 2: ", real)
                    real=""
                    identificador=""
                    numero=""
                elif(len(numero)!=0):
                    obj = Terminal(numero, 1)
                    lexList.append(obj)
                    print("Entero Tipo 1: ", numero)
                    real=""
                    identificador=""
                    numero=""
                
                for cadenaCar in range(c, len(self.cadena)):
                    cont=cont+1
                    if (self.cadena[cadenaCar] == '$'):
                        print("ERROR CADENA NO CIERRA")
                        obj = Terminal('$', 23)
                        lexList.append(obj)
                        skip = True
                        break
                    elif (self.cadena[cadenaCar]=="'") or (self.cadena[cadenaCar]=='"'):
                        skip = True
                        obj = Terminal(cadenaS, 3)
                        lexList.append(obj)
                        print("Cadena Tipo 3: ", cadenaS)
                        real=""
                        identificador=""
                        numero=""
                        cadenaS=""
                        break
                    cadenaS=cadenaS + self.cadena[cadenaCar]

            elif (caracter == '+') or (caracter == '-'):
                if(len(real)!=0):
                    obj = Terminal(real, 2)
                    lexList.append(obj)
                    print("Real Tipo 2: ", real)
                    real=""
                    identificador=""
                    numero=""
                    obj = Terminal(caracter, 5)
                    #obj = Terminal(caracter, 1)
                    lexList.append(obj)
                    print("opSuma Tipo 5: ", caracter)
                elif(len(numero)!=0):
                    obj = Terminal(numero, 1)
                    lexList.append(obj)
                    print("Entero Tipo 1: ", numero)
                    real=""
                    identificador=""
                    numero=""
                    obj = Terminal(caracter, 5)
                    #obj = Terminal(caracter, 1)
                    lexList.append(obj)
                    print("opSuma Tipo 5: ", caracter)
                elif(len(identificador)!=0):
                    if(identificador in tipo):
                        obj = Terminal(identificador, 4)
                        lexList.append(obj)
                        print("TipoDato Tipo 4: ", identificador)
                        obj = Terminal(caracter, 5)
                        #obj = Terminal(caracter, 1)
                        lexList.append(obj)
                        print("opSuma Tipo 5: ", caracter)
                        identificador=""

                    elif (identificador in reservadas):
                        it = 0
                        for it in range(0, len(reservadas)):
                            if identificador == reservadas[it]:
                                tipoS = tipoR[it]
                            it= it+1 
                        obj = Terminal(identificador, int(tipoS))
                        lexList.append(obj)
                        print("Reservada Tipo "+ tipoS + ":", identificador)
                        obj = Terminal(caracter, 5)
                        #obj = Terminal(caracter, 1)
                        lexList.append(obj)
                        print("opSuma Tipo 5: ", caracter)
                        identificador=""
                    else:
                        obj = Terminal(identificador, 0)
                        lexList.append(obj)
                        print("Identificador Tipo 0: ", identificador)
                        real=""
                        identificador=""
                        numero=""
                        obj = Terminal(caracter, 5)
                        #obj = Terminal(caracter, 1)
                        lexList.append(obj)
                        print("opSuma Tipo 5: ", caracter)
                else:
                    obj = Terminal(caracter, 5)
                    #obj = Terminal(caracter, 1)
                    lexList.append(obj)
                    print("opSuma Tipo 5: ", caracter)
            
            elif (caracter == '*') or (caracter == '/'):
                if(len(real)!=0):
                    obj = Terminal(real, 2)
                    lexList.append(obj)
                    print("Real Tipo 2: ", real)
                    real=""
                    identificador=""
                    numero=""
                    obj = Terminal(caracter, 6)
                    lexList.append(obj)
                    print("opMul Tipo 6: ", caracter)
                elif(len(numero)!=0):
                    obj = Terminal(numero, 1)
                    lexList.append(obj)
                    print("Entero Tipo 1: ", numero)
                    real=""
                    identificador=""
                    numero=""
                    obj = Terminal(caracter, 6)
                    lexList.append(obj)
                    print("opMul Tipo 6: ", caracter)
                elif(len(identificador)!=0):
                    if(identificador in tipo):
                        obj = Terminal(identificador, 4)
                        lexList.append(obj)
                        print("TipoDato Tipo 4: ", identificador)
                        obj = Terminal(caracter, 6)
                        lexList.append(obj)
                        print("opMul Tipo 6: ", caracter)
                        identificador=""

                    elif (identificador in reservadas):
                        it = 0
                        for it in range(0, len(reservadas)):
                            if identificador == reservadas[it]:
                                tipoS = tipoR[it]
                            it= it+1 
                        obj = Terminal(identificador, int(tipoS))
                        lexList.append(obj)
                        print("Reservada Tipo "+ tipoS + ":", identificador)
                        obj = Terminal(caracter, 6)
                        lexList.append(obj)
                        print("opMul Tipo 6: ", caracter)
                        identificador=""
                    else:
                        obj = Terminal(identificador, 0)
                        lexList.append(obj)
                        print("Identificador Tipo 0: ", identificador)
                        real=""
                        identificador=""
                        numero=""
                        obj = Terminal(caracter, 6)
                        lexList.append(obj)
                        print("opMul Tipo 6: ", caracter)
                else:
                    obj = Terminal(caracter, 6)
                    lexList.append(obj)
                    print("opMul Tipo 6: ", caracter)

            elif (caracter == '<') or (caracter == '>') or (caracter == '!'):
                if(len(real)!=0):
                    obj = Terminal(real, 2)
                    lexList.append(obj)
                    print("Real Tipo 2: ", real)
                    real=""
                    identificador=""
                    numero=""
                elif(len(numero)!=0):
                    obj = Terminal(numero, 1)
                    lexList.append(obj)
                    print("Entero Tipo 1: ", numero)
                    real=""
                    identificador=""
                    numero=""
                elif(len(identificador)!=0):
                    if(identificador in tipo):
                        obj = Terminal(identificador, 4)
                        lexList.append(obj)
                        print("TipoDato Tipo 4: ", identificador)
                        identificador=""

                    elif (identificador in reservadas):
                        it = 0
                        for it in range(0, len(reservadas)):
                            if identificador == reservadas[it]:
                                tipoS = tipoR[it]
                            it= it+1 
                        obj = Terminal(identificador, int(tipoS))
                        lexList.append(obj)
                        print("Reservada Tipo "+ tipoS + ":", identificador)
                        identificador=""
                    else:
                        obj = Terminal(identificador, 0)
                        lexList.append(obj)
                        print("Identificador Tipo 0: ", identificador)
                        real=""
                        identificador=""
                        numero=""
                if (self.cadena[i+1]=="="):
                    cont= 1
                    skip = True
                    relac = caracter + self.cadena[i+1]
                    obj = Terminal(relac, 7)
                    lexList.append(obj)
                    print("opRelac Tipo 7: ", relac)
                    cont = 1
                    skip = True
                else:
                    obj = Terminal(caracter, 7)
                    lexList.append(obj)
                    print("opRelac Tipo 7: ", caracter)

            elif (caracter == '='):
                if(len(real)!=0):
                    obj = Terminal(real, 2)
                    lexList.append(obj)
                    print("Real Tipo 2: ", real)
                    real=""
                    identificador=""
                    numero=""
                elif(len(numero)!=0):
                    obj = Terminal(numero, 1)
                    lexList.append(obj)
                    print("Entero Tipo 1: ", numero)
                    real=""
                    identificador=""
                    numero=""
                elif(len(identificador)!=0):
                    if(identificador in tipo):
                        obj = Terminal(identificador, 4)
                        lexList.append(obj)
                        print("TipoDato Tipo 4: ", identificador)
                        identificador=""

                    elif (identificador in reservadas):
                        it = 0
                        for it in range(0, len(reservadas)):
                            if identificador == reservadas[it]:
                                tipoS = tipoR[it]
                            it= it+1 
                        obj = Terminal(identificador, int(tipoS))
                        lexList.append(obj)
                        print("Reservada Tipo "+ tipoS + ":", identificador)
                        identificador = ""
                    else:
                        obj = Terminal(identificador, 0)
                        lexList.append(obj)
                        print("Identificador Tipo 0: ", identificador)
                        real=""
                        identificador=""
                        numero=""
                if (self.cadena[i+1]=="="):
                    relac = caracter + self.cadena[i+1]
                    obj = Terminal(relac, 7)
                    lexList.append(obj)
                    print("opRelac Tipo 7: ", relac)
                    cont = 1
                    skip = True
                else:
                    obj = Terminal(caracter, 18)
                    lexList.append(obj)
                    print("opAsignacion Tipo 18: ", caracter)
                
            elif (caracter == '|'):
                if(len(real)!=0):
                    obj = Terminal(real, 2)
                    lexList.append(obj)
                    print("Real Tipo 2: ", real)
                    real=""
                    identificador=""
                    numero=""
                elif(len(numero)!=0):
                    obj = Terminal(numero, 1)
                    lexList.append(obj)
                    print("Entero Tipo 1: ", numero)
                    real=""
                    identificador=""
                    numero=""
                elif(len(identificador)!=0):
                    if(identificador in tipo):
                        obj = Terminal(identificador, 4)
                        lexList.append(obj)
                        print("TipoDato Tipo 4: ", identificador)
                        identificador=""

                    elif (identificador in reservadas):
                        it = 0
                        for it in range(0, len(reservadas)):
                            if identificador == reservadas[it]:
                                tipoS = tipoR[it]
                            it= it+1 
                        obj = Terminal(identificador, int(tipoS))
                        lexList.append(obj)
                        print("Reservada Tipo "+ tipoS + ":", identificador)
                        identificador=""
                    else:
                        obj = Terminal(identificador, 0)
                        lexList.append(obj)
                        print("Identificador Tipo 0: ", identificador)
                        real=""
                        identificador=""
                        numero=""
                if (self.cadena[i+1]=="|"):
                    orV = caracter + self.cadena[i+1]
                    obj = Terminal(orV, 8)
                    lexList.append(obj)
                    print("opOr Tipo 8: ", orV)
                    cont = 1
                    skip = True
                else:
                    print("OpOr incompleto ")

            elif (caracter == '&'):
                if(len(real)!=0):
                    obj = Terminal(real, 2)
                    lexList.append(obj)
                    print("Real Tipo 2: ", real)
                    real=""
                    identificador=""
                    numero=""
                elif(len(numero)!=0):
                    obj = Terminal(numero, 1)
                    lexList.append(obj)
                    print("Entero Tipo 1: ", numero)
                    real=""
                    identificador=""
                    numero=""
                elif(len(identificador)!=0):
                    if(identificador in tipo):
                        obj = Terminal(identificador, 4)
                        lexList.append(obj)
                        print("TipoDato Tipo 4: ", identificador)
                        identificador=""

                    elif (identificador in reservadas):
                        it = 0
                        for it in range(0, len(reservadas)):
                            if identificador == reservadas[it]:
                                tipoS = tipoR[it]
                            it= it+1 
                        obj = Terminal(identificador, int(tipoS))
                        lexList.append(obj)
                        print("Reservada Tipo "+ tipoS + ":", identificador)
                        identificador=""
                    else:
                        obj = Terminal(identificador, 0)
                        lexList.append(obj)
                        print("Identificador Tipo 0: ", identificador)
                        real=""
                        identificador=""
                        numero=""
                if (self.cadena[i+1]=="&"):
                    andV = caracter + self.cadena[i+1]
                    obj = Terminal(andV, 9)
                    lexList.append(obj)
                    print("opAnd Tipo 9: ", andV)
                    cont = 1
                    skip = True
                else:
                    print("OpAnd incompleto ")

            elif (caracter == '!'):
                if(len(real)!=0):
                    obj = Terminal(real, 2)
                    lexList.append(obj)
                    print("Real Tipo 2: ", real)
                    real=""
                    identificador=""
                    numero=""
                    obj = Terminal(caracter, 10)
                    lexList.append(obj)
                    print("opNot Tipo 10: ", caracter)
                elif(len(numero)!=0):
                    obj = Terminal(numero, 1)
                    lexList.append(obj)
                    print("Entero Tipo 1: ", numero)
                    real=""
                    identificador=""
                    numero=""
                    obj = Terminal(caracter, 10)
                    lexList.append(obj)
                    print("opNot Tipo 10: ", caracter)
                elif(len(identificador)!=0):
                    if(identificador in tipo):
                        obj = Terminal(identificador, 4)
                        lexList.append(obj)
                        print("TipoDato Tipo 4: ", identificador)
                        obj = Terminal(caracter, 10)
                        lexList.append(obj)
                        print("opNot Tipo 10: ", caracter)
                        identificador=""
                    elif (identificador in reservadas):
                        it = 0
                        for it in range(0, len(reservadas)):
                            if identificador == reservadas[it]:
                                tipoS = tipoR[it]
                            it= it+1 
                        obj = Terminal(identificador, int(tipoS))
                        lexList.append(obj)
                        print("Reservada Tipo "+ tipoS + ":", identificador)
                        identificador = ""
                    else:
                        obj = Terminal(identificador, 0)
                        lexList.append(obj)
                        print("Identificador Tipo 0: ", identificador)
                        real=""
                        identificador=""
                        numero=""
                        obj = Terminal(caracter, 10)
                        lexList.append(obj)
                        print("opNot Tipo 10: ", caracter)
                else:
                    obj = Terminal(caracter, 10)
                    lexList.append(obj)
                    print("opNot Tipo 10: ", caracter)

            elif (caracter in simbolos):
                it = 0
                for it in range(0, len(simbolos)):
                    if caracter == simbolos[it]:
                        tipoS = tipoA[it]
                    it= it+1

                if(len(real)!=0):
                    obj = Terminal(real, 2)
                    lexList.append(obj)
                    print("Real Tipo 2: ", real)
                    real=""
                    identificador=""
                    numero=""
                elif(len(numero)!=0):
                    obj = Terminal(numero, 1)
                    lexList.append(obj)
                    print("Entero Tipo 1: ", numero)
                    real=""
                    identificador=""
                    numero=""
                elif(len(identificador)!=0):
                    if(identificador in tipo):
                        obj = Terminal(identificador, 4)
                        lexList.append(obj)
                        print("TipoDato Tipo 4: ", identificador)
                        identificador=""

                    elif (identificador in reservadas):
                        it = 0
                        for it in range(0, len(reservadas)):
                            if identificador == reservadas[it]:
                                tipoS = tipoR[it]
                            it= it+1 
                        obj = Terminal(identificador, int(tipoS))
                        lexList.append(obj)
                        print("Reservada Tipo "+ tipoS + ":", identificador)
                        identificador=""
                        
                    else:
                        obj = Terminal(identificador, 0)
                        lexList.append(obj)
                        print("Identificador Tipo 0: ", identificador)
                        real=""
                        identificador=""
                        numero=""
                obj = Terminal(caracter, int(tipoS))
                lexList.append(obj)
                print("Simbolo Tipo "+ tipoS + ":", caracter)
             
            
            i=i+1            

        if(len(real)!=0):
            obj = Terminal(real, 2)
            lexList.append(obj)
            print("Real Tipo 2", real)
            real=""
            identificador=""
            numero=""
        elif(len(numero)!=0):
            obj = Terminal(numero, 1)
            lexList.append(obj)
            print("Entero Tipo 1", numero)
            real=""
            identificador=""
            numero=""
        elif(len(identificador)!=0):
            if(identificador in tipo):
                obj = Terminal(identificador, 4)
                lexList.append(obj)
                print("TipoDato Tipo 4: ", identificador)
                identificador=""

            elif (identificador in reservadas):
                        it = 0
                        for it in range(0, len(reservadas)):
                            if identificador == reservadas[it]:
                                tipoS = tipoR[it]
                            it= it+1 
                        obj = Terminal(identificador, int(tipoS))
                        lexList.append(obj)
                        print("Reservada Tipo "+ tipoS + ":", identificador)
                        identificador=""
            else:
                obj = Terminal(identificador, 0)
                lexList.append(obj)
                print("Identificador Tipo 0", identificador)
                real=""
                identificador=""
                numero=""
                obj = Terminal("$", 23)
                lexList.append(obj)


ParamList = list()
ParamCList = list()
TermList = list()
ExpList = list()
ConList = list()
RetList = list()
TermCList = list()
SenList = list()
CallList = list()
VarList = list()
ListaVarList = list()
ErrorList = list()
OpList = list()
class variable:
    def __init__(self, tipo, id, contexto):
        self.tipo = tipo
        self.id = id
        self.contexto = contexto

class retorno:
    def __init__(self, cad, tipo, context):
        self.cad = cad
        self.tipo = tipo
        self.context = context
    
class Sintactico: 
    def __init__(self):
        pass
    
    def remplazar(self, elim, num, flagR):
        while elim !=0:
            if flagR == 1:
                flagR = 0   
                objetoL.append(pila[-1])
            else:
                flagR = 1
            pila.pop()
            elim -=1
        for elem in objetoL:
            #print(elem.fuente)
            pass
        if num == 1: 
            obj = Programa(objetoL[0], Node('Programa', parent=root))
            obj.definiciones.nodo.parent = obj.nodo
        elif num == 2:
            obj = NoElim(num, "Definiciones", Node('Definiciones', parent=root))
        elif num == 3:
            obj = Definiciones3(objetoL[1], objetoL[0], Node('Definiciones', parent=root))
            obj.definicion.nodo.parent = obj.nodo
            obj.definiciones.nodo.parent = obj.nodo
        elif num == 4 or num == 5:
            obj = Definicion(objetoL[0], Node('Definicion', parent=root))
            obj.defi.nodo.parent = obj.nodo
        elif num == 5:
            obj = NoElim(num, "Definicion", Node('Definicion', parent=root))
        elif num == 6:
            obj = DefVar(objetoL[3], objetoL[2], objetoL[1], objetoL[0],Node('DefVar', parent=root))
            Node(objetoL[3].fuente, parent = obj.nodo)
            Node(objetoL[2].fuente, parent = obj.nodo)
            obj.listaVar.nodo.parent = obj.nodo
            Node(objetoL[0].fuente, parent = obj.nodo)
            globals()['VarFlag'] +=1
            if obj.listaVar.__class__.__name__ == 'NoElim':
                obj.listaVar = globals()['ambito']
                if obj.listaVar == '':
                    obj.listaVar = 'Global'
            VarList.append(obj)
            if len(ListaVarList)!=0:
                for i in range(len(ListaVarList)):
                    auxiliar = ListaVarList.pop(0)
                    auxiliar.tipo = objetoL[3]
                    auxiliar.listaVar = objetoL[1]
                    ListaVarList.append(auxiliar)
                    VarList.append(auxiliar)
        elif num == 7:
            obj = NoElim(num, "ListaVar", Node('ListaVar', parent=root))
        elif num == 8:
            obj = ListaVar8(objetoL[1], objetoL[0], Node('ListaVar', parent=root))
            Node(objetoL[1].fuente, parent = obj.nodo)
            obj.listaVar.nodo.parent = obj.nodo
            ListaVarList.append(DefVar('Tipo', objetoL[1], objetoL[0]))
        elif num == 9:
            obj = DefFunc(objetoL[5], objetoL[4], objetoL[3], objetoL[2], objetoL[1], objetoL[0], Node('DefFunc', parent=root))
            Node(objetoL[5].fuente, parent = obj.nodo)
            Node(objetoL[4].fuente, parent = obj.nodo)
            Node(objetoL[3].fuente, parent = obj.nodo)
            obj.parametros.nodo.parent = obj.nodo
            Node(objetoL[1].fuente, parent = obj.nodo)
            obj.bloqFunc.nodo.parent = obj.nodo
            aux = globals()['ambito']
            globals()['ambito'] =''
            if globals()['tiporetorno'] != objetoL[5].fuente:
                if globals()['tiporetorno'] == '':
                    pass
                else:
                    ErrorList.append('Error en la funcion ' + aux)
            globals()['tiporetorno'] = ""
            OpList.clear()
        elif num == 10:
            obj = NoElim(num, "Parametros", Node('Parametros', parent=root))
        elif num == 11:
            obj = Parametros(objetoL[2], objetoL[1], objetoL[0], Node('Parametros', parent=root ))
            Node(objetoL[2].fuente, parent = obj.nodo)
            Node(objetoL[1].fuente, parent = obj.nodo)
            obj.listaParam.nodo.parent = obj.nodo
            globals()['parametro'] = obj
            ParamList.append(obj)
            contexto = ''
            i = 0
            posi =2
            posfi = 6
            if pila[2].fuente=='Definicion':
                while i == 0: 
                    posi = posi +2
                    if pila[posi].fuente == 'Definicion':
                        posfi = posfi +2
                    else:
                        contexto =pila[posfi].fuente
                        i = 1
                        break
            else:
                contexto= pila[4].fuente
            ParamCList.append(ParametrosCon(objetoL[2], objetoL[1], contexto, Node('ParametrosCon', parent=root2) ))
        elif num == 12:
            obj = NoElim(num, "ListaParam", Node('ListaParam', parent=root))
        elif num == 13:
            obj = ListaParam(objetoL[2], objetoL[1], objetoL[0], Node('ListaParam', parent=root))
            Node(objetoL[2].fuente, parent = obj.nodo)
            Node(objetoL[1].fuente, parent = obj.nodo)
            obj.listaParam.nodo.parent = obj.nodo
            globals()['parametro'] = obj
            ParamList.append(obj)
            contexto = ''
            i = 0
            posi =2
            posfi = 6
            if pila[2].fuente=='Definicion':
                while i == 0: 
                    posi = posi +2
                    if pila[posi].fuente == 'Definicion':
                        posfi = posfi +2
                    else:
                        contexto =pila[posfi].fuente
                        i = 1
                        break
            else:
                contexto= pila[4].fuente
            ParamCList.append(ParametrosCon(objetoL[2], objetoL[1], contexto,  Node('ParametrosCon', parent=root2) ))
        elif num == 14:
            obj = BloqFunc(objetoL[2], objetoL[1], objetoL[0], Node('BloqFunc', parent=root))
            Node(objetoL[2].fuente, parent = obj.nodo)
            obj.defLocales.nodo.parent = obj.nodo
            Node(objetoL[0].fuente, parent = obj.nodo)
            TermList.clear()
        elif num == 15:
            obj = NoElim(num, "DefLocales", Node('DefLocales', parent=root))
        elif num == 16:
            obj = DefLocales16(objetoL[1], objetoL[0], Node('DefLocales', parent=root))
            obj.defLocal.nodo.parent = obj.nodo
            obj.defLocales.nodo.parent = obj.nodo
        elif num == 17 or num == 18:
            obj = DefLocal(objetoL[0], Node('DefLocal', parent=root))
            obj.defSent.nodo.parent = obj.nodo
            if len(ListaVarList)!=0:
                ListaVarList.pop(0)
        elif num == 18:
            obj = NoElim(num, "DefLocal", Node('DefLocal', parent=root))
        elif num == 19:
            obj = NoElim(num, "Sentencias", Node('Sentencias', parent=root))
        elif num == 20:
            obj = Sentencias20(objetoL[1], objetoL[0], Node('Sentencias', parent=root))
            obj.sentencia.nodo.parent = obj.nodo
            obj.sentencias.nodo.parent = obj.nodo
            SenList.append(obj)
            CallList.clear()
        elif num == 21:
            objS = Sentencia21(objetoL[3], objetoL[2], objetoL[1], objetoL[0], Node('Sentencia', parent=root))
            Node(objetoL[3].fuente, parent = objS.nodo)
            Node(objetoL[2].fuente, parent = objS.nodo)
            objS.expresion.nodo.parent = objS.nodo
            Node(objetoL[0].fuente, parent = objS.nodo)
            SenList.append(objS)
            cont = 0
            ExpList.clear()
            anadidos = 0
            x = 0
            partederecha = 0
            if ExpList!=0:
                for obj in VarList:

                    if objetoL[3].fuente == obj.identificador.fuente and obj.listaVar == globals()['ambito']:
                        aux= obj.tipo.fuente
                        aux2 = obj
                        cont = 0
                        while x < anadidos:
                            ErrorList.pop()
                            x+=1
                        break
                    else:
                        if cont ==0:
                            cont = 1
                            ErrorList.append('Error al asignar ' + str(objetoL[3].fuente) +' Variable no existe o no en este contexto')
                            aux = 'mmm'
                            aux2 = 'mmm'
                            anadidos +=1
                        else:
                            pass

                for obj in TermList:
                    objS.listateraux.append(obj)
                i =0
                coincidencias = len(objS.listateraux)
                coincidenciasobj = 0
                variables = list()
                bandera = 0
                correcto = 0
                largo = len(VarList)
                for obj in VarList:
                    if bandera == 1:
                        break
                    if coincidenciasobj == coincidencias:
                        break
                    for obj2 in objS.listateraux:
                        if obj.identificador.fuente == objS.listateraux[i].fuente:

                            bandera = 0
                            correcto = 1
                            coincidenciasobj +=1
                            if obj.tipo.fuente != aux:
                                if cont ==0:
                                    ErrorList.append('Error al asignar ' + str(aux2.identificador.fuente) +' tipos de datos diferentes')
                                    bandera = 1
                                    cont+=1
                            else:

                                pass

                        else:
                            largo -=1
                            correcto =0
                            pass                       
                                
                        i +=1

                    i=0
                if largo <=0 and correcto == 0 and coincidenciasobj != coincidencias:
                    if len(VarList)==0:
                        ErrorList.append('Error al asignar ' + str(objetoL[3].fuente) +' No existe o no dentro de este contexto')
                        cont+=1
                    else:
                        bandera =1
                contador = 0
                esparametro= 0
                #espa
                if bandera ==1: #ARREGLAR TIPO
                    if obj2.tipo == 2:
                        obj2.tipo = 'float'
                    elif obj2.tipo == 1:
                        obj2.tipo = 'int'
                    elif obj2.tipo == 0:
                        esparametro= 1
                        for objeto in ParamCList:
                            if objeto.identificador.fuente == objS.listateraux[contador].fuente:
                                obj2.tipo = objeto.tipo.fuente
                                break
                            else: 
                                pass
                                
                    if obj2.tipo != aux:

                        if globals()['CallFlag']!=0:
                            pass
                        else:
                            if cont ==0:
                                ErrorList.append('Error al asignar ' + str(aux2.identificador.fuente) +' tipos de datos diferentes')
                                cont+=1
                    else:
                        if len(OpList)==0:
                            if globals()['callFunc']==0:
                                if esparametro== 0:
                                    pass 
                                else:
                                    pass
                            else:
                                globals()['callFunc']=0
                        else:
                            pass
                        
                if cont ==0 and len(OpList)!=0:
                    for obj5 in TermList:
                        variables.append(Variables(obj5.fuente, globals()['ambito']))
                    partederecha = len(variables)
                    if OpList[0] == '+' or OpList[0] == '*':
                        pass
                for ter in TermList:
                    TermCList.append(ter)
                TermList.clear()
                OpList.clear()
                globals()['CallFlag']=0


                if globals()['PrintFlag']==1:
                    pass
                globals()['PrintFlag']=0
                globals()['printV']=''
            else:
                pass
            aux = 'Sentencia'
            objetoL.clear()
            #Node(obj.fuente, parent=root)
            return objS
        elif num == 22:
            obj = Sentencia22(objetoL[5], objetoL[4], objetoL[3], objetoL[2], objetoL[1], objetoL[0], Node('Sentencia', parent=root))
            Node(objetoL[5].fuente, parent = obj.nodo)
            Node(objetoL[4].fuente, parent = obj.nodo)
            obj.expresion.nodo.parent = obj.nodo
            Node(objetoL[2].fuente, parent = obj.nodo)
            obj.sentenciaB.nodo.parent = obj.nodo
            obj.otro.nodo.parent = obj.nodo
            TermCList.clear()
            ConList.append(obj)
        elif num == 23:
            obj = Sentencia23(objetoL[4], objetoL[3], objetoL[2], objetoL[1], objetoL[0], Node('Sentencia', parent=root))
            Node(objetoL[3].fuente, parent = obj.nodo)
            Node(objetoL[2].fuente, parent = obj.nodo)
            obj.expresion.nodo.parent = obj.nodo
            Node(objetoL[1].fuente, parent = obj.nodo)
            obj.bloque.nodo.parent = obj.nodo
        elif num == 24:
            obj = Sentencia24(objetoL[2], objetoL[1], objetoL[0], Node('Sentencia', parent=root))
            Node(objetoL[2].fuente, parent = obj.nodo)
            obj.valorR.nodo.parent = obj.nodo
            Node(objetoL[0].fuente, parent = obj.nodo)
            TermList.pop()
            SenList.append(obj)
        elif num == 25:
            obj = Sentencia25(objetoL[1], objetoL[0], Node('Sentencia', parent=root))
            obj.llamadaF.nodo.parent = obj.nodo
            Node(objetoL[0].fuente, parent = obj.nodo)
        elif num == 26:
            obj = NoElim(num, "Otro", Node('Otro', parent=root))
        elif num == 27:
            obj = Otro27(objetoL[1], objetoL[0], Node('Otro', parent=root))
            Node(objetoL[1].fuente, parent = obj.nodo)
            obj.sentenciaB.nodo.parent = obj.nodo
            ConList.append(obj)
        elif num == 28:
            obj = Bloque(objetoL[2], objetoL[1], objetoL[0], Node('Bloque', parent=root))
            Node(objetoL[2].fuente, parent = obj.nodo)
            obj.sentencias.nodo.parent = obj.nodo
            Node(objetoL[0].fuente, parent = obj.nodo)
        elif num == 29:
            obj = NoElim(num, "ValorRegresa", Node('ValorRegresa', parent=root))
        elif num == 30:
            obj = ValorRegresa(objetoL[0], Node('ValorRegresa', parent=root))
            obj.expresion.nodo.parent = obj.nodo
            tipo = ''
            contexto = ''
            i = 0
            posi =2
            posfi = 6
            if pila[2].fuente=='Definicion':
                while i == 0: 
                    posi = posi +2
                    if pila[posi].fuente == 'Definicion':
                        posfi = posfi +2
                    else:
                        contexto =pila[posfi].fuente
                        i = 1
                        break
            else:
                contexto= pila[4].fuente
            if TermList[-1].tipo == 2:
                tipo = 'float'
            elif TermList[-1].tipo == 1:
                tipo = 'int'
            elif TermList[-1].tipo == 0:
                for obj in ParamCList:
                    if TermList[-1].fuente == obj.identificador.fuente and contexto == obj.contexto:
                        tipo = obj.tipo
                if tipo == '':
                    for obj in VarList:
                        if TermList[-1].fuente == obj.identificador.fuente and contexto == obj.listaVar:
                            tipo = obj.tipo.fuente
                            break
            else:
                tipo = TermList[-1].tipo
            globals()['tiporetorno'] = tipo.fuente
            variables = list()
            if len(OpList)!=0:
                for obj5 in TermList:
                    variables.append(Variables(obj5.fuente, globals()['ambito']))
                partederecha = len(variables)
                OpList.clear()
            else:
                pass
            RetList.append(retorno(TermList[-1].fuente, tipo, contexto))
        elif num == 31:
            obj = NoElim(num, "Argumentos", Node('Argumentos', parent=root))
        elif num == 32:
            obj = Argumentos(objetoL[1], objetoL[0], Node('Argumentos', parent=root))
            obj.expresion.nodo.parent = obj.nodo
            obj.listaA.nodo.parent = obj.nodo
        elif num == 33:
            obj = NoElim(num, "ListaArgumentos", Node('ListaArgumentos', parent=root))
        elif num == 34:
            obj = ListaArgumentos(objetoL[2], objetoL[1], objetoL[0], Node('ListaArgumentos', parent=root))
            Node(objetoL[2].fuente, parent = obj.nodo)
            obj.expresion.nodo.parent = obj.nodo
            obj.listaA.nodo.parent = obj.nodo
        elif num == 35:
            obj = Termino35(objetoL[0], Node('Termino', parent=root))
            print('SDKNSOIDNS', obj.llamadaFunc.identificador.fuente)
            obj.llamadaFunc.nodo.parent = obj.nodo
            CallList.append('Llamada')
        elif num == 36 or num == 37 or num == 38 or num == 39:
            obj = Termino(objetoL[0], Node('Termino', parent=root))
            Node(objetoL[0].fuente, parent=obj.nodo)
            if num == 36:
                i =0
                largo = len(VarList)
                correcto = 0
                while i <globals()['VarFlag']:
                    if objetoL[0].fuente == VarList[i].identificador.fuente:
                        correcto = 1
                        contexto = VarList[i].listaVar
                        tipo = VarList[i].tipo
                        break
                    i+=1
                    largo-=1
                    correcto = 0
                flagencontrado = 0
                if largo <=0 and correcto == 0:
                    for objP in ParamCList:
                        if objP.identificador.fuente == objetoL[0].fuente:
                            flagencontrado = 0
                            break
                        else: 
                            flagencontrado = 1
                if flagencontrado==1:
                    ErrorList.append('Error en la variable ' + str(objetoL[0].fuente) +' No existe')
                try:
                    if pila[-2].fuente=='return' or pila[16].fuente=='return':
                        contexto =""
                        i = 0
                        posi =2
                        posfi = 6
                        if pila[2]=='Definicion':
                            while i == 0: 
                                posi = posi +2
                                if pila[posi] == 'Definicion':
                                    posfi = posfi +2
                                else:
                                    contexto =pila[posfi].fuente
                                    i = 1
                                    break
                        else:
                            contexto= pila[4].fuente
                        obj.contexto = 'Retorno'+contexto
                    else:
                        obj.contexto = contexto
                except:
                    obj.contexto = contexto
                TermList.append(objetoL[0])
            elif num == 37 or num == 38:  
                obj.contexto = globals()['ambito']
                try:
                    if pila[14].fuente=='return':

                        i = 0
                        contexto = ''
                        posi =2
                        posfi = 6
                        if pila[2]=='Definicion':
                            while i == 0: 
                                posi = posi +2
                                if pila[posi] == 'Definicion':
                                    posfi = posfi +2
                                else:
                                    contexto =pila[posfi].fuente
                                    i = 1
                                    break
                            obj.contexto = 'Retorno'+contexto
                        else:
                            obj.contexto = 'Retorno'+pila[4].fuente

                    else:
                        obj.contexto = obj.contexto
                except:
                    obj.contexto = obj.contexto
                TermList.append(objetoL[0])
        elif num == 40:
            objS = LlamadaFunc(objetoL[3], objetoL[2], objetoL[1], objetoL[0], Node('LlamadaFunc', parent=root))
            Node(objetoL[3].fuente, parent=objS.nodo)
            Node(objetoL[2].fuente, parent=objS.nodo)
            objS.argumentos.nodo.parent = objS.nodo
            Node(objetoL[0].fuente, parent=objS.nodo)
            bandera = 0
            bandera2 =0
            bandera3 = 0
            contexto  = ''
            i = 0
            posi =2
            posfi = 6
            if pila[2].fuente=='Definicion':
                while i == 0: 
                    posi = posi +2
                    if pila[posi].fuente == 'Definicion':
                        posfi = posfi +2
                    else:
                        contexto =pila[posfi].fuente
                        i = 1
                        break
            else:
                contexto= pila[4].fuente
            entre = 0
            if len(ParamCList)!=0:
                for obj in ParamCList:
                    if objetoL[3].fuente == obj.contexto:
                        #self.funcion= obj.tipo
                        

                        try:
                            #print(TermList[-1].cad)
                            pass
                        except:
                            bandera=1
                            break
                        for obj2 in VarList:

                            if TermList[-1].fuente == obj2.identificador.fuente and obj2.listaVar == contexto:

                                if obj.tipo.fuente == obj2.tipo.fuente:
                                    bandera = 0
                                    bandera2=0
                                    if entre ==0:
                                        entre+=1
                                    
                                    if bandera3 ==0:
                                        bandera3+=1
                                    else:
                                        pass
                                    num = ParamCList.index(obj)
                                    TermList.pop()
                                    break
                                else:
                                    bandera = 1

                            else:
                                bandera2=1
                        
                        if bandera2 ==1:
                            tipo = ''
                            if TermList[-1].tipo == 1:
                                tipo = 'int'
                            elif TermList[-1].tipo == 2:
                                tipo = 'float'
                            if tipo == obj.tipo.fuente:
                                break
                            else:
                                bandera = 1
                                

                        else:
                            pass

                    else:
                        pass
                tipo = ''
                tipo2 = ''
                if len(RetList)>0:
                    for obj in RetList:
                        if objS.identificador.fuente == obj.context:
                            
                            tipo = obj.tipo.fuente
                else:
                    tipo = 'void'

                for obj in VarList:
                    if obj.identificador.fuente == pila[-4].fuente and obj.listaVar == contexto:
                        tipo2 = obj.tipo.fuente
                if tipo != tipo2:
                    if tipo == 'void':
                        pass
                    else:
                        ErrorList.append('Error en el retorno de la funcion ' + objetoL[3].fuente + ' O tipos de datos diferentes')

                if bandera == 1:
                    ErrorList.append('Error en la llamada a la funcion ' + objetoL[3].fuente + ' O tipos de datos diferentes')
                globals()['CallFlag']=1
            objetoL.clear()
            return objS
        elif num == 41 or num == 42:
            obj = SentenciaBloque(objetoL[0], Node('SentenciaBloque', parent=root))
            obj.senBlo.nodo.parent = obj.nodo
        elif num == 43:
            obj = Expresion43(objetoL[2], objetoL[1], objetoL[0], Node('Expresion', parent=root))
            Node(objetoL[2].fuente, parent=obj.nodo)
            obj.expresion.nodo.parent = obj.nodo
            Node(objetoL[0].fuente, parent=obj.nodo)
        elif num == 44 or num == 45:
            obj = Expresion44(objetoL[1], objetoL[0], Node('Expresion', parent=root))
            Node(objetoL[1].fuente, parent=obj.nodo)
            obj.expresion.nodo.parent = obj.nodo
        elif num == 46 or num == 47 or num == 48 or num == 49 or num == 50 or num == 51:
            obj = Expresion46(objetoL[2], objetoL[1], objetoL[0], Node('Expresion', parent=root))
            obj.expresion1.nodo.parent = obj.nodo
            Node(objetoL[1].fuente, parent=obj.nodo)
            obj.expresion2.nodo.parent = obj.nodo
            if num == 46:
                TermCList.clear()
                OpList.append('*')
                ExpList.append(obj)
            elif num == 47:
                TermCList.clear()
                OpList.append(pila[-4].fuente)
                ExpList.append(obj)
            elif num == 48:
                TermCList.clear()
                ExpList.append(obj)
            elif num == 49:
                TermCList.clear()
                ExpList.append(obj)
        elif num == 52:
            obj = Expresion52(objetoL[0], Node('Expresion', parent=root))
            obj.termino.nodo.parent = obj.nodo
            #pila.append(obj)

            ExpList.append(obj)
        else:
            obj = Termino("Hola")
        objetoL.clear()
        #Node(obj.fuente, parent=root)
        return obj
    
    def analizar(self):
        i=0
        pilaS=''
        while True:
            obj = lexList[i]
            fila = pila[-1]
            columna = obj.tipo
            accion = tlr1[fila.fuente][columna]
            if obj.fuente == 'print':
                i+=1
                obj = lexList[i]
                while obj.fuente != ')':
                    i+=1
                    obj = lexList[i]
                i+=1
                obj = lexList[i]
            elif (accion == 0):
                acc = "NADA"
                break
            elif (accion > 0):
                i+=1
                acc = "d"+str(accion)
                pila.append(Terminal(obj.fuente, obj.tipo))
                pila.append(Estado(accion))
            elif (accion == -1):
                acc = "r0(acept)"
                break
            else:
                acc = "r"+str(abs(accion+1))
                for obj2 in reglas:
                    if (accion == (obj2.num + 1)*-1):
                        acc = "r"+str(obj2.num)
                        accion = tlr1[fila.fuente][obj2.num2]
                        if obj2.elem !=0:
                            elim = obj2.elem*2
                            flagR = 0
                            obj3 = self.remplazar(elim, obj2.num, flagR)
                            fila = pila[-1]
                            accion = tlr1[fila.fuente][obj2.num2]
                            pila.append(obj3)
                            pilaNodo.append(obj3)
                            pila.append(Estado(accion))
                        else:
                            if obj2.num == 10:
                                globals()['ambito'] = pila[-4].fuente
                            elif obj2.num == 12:
                                z = 0
                                posi =2
                                posfi = 6
                                if pila[2]=='Definicion':
                                    while z == 0: 
                                        posi = posi +2
                                        if pila[posi] == 'Definicion':
                                            posfi = posfi +2
                                        else:
                                            globals()['ambito'] =pila[posfi].fuente
                                            z = 1
                                            break
                                else:
                                    globals()['ambito']= pila[4].fuente
                            obj3 = self.remplazar(0, obj2.num, 0)
                            pila.append(obj3)
                            pilaNodo.append(obj3)
                            pila.append(Estado(accion))
                        break
            if(i == len(lexList)):
                print("FIN")
            
            for p in pila:
                pilaS += str(p.fuente)
            data.append([pilaS, obj.fuente, acc])
            pilaS = ""
class analizadorSemantico:
    def __init__(self):
        self.tablaSimbolos = {}
    
    def recorrer(self, arbol):
        for node in PreOrderIter(arbol):
            # if node.name == 'DefVar':
            #     self.defVar(node)
            if node.name == 'DefFunc':
                self.defFunc(node)
            elif node.name == 'LlamadaFunc':
                self.llamadaFunc(node)
            
    def defVar(self, node):
        tipo = node.children[0].name
        print('TIPO', tipo)
        if tipo not in ["int", "void", "float"]:
            raise ValueError(f"Error tipo de dato invalido en la variable {node.children[1].name}")
        
        if node.children[1].name not in self.tablaSimbolos:
            # raise ValueError(f"Error la variale {node.children[1].name} ya fue definida")
            self.tablaSimbolos[node.children[1].name] = tipo

    def defFunc(self, node):
        # tipo = node.children[0].name
        # if tipo not in ["int", "void", "float"]:
        #     raise ValueError(f"Error tipo de dato invalido en la funcion {node.children[1].name}")
        
        if node.children[1].name not in self.tablaSimbolos:
            #raise ValueError(f"Error la funcion {node.children[1].name} ya fue definida")
            self.tablaSimbolos[node.children[1].name] = 'funcion'
        # if node.children[3].children:
        #     if node.children[3].children[0].name not in ["int", "void", "float"]:
        #         raise ValueError(f"Error tipo de dato invalido en la variable {node.children[3].children[0].name}")
        # for param in node.children[3].children:
        #     if param.name not in ["int", "void", "float"]:
        #         raise ValueError(f"Error tipo de dato invalido en la variable {param.name}")
        #     print(param)

    def llamadaFunc(self, node):
        if node.children[0].name not in self.tablaSimbolos:
            ErrorList.append("Error la funcion "+node.children[0].name + " no ha sido definida")
            #raise ValueError(f"Error la funcion {node.children[0].name} no ha sido definida")

cadena = "void menu(){hola = 5;}"
Lexico(cadena).analizar()
Sintactico().analizar()
analizadorSemantico().recorrer(root)
print(tabulate(data, headers=["Pila", "Entrada", "Salida"]))

for pre, fill, node, in RenderTree(root):
    print("%s%s" % (pre, node.name))

if len(ErrorList)!=0:
    for obj in ErrorList:
        print(obj)

print('Variables')
for obj in VarList:
    data2.append([obj.tipo.fuente, obj.identificador.fuente, obj.listaVar])
print(tabulate(data2, headers=["Tipo", "Nombre", "Contexto"]))