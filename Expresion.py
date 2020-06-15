from Tipo import *
from CError import CError
from tkinter import *
import sys

class primitivo:
    def __init__(self,t,v,c,l,n):
        self.columna=c
        self.linea=l
        self.vNodo=nodoAST(v,n)
        self.valor=v
        self.tipo=t
    def getvalor(self,entorno,estat):
        return self

class id_:
    def __init__(self,d,c,l,n):
        self.columna=c
        self.linea=l
        self.vNodo=nodoAST(d,n)
        self.variable=d
        self.tipo=tipoPrimitivo.variable
    def getvalor(self,entorno,estat):
        temp=entorno.buscar(self.variable,self.columna,self.linea,estat)
        if temp!=None:
            return temp.valor.getvalor(entorno,estat)
        else:
            return primitivo(tipoPrimitivo.Error,'@error@',self.columna,self.linea,0)


class newSuma:
    def __init__(self,izq,der,c,l,n):
        self.columna=c
        self.linea=l
        self.vNodo=nodoAST('+',n)
        self.vNodo.hijos.append(izq.vNodo)
        self.vNodo.hijos.append(der.vNodo)
        self.hijoIzq=izq
        self.hijoDer=der
    def getvalor(self,entorno,estat):
        izq=self.hijoIzq.getvalor(entorno,estat)
        der=self.hijoDer.getvalor(entorno,estat)
        if izq.tipo==tipoPrimitivo.Entero:
            if der.tipo==tipoPrimitivo.Entero:
                return primitivo(tipoPrimitivo.Entero,int(izq.valor)+int(der.valor),self.columna,self.linea,0)
            elif der.tipo==tipoPrimitivo.Doble:
                return primitivo(tipoPrimitivo.Doble,float(int(izq.valor)+float(der.valor)),self.columna,self.linea,0)
        elif izq.tipo==tipoPrimitivo.Doble:
            if der.tipo==tipoPrimitivo.Entero:
                return primitivo(tipoPrimitivo.Doble,float(float(izq.valor)+int(der.valor)),self.columna,self.linea,0)
            elif der.tipo==tipoPrimitivo.Doble:
                return primitivo(tipoPrimitivo.Doble,float(float(izq.valor)+float(der.valor)),self.columna,self.linea,0)
        elif izq.tipo==tipoPrimitivo.Cadena:
            if der.tipo==tipoPrimitivo.Cadena:
                return primitivo(tipoPrimitivo.Cadena,str(izq.valor)+str(der.valor),self.columna,self.linea,0)
        
        estat.Lerrores.append(CError('Semantico','Error al realizar la SUMA',self.columna,self.linea))
        return primitivo(tipoPrimitivo.Error,'@error@',self.columna,self.linea,0)

class newResta:
    def __init__(self,izq,der,c,l,n):
        self.columna=c
        self.linea=l
        self.vNodo=nodoAST('-',n)
        self.vNodo.hijos.append(izq.vNodo)
        self.vNodo.hijos.append(der.vNodo)
        self.hijoIzq=izq
        self.hijoDer=der
    def getvalor(self,entorno,estat):
        izq=self.hijoIzq.getvalor(entorno,estat)
        der=self.hijoDer.getvalor(entorno,estat)
        if izq.tipo==tipoPrimitivo.Entero:
            if der.tipo==tipoPrimitivo.Entero:
                return primitivo(tipoPrimitivo.Entero,int(izq.valor)-int(der.valor),self.columna,self.linea,0)
            elif der.tipo==tipoPrimitivo.Doble:
                return primitivo(tipoPrimitivo.Doble,float(int(izq.valor)-float(der.valor)),self.columna,self.linea,0)
        elif izq.tipo==tipoPrimitivo.Doble:
            if der.tipo==tipoPrimitivo.Entero:
                return primitivo(tipoPrimitivo.Doble,float(float(izq.valor)-int(der.valor)),self.columna,self.linea,0)
            elif der.tipo==tipoPrimitivo.Doble:
                return primitivo(tipoPrimitivo.Doble,float(float(izq.valor)-float(der.valor)),self.columna,self.linea,0)
        
        estat.Lerrores.append(CError('Semantico','Error al realizar la RESTA',self.columna,self.linea))
        return primitivo(tipoPrimitivo.Error,'@error@',self.columna,self.linea,0)

class newMultiplicacion:
    def __init__(self,izq,der,c,l,n):
        self.columna=c
        self.linea=l
        self.vNodo=nodoAST('*',n)
        self.vNodo.hijos.append(izq.vNodo)
        self.vNodo.hijos.append(der.vNodo)
        self.hijoIzq=izq
        self.hijoDer=der
    def getvalor(self,entorno,estat):
        izq=self.hijoIzq.getvalor(entorno,estat)
        der=self.hijoDer.getvalor(entorno,estat)
        if izq.tipo==tipoPrimitivo.Entero:
            if der.tipo==tipoPrimitivo.Entero:
                return primitivo(tipoPrimitivo.Entero,int(izq.valor)*int(der.valor),self.columna,self.linea,0)
            elif der.tipo==tipoPrimitivo.Doble:
                return primitivo(tipoPrimitivo.Doble,float(int(izq.valor)*float(der.valor)),self.columna,self.linea,0)
        elif izq.tipo==tipoPrimitivo.Doble:
            if der.tipo==tipoPrimitivo.Entero:
                return primitivo(tipoPrimitivo.Doble,float(float(izq.valor)*int(der.valor)),self.columna,self.linea,0)
            elif der.tipo==tipoPrimitivo.Doble:
                return primitivo(tipoPrimitivo.Doble,float(float(izq.valor)*float(der.valor)),self.columna,self.linea,0)
        
        estat.Lerrores.append(CError('Semantico','Error al realizar la MULTIPLICACION',self.columna,self.linea))
        return primitivo(tipoPrimitivo.Error,'@error@',self.columna,self.linea,0)

