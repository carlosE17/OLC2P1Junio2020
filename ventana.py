from tkinter import *
import tkinter.scrolledtext as scrolledtext
import tkinter.ttk as ttk
import tkinter.messagebox
from tkinter import filedialog

rutas=[]


class Ventana:
    
    def __init__(self, master):
        self.nVentanas=0
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

        barraMenu.add_cascade(label="Archivo", menu=menuArchivos)
        barraMenu.add_cascade(label="Colores", menu=menuColores)
        barraMenu.add_cascade(label="Debugger", menu=menuDebug)
        barraMenu.add_cascade(label="Ayuda", menu=menuAyuda)

        menuArchivos.add_command(label="Nuevo",command=self.nuevo)
        menuArchivos.add_command(label="Abrir...",command=self.abrir)
        menuArchivos.add_command(label="Guardar",command=self.guardar)
        menuArchivos.add_command(label="Guardar como...",command=self.guardarComo)
        menuArchivos.add_separator()
        menuArchivos.add_command(label="Salir",command=self.salir)

        menuColores.add_command(label="original",command=self.color1)
        menuColores.add_command(label="negro",command=self.color2)
        menuColores.add_command(label="azul",command=self.color3)
        menuColores.add_command(label="morado",command=self.color4)

        menuDebug.add_command(label="debuggear",command=self.debugg)

        menuAyuda.add_command(label="ayuda",command=self.ayuda)
        menuAyuda.add_command(label="Sobre nosotros",command=self.aboutus)

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

        # fin botones etc-------------------------------------------

        # vamos a pasar la consola para que asi siempre se trabaje sobre la misma
        # def addtext(c,t):
        #     c.insert(INSERT,str(t)+'\n')
        # addtext(salida,'prueba')

        # fin bottomFrame----------------------------------------------------------------------------------------

    def getTextoActual(self):
        return self.ventanas._nametowidget(self.ventanas.tabs()[self.ventanas.index("current")]).winfo_children()[1].get(1.0,END)

    def ejecutar(self):
        txtEntrada=self.getTextoActual()
        print(self.esDescendente.get())
        if(self.esDescendente.get()):
            self.salida.insert(INSERT, txtEntrada)
            print("Descendente")
        else:
            self.salida.insert(INSERT, txtEntrada)
            print("ascendente")

    def nuevo(self):
        editor = scrolledtext.ScrolledText(undo=True, width=80, height=10,wrap=WORD)
        editor['font'] = ('consolas', 12)
        editor.focus()
        t0='Nuevo'+str(self.nVentanas)
        self.ventanas.add(editor, text=t0, padding=10)
        self.nVentanas+=1
        rutas.append(t0+'.txt')

    def abrir(self):
        ftypes = [('Python files', '*.py'), ('All files', '*')]
        dlg = filedialog.Open( filetypes = ftypes)
        fl = dlg.show()
        if fl != '':
            text = open(fl,"r").read()
            editor = scrolledtext.ScrolledText(undo=True, width=80, height=10,wrap=WORD)
            editor['font'] = ('consolas', 12)
            editor.insert(INSERT,text)
            editor.focus()
            self.ventanas.add(editor, text=fl, padding=10)
            self.nVentanas+=1
            rutas.append(fl)
        print('abrir')

    def guardar(self):
        print('guardar')

    def guardarComo(self):
        print('guardar como...')


    def salir(self):
        ventana1.destroy()

    def color1(self):
        self.ventanas._nametowidget(self.ventanas.tabs()[self.ventanas.index("current")]).winfo_children()[1].config( background="white")
        
    def color2(self):
        self.ventanas._nametowidget(self.ventanas.tabs()[self.ventanas.index("current")]).winfo_children()[1].config( background="gray")

    def color3(self):
        self.ventanas._nametowidget(self.ventanas.tabs()[self.ventanas.index("current")]).winfo_children()[1].config( background="RoyalBlue1")

    def color4(self):
        self.ventanas._nametowidget(self.ventanas.tabs()[self.ventanas.index("current")]).winfo_children()[1].config( background="MediumPurple1")


    def ayuda(self):
        help=tkinter.messagebox.askyesno(message="Desea consultar los manuales?", title="ayuda")
        if help:
            print('abrir manuales')
        else:
            print("ok, tu puedes")

    def aboutus(self):
        tkinter.messagebox.showinfo(message="Carlos Rodrigo Estrada Najarro\nCarnet: 201700314", title="About Us")

    def debugg(self):
        print('debugg')


# loop------------------------------------------------
ventana1 = Tk()
ventana1.title('Proyecto1')
v0 = Ventana(ventana1)
ventana1.mainloop()
# endLoop---------------------------------------------
