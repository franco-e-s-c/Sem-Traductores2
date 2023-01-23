class miniLexico:
    def __init__(self, cadena):
        self.cadena = cadena + '$'

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
                    print("Real: ", real)
                    real=""
                    identificador=""
                    numero=""
                    identificador += caracter
                elif(len(numero)!=0):
                    print("Entero: ", numero)
                    real=""
                    identificador=""
                    numero=""
                    identificador += caracter
                elif(len(cadenaS)!=0):
                    print("Cadena: ", cadenaS)
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
                        print("Tipo: ", identificador)
                        identificador=""
                    #print("identificador", identificador)
                    #real=""
                    #identificador=""
                    #numero=""
                #if(len(real)!=0):
                    #real += caracter
                #elif(len(identificador)!=0):
                    #identificador += caracter
                elif(len(cadenaS)!=0):
                    print("Cadena: ", cadenaS)
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
                        print("Tipo: ", identificador)
                        identificador=""
                    else:
                        print("Identificador: ", identificador)
                        real=""
                        identificador=""
                        numero=""
                elif(len(real)!=0):
                    print("Real: ", real)
                    real=""
                    identificador=""
                    numero=""
                elif(len(numero)!=0):
                    print("Entero: ", numero)
                    real=""
                    identificador=""
                    numero=""
                elif(len(cadenaS)!=0):
                    print("Cadena: ", cadenaS)
                    real=""
                    identificador=""
                    numero=""
                    cadenaS=""
                    
            
            elif (caracter =="'") or (caracter == '"'):
                c=i+1
                cont = 0
                if(len(identificador)!=0):
                    if(identificador in tipo):
                        print("Tipo: ", identificador)
                        identificador=""
                    else:
                        print("Identificador: ", identificador)
                        real=""
                        identificador=""
                        numero=""
                elif(len(real)!=0):
                    print("Real: ", real)
                    real=""
                    identificador=""
                    numero=""
                elif(len(numero)!=0):
                    print("Entero: ", numero)
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
                        print("Cadena: ", cadenaS)
                        real=""
                        identificador=""
                        numero=""
                        cadenaS=""
                        break
                    cadenaS=cadenaS + self.cadena[cadenaCar]




            elif (caracter == '+') or (caracter == '-'):
                if(len(numero)!=0):
                    print("Entero: ", numero)
                    real=""
                    identificador=""
                    numero=""
                    print("opSuma: ", caracter)
                elif(len(real)!=0):
                    print("Real: ", real)
                    real=""
                    identificador=""
                    numero=""
                    print("opSuma: ", caracter)
                elif(len(identificador)!=0):
                    if(identificador in tipo):
                        print("Tipo: ", identificador)
                        identificador=""
                    else:
                        print("Identificador: ", identificador)
                        real=""
                        identificador=""
                        numero=""
                        print("opSuma: ", caracter)
                else:
                    print("opSuma: ", caracter)
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
            else:
                print("Identificador", identificador)
                real=""
                identificador=""
                numero=""
            

print("Ingresa una cadena")
cadena = input()
miniLexico(cadena).analizar()
