from tkinter import *
import tkinter.scrolledtext as scrolledtext
import tkinter.ttk as ttk
import tkinter.messagebox
from tkinter import filedialog
from AST import Estaticos
from Entorno import Entorno
from Tipo import tipoInstruccion
import gAscendente as g1
from Instruccion import newEtiqueta
from graphviz import Source
rutas = []

def Ejec(Linstr,c,Le):
    LErr=Le
    ast=Estaticos(c,LErr,len(Linstr))
    entornoG=Entorno()
    iEt=0
    try:
        while iEt<len(Linstr):
            if(isinstance(Linstr[iEt],newEtiqueta)):
                entornoG.addEtiqueta(Linstr[iEt].label_,iEt)
            iEt+=1
    except Exception as e:
        print('ventana[25] '+e)


    try:
        while ast.i<len(Linstr):
            Linstr[ast.i].ejecutar(entornoG,ast)
            ast.i+=1
    except Exception as e:
        print('veentana[33]'+str(e))
    # generar reportes de errores, y graficar el arbol
    gReporteErr(ast.Lerrores)
    gReporteTs(entornoG.tabla.items())
    graphAST(Linstr)

def gReporteErr(L):
    if len(L)>0:
        texto='digraph {\n'
        t=''
        repL=''
        repS=''
        repSem=''
        for i in L:
            t+=i.getTexto()
            if i.tipo=='Lexico': repL+=i.getTexto()
            elif i.tipo=='Sintactico': repS+=i.getTexto()
            else: repSem+=i.getTexto()
        texto += "node0" + " ["+ "    shape=plaintext\n"+ "    label=<\n"+ "\n" +"      <table cellspacing='0'>\n"+ "      <tr><td>TIPO</td><td>Descripcion</td><td>Linea</td></tr>\n"+ t+ "    </table>\n" + ">];}"
        with open('reporteErrores.dot', "w") as f:
                f.write(texto)
        texto = "digraph {\n node0" + " ["+ "    shape=plaintext\n"+ "    label=<\n"+ "\n" +"      <table cellspacing='0'>\n"+ "      <tr><td>TIPO</td><td>Descripcion</td><td>Linea</td></tr>\n"+ repL+ "    </table>\n" + ">];}"
        with open('reporteErroresLexicos.dot', "w") as f:
                f.write(texto)
        texto = "digraph {\n node0" + " ["+ "    shape=plaintext\n"+ "    label=<\n"+ "\n" +"      <table cellspacing='0'>\n"+ "      <tr><td>TIPO</td><td>Descripcion</td><td>Linea</td></tr>\n"+ repS+ "    </table>\n" + ">];}"
        with open('reporteErroresSintacticos.dot', "w") as f:
                f.write(texto)
        texto = "digraph {\n node0" + " ["+ "    shape=plaintext\n"+ "    label=<\n"+ "\n" +"      <table cellspacing='0'>\n"+ "      <tr><td>TIPO</td><td>Descripcion</td><td>Linea</td></tr>\n"+ repSem+ "    </table>\n" + ">];}"
        with open('reporteErroresSemanticos.dot', "w") as f:
                f.write(texto)
    else:
        t='digraph G {\"No hay errores\"}'
        with open('reporteErrores.dot', "w") as f:
                f.write(t)
        with open('reporteErroresLexicos.dot', "w") as f:
                f.write(t)
        with open('reporteErroresSintacticos.dot', "w") as f:
                f.write(t)
        with open('reporteErroresSemanticos.dot', "w") as f:
                f.write(t)

