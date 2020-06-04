import enum

class tipoPrimitivo(enum.Enum):
    Entero=1
    Cadena=2
    Doble=3
    Arreglo=4
    Error=5

class tipoInstruccion(enum.Enum):
    etiqueta=1
    asignacionT=2
    asignacionA=3
    asignacionV=4
    salto=5
    condicional=6