class newDivision:
    def __init__(self,izq,der,c,l,n):
        self.columna=c
        self.linea=l
        self.vNodo=nodoAST('/',n)
        self.vNodo.hijos.append(izq.vNodo)
        self.vNodo.hijos.append(der.vNodo)
        self.hijoIzq=izq
        self.hijoDer=der
    def getvalor(self,entorno,estat):
        izq=self.hijoIzq.getvalor(entorno,estat)
        der=self.hijoDer.getvalor(entorno,estat)
        if izq.tipo==tipoPrimitivo.Entero:
            if der.tipo==tipoPrimitivo.Entero:
                if float(der.valor)==0:
                    estat.Lerrores.append(CError('Semantico','No se puede dividir dentro de 0',self.columna,self.linea))
                    return primitivo(tipoPrimitivo.Error,'@error@',self.columna,self.linea,0)

                return primitivo(tipoPrimitivo.Doble,float(int(izq.valor)/int(der.valor)),self.columna,self.linea,0)
            elif der.tipo==tipoPrimitivo.Doble:
                if float(der.valor)==0:
                    estat.Lerrores.append(CError('Semantico','No se puede dividir dentro de 0',self.columna,self.linea))
                    return primitivo(tipoPrimitivo.Error,'@error@',self.columna,self.linea,0)

                return primitivo(tipoPrimitivo.Doble,float(int(izq.valor)/float(der.valor)),self.columna,self.linea,0)
        elif izq.tipo==tipoPrimitivo.Doble:
            if der.tipo==tipoPrimitivo.Entero:
                if float(der.valor)==0:
                    estat.Lerrores.append(CError('Semantico','No se puede dividir dentro de 0',self.columna,self.linea))
                    return primitivo(tipoPrimitivo.Error,'@error@',self.columna,self.linea,0)

                return primitivo(tipoPrimitivo.Doble,float(float(izq.valor)/int(der.valor)),self.columna,self.linea,0)
            elif der.tipo==tipoPrimitivo.Doble:
                if float(der.valor)==0:
                    estat.Lerrores.append(CError('Semantico','No se puede dividir dentro de 0',self.columna,self.linea))
                    return primitivo(tipoPrimitivo.Error,'@error@',self.columna,self.linea,0)

                return primitivo(tipoPrimitivo.Doble,float(float(izq.valor)/float(der.valor)),self.columna,self.linea,0)
        
        estat.Lerrores.append(CError('Semantico','Error al realizar la DIVISION',self.columna,self.linea))
        return primitivo(tipoPrimitivo.Error,'@error@',self.columna,self.linea,0)

class newModulo:
    def __init__(self,izq,der,c,l,n):
        self.columna=c
        self.linea=l
        self.vNodo=nodoAST('/',n)
        self.vNodo.hijos.append(izq.vNodo)
        self.vNodo.hijos.append(der.vNodo)
        self.hijoIzq=izq
        self.hijoDer=der
    def getvalor(self,entorno,estat):
        izq=self.hijoIzq.getvalor(entorno,estat)
        der=self.hijoDer.getvalor(entorno,estat)
        if izq.tipo==tipoPrimitivo.Entero:
            if der.tipo==tipoPrimitivo.Entero:
                if float(der.valor)==0:
                    estat.Lerrores.append(CError('Semantico','No se puede dividir dentro de 0',self.columna,self.linea))
                    return primitivo(tipoPrimitivo.Error,'@error@',self.columna,self.linea,0)

                return primitivo(tipoPrimitivo.Doble,float(int(izq.valor)%int(der.valor)),self.columna,self.linea,0)
            elif der.tipo==tipoPrimitivo.Doble:
                if float(der.valor)==0:
                    estat.Lerrores.append(CError('Semantico','No se puede dividir dentro de 0',self.columna,self.linea))
                    return primitivo(tipoPrimitivo.Error,'@error@',self.columna,self.linea,0)

                return primitivo(tipoPrimitivo.Doble,float(int(izq.valor)%float(der.valor)),self.columna,self.linea,0)
        elif izq.tipo==tipoPrimitivo.Doble:
            if der.tipo==tipoPrimitivo.Entero:
                if float(der.valor)==0:
                    estat.Lerrores.append(CError('Semantico','No se puede dividir dentro de 0',self.columna,self.linea))
                    return primitivo(tipoPrimitivo.Error,'@error@',self.columna,self.linea,0)

                return primitivo(tipoPrimitivo.Doble,float(float(izq.valor)%int(der.valor)),self.columna,self.linea,0)
            elif der.tipo==tipoPrimitivo.Doble:
                if float(der.valor)==0:
                    estat.Lerrores.append(CError('Semantico','No se puede dividir dentro de 0',self.columna,self.linea))
                    return primitivo(tipoPrimitivo.Error,'@error@',self.columna,self.linea,0)

                return primitivo(tipoPrimitivo.Doble,float(float(izq.valor)%float(der.valor)),self.columna,self.linea,0)
        
        estat.Lerrores.append(CError('Semantico','Error al realizar MODULO',self.columna,self.linea))
        return primitivo(tipoPrimitivo.Error,'@error@',self.columna,self.linea,0)


class newAnd:
    def __init__(self,izq,der,c,l,n):
        self.columna=c
        self.linea=l
        self.vNodo=nodoAST('&&',n)
        self.vNodo.hijos.append(izq.vNodo)
        self.vNodo.hijos.append(der.vNodo)
        self.hijoIzq=izq
        self.hijoDer=der
    def getvalor(self,entorno,estat):
        izq=self.hijoIzq.getvalor(entorno,estat)
        der=self.hijoDer.getvalor(entorno,estat)
        if izq.tipo==tipoPrimitivo.Entero:
            if der.tipo==tipoPrimitivo.Entero:
                if(int(izq.valor)!=0):
                    izq=1
                else:
                    izq=0
                if(int(der.valor)!=0):
                    der=1
                else:
                    der=0
                return primitivo(tipoPrimitivo.Entero,izq and der,self.columna,self.linea,0)
        
        estat.Lerrores.append(CError('Semantico','Error al realizar And',self.columna,self.linea))
        return primitivo(tipoPrimitivo.Error,'@error@',self.columna,self.linea,0)

