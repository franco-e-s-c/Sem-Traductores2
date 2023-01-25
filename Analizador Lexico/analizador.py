class miniLexico:
    def __init__(self, cadena):
        self.cadena = cadena + '$'

    def comprobar(self):
        pass

    def analizar(self):
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
        reservadas = ["while", "return", "else"]
        tipoR = ["20", "21", "22"]
        for caracter in self.cadena:
            asCarac = ord(caracter)
            if (caracter == '$'):
                break
            elif(skip==True):
                if(n != cont-1):
                    n=n+1
                    continue
                else:
                    skip=False
            elif (asCarac > 64 and asCarac < 91) or (asCarac>96 and asCarac<123): #Comprobamos si el caracter es una letra
                if(len(real)!=0):
                    print("Real Tipo 2: ", real)
                    real=""
                    identificador=""
                    numero=""
                    identificador += caracter
                elif(len(numero)!=0):
                    print("Entero Tipo 1: ", numero)
                    real=""
                    identificador=""
                    numero=""
                    identificador += caracter
                elif(len(cadenaS)!=0):
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
                        print("TipoDato Tipo 4: ", identificador)
                        identificador=""

                    elif (identificador in reservadas):
                        it = 0
                        for it in range(0, len(reservadas)):
                            if identificador == reservadas[it]:
                                tipoS = tipoR[it]
                            it= it+1 
                        print("Reservada Tipo "+ tipoS + ":", identificador)
                elif(len(cadenaS)!=0):
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
                        print("TipoDato Tipo 4: ", identificador)
                        identificador=""

                    elif (identificador in reservadas):
                        it = 0
                        for it in range(0, len(reservadas)):
                            if identificador == reservadas[it]:
                                tipoS = tipoR[it]
                            it= it+1 
                        print("Reservada Tipo "+ tipoS + ":", identificador)
                    else:
                        print("Identificador Tipo 0: ", identificador)
                        real=""
                        identificador=""
                        numero=""
                elif(len(real)!=0):
                    print("Real Tipo 2: ", real)
                    real=""
                    identificador=""
                    numero=""
                elif(len(numero)!=0):
                    print("Entero Tipo 1: ", numero)
                    real=""
                    identificador=""
                    numero=""
                elif(len(cadenaS)!=0):
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
                        print("TipoDato Tipo 4: ", identificador)
                        identificador=""

                    elif (identificador in reservadas):
                        it = 0
                        for it in range(0, len(reservadas)):
                            if identificador == reservadas[it]:
                                tipoS = tipoR[it]
                            it= it+1 
                        print("Reservada Tipo "+ tipoS + ":", identificador)
                    else:
                        print("Identificador Tipo 0: ", identificador)
                        real=""
                        identificador=""
                        numero=""
                elif(len(real)!=0):
                    print("Real Tipo 2: ", real)
                    real=""
                    identificador=""
                    numero=""
                elif(len(numero)!=0):
                    print("Entero Tipo 1: ", numero)
                    real=""
                    identificador=""
                    numero=""
                
                for cadenaCar in range(c, len(self.cadena)):
                    cont=cont+1
                    if (self.cadena[cadenaCar] == '$'):
                        print("ERROR CADENA NO CIERRA")
                        skip = True
                        break
                    elif (self.cadena[cadenaCar]=="'") or (self.cadena[cadenaCar]=='"'):
                        skip = True
                        print("Cadena Tipo 3: ", cadenaS)
                        real=""
                        identificador=""
                        numero=""
                        cadenaS=""
                        break
                    cadenaS=cadenaS + self.cadena[cadenaCar]

            elif (caracter == '+') or (caracter == '-'):
                if(len(numero)!=0):
                    print("Entero Tipo 1: ", numero)
                    real=""
                    identificador=""
                    numero=""
                    print("opSuma Tipo 5: ", caracter)
                elif(len(real)!=0):
                    print("Real Tipo 2: ", real)
                    real=""
                    identificador=""
                    numero=""
                    print("opSuma Tipo 5: ", caracter)
                elif(len(identificador)!=0):
                    if(identificador in tipo):
                        print("TipoDato Tipo 4: ", identificador)
                        print("opSuma Tipo 5: ", caracter)
                        identificador=""

                    elif (identificador in reservadas):
                        it = 0
                        for it in range(0, len(reservadas)):
                            if identificador == reservadas[it]:
                                tipoS = tipoR[it]
                            it= it+1 
                        print("Reservada Tipo "+ tipoS + ":", identificador)
                    else:
                        print("Identificador Tipo 0: ", identificador)
                        real=""
                        identificador=""
                        numero=""
                        print("opSuma Tipo 5: ", caracter)
                else:
                    print("opSuma Tipo 5: ", caracter)
            
            elif (caracter == '*') or (caracter == '/'):
                if(len(numero)!=0):
                    print("Entero Tipo 1: ", numero)
                    real=""
                    identificador=""
                    numero=""
                    print("opMul Tipo 6: ", caracter)
                elif(len(real)!=0):
                    print("Real Tipo 2: ", real)
                    real=""
                    identificador=""
                    numero=""
                    print("opMul Tipo 6: ", caracter)
                elif(len(identificador)!=0):
                    if(identificador in tipo):
                        print("TipoDato Tipo 4: ", identificador)
                        print("opMul Tipo 6: ", caracter)
                        identificador=""

                    elif (identificador in reservadas):
                        it = 0
                        for it in range(0, len(reservadas)):
                            if identificador == reservadas[it]:
                                tipoS = tipoR[it]
                            it= it+1 
                        print("Reservada Tipo "+ tipoS + ":", identificador)
                    else:
                        print("Identificador Tipo 0: ", identificador)
                        real=""
                        identificador=""
                        numero=""
                        print("opMul Tipo 6: ", caracter)
                else:
                    print("opMul Tipo 6: ", caracter)

            elif (caracter == '<') or (caracter == '>') or (caracter == '!'):
                if(len(numero)!=0):
                    print("Entero Tipo 1: ", numero)
                    real=""
                    identificador=""
                    numero=""
                elif(len(real)!=0):
                    print("Real Tipo 2: ", real)
                    real=""
                    identificador=""
                    numero=""
                elif(len(identificador)!=0):
                    if(identificador in tipo):
                        print("TipoDato Tipo 4: ", identificador)
                        identificador=""

                    elif (identificador in reservadas):
                        it = 0
                        for it in range(0, len(reservadas)):
                            if identificador == reservadas[it]:
                                tipoS = tipoR[it]
                            it= it+1 
                        print("Reservada Tipo "+ tipoS + ":", identificador)
                    else:
                        print("Identificador Tipo 0: ", identificador)
                        real=""
                        identificador=""
                        numero=""
                if (self.cadena[i+1]=="="):
                    cont= 1
                    skip = True
                    relac = caracter + self.cadena[i+1]
                    print("opRelac Tipo 7: ", relac)
                else:
                    print("opRelac Tipo 7: ", caracter)

            elif (caracter == '='):
                if(len(numero)!=0):
                    print("Entero Tipo 1: ", numero)
                    real=""
                    identificador=""
                    numero=""
                elif(len(real)!=0):
                    print("Real Tipo 2: ", real)
                    real=""
                    identificador=""
                    numero=""
                elif(len(identificador)!=0):
                    if(identificador in tipo):
                        print("TipoDato Tipo 4: ", identificador)
                        identificador=""

                    elif (identificador in reservadas):
                        it = 0
                        for it in range(0, len(reservadas)):
                            if identificador == reservadas[it]:
                                tipoS = tipoR[it]
                            it= it+1 
                        print("Reservada Tipo "+ tipoS + ":", identificador)
                    else:
                        print("Identificador Tipo 0: ", identificador)
                        real=""
                        identificador=""
                        numero=""
                if (self.cadena[i+1]=="="):
                    relac = caracter + self.cadena[i+1]
                    print("opRelac Tipo 7: ", relac)
                else:
                    print("opAsignacion Tipo 18: ", caracter)
                
            elif (caracter == '|'):
                if(len(numero)!=0):
                    print("Entero Tipo 1: ", numero)
                    real=""
                    identificador=""
                    numero=""
                elif(len(real)!=0):
                    print("Real Tipo 2: ", real)
                    real=""
                    identificador=""
                    numero=""
                elif(len(identificador)!=0):
                    if(identificador in tipo):
                        print("TipoDato Tipo 4: ", identificador)
                        identificador=""

                    elif (identificador in reservadas):
                        it = 0
                        for it in range(0, len(reservadas)):
                            if identificador == reservadas[it]:
                                tipoS = tipoR[it]
                            it= it+1 
                        print("Reservada Tipo "+ tipoS + ":", identificador)
                    else:
                        print("Identificador Tipo 0: ", identificador)
                        real=""
                        identificador=""
                        numero=""
                if (self.cadena[i+1]=="|"):
                    orV = caracter + self.cadena[i+1]
                    print("opOr Tipo 8: ", orV)
                else:
                    print("OpOr incompleto ")

            elif (caracter == '&'):
                if(len(numero)!=0):
                    print("Entero Tipo 1: ", numero)
                    real=""
                    identificador=""
                    numero=""
                elif(len(real)!=0):
                    print("Real Tipo 2: ", real)
                    real=""
                    identificador=""
                    numero=""
                elif(len(identificador)!=0):
                    if(identificador in tipo):
                        print("TipoDato Tipo 4: ", identificador)
                        identificador=""

                    elif (identificador in reservadas):
                        it = 0
                        for it in range(0, len(reservadas)):
                            if identificador == reservadas[it]:
                                tipoS = tipoR[it]
                            it= it+1 
                        print("Reservada Tipo "+ tipoS + ":", identificador)
                    else:
                        print("Identificador Tipo 0: ", identificador)
                        real=""
                        identificador=""
                        numero=""
                if (self.cadena[i+1]=="&"):
                    andV = caracter + self.cadena[i+1]
                    print("opAnd Tipo 9: ", andV)
                else:
                    print("OpAnd incompleto ")

            elif (caracter == '!'):
                if(len(numero)!=0):
                    print("Entero Tipo 1: ", numero)
                    real=""
                    identificador=""
                    numero=""
                    print("opNot Tipo 10: ", caracter)
                elif(len(real)!=0):
                    print("Real Tipo 2: ", real)
                    real=""
                    identificador=""
                    numero=""
                    print("opNot Tipo 10: ", caracter)
                elif(len(identificador)!=0):
                    if(identificador in tipo):
                        print("TipoDato Tipo 4: ", identificador)
                        print("opNot Tipo 10: ", caracter)
                        identificador=""
                    elif (identificador in reservadas):
                        it = 0
                        for it in range(0, len(reservadas)):
                            if identificador == reservadas[it]:
                                tipoS = tipoR[it]
                            it= it+1 
                        print("Reservada Tipo "+ tipoS + ":", identificador)
                    else:
                        print("Identificador Tipo 0: ", identificador)
                        real=""
                        identificador=""
                        numero=""
                        print("opNot Tipo 10: ", caracter)
                else:
                    print("opNot Tipo 10: ", caracter)

            elif (caracter in simbolos):
                it = 0
                for it in range(0, len(simbolos)):
                    if caracter == simbolos[it]:
                        tipoS = tipoA[it]
                    it= it+1

                if(len(numero)!=0):
                    print("Entero Tipo 1: ", numero)
                    real=""
                    identificador=""
                    numero=""
                elif(len(real)!=0):
                    print("Real Tipo 2: ", real)
                    real=""
                    identificador=""
                    numero=""
                elif(len(identificador)!=0):
                    if(identificador in tipo):
                        print("TipoDato Tipo 4: ", identificador)
                        identificador=""

                    elif (identificador in reservadas):
                        it = 0
                        for it in range(0, len(reservadas)):
                            if identificador == reservadas[it]:
                                tipoS = tipoR[it]
                            it= it+1 
                        print("Reservada Tipo "+ tipoS + ":", identificador)
                        
                    else:
                        print("Identificador Tipo 0: ", identificador)
                        real=""
                        identificador=""
                        numero=""
                print("Simbolo Tipo "+ tipoS + ":", caracter)
             
            
            i=i+1

                    

        if(len(real)!=0):
            print("Real", real)
            real=""
            identificador=""
            numero=""
        elif(len(numero)!=0):
            print("Entero", numero)
            real=""
            identificador=""
            numero=""
        elif(len(identificador)!=0):
            if(identificador in tipo):
                print("Tipo: ", identificador)
                identificador=""

            elif (identificador in reservadas):
                        it = 0
                        for it in range(0, len(reservadas)):
                            if identificador == reservadas[it]:
                                tipoS = tipoR[it]
                            it= it+1 
                        print("Reservada Tipo "+ tipoS + ":", identificador)
            else:
                print("Identificador", identificador)
                real=""
                identificador=""
                numero=""
            

print("Ingresa una cadena")
cadena = input()
miniLexico(cadena).analizar()

