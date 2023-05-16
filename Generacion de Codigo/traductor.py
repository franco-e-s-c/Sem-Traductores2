import re
RefList = list()
globals()['contexto']=''
globals()['primera']=0
class traductor():
    def __init__(self):

        self.lineas = list()
        self.pos = 4
        self.star = 0
        self.lineas2 = list()
        self.paramC = 0
    def TP10(self, bandera, code):
        self.bandera = bandera
        self.code = code


        if self.bandera == 6:
            self.lineas.append(str(self.code)+': db 0')

        if self.bandera == 10 or self.bandera == 12:
            if globals()['primera']==0:
                self.lineas.append('section .text \n')
                self.lineas.append('global '+str(self.code))
                self.lineas.append('\n'+str(self.code)+':' + '\n \t'  +'PUSH rbp \n\t' + 'MOV rbp, rsp \n\t' 'SUB rsp, 48 \n\t')
                globals()['primera']=1
            else:
                patron = re.compile("[global]+")
                for indice in range(len(self.lineas)):
                    if patron.match(self.lineas[indice]) != None:

                        self.lineas[indice] = self.lineas[indice] + ', ' + str(self.code) 
                        break
                        
                    else:
                        pass
                self.lineas.append('\n'+str(self.code)+':' + '\n \t'  +'PUSH rbp \n\t' + 'MOV rbp, rsp \n\t' 'SUB rsp, 48 \n\t')
            globals()['contexto']= self.code   
    def TSen21(self, bandera, valor, var):
        self.bandera = bandera
        self.valor = valor
        self.var = var
        bandera = 0
        posicionaux =0
        #numeros
        if self.bandera == 21:

            for obj in RefList:
                if self.var == obj.var and obj.contexto == globals()['contexto']:
                    bandera = 1
                    posicionaux = obj.pos
                    break
                else:
                    bandera = 0
            if bandera ==1:
                self.lineas.append('\tMOV WORD [rbp -' + str(posicionaux)+'] , '+str(self.valor)+'\n')
            elif bandera == 0:
                self.lineas.append('\tMOV WORD [rbp -' + str(self.pos)+'] , '+str(self.valor)+'\n')
                RefList.append(referencia(self.var, globals()['contexto'], self.pos))
                self.pos +=4
        #id de parametro
        if self.bandera == 22:

            for obj in RefList:
                if obj.var == self.valor:

                    self.lineas.append('\tMOV rax, QWORD [rbp -' + str(obj.pos)+']\n')
                    break
            self.lineas.append('\tMOV QWORD [rbp -' + str(self.pos)+'] , rax \n\t')
            RefList.append(referencia(self.var, globals()['contexto'], self.pos))

        #id
        if self.bandera == 23:

            self.lineas.append('\tMOV WORD [rbp -' + str(self.pos)+'] , '+str(self.valor))
            RefList.append(referencia(self.var, globals()['contexto'], self.pos))
            self.pos +=4
    def TConI(self, operacion, variables, banderaelse):
        self.operacion = operacion
        self.variables = variables
        self.encontrado = list()
        for obj in self.variables:
            for obj2 in RefList:
                if obj.fuente == obj2.var:
                    self.encontrado.append(obj2)
                    break
        vuelta = 0
        for obj in self.encontrado:
            if vuelta == 0:
                self.lineas.insert(-2,'\tMOV ax, WORD[rbp -'+str(obj.pos) +']')
                vuelta+=1
            else:
                self.lineas.insert(-2,'\n\tMOV bx, WORD[rbp -'+str(obj.pos) +']')
                self.lineas.insert(-2,'\n\tCMP ax, bx')
                break
        if self.operacion.fuente == '>':
            self.lineas.insert(-2,'\n\tjg if\n')
        elif self.operacion.fuente == '<':
            self.lineas.insert(-2,'\n\tjl if\n')
        elif self.operacion.fuente == '==':
            self.lineas.insert(-2,'\n\tjn if\n')
            
        #self.codigo.append('\nif:\n\t')
        auxiliar= self.lineas.pop(-2)
        self.lineas.insert(-1, auxiliar)
        self.lineas2.append('\nif:\n')
        aux = self.lineas.pop()
        self.lineas2.append(aux)
        self.lineas2.append('\tjmp regreso')
        self.lineas.append('regreso:\n\t')
        
    def TOp2(self, bandera, variables, contexto, num):
        self.bandera = bandera
        self.variables = variables
        self.contexto = contexto
        self.partederecha = num
        i =0
        contador = 0
        vuelta = 0
        bandera = 0
        banderarealizada = 0
        cad = 'MOV rax, '
        cad2 = 'MOV rdi, '
        banderadigito =0
        while contador < self.partederecha:
            for obj in self.variables:
                
                for obj2 in RefList:
                    if obj.fuente == obj2.var and obj.contexto == obj2.contexto and obj.contexto == globals()['contexto'] or obj.fuente.isdigit() and banderadigito==0:
                        if vuelta == 0:
                            if bandera ==0:
                                if obj.fuente.isdigit():
                                    cad = cad + ''+obj.fuente
                                    banderadigito=1
                                else:
                                    cad = cad + 'QWORD [rbp -'+ str(obj2.pos)+']'
                                self.lineas.append('\t' + cad +'\n')
                            else:
                                if obj.fuente.isdigit():
                                    cad2 = cad2 + ''+obj.fuente
                                else:
                                    cad2 = cad2 + 'QWORD [rbp -'+ str(obj2.pos)+']'
                                self.lineas.append('\t' + cad2+'\n')
                            i = 0
                            vuelta += 1
                            contador +=1
                            
                        else:
                            if bandera ==0:
                                if obj.fuente.isdigit():
                                    cad2 = cad2 + ''+obj.fuente
                                    
                                    
                                else:
                                    cad2 = cad2 + 'QWORD [rbp -'+ str(obj2.pos)+']'
                                self.lineas.append('\t' + cad2+'\n')
                                vuelta += 1
                            else:
                                if self.bandera[0]=='+':
                                    self.lineas.append('\t'+'ADD rax, rdi'+'\n')
                                elif self.bandera[0]=='*':
                                    self.lineas.append('\t'+'MUL rax, rdi'+'\n')
                                elif self.bandera[0]=='-':
                                    self.lineas.append('\t'+'SUB rax, rdi'+'\n')
                                self.bandera.pop(0)
                                #self.codigo.append('\t'+'ADD rax, rdi'+'\n')
                                banderarealizada= 1
                                vuelta -= 1
                                cad = 'MOV rax, '
                                cad2 = 'MOV rdi, '
                                cad2 = cad2 + 'QWORD [rbp -'+ str(obj2.pos)+']'
                                self.lineas.append('\t' + cad2+'\n')

                            #vuelta =0
                            
                                
                            i = 0
                            
                            contador +=1

                        if (vuelta ==2 or contador >= self.partederecha):
                            try:
                                if self.bandera[0]=='+':
                                    self.lineas.append('\t'+'ADD rax, rdi'+'\n')
                                elif self.bandera[0]=='*':
                                    self.lineas.append('\t'+'MUL rax, rdi'+'\n')
                                elif self.bandera[0]=='-':
                                    self.lineas.append('\t'+'SUB rax, rdi'+'\n')
                                self.bandera.pop(0)
                            except:
                                pass
                            
                            vuelta = 0
                            bandera = 1
                            cad = 'MOV rax, '
                            cad2 = 'MOV rdi, '
                            break
                    else:
                        i+1
                        banderadigito=0

        

    def TOp(self, bandera, var1, variables, contexto, num):
        self.bandera = bandera
        self.var1 = var1
        self.variables = variables
        self.contexto = contexto
        self.partederecha = num
        i =0
        contador = 0
        vuelta = 0
        bandera = 0
        banderarealizada = 0
        cad = 'MOV rax, '
        cad2 = 'MOV rdi, '
        banderadigito =0
        while contador < self.partederecha:
            for obj in self.variables:
                
                for obj2 in RefList:
                    if obj.fuente == obj2.var and obj.contexto == obj2.contexto and obj.contexto == globals()['contexto'] or obj.fuente.isdigit() and banderadigito==0:
                        if vuelta == 0:
                            if bandera ==0:
                                if obj.fuente.isdigit():
                                    cad = cad + ''+obj.fuente
                                    banderadigito=1
                                else:
                                    cad = cad + 'QWORD [rbp -'+ str(obj2.pos)+']'
                                self.lineas.append('\t' + cad +'\n')
                            else:
                                if obj.fuente.isdigit():
                                    cad2 = cad2 + ''+obj.fuente
                                else:
                                    cad2 = cad2 + 'QWORD [rbp -'+ str(obj2.pos)+']'
                                self.lineas.append('\t' + cad2+'\n')
                            i = 0
                            vuelta += 1
                            contador +=1
                            
                        else:
                            if bandera ==0:
                                if obj.fuente.isdigit():
                                    cad2 = cad2 + ''+obj.fuente
                                    
                                    
                                else:
                                    cad2 = cad2 + 'QWORD [rbp -'+ str(obj2.pos)+']'
                                self.lineas.append('\t' + cad2+'\n')
                                vuelta += 1
                            else:
                                if self.bandera[0]=='+':
                                    self.lineas.append('\t'+'ADD rax, rdi'+'\n')
                                elif self.bandera[0]=='*':
                                    self.lineas.append('\t'+'MUL rax, rdi'+'\n')
                                elif self.bandera[0]=='-':
                                    self.lineas.append('\t'+'SUB rax, rdi'+'\n')
                                self.bandera.pop(0)
                                #self.codigo.append('\t'+'ADD rax, rdi'+'\n')
                                banderarealizada= 1
                                vuelta -= 1
                                cad = 'MOV rax, '
                                cad2 = 'MOV rdi, '
                                cad2 = cad2 + 'QWORD [rbp -'+ str(obj2.pos)+']'
                                self.lineas.append('\t' + cad2+'\n')

                            #vuelta =0
                            
                                
                            i = 0
                            
                            contador +=1

                        if (vuelta ==2 or contador >= self.partederecha):
                            try:
                                if self.bandera[0]=='+':
                                    self.lineas.append('\t'+'ADD rax, rdi'+'\n')
                                elif self.bandera[0]=='*':
                                    self.lineas.append('\t'+'MUL rax, rdi'+'\n')
                                elif self.bandera[0]=='-':
                                    self.lineas.append('\t'+'SUB rax, rdi'+'\n')
                                self.bandera.pop(0)
                            except:
                                pass
                            
                            vuelta = 0
                            bandera = 1
                            cad = 'MOV rax, '
                            cad2 = 'MOV rdi, '
                            break
                    else:
                        i+1
                        banderadigito=0

        for obj in RefList:
            if self.var1 == obj.var and self.contexto == obj.contexto:
                self.lineas.append('\t''MOV QWORD [rbp -'+ str(obj.pos)+'], ' + 'rax\n')

    def Tparam(self, cantidad, nombre):
        self.cantidad = cantidad
        self.nombre = nombre
        i =0
        if self.star == 0:
            self.star = self.pos +20
        else:
            self.star = self.star
        while i < cantidad:
            if self.paramC==0:
                self.lineas.append('MOV QWORD [rbp -' +str(self.star)+'], rdi \n')
            elif self.paramC==1:    
                self.lineas.append('MOV QWORD [rbp -' +str(self.star)+'], rsi \n')
            RefList.append(referencia(self.nombre, globals()['contexto'], self.star))
            i+=1
            self.star+=4
        self.paramC+=1


    def TDefFunc(self):
        if globals()['contexto']=='main':
            self.lineas.append('\n\t' 'ADD rsp, 48 \n\t'+ 'MOV rsp, rbp \n\t' +'MOV rax, 60 \n\t'+'MOV rdi, 0 \n\t' + 'syscall \n\t')
        else:
            self.lineas.append('\n\t' 'ADD rsp, 48 \n\t'+ 'MOV rsp, rbp \n\t' +'POP rbp \n\t' + 'ret \n\t')
        self.pos = 4
        self.star = 0
        for obj in self.lineas2:
            self.lineas.append(obj)
    def TRet(self, cad, contexto):
        self.fuente = cad
        self.contexto = contexto
        for obj in RefList:
            if self.fuente == obj.var and self.contexto == obj.contexto:
                self.lineas.append('MOV rax, QWORD [rbp -'+ str(obj.pos)+']\n')

    def TLlamFunc(self, enviados, llamado, nombre):
        self.enviados = enviados
        self.llamado = llamado
        self.nombre = nombre
        vuelta = 0
        for obj in RefList:
            for obj2 in self.enviados:
                if obj2.fuente == obj.var and globals()['contexto'] == obj.contexto:
                    if vuelta == 0:
                        self.lineas.append('\t''MOV rax, QWORD [rbp -'+ str(obj.pos)+']\n')
                        self.lineas.append('\t''MOV rdi, rax \n')
                        vuelta+=1
                    elif vuelta == 1:
                        self.lineas.append('\t''MOV rax, QWORD [rbp -'+ str(obj.pos)+']\n')
                        self.lineas.append('\t''MOV rsi, rax')
        self.lineas.append('\n\t''call '+ str(nombre))
        for obj in RefList:
            if self.llamado == obj.var and globals()['contexto'] == obj.contexto:
                self.lineas.append('\n\t''MOV QWORD [rbp -'+ str(obj.pos)+'], rax\n\t')
    def TLlamFunc2(self, enviados, llamado, nombre):
        self.enviados = enviados
        self.llamado = llamado
        self.nombre = nombre
        vuelta = 0
        for obj in self.enviados:
            self.lineas.append('\t''MOV ax,' +str(obj.fuente)+ '\n')
            if vuelta == 0:
                
                self.lineas.append('\t''MOV rdi, rax')
                vuelta+=1
            elif vuelta ==1:
                self.lineas.append('\t''MOV rsi, rax')
        
        self.lineas.append('\n\t''call '+ str(nombre))
        for obj in RefList:
            if self.llamado == obj.var and globals()['contexto'] == obj.contexto:
                self.lineas.append('\n\t''MOV QWORD [rbp -'+ str(obj.pos)+'], rax\n\t')
    
    def Tprint(self, valor):
        for obj in RefList:
            if obj.var == valor.fuente and globals()['contexto'] == obj.contexto:
                self.lineas.insert(0, 'section .data  \n\tprimr: db  "Resultado := %lf",10,0 \nsection .bss \n\tresp: resq 2\n')
                self.lineas.insert(2, '\nextern printf\n')
                self.lineas.append('\n\tPUSH qword[rbp -'+str(obj.pos)+']')
                self.lineas.append('\n\tFILD dword[rsp]')
                self.lineas.append('\n\tFSTP qword[rel resp]')
                self.lineas.append('\n\tADD rsp, 8')
                self.lineas.append('\n\tMOVSD xmm0,qword[rel resp]')
                self.lineas.append('\n\tMOV rdi, primr')
                self.lineas.append('\n\tMOV al, 1')
                self.lineas.append('\n\tcall printf WRT ..plt \n\t')
    def ensamblador(self):
        print('****************Traduccion a Codigo ASM****************')
        for obj in self.lineas:
            print(obj)
        Archivo=open("ensamblador.asm","w")
        for i in range(len(self.lineas)):
            Archivo.write(self.lineas[i])   
        del self.lineas[:]
        Archivo.close()

class referencia():
    def __init__(self, var, contexto, pos):
        self.var = var
        self.contexto = contexto
        self.pos = pos