class newOr:
    def __init__(self,izq,der,c,l,n):
        self.columna=c
        self.linea=l
        self.vNodo=nodoAST('||',n)
        self.vNodo.hijos.append(izq.vNodo)
        self.vNodo.hijos.append(der.vNodo)
        self.hijoIzq=izq
        self.hijoDer=der
    def getvalor(self,entorno,estat):
        izq=self.hijoIzq.getvalor(entorno,estat)
        der=self.hijoDer.getvalor(entorno,estat)
        if izq.tipo==tipoPrimitivo.Entero:
            if der.tipo==tipoPrimitivo.Entero:
                if(int(izq.valor)!=0):
                    izq=1
                else:
                    izq=0
                if(int(der.valor)!=0):
                    der=1
                else:
                    der=0
                return primitivo(tipoPrimitivo.Entero,izq or der,self.columna,self.linea,0)
        
        estat.Lerrores.append(CError('Semantico','Error al realizar Or',self.columna,self.linea))
        return primitivo(tipoPrimitivo.Error,'@error@',self.columna,self.linea,0)

class newXor:
    def __init__(self,izq,der,c,l,n):
        self.columna=c
        self.linea=l
        self.vNodo=nodoAST('Xor',n)
        self.vNodo.hijos.append(izq.vNodo)
        self.vNodo.hijos.append(der.vNodo)
        self.hijoIzq=izq
        self.hijoDer=der
    def getvalor(self,entorno,estat):
        izq=self.hijoIzq.getvalor(entorno,estat)
        der=self.hijoDer.getvalor(entorno,estat)
        if izq.tipo==tipoPrimitivo.Entero:
            if der.tipo==tipoPrimitivo.Entero:
                if(int(izq.valor)!=0):
                    izq=1
                else:
                    izq=0
                if(int(der.valor)!=0):
                    der=1
                else:
                    der=0
                return primitivo(tipoPrimitivo.Entero,izq ^ der,self.columna,self.linea,0)
        
        estat.Lerrores.append(CError('Semantico','Error al realizar Xor',self.columna,self.linea))
        return primitivo(tipoPrimitivo.Error,'@error@',self.columna,self.linea,0)

class newNot:
    def __init__(self,der,c,l,n):
        self.columna=c
        self.linea=l
        self.vNodo=nodoAST('Not',n)
        self.vNodo.hijos.append(nodoAST('!',n+1))
        self.vNodo.hijos.append(der.vNodo)
        self.hijoDer=der
    def getvalor(self,entorno,estat):
        der=self.hijoDer.getvalor(entorno,estat)
        if der.tipo==tipoPrimitivo.Entero:
            if(int(der.valor)!=0):
                der=1
            else:
                der=0
            return primitivo(tipoPrimitivo.Entero,int(not der),self.columna,self.linea,0)
        else:
            estat.Lerrores.append(CError('Semantico','Error al realizar Xor',self.columna,self.linea))
            return primitivo(tipoPrimitivo.Error,'@error@',self.columna,self.linea,0)

class newEqual:
    def __init__(self,izq,der,c,l,n):
        self.columna=c
        self.linea=l
        self.vNodo=nodoAST('==',n)
        self.vNodo.hijos.append(izq.vNodo)
        self.vNodo.hijos.append(der.vNodo)
        self.hijoIzq=izq
        self.hijoDer=der
    def getvalor(self,entorno,estat):
        izq=self.hijoIzq.getvalor(entorno,estat)
        der=self.hijoDer.getvalor(entorno,estat)
        if izq.tipo==tipoPrimitivo.Entero:
            if der.tipo==tipoPrimitivo.Entero:
                return primitivo(tipoPrimitivo.Entero,int(int(izq.valor)==int(der.valor)),self.columna,self.linea,0)
            elif der.tipo==tipoPrimitivo.Doble:
                return primitivo(tipoPrimitivo.Entero,int(int(izq.valor)==float(der.valor)),self.columna,self.linea,0)
            elif der.tipo==tipoPrimitivo.Cadena:
                if str(der.valor).lstrip('-').replace('.','',1).isdigit():
                    return primitivo(tipoPrimitivo.Entero,int(float(izq.valor)==float(der.valor)),self.columna,self.linea,0)
                else:
                    return primitivo(tipoPrimitivo.Entero,0,self.columna,self.linea,0)
        elif izq.tipo==tipoPrimitivo.Doble:
            if der.tipo==tipoPrimitivo.Entero:
                return primitivo(tipoPrimitivo.Entero,int(float(izq.valor)==int(der.valor)),self.columna,self.linea,0)
            elif der.tipo==tipoPrimitivo.Doble:
                return primitivo(tipoPrimitivo.Entero,int(float(izq.valor)==float(der.valor)),self.columna,self.linea,0)
            elif der.tipo==tipoPrimitivo.Cadena:
                if str(der.valor).lstrip('-').replace('.','',1).isdigit():
                    return primitivo(tipoPrimitivo.Entero,int(float(izq.valor)==float(der.valor)),self.columna,self.linea,0)
                else:
                    return primitivo(tipoPrimitivo.Entero,0,self.columna,self.linea,0)
        elif izq.tipo==tipoPrimitivo.Cadena:
            if der.tipo==tipoPrimitivo.Cadena:
                return primitivo(tipoPrimitivo.Entero,int(str(izq.valor)==str(der.valor)),self.columna,self.linea,0)
            elif der.tipo==tipoPrimitivo.Entero or der.tipo==tipoPrimitivo.Doble:
                if str(izq.valor).lstrip('-').replace('.','',1).isdigit():
                    return primitivo(tipoPrimitivo.Entero,int(float(izq.valor)==float(der.valor)),self.columna,self.linea,0)
                return primitivo(tipoPrimitivo.Entero,0,self.columna,self.linea,0)

        
        estat.Lerrores.append(CError('Semantico','Error al realizar la Igualacion',self.columna,self.linea))
        return primitivo(tipoPrimitivo.Error,'@error@',self.columna,self.linea,0)