def gReporteTs(L):
    nTipos=['Int','String','Float','Array','error',' ',' ','puntero']
    texto='digraph {\n'
    t=''
    for k,v in L:
        if int(v.tipo.value)-1==7:
            t+="<tr> <td> " + str(k) + "</td><td> " + nTipos[int(v.tipo.value)-1] + " </td><td> " + str(v.valor.exp.variable) + " </td><td> "+'1' + " </td><td> " + str(v.valor.linea) + " </td><td> "+ str(v.valor.exp.variable) + "</td> </tr>"
        elif int(v.tipo.value)-1==3:
            t+="<tr> <td> " + str(k) + "</td><td> " + nTipos[int(v.tipo.value)-1] + " </td><td> " + str(v.valor.getTabla()) + " </td><td> "+str(v.valor.getProfundidad()) + " </td><td> " + str(v.valor.linea) + " </td><td> "+ '---' + "</td> </tr>"            
        else:                
            t+="<tr> <td> " + str(k) + "</td><td> " + nTipos[int(v.tipo.value)-1] + " </td><td> " + str(v.valor.valor) + " </td><td> "+'1' + " </td><td> " + str(v.valor.linea) + " </td><td> "+ '---' + "</td> </tr>"
    texto += "node0" + " ["+ "    shape=plaintext\n"+ "    label=<\n"+ "\n" +"      <table cellspacing='0'>\n"+ "      <tr><td>ID</td><td>Tipo</td><td>Valor</td><td>Dimension</td><td>Linea</td><td>Referencia</td></tr>\n"+ t+ "    </table>\n" + ">];}"
    with open('reporteTs.dot', "w") as f:
        f.write(texto)

        
def graphAST(L):
    if len(L)!=0:
        t='digraph Q { \n  node [shape=record];\n'
        for i in L:
            t+='node'+i.vNodo.nNodo+'[label=\"'+i.vNodo.vNodo+'\"];\n'
            t+='p_inicio ->'+'node'+i.vNodo.nNodo+';\n'
            t+=dibujo(i.vNodo)
        t+='\n}'
        with open('reporteAST.dot', "w") as f:
                f.write(t)
    else:
        with open('reporteAST.dot', "w") as f:
                f.write('digraph G {\"No hay instrucciones\"}')

def dibujo(n):
    t=''
    for i in n.hijos:
        t+='node'+i.nNodo+'[label=\"'+i.vNodo+'\"];\n'
        t+='node'+n.nNodo+' -> node'+i.nNodo+';\n'
        t+=dibujo(i)
    return t



