from Tipo import *
from CError import CError
from Simbolo import Simbolo
from tkinter import *
from Expresion import newPuntero
class newEtiqueta:
    def __init__(self,v,c,l,n):
        self.tipo=tipoInstruccion.etiqueta
        self.label_=v
        self.columna=c
        self.linea=l
        self.vNodo=nodoAST('LABEL',n)
        self.vNodo.hijos.append(nodoAST(v,n+1))
    
    def ejecutar(self,entorno,estat):
        return

class newSalto:
    def __init__(self,v,c,l,n):
        self.tipo=tipoInstruccion.salto
        self.label_=v
        self.columna=c
        self.linea=l
        self.vNodo=nodoAST('SALTO',n)
        self.vNodo.hijos.append(nodoAST('GOTO',n+1))
        self.vNodo.hijos.append(nodoAST(v,n+2))

    def ejecutar(self,entorno,estat):
        if self.label_ in entorno.etiquetas:
            estat.i=int(entorno.etiquetas[self.label_])
        else:
            estat.Lerrores.append(CError('Semantico','no se encontro la etiqueta \''+str(self.label_)+'\'',self.columna,self.linea))


class newAsignacion:
    def __init__(self,id,Li,v,c,l,n):
        self.id=id
        self.indices=Li
        self.valor=v
        self.columna=c
        self.linea=l
        self.vNodo=nodoAST('ASIGNACION',n)
        self.vNodo.hijos.append(nodoAST(self.id,n+1))
        self.vNodo.hijos.append(nodoAST('Indices',n+2))
        for i in Li:
            self.vNodo.hijos[1].hijos.append(i.vNodo)
        self.vNodo.hijos.append(nodoAST('=',n+3))
        self.vNodo.hijos.append(v.vNodo)

    def ejecutar(self,entorno,estat):
        resultado=self.valor.getvalor(entorno,estat)
        if resultado.tipo==tipoPrimitivo.Error:
            estat.Lerrores.append(CError('Semantico','no se puede asignar error a la variable \''+str(self.id)+'\'',self.columna,self.linea))
            return
        temp=None
        if isinstance(self.valor,newPuntero):
            temp=Simbolo(self.valor.tipo,self.valor)
        else:
            temp=Simbolo(resultado.tipo,resultado)
        
        if len(self.indices)==0:
            entorno.actualizar(self.id,temp)
        else:
            print('aun no hay arreglos xd')


class newUnset:
    def __init__(self,id,c,l,n):
        self.id=id
        self.columna=c
        self.linea=l
        self.vNodo=nodoAST('UNSET',n)
        self.vNodo.hijos.append(nodoAST('unset',n+1))
        self.vNodo.hijos.append(nodoAST('(',n+2))
        self.vNodo.hijos.append(self.id.vNodo)
        self.vNodo.hijos.append(nodoAST(')',n+3))

    def ejecutar(self,entorno,estat):
        if self.id.tipo==tipoPrimitivo.variable:
            d=self.id.variable
            if(d in entorno.tabla):
                entorno.tabla.pop(d)
            else:
                estat.Lerrores.append(CError('Semantico','Error al aplicar unset(), No existe la variable \''+str(d)+'\'',self.columna,self.linea))
            return
        else:
            print('aun no hay arreglos xd')

class newImprimir:
    def __init__(self,v,c,l,n):
        self.v=v
        self.columna=c
        self.linea=l
        self.vNodo=nodoAST('PRINT',n)
        self.vNodo.hijos.append(nodoAST('print',n+1))
        self.vNodo.hijos.append(nodoAST('(',n+2))
        self.vNodo.hijos.append(v.vNodo)
        self.vNodo.hijos.append(nodoAST(')',n+3))

    def ejecutar(self,entorno,estat):
        temp=self.v.getvalor(entorno,estat)
        if temp.tipo!=tipoPrimitivo.Error:
            estat.consola.insert(INSERT, str(temp.valor).replace('\\n','\n').replace('\\t','\t')+"\n")
        else:
           estat.Lerrores.append(CError('Semantico','No se puede imprimir un error',self.columna,self.linea))
 
class newSalir:
    def __init__(self,c,l,n):
        self.columna=c
        self.linea=l
        self.vNodo=nodoAST('exit',n)

    def ejecutar(self,entorno,estat):
        estat.i=estat.e

class newIF:
    def __init__(self,cond,label,c,l,n):
        self.columna=c
        self.linea=l
        self.condicion=cond
        self.label=label
        self.vNodo=nodoAST('IF',n)
        self.vNodo.hijos.append(nodoAST('if',n+1))
        self.vNodo.hijos.append(nodoAST('(',n+2))
        self.vNodo.hijos.append(cond.vNodo)
        self.vNodo.hijos.append(nodoAST(')',n+3))
        self.vNodo.hijos.append(nodoAST('goto',n+4))
        self.vNodo.hijos.append(nodoAST(label,n+5))
    def ejecutar(self,entorno,estat):
        temp=self.condicion.getvalor(entorno,estat)
        if temp.tipo==tipoPrimitivo.Entero:
            valtemp=int(temp.valor)
            if valtemp!=0:
                if self.label in entorno.etiquetas:
                    estat.i=int(entorno.etiquetas[self.label])
                else:
                    estat.Lerrores.append(CError('Semantico','no se encontro la etiqueta \''+str(self.label)+'\'',self.columna,self.linea))
            else:
                return
        else:
            estat.Lerrores.append(CError('Semantico','Se esperaba expresion de tipo entero en el IF, pero se encontro tipo \''+temp.tipo.name+'\'',self.columna,self.linea))




        