class newNotEqual:
    def __init__(self,izq,der,c,l,n):
        self.columna=c
        self.linea=l
        self.vNodo=nodoAST('!=',n)
        self.vNodo.hijos.append(izq.vNodo)
        self.vNodo.hijos.append(der.vNodo)
        self.hijoIzq=izq
        self.hijoDer=der
    def getvalor(self,entorno,estat):
        izq=self.hijoIzq.getvalor(entorno,estat)
        der=self.hijoDer.getvalor(entorno,estat)
        if izq.tipo==tipoPrimitivo.Entero:
            if der.tipo==tipoPrimitivo.Entero:
                return primitivo(tipoPrimitivo.Entero,int(int(izq.valor)!=int(der.valor)),self.columna,self.linea,0)
            elif der.tipo==tipoPrimitivo.Doble:
                return primitivo(tipoPrimitivo.Entero,int(int(izq.valor)!=float(der.valor)),self.columna,self.linea,0)
            elif der.tipo==tipoPrimitivo.Cadena:
                if str(der.valor).lstrip('-').replace('.','',1).isdigit():
                    return primitivo(tipoPrimitivo.Entero,int(float(izq.valor)!=float(der.valor)),self.columna,self.linea,0)
                else:
                    return primitivo(tipoPrimitivo.Entero,1,self.columna,self.linea,0)
        elif izq.tipo==tipoPrimitivo.Doble:
            if der.tipo==tipoPrimitivo.Entero:
                return primitivo(tipoPrimitivo.Entero,int(float(izq.valor)!=int(der.valor)),self.columna,self.linea,0)
            elif der.tipo==tipoPrimitivo.Doble:
                return primitivo(tipoPrimitivo.Entero,int(float(izq.valor)!=float(der.valor)),self.columna,self.linea,0)
            elif der.tipo==tipoPrimitivo.Cadena:
                if str(der.valor).lstrip('-').replace('.','',1).isdigit():
                    return primitivo(tipoPrimitivo.Entero,int(float(izq.valor)!=float(der.valor)),self.columna,self.linea,0)
                else:
                    return primitivo(tipoPrimitivo.Entero,1,self.columna,self.linea,0)
        elif izq.tipo==tipoPrimitivo.Cadena:
            if der.tipo==tipoPrimitivo.Cadena:
                return primitivo(tipoPrimitivo.Entero,int(str(izq.valor)!=str(der.valor)),self.columna,self.linea,0)
            elif der.tipo==tipoPrimitivo.Entero or der.tipo==tipoPrimitivo.Doble:
                if str(izq.valor).lstrip('-').replace('.','',1).isdigit():
                    return primitivo(tipoPrimitivo.Entero,int(float(izq.valor)!=float(der.valor)),self.columna,self.linea,0)
                return primitivo(tipoPrimitivo.Entero,1,self.columna,self.linea,0)

        
        estat.Lerrores.append(CError('Semantico','Error al realizar la Diferencia',self.columna,self.linea))
        return primitivo(tipoPrimitivo.Error,'@error@',self.columna,self.linea,0)


class newMenorq:
    def __init__(self,izq,der,c,l,n):
        self.columna=c
        self.linea=l
        self.vNodo=nodoAST('<',n)
        self.vNodo.hijos.append(izq.vNodo)
        self.vNodo.hijos.append(der.vNodo)
        self.hijoIzq=izq
        self.hijoDer=der
    def getvalor(self,entorno,estat):
        izq=self.hijoIzq.getvalor(entorno,estat)
        der=self.hijoDer.getvalor(entorno,estat)
        if izq.tipo==tipoPrimitivo.Entero or izq.tipo==tipoPrimitivo.Doble:
            if der.tipo==tipoPrimitivo.Entero or der.tipo==tipoPrimitivo.Doble:
                return primitivo(tipoPrimitivo.Entero,int(float(izq.valor)<float(der.valor)),self.columna,self.linea,0)

        estat.Lerrores.append(CError('Semantico','Error al realizar Menor Que',self.columna,self.linea))
        return primitivo(tipoPrimitivo.Error,'@error@',self.columna,self.linea,0)

class newMayorq:
    def __init__(self,izq,der,c,l,n):
        self.columna=c
        self.linea=l
        self.vNodo=nodoAST('>',n)
        self.vNodo.hijos.append(izq.vNodo)
        self.vNodo.hijos.append(der.vNodo)
        self.hijoIzq=izq
        self.hijoDer=der
    def getvalor(self,entorno,estat):
        izq=self.hijoIzq.getvalor(entorno,estat)
        der=self.hijoDer.getvalor(entorno,estat)
        if izq.tipo==tipoPrimitivo.Entero or izq.tipo==tipoPrimitivo.Doble:
            if der.tipo==tipoPrimitivo.Entero or der.tipo==tipoPrimitivo.Doble:
                return primitivo(tipoPrimitivo.Entero,int(float(izq.valor)>float(der.valor)),self.columna,self.linea,0)

        estat.Lerrores.append(CError('Semantico','Error al realizar Mayor Que',self.columna,self.linea))
        return primitivo(tipoPrimitivo.Error,'@error@',self.columna,self.linea,0)

