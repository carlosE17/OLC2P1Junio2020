from Tipo import *
from CError import CError

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
    def getvalor(self,entorno,estat):
        temp=entorno.buscar(self.variable,self.columna,self.linea,estat)
        if temp!=None:
            return temp.valor
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
        else:
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
        else:
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
        else:
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
        else:
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
        else:
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
                if(int(der.valor)!=0):
                    der=1
                return primitivo(tipoPrimitivo.Entero,izq and der,self.columna,self.linea,0)
        else:
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
                if(int(der.valor)!=0):
                    der=1
                return primitivo(tipoPrimitivo.Entero,izq or der,self.columna,self.linea,0)
        else:
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
                if(int(der.valor)!=0):
                    der=1
                return primitivo(tipoPrimitivo.Entero,izq ^ der,self.columna,self.linea,0)
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

        else:
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

        else:
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
        print(str(izq)+' '+str(der))
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
        else:
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
        else:
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
        else:
            estat.Lerrores.append(CError('Semantico','Error al realizar XOR bit a bit',self.columna,self.linea))
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
        else:
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
        else:
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
        else:
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
                return temp
            else:
                return primitivo(tipoPrimitivo.Error,'@error@',self.columna,self.linea,0)
        else:
            print('aun no hay arreglos xd')
            
        
        


            
