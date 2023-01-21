class miniLexico:
    def __init__(self, cadena):
        self.cadena = cadena + '$'

    def analizar(self):
        identificador = ""
        numero = ""
        real = ""
        entero = ""
        for caracter in self.cadena:
            asCarac = ord(caracter)
            if (caracter == '$'):
                break
            elif (asCarac > 64 and asCarac < 91) or (asCarac>96 and asCarac<123): #Comprobamos si el caracter es una letra
                if(len(real)!=0):
                    print("REAL", real)
                    real=""
                    identificador=""
                    numero=""
                    identificador += caracter
                elif(len(numero)!=0):
                    print("numero", numero)
                    real=""
                    identificador=""
                    numero=""
                    identificador += caracter
                else:
                    identificador += caracter

            elif (asCarac > 47 and asCarac < 58):
                if(len(identificador)!=0):
                    identificador += caracter
                    print("identificador", identificador)
                    real=""
                    identificador=""
                    numero=""
                #if(len(real)!=0):
                    #real += caracter
                #elif(len(identificador)!=0):
                    #identificador += caracter
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
                    print("IDENTIFICADOR", identificador)
                    real=""
                    identificador=""
                    numero=""

        if(len(real)!=0):
            print("REAL", real)
            real=""
            identificador=""
            numero=""
        elif(len(numero)!=0):
            print("numero", numero)
            real=""
            identificador=""
            numero=""
        elif(len(identificador)!=0):
            print("identificador", identificador)
            real=""
            identificador=""
            numero=""
            

print("Ingresa una cadena")
cadena = input()
miniLexico(cadena).analizar()