class newMenorIgualq:
    def __init__(self,izq,der,c,l,n):
        self.columna=c
        self.linea=l
        self.vNodo=nodoAST('<=',n)
        self.vNodo.hijos.append(izq.vNodo)
        self.vNodo.hijos.append(der.vNodo)
        self.hijoIzq=izq
        self.hijoDer=der
    def getvalor(self,entorno,estat):
        izq=self.hijoIzq.getvalor(entorno,estat)
        der=self.hijoDer.getvalor(entorno,estat)
        if izq.tipo==tipoPrimitivo.Entero or izq.tipo==tipoPrimitivo.Doble:
            if der.tipo==tipoPrimitivo.Entero or der.tipo==tipoPrimitivo.Doble:
                return primitivo(tipoPrimitivo.Entero,int(float(izq.valor)<=float(der.valor)),self.columna,self.linea,0)

        estat.Lerrores.append(CError('Semantico','Error al realizar Menor igual Que',self.columna,self.linea))
        return primitivo(tipoPrimitivo.Error,'@error@',self.columna,self.linea,0)

class newMayorIgualq:
    def __init__(self,izq,der,c,l,n):
        self.columna=c
        self.linea=l
        self.vNodo=nodoAST('>=',n)
        self.vNodo.hijos.append(izq.vNodo)
        self.vNodo.hijos.append(der.vNodo)
        self.hijoIzq=izq
        self.hijoDer=der
    def getvalor(self,entorno,estat):
        izq=self.hijoIzq.getvalor(entorno,estat)
        der=self.hijoDer.getvalor(entorno,estat)
        if izq.tipo==tipoPrimitivo.Entero or izq.tipo==tipoPrimitivo.Doble:
            if der.tipo==tipoPrimitivo.Entero or der.tipo==tipoPrimitivo.Doble:
                return primitivo(tipoPrimitivo.Entero,int(float(izq.valor)>=float(der.valor)),self.columna,self.linea,0)

        estat.Lerrores.append(CError('Semantico','Error al realizar Mayor Igual Que',self.columna,self.linea))
        return primitivo(tipoPrimitivo.Error,'@error@',self.columna,self.linea,0)

class popupWindow(object):
    def __init__(self,master):
        top=self.top=Toplevel(master)
        self.l=Label(top,text="Hello World")
        self.l.pack()
        self.e=Entry(top)
        self.e.pack()
        self.b=Button(top,text='Ok',command=self.cleanup)
        self.b.pack()
    def cleanup(self):
        self.value=self.e.get()
        self.top.destroy()

class newLeer:
    def __init__(self,c,l,n):
        self.columna=c
        self.linea=l
        self.vNodo=nodoAST('Leer',n)
        self.vNodo.hijos.append(nodoAST('read',n+1))
        self.vNodo.hijos.append(nodoAST('(',n+2))
        self.vNodo.hijos.append(nodoAST(')',n+3))
    def getvalor(self,entorno,estat):
        
        parent = estat.consola.master
        entrada=popupWindow(parent)
        # parent.configure(state='disable')
        parent.wait_window(entrada.top)
        # parent.configure(state='enable')
        txtinput=str(entrada.value)
        if txtinput.lstrip('-').replace('.','',1).isdigit():
            if "." in txtinput:
                return primitivo(tipoPrimitivo.Doble,float(txtinput),self.columna,self.linea,0)
            else:
                return primitivo(tipoPrimitivo.Entero,int(txtinput),self.columna,self.linea,0)
        else:
            return primitivo(tipoPrimitivo.Cadena,txtinput,self.columna,self.linea,0)

class newAbsoluto:
    def __init__(self,v,c,l,n):
        self.columna=c
        self.linea=l
        self.v1=v
        self.vNodo=nodoAST('vAbsoluto',n)
        self.vNodo.hijos.append(nodoAST('abs',n+1))
        self.vNodo.hijos.append(nodoAST('(',n+2))
        self.vNodo.hijos.append(v.vNodo)
        self.vNodo.hijos.append(nodoAST(')',n+3))
    def getvalor(self,entorno,estat):
        temp=self.v1.getvalor(entorno,estat)
        if temp.tipo==tipoPrimitivo.Entero:
            return primitivo(tipoPrimitivo.Entero,abs(int(temp.valor)),self.columna,self.linea,0)
        elif temp.tipo==tipoPrimitivo.Doble:
            return primitivo(tipoPrimitivo.Doble,abs(float(temp.valor)),self.columna,self.linea,0)
        estat.Lerrores.append(CError('Semantico','Error al realizar abs()',self.columna,self.linea))
        return primitivo(tipoPrimitivo.Error,'@error@',self.columna,self.linea,0)


class newAndBtb:
    def __init__(self,izq,der,c,l,n):
        self.columna=c
        self.linea=l
        self.vNodo=nodoAST('&',n)
        self.vNodo.hijos.append(izq.vNodo)
        self.vNodo.hijos.append(der.vNodo)
        self.hijoIzq=izq
        self.hijoDer=der
    def getvalor(self,entorno,estat):
        izq=self.hijoIzq.getvalor(entorno,estat)
        der=self.hijoDer.getvalor(entorno,estat)
        if izq.tipo==tipoPrimitivo.Entero:
            if der.tipo==tipoPrimitivo.Entero:
                bizq=bin(int(izq.valor)).replace("b","").replace('-','')
                bder=bin(int(der.valor)).replace("b","").replace('-','')
                while(len(bizq)<len(bder)):
                    bizq='0'+bizq
                while(len(bder)<len(bizq)):
                    bder='0'+bder
                res='0'
                pos=0
                while pos<len(bizq):
                    res+=str(int(bizq[pos]) and int(bder[pos]))
                    pos+=1
                
                return primitivo(tipoPrimitivo.Entero,int(res,2),self.columna,self.linea,0)
        
        estat.Lerrores.append(CError('Semantico','Error al realizar And bit a bit',self.columna,self.linea))
        return primitivo(tipoPrimitivo.Error,'@error@',self.columna,self.linea,0)