class Ventana:

    def __init__(self, master):
        self.nVentanas = 0
        # cuerpo general del frame----------------------------
        topFrame = Frame(master)
        topFrame.pack()
        bottomFrame = Frame(master)
        bottomFrame.pack(side=BOTTOM)
        # fin cuerpo general del frame------------------------
        # topFrame-----------------------------------------------------------------------------------------------
        # menu----------------------------
        barraMenu = Menu(master)
        master.config(menu=barraMenu)

        menuArchivos = Menu(barraMenu)
        menuColores = Menu(barraMenu)
        menuDebug = Menu(barraMenu)
        menuAyuda = Menu(barraMenu)
        menuReportes=Menu(barraMenu)

        barraMenu.add_cascade(label="Archivo", menu=menuArchivos)
        barraMenu.add_cascade(label="Colores", menu=menuColores)
        barraMenu.add_cascade(label="Debugger", menu=menuDebug)
        barraMenu.add_cascade(label="Reportes",menu=menuReportes)
        barraMenu.add_cascade(label="Ayuda", menu=menuAyuda)
        

        menuArchivos.add_command(label="Nuevo", command=self.nuevo)
        menuArchivos.add_command(label="Abrir...", command=self.abrir)
        menuArchivos.add_command(label="Guardar", command=self.guardar)
        menuArchivos.add_command(label="Guardar como...", command=self.guardarComo)
        menuArchivos.add_separator()
        menuArchivos.add_command(label="Salir", command=self.salir)

        menuColores.add_command(label="original", command=self.color1)
        menuColores.add_command(label="negro", command=self.color2)
        menuColores.add_command(label="azul", command=self.color3)
        menuColores.add_command(label="morado", command=self.color4)

        menuDebug.add_command(label="debuggear", command=self.debugg)

        menuReportes.add_command(label='Todos los Errores',command=self.repoErrores)
        menuReportes.add_separator()
        menuReportes.add_command(label="Errores Lexicos", command=self.errLex)
        menuReportes.add_command(label="Errores Sintacticos", command=self.errSin)
        menuReportes.add_command(label="Errores Semanticos", command=self.errSem)
        menuReportes.add_separator()
        menuReportes.add_command(label="Tabla de Simbolos", command=self.tbSimb)
        menuReportes.add_command(label="AST",command=self.astRepo)
        menuReportes.add_command(label="Reporte Gramatical", command=self.repoGram)


        menuAyuda.add_command(label="ayuda", command=self.ayuda)
        menuAyuda.add_command(label="Sobre nosotros", command=self.aboutus)

        # fin menu------------------------

        txtTitulo1 = Label(topFrame, text="Proyecto 1: AUGUS")
        txtTitulo1.config(font=("Arial", 24))

        txtTitulo1.grid(row=2, columnspan=2)

        # editor-------------------
        # ventanas---
        self.ventanas = ttk.Notebook(topFrame)
        #self.ventanas.add(self.editor, text='ventana0', padding=10)
        self.ventanas.grid(row=3, columnspan=2, pady=10, padx=10)
        self.ventanas.focus()
        # boton tipo de analizador------------
        self.esDescendente = BooleanVar()
        aDescendente = Checkbutton(topFrame, text="Ejecutar de forma Descendente", onvalue=True,
                                   offvalue=False, variable=self.esDescendente)
        aDescendente.grid(row=5, column=1)
        # fin topFrame-------------------------------------------------------------------------------------------

        # bottomFrame--------------------------------------------------------------------------------------------
        txtTitulo2 = Label(bottomFrame, text="Salida:")
        txtTitulo2.config(font=("Arial", 20))
        txtTitulo2.grid(row=0)

        # salida---------------------
        self.salida = scrolledtext.ScrolledText(bottomFrame, undo=True, width=80, height=10,
                                                wrap=WORD, bg="black",
                                                fg="light green",
                                                insertbackground='light green')

        # este tambien funciona como append
        self.salida.insert(INSERT, "Output:\n")
        self.salida['font'] = ('consolas', 12)
        self.salida.focus()
        self.salida.grid(row=2, columnspan=2, pady=10, padx=10)
        # salida.delete('1.0', END) # limpiar consola
        # finSalida------------------
        # botones etc-----------------------------------------------
        self.btnEjecutar = Button(topFrame, text="Ejecutar", bg="light sky blue", fg="black",
                                  font=("Arial", 12), command=self.ejecutar)
        self.btnEjecutar.grid(row=5, column=0)

        self.btnNext = Button(topFrame, text="Next", bg="light gray", fg="black",
                                  font=("Arial", 12),state=DISABLED,command=self.nextDebug)
        self.btnNext.grid(row=6, column=1)

    def getTextoActual(self):
        return self.ventanas._nametowidget(self.ventanas.tabs()[self.ventanas.index("current")]).winfo_children()[1].get(1.0, END)

    def ejecutar(self):
        if not (len(self.ventanas.tabs()) != 0 and len(rutas) > self.ventanas.index('current')):
            tkinter.messagebox.showerror(
                "Error", "No se encontro consola de entrada de texto")
            return

        txtEntrada = self.getTextoActual()
        if len(txtEntrada)<=1:
            return
        self.salida.delete('1.0', END)
        self.salida.insert(INSERT, "Output:\n")

        if(self.esDescendente.get()):
            self.salida.insert(INSERT, txtEntrada)
            print("Descendente")
        else:
            g1.resetLerr()
            g1.resetNonodo()
            resultado=g1.parse(txtEntrada)
            Ejec(resultado,self.salida,g1.Lerr)
        if len(g1.Lerr)>0:
            tkinter.messagebox.showerror(
                "Error", "Se encontraron errores al ejecutar")
            s = Source.from_file("reporteErrores.dot", format="pdf")
            s.view()


    def nuevo(self):
        editor = scrolledtext.ScrolledText(
            undo=True, width=80, height=10, wrap=WORD)
        editor['font'] = ('consolas', 12)
        editor.focus()
        t0 = 'Nuevo'+str(self.nVentanas)
        self.ventanas.add(editor, text=t0, padding=10)
        self.nVentanas += 1
        rutas.append(t0+'.txt')

    def abrir(self):
        ftypes = [('All files', '*')]
        dlg = filedialog.Open(filetypes=ftypes)
        fl = dlg.show()
        if fl != '':
            with open(fl, "r") as f:
                text = f.read()
                editor = scrolledtext.ScrolledText(
                    undo=True, width=80, height=10, wrap=WORD)
                editor['font'] = ('consolas', 12)
                editor.insert(INSERT, text)
                editor.focus()
                self.ventanas.add(editor, text=fl, padding=10)
                self.nVentanas += 1
                rutas.append(fl)


    def guardar(self):
        if(len(self.ventanas.tabs()) != 0 and len(rutas) > self.ventanas.index('current')):
            with open(rutas[self.ventanas.index('current')], "w") as f:
                f.write(self.getTextoActual())
        else:
            tkinter.messagebox.showerror(
                "Error", "se encontro un error al guardar")

    def guardarComo(self):
        r=filedialog.asksaveasfilename()
        if r!="" and (len(self.ventanas.tabs()) != 0 and len(rutas) > self.ventanas.index('current')):
            with open(r, "w") as f:
                f.write(self.getTextoActual())
            rutas[self.ventanas.index('current')]=r
            self.ventanas.tab(self.ventanas.tabs()[self.ventanas.index("current")],text=r)
        else:
            tkinter.messagebox.showerror(
                "Error", "se encontro un error al guardar")

    def salir(self):
        ventana1.destroy()

    def color1(self):
        self.ventanas._nametowidget(self.ventanas.tabs()[self.ventanas.index(
            "current")]).winfo_children()[1].config(background="white")

    def color2(self):
        self.ventanas._nametowidget(self.ventanas.tabs()[self.ventanas.index(
            "current")]).winfo_children()[1].config(background="gray")

    def color3(self):
        self.ventanas._nametowidget(self.ventanas.tabs()[self.ventanas.index(
            "current")]).winfo_children()[1].config(background="RoyalBlue1")

    def color4(self):
        self.ventanas._nametowidget(self.ventanas.tabs()[self.ventanas.index(
            "current")]).winfo_children()[1].config(background="MediumPurple1")

    def ayuda(self):
        help = tkinter.messagebox.askyesno(
            message="Desea consultar los manuales?", title="ayuda")
        if help:
            print('abrir manuales')
        else:
            print("ok, tu puedes")

    def aboutus(self):
        tkinter.messagebox.showinfo(
            message="Carlos Rodrigo Estrada Najarro\nCarnet: 201700314", title="About Us")

    def debugg(self):
        if not (len(self.ventanas.tabs()) != 0 and len(rutas) > self.ventanas.index('current')):
            tkinter.messagebox.showerror(
                "Error", "No se encontro consola de entrada de texto")
            return

        txtEntrada = self.getTextoActual()
        if len(txtEntrada)==0:
            return
        self.salida.delete('1.0', END)
        self.salida.insert(INSERT, "Output:\n")
        g1.resetLerr()
        g1.resetNonodo()
        resultado=g1.parse(txtEntrada)
        self.astDebug=Estaticos(self.salida,g1.Lerr,len(resultado))
        self.entornoDebug=Entorno()
        self.Ldebugger=resultado
        iEt=0
        try:
            while iEt<len(resultado):
                if(isinstance(resultado[iEt],newEtiqueta)):
                    self.entornoDebug.addEtiqueta(resultado[iEt].label_,iEt)
                iEt+=1
        except Exception as e:
            print('ventana[292] '+e)

        self.btnNext.config(state=NORMAL)

    def errLex(self):
        s = Source.from_file("reporteErroresLexicos.dot", format="pdf")
        s.view()
    def errSin(self):
        s = Source.from_file("reporteErroresSintacticos.dot", format="pdf")
        s.view()
    def errSem(self):
        s = Source.from_file("reporteErroresSemanticos.dot", format="pdf")
        s.view()
    def tbSimb(self):
        s = Source.from_file("reporteTs.dot", format="pdf")
        s.view()
    def astRepo(self):
        s = Source.from_file("reporteAST.dot", format="pdf")
        s.view()
    def repoGram(self):
        print("repo gramatica")
    def repoErrores(self):
        s = Source.from_file("reporteErrores.dot", format="pdf")
        s.view()
    def nextDebug(self):
        try:
            if self.astDebug.i<len(self.Ldebugger):
                self.Ldebugger[self.astDebug.i].ejecutar(self.entornoDebug,self.astDebug)
                self.astDebug.i+=1
            else:
                self.btnNext.config(state=DISABLED)
                graphAST(self.Ldebugger)                
        except Exception as e:
            print(str(e)+'ventana[314]')
            self.astDebug.i+=1
        # generar reportes de errores, y graficar el arbol
        gReporteErr(self.astDebug.Lerrores)
        gReporteTs(self.entornoDebug.tabla.items())


# loop------------------------------------------------
ventana1 = Tk()
ventana1.title('Proyecto1')
v0 = Ventana(ventana1)
ventana1.mainloop()
# endLoop---------------------------------------------