class newOrBtb:
    def __init__(self,izq,der,c,l,n):
        self.columna=c
        self.linea=l
        self.vNodo=nodoAST('|',n)
        self.vNodo.hijos.append(izq.vNodo)
        self.vNodo.hijos.append(der.vNodo)
        self.hijoIzq=izq
        self.hijoDer=der
    def getvalor(self,entorno,estat):
        izq=self.hijoIzq.getvalor(entorno,estat)
        der=self.hijoDer.getvalor(entorno,estat)
        if izq.tipo==tipoPrimitivo.Entero:
            if der.tipo==tipoPrimitivo.Entero:
                bizq=bin(int(izq.valor)).replace("b","").replace('-','')
                bder=bin(int(der.valor)).replace("b","").replace('-','')
                while(len(bizq)<len(bder)):
                    bizq='0'+bizq
                while(len(bder)<len(bizq)):
                    bder='0'+bder
                res='0'
                pos=0
                while pos<len(bizq):
                    res+=str(int(bizq[pos]) or int(bder[pos]))
                    pos+=1
                
                return primitivo(tipoPrimitivo.Entero,int(res,2),self.columna,self.linea,0)
        
        estat.Lerrores.append(CError('Semantico','Error al realizar OR bit a bit',self.columna,self.linea))
        return primitivo(tipoPrimitivo.Error,'@error@',self.columna,self.linea,0)

class newXorBtb:
    def __init__(self,izq,der,c,l,n):
        self.columna=c
        self.linea=l
        self.vNodo=nodoAST('^',n)
        self.vNodo.hijos.append(izq.vNodo)
        self.vNodo.hijos.append(der.vNodo)
        self.hijoIzq=izq
        self.hijoDer=der
    def getvalor(self,entorno,estat):
        izq=self.hijoIzq.getvalor(entorno,estat)
        der=self.hijoDer.getvalor(entorno,estat)
        if izq.tipo==tipoPrimitivo.Entero:
            if der.tipo==tipoPrimitivo.Entero:
                bizq=bin(int(izq.valor)).replace("b","").replace('-','')
                bder=bin(int(der.valor)).replace("b","").replace('-','')
                while(len(bizq)<len(bder)):
                    bizq='0'+bizq
                while(len(bder)<len(bizq)):
                    bder='0'+bder
                res='0'
                pos=0
                while pos<len(bizq):
                    res+=str(int(bizq[pos]) ^ int(bder[pos]))
                    pos+=1
                
                return primitivo(tipoPrimitivo.Entero,int(res,2),self.columna,self.linea,0)
        
        estat.Lerrores.append(CError('Semantico','Error al realizar XOR bit a bit',self.columna,self.linea))
        return primitivo(tipoPrimitivo.Error,'@error@',self.columna,self.linea,0)

class newNotBtb:
    def __init__(self,izq,c,l,n):
        self.columna=c
        self.linea=l
        self.vNodo=nodoAST('~',n)
        self.vNodo.hijos.append(izq.vNodo)
        self.hijoIzq=izq
    def getvalor(self,entorno,estat):
        izq=self.hijoIzq.getvalor(entorno,estat)
        if izq.tipo==tipoPrimitivo.Entero:
            bizq=bin(int(izq.valor)).replace("b","").replace('-','')
            res='0'
            pos=1
            while pos<len(bizq):
                res+=str(int(not int(bizq[pos])))
                pos+=1    
            return primitivo(tipoPrimitivo.Entero,int(res,2),self.columna,self.linea,0)
        
        estat.Lerrores.append(CError('Semantico','Error al realizar Not bit a bit',self.columna,self.linea))
        return primitivo(tipoPrimitivo.Error,'@error@',self.columna,self.linea,0)


class newDespIzqBtb:
    def __init__(self,izq,der,c,l,n):
        self.columna=c
        self.linea=l
        self.vNodo=nodoAST('^',n)
        self.vNodo.hijos.append(izq.vNodo)
        self.vNodo.hijos.append(der.vNodo)
        self.hijoIzq=izq
        self.hijoDer=der
    def getvalor(self,entorno,estat):
        izq=self.hijoIzq.getvalor(entorno,estat)
        der=self.hijoDer.getvalor(entorno,estat)
        if izq.tipo==tipoPrimitivo.Entero:
            if der.tipo==tipoPrimitivo.Entero:
                bizq=bin(int(izq.valor)).replace("b","").replace('-','')
                pos=int(der.valor)
                if pos<0:
                    estat.Lerrores.append(CError('Semantico','Error al realizar XOR bit a bit',self.columna,self.linea))
                    return primitivo(tipoPrimitivo.Error,'@error@',self.columna,self.linea,0)

                res=str(bizq)
                for i in range(pos):
                    res+='0'

                return primitivo(tipoPrimitivo.Entero,int(res,2),self.columna,self.linea,0)
        
        estat.Lerrores.append(CError('Semantico','Error al realizar Desplazamiento izquierdo bit a bit',self.columna,self.linea))
        return primitivo(tipoPrimitivo.Error,'@error@',self.columna,self.linea,0)

class newDespDerBtb:
    def __init__(self,izq,der,c,l,n):
        self.columna=c
        self.linea=l
        self.vNodo=nodoAST('^',n)
        self.vNodo.hijos.append(izq.vNodo)
        self.vNodo.hijos.append(der.vNodo)
        self.hijoIzq=izq
        self.hijoDer=der
    def getvalor(self,entorno,estat):
        izq=self.hijoIzq.getvalor(entorno,estat)
        der=self.hijoDer.getvalor(entorno,estat)
        if izq.tipo==tipoPrimitivo.Entero:
            if der.tipo==tipoPrimitivo.Entero:
                bizq=bin(int(izq.valor)).replace("b","").replace('-','')
                pos=0
                cond=len(bizq)-int(der.valor)
                if cond<=0:
                    res='0'
                else:
                    res=''
                    while pos<cond:
                        res+=str(int(bizq[pos]))
                        pos+=1
                
                return primitivo(tipoPrimitivo.Entero,int(res,2),self.columna,self.linea,0)
        
        estat.Lerrores.append(CError('Semantico','Error al realizar Desplazamiento derecha bit a bit',self.columna,self.linea))
        return primitivo(tipoPrimitivo.Error,'@error@',self.columna,self.linea,0)


class newNegacion:
    def __init__(self,v,c,l,n):
        self.columna=c
        self.linea=l
        self.vNodo=nodoAST('-',n)
        self.vNodo.hijos.append(v.vNodo)
        self.exp=v
    def getvalor(self,entorno,estat):
        temp=self.exp.getvalor(entorno,estat)
        if temp.tipo==tipoPrimitivo.Entero:
            return primitivo(tipoPrimitivo.Entero,int(int(temp.valor)*-1),self.columna,self.linea,0)
        elif temp.tipo==tipoPrimitivo.Doble:
            return primitivo(tipoPrimitivo.Doble,float(float(temp.valor)*-1),self.columna,self.linea,0)
        
        estat.Lerrores.append(CError('Semantico','Error al realizar Negacion numerica',self.columna,self.linea))
        return primitivo(tipoPrimitivo.Error,'@error@',self.columna,self.linea,0) 

class newPuntero:
    def __init__(self,v,c,l,n):
        self.columna=c
        self.linea=l
        self.vNodo=nodoAST('puntero',n)
        self.vNodo.hijos.append(nodoAST('&',n+1))
        self.vNodo.hijos.append(v.vNodo)
        self.exp=v
        self.tipo=tipoPrimitivo.puntero
    def getvalor(self,entorno,estat):
        if(isinstance(self.exp,id_)):
            temp=entorno.buscar(self.exp.variable,self.columna,self.linea,estat)
            if temp!=None:
                return temp.valor
            else:
                return primitivo(tipoPrimitivo.Error,'@error@',self.columna,self.linea,0)
        else:
            t=self.exp.getvalor(entorno,estat)
            if t.tipo==tipoPrimitivo.Error:
                return t
            return self.exp
            

class newCasteoInt:
    def __init__(self,izq,c,l,n):
        self.columna=c
        self.linea=l
        self.vNodo=nodoAST('Casteo',n)
        self.vNodo.hijos.append(nodoAST('(',n+1))
        self.vNodo.hijos.append(nodoAST('int',n+2))
        self.vNodo.hijos.append(nodoAST('(',n+3))
        self.vNodo.hijos.append(izq.vNodo)
        self.hijoIzq=izq

    def getvalor(self,entorno,estat):
        izq=self.hijoIzq.getvalor(entorno,estat)
        if izq.tipo==tipoPrimitivo.Entero:
            return primitivo(tipoPrimitivo.Entero,int(float(izq.valor)),self.columna,self.linea,0)
        elif izq.tipo==tipoPrimitivo.Doble:
            return primitivo(tipoPrimitivo.Entero,int(float(izq.valor)),self.columna,self.linea,0)
        elif izq.tipo==tipoPrimitivo.Cadena:
            return primitivo(tipoPrimitivo.Entero,ord(str(izq.valor)[0]),self.columna,self.linea,0)
        elif izq.tipo==tipoPrimitivo.Arreglo:
            if len(izq.arreglo)==0:
                estat.Lerrores.append(CError('Semantico','Error al realizar casteo a Int',self.columna,self.linea))
                return primitivo(tipoPrimitivo.Error,'@error@',self.columna,self.linea,0)

            return newCasteoInt(izq.arreglo[list(izq.arreglo.keys())[0]],self.columna,self.linea,0).getvalor(entorno,estat)
        else:
            estat.Lerrores.append(CError('Semantico','Error al realizar casteo a Int',self.columna,self.linea))
            return primitivo(tipoPrimitivo.Error,'@error@',self.columna,self.linea,0)

class newCasteoFloat:
    def __init__(self,izq,c,l,n):
        self.columna=c
        self.linea=l
        self.vNodo=nodoAST('Casteo',n)
        self.vNodo.hijos.append(nodoAST('(',n+1))
        self.vNodo.hijos.append(nodoAST('float',n+2))
        self.vNodo.hijos.append(nodoAST('(',n+3))
        self.vNodo.hijos.append(izq.vNodo)
        self.hijoIzq=izq

    def getvalor(self,entorno,estat):
        izq=self.hijoIzq.getvalor(entorno,estat)
        if izq.tipo==tipoPrimitivo.Entero:
            return primitivo(tipoPrimitivo.Entero,float(izq.valor),self.columna,self.linea,0)
        elif izq.tipo==tipoPrimitivo.Doble:
            return primitivo(tipoPrimitivo.Entero,float(izq.valor),self.columna,self.linea,0)
        elif izq.tipo==tipoPrimitivo.Cadena:
            return primitivo(tipoPrimitivo.Entero,float(ord(str(izq.valor)[0])),self.columna,self.linea,0)
        elif izq.tipo==tipoPrimitivo.Arreglo:
            if len(izq.arreglo)==0:
                estat.Lerrores.append(CError('Semantico','Error al realizar casteo a Float',self.columna,self.linea))
                return primitivo(tipoPrimitivo.Error,'@error@',self.columna,self.linea,0)
                
            return newCasteoFloat(izq.arreglo[list(izq.arreglo.keys())[0]],self.columna,self.linea,0).getvalor(entorno,estat)
        else:
            estat.Lerrores.append(CError('Semantico','Error al realizar casteo a Float',self.columna,self.linea))
            return primitivo(tipoPrimitivo.Error,'@error@',self.columna,self.linea,0)

class newCasteoChar:
    def __init__(self,izq,c,l,n):
        self.columna=c
        self.linea=l
        self.vNodo=nodoAST('Casteo',n)
        self.vNodo.hijos.append(nodoAST('(',n+1))
        self.vNodo.hijos.append(nodoAST('char',n+2))
        self.vNodo.hijos.append(nodoAST('(',n+3))
        self.vNodo.hijos.append(izq.vNodo)
        self.hijoIzq=izq

    def getvalor(self,entorno,estat):
        izq=self.hijoIzq.getvalor(entorno,estat)
        if izq.tipo==tipoPrimitivo.Entero or izq.tipo==tipoPrimitivo.Doble:
            temp=int(float(izq.valor))
            if(temp>255):
                temp=temp%256            
            return primitivo(tipoPrimitivo.Cadena,chr(int(temp)),self.columna,self.linea,0)        
        elif izq.tipo==tipoPrimitivo.Cadena:
            return primitivo(tipoPrimitivo.Cadena,str(izq.valor)[0],self.columna,self.linea,0)
        elif izq.tipo==tipoPrimitivo.Arreglo:
            if len(izq.arreglo)==0:
                estat.Lerrores.append(CError('Semantico','Error al realizar casteo a Char',self.columna,self.linea))
                return primitivo(tipoPrimitivo.Error,'@error@',self.columna,self.linea,0)
                
            return newCasteoChar(izq.arreglo[list(izq.arreglo.keys())[0]],self.columna,self.linea,0).getvalor(entorno,estat)
        else:
            estat.Lerrores.append(CError('Semantico','Error al realizar casteo a Char',self.columna,self.linea))
            return primitivo(tipoPrimitivo.Error,'@error@',self.columna,self.linea,0)

        
class newArreglo:
    def __init__(self,c,l,n):
        self.columna=c
        self.linea=l
        self.vNodo=nodoAST('array()',n)
        self.arreglo={}
        self.valor=str(self.arreglo)
        self.tipo=tipoPrimitivo.Arreglo
    def getvalor(self,entorno,estat):
        # actualizar valor en caso se imprima arreglo
        return self
    def getClave(self,v,entorno,estat):
        temp=v.getvalor(entorno,estat)
        if temp.tipo==tipoPrimitivo.Entero: return int(temp.valor)
        elif temp.tipo==tipoPrimitivo.Cadena: return str(temp.valor)
        elif temp.tipo==tipoPrimitivo.Doble: return float(temp.valor)
        else:
            estat.Lerrores.append(CError('Semantico','Se esperaba un Int, Float, o String como indice de acceso al struct/Arreglo',self.columna,self.linea))
            return primitivo(tipoPrimitivo.Error,'@error@',self.columna,self.linea,0)

    def getPos(self,v,entorno,estat):
        indice=self.getClave(v,entorno,estat)
        if isinstance(indice,primitivo):
            return indice
        else:
            if indice in self.arreglo:
                return self.arreglo[indice].getvalor(entorno,estat)
            else:
                estat.Lerrores.append(CError('Semantico','No se encontro el indice '+str(indice),self.columna,self.linea))
                return primitivo(tipoPrimitivo.Error,'@error@',self.columna,self.linea,0)
    def setPos(self,i,v,entorno,estat):
        indice=self.getClave(i,entorno,estat)
        if isinstance(indice,primitivo):
            return
        else:
            if isinstance(v,newPuntero):
                temp=v
            else:
                temp=v.getvalor(entorno,estat)

            if temp.tipo!=tipoPrimitivo.Error:
                self.arreglo[indice]=temp
            else:
                estat.Lerrores.append(CError('Semantico','Error al asignar posicion de arreglo ',self.columna,self.linea))
                


    def getTabla(self):
        texto='\n<table color=\'blue\' cellspacing=\'0\'>\n<tr><td>Clave </td><td>Valor </td></tr>\n'
        for x,y in self.arreglo.items():
            if int(y.tipo.value)-1==7:
                texto+='<tr><td>'+str(x)+'  </td><td> '+str(y.exp.variable)+'  </td></tr>'
            elif int(y.tipo.value)-1==3:
                texto+='<tr><td>'+str(x)+'  </td><td>'+str(y.getTabla())+'  </td></tr>'            
            else:
                texto+='<tr><td>'+str(x)+'  </td><td>'+str(y.valor)+'  </td></tr>'
        texto+='</table>'
        return texto
    def getProfundidad(self):
        p=0
        for x,y in self.arreglo.items():
            if int(y.tipo.value)-1==3:
                act=y.getProfundidad()
                if act>p: p=act
        return p+1


class newAcceso:
    def __init__(self,var,Li,c,l,n):
        self.columna=c
        self.linea=l
        self.indices=Li
        self.ref=var
        self.variable=str(var)
        self.vNodo=nodoAST('acceso',n)
        self.vNodo.hijos.append(nodoAST(str(var),n+1))
        self.vNodo.hijos.append(nodoAST('Indices',n+2))
        for i in Li:
            self.vNodo.hijos[1].hijos.append(i.vNodo)
            tmp=''
            if isinstance(i,primitivo):tmp=i.valor
            elif isinstance(i,id_):tmp=i.variable
            self.variable+='['+str(tmp)+']'
    def getvalor(self,entorno,estat):
        temp=entorno.buscar(self.ref,self.columna,self.linea,estat).valor.getvalor(entorno,estat)

        for i in self.indices:
            if isinstance(temp,newArreglo):
                temp=temp.getPos(i,entorno,estat)
            elif temp.tipo==tipoPrimitivo.Cadena:
                t=i.getvalor(entorno,estat)
                if t.tipo==tipoPrimitivo.Entero:
                    t=int(t.valor)
                    if t<len(temp.valor):
                        temp=primitivo(tipoPrimitivo.Cadena,temp.valor[t],self.columna,self.linea,0)
                    else:
                        estat.Lerrores.append(CError('Semantico','Indice fuera de rango ',self.columna,self.linea))
                        return primitivo(tipoPrimitivo.Error,'@error@',self.columna,self.linea,0)
                else:
                    estat.Lerrores.append(CError('Semantico','No se puede acceder, se esperaba indice tipo Int ',self.columna,self.linea))
                    return primitivo(tipoPrimitivo.Error,'@error@',self.columna,self.linea,0)
            else:
                estat.Lerrores.append(CError('Semantico','solo se puede acceder a Array String ',self.columna,self.linea))
                return primitivo(tipoPrimitivo.Error,'@error@',self.columna,self.linea,0)
        
        return temp







            
