from tkinter import *
from tkinter import ttk
import math

def darkMode(*args):
    entrada.set("")
    entrada1.set("")
    styles.configure("mainframe.TFrame", background="#010924")
    styles.configure("Label.TLabel", background="#010924", foreground="#FFFFFF")
    styles.configure("Labell.TLabel", background="#010924", foreground="#FFFFFF")

    styles.configure("estilos_numeros.TButton", background="#00044A", foreground="white")
    styles.map("estilos_numeros.TButton", background=[("active", "#020A90")])
    
    styles.configure("borrar_botones.TButton", background="#010924", foreground="white")
    styles.map("borrar_botones.TButton", background=[("active", "#000AB1")])
    
    styles.configure("botones_restantes.TButton", background="#010924", foreground="white")
    styles.map("botones_restantes.TButton", background=[("active", "#000AB1")])

def calmMode(*args):
    
    entrada.set("")
    entrada1.set("")
    
    styles.configure("mainframe.TFrame", background="#DBDBDB", foreground="black")
    styles.configure("Label.TLabel", background="#DBDBDB", foreground="black")
    styles.configure("Labell.TLabel", background="#DBDBDB", foreground="black")
    
    styles.configure("estilos_numeros.TButton", background="#FFFFFF", foreground="black")
    styles.map("estilos_numeros.TButton", background=[("active","#B9B9B9")])
    
    styles.configure("borrar_botones.TButton", background="#CECECE", foreground="black")
    styles.map("borrar_botones.TButton", foreground=[("active", "#FF0000")], background=[("active", "#858585")])
    
    styles.configure("botones_restantes.TButton", background="#CECECE", foreground="black")
    styles.map("botones_restantes.TButton",background=[("active", "#858585")])


#Ingresar valores
def ingresarValor(tecla):
    if tecla >= "0" and tecla <= "9" or tecla == "(" or tecla == ")" or tecla == ".":
        entrada1.set(entrada1.get()+tecla)
        
    if tecla == "x" or tecla == "/" or tecla == "+" or tecla == "-":
        if tecla == "+":
            entrada.set(entrada1.get()+"+")
        elif tecla == "-":
            entrada.set(entrada1.get()+"-")
        elif tecla == "/":
            entrada.set(entrada1.get()+"/")
        elif tecla == "x":
            entrada.set(entrada1.get()+"*")
            
        entrada1.set("")
        
    if tecla == "=":
            contador = 0
            if contador == 0:
                print(contador)
                entrada.set(entrada.get()+ entrada1.get())
                resultado = eval(entrada.get())
                entrada1.set(resultado)
                contador = contador+1
                
def escribirTeclado(event):
    tecla = event.char
    tecla_presionada = event.keysym
    print(tecla_presionada)
   
    
    if tecla_presionada == "BackSpace":
        entrada1.set(entrada1.get()[:-1])
        
    if tecla_presionada == "Return":
            contador = 0
            if contador == 0:
                entrada.set(entrada.get()+ entrada1.get())
                resultado = eval(entrada.get())
                entrada1.set(resultado)
                contador = contador + 1  
                    
    if tecla >= "0" and tecla <= "9" or tecla == "(" or tecla == ")" or tecla == ".":
        entrada1.set(entrada1.get()+tecla)

    if tecla == "*" or tecla == "/" or tecla == "+" or tecla == "-":
        if tecla == "+":
            entrada.set(entrada1.get()+"+")
        elif tecla == "-":
            entrada.set(entrada1.get()+"-")
        elif tecla == "/":
            entrada.set(entrada1.get()+"/")
        elif tecla_presionada == "asterisk":
            entrada.set(entrada1.get()+"*")
            
        entrada1.set("")
            
def raizCuadrada():
   entrada.set("")
   resultado = math.sqrt(float(entrada1.get()))
   entrada1.set(resultado)
   
def borrarTecla():
    inicio = 0
    final = entrada1.get()
    entrada1.set(entrada1.get()[:-1])

def borrarTodo():
    entrada.set("")
    entrada1.set("")

# El root es el contenedor de la app
root = Tk()

#Determinando el nombre que tendra en el contenedor
root.title("Calculadora")

#Determinando la posicio del contenedor en los ejes x Y y
root.geometry("+500+80")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

#Estilos del frame
styles = ttk.Style()
styles.theme_use("clam")
styles.configure("mainframe.TFrame", background="#DBDBDB")

#El frame es la base de la calculadora
mainframe = ttk.Frame(root, style="mainframe.TFrame")

#Espacio que va a ocupar el mainframe dentro del contenedor
mainframe.grid(column=0, row=0, sticky=(W, N, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.columnconfigure(1, weight=1)
mainframe.columnconfigure(2, weight=1)
mainframe.columnconfigure(3, weight=1)
mainframe.columnconfigure(4, weight=2)
mainframe.columnconfigure(5, weight=2)

mainframe.rowconfigure(0, weight=1)
mainframe.rowconfigure(1, weight=1)
mainframe.rowconfigure(2, weight=1)
mainframe.rowconfigure(3, weight=1)
mainframe.rowconfigure(4, weight=1)
mainframe.rowconfigure(5, weight=1)
mainframe.rowconfigure(6, weight=1)
mainframe.rowconfigure(7, weight=1)
#Estilos label
styles.configure("Label.TLabel", font="arial 15", ANCHOR="e")

#Entrada sera el valor que se mostrara en el label
entrada =  StringVar()
label_entrada = ttk.Label(mainframe, textvariable=entrada, style="Label.TLabel")
label_entrada.grid(column=0, row=0, columnspan=4, sticky=("W,E"))

#Estilos label 1
styles.configure("Labell.TLabel", font="arial 40", ANCHOR="e")

entrada1 = StringVar()
label_entrada1 = ttk.Label(mainframe, textvariable=entrada1, style="Labell.TLabel")
label_entrada1.grid(column=0, row=1, columnspan=4, sticky=("W,E"))

#Historial de operaciones
historial_entrada = StringVar()
historial = ttk.Label(mainframe, textvariable=historial_entrada)
historial.grid(column=4, row=2 , columnspan=2)
styles.configure("historial.TLabel", font="arial 27", ANCHOR="e")

#Estilos Botones

styles.configure("estilos_numeros.TButton", font="arial 22", width=5, background="#FFFFFF", relief=FLAT)
styles.configure("borrar_botones.TButton", font="arial 22", width=5, background="#CECECE", relief=FLAT)
styles.configure("botones_restantes.TButton", font="arial 22", width=5, background="#CECECE", relief=FLAT)

#Aplicar estilo a los botones de borrar cuando el mouse este por encima, foreground para el texto y background para el boton completo
styles.map("borrar_botones.TButton", foreground=[("active", "#FF0000")], background=[("active", "#858585")])
styles.map("estilos_numeros.TButton", background=[("active","#B9B9B9")])
styles.map("botones_restantes.TButton",background=[("active", "#858585")])

#Botones
btn0 = ttk.Button(mainframe, text="0",style="estilos_numeros.TButton" ,command=lambda: ingresarValor("0"))
btn1 = ttk.Button(mainframe, text="1",style="estilos_numeros.TButton", command=lambda: ingresarValor("1"))
btn2 = ttk.Button(mainframe, text="2",style="estilos_numeros.TButton", command=lambda: ingresarValor("2"))
btn3 = ttk.Button(mainframe, text="3",style="estilos_numeros.TButton" ,command=lambda: ingresarValor("3"))
btn4 = ttk.Button(mainframe, text="4",style="estilos_numeros.TButton", command=lambda: ingresarValor("4"))
btn5 = ttk.Button(mainframe, text="5",style="estilos_numeros.TButton", command=lambda: ingresarValor("5"))
btn6 = ttk.Button(mainframe, text="6",style="estilos_numeros.TButton", command=lambda: ingresarValor("6"))
btn7 = ttk.Button(mainframe, text="7",style="estilos_numeros.TButton" ,command=lambda: ingresarValor("7"))
btn8 = ttk.Button(mainframe, text="8",style="estilos_numeros.TButton" ,command=lambda: ingresarValor("8"))
btn9 = ttk.Button(mainframe, text="9", style="estilos_numeros.TButton" ,command=lambda: ingresarValor("9"))

btn_borrar = ttk.Button(mainframe, text=chr(9003), style="borrar_botones.TButton", command=lambda:borrarTecla())
btn_borrar_todo = ttk.Button(mainframe, text="C", style="borrar_botones.TButton", command=lambda:borrarTodo())
btn_parentesis1 = ttk.Button(mainframe, text="(", style="botones_restantes.TButton", command=lambda:ingresarValor("("))
btn_parentesis2 = ttk.Button(mainframe, text=")", style="botones_restantes.TButton", command=lambda:ingresarValor(")"))
btn_punto = ttk.Button(mainframe, text=".", style="botones_restantes.TButton", command=lambda:ingresarValor("."))

#botones para operaciones
btn_suma = ttk.Button(mainframe, text="+", style="botones_restantes.TButton", command=lambda:ingresarValor("+"))
btn_resta = ttk.Button(mainframe, text="-", style="botones_restantes.TButton", command=lambda:ingresarValor("-"))
btn_dividir = ttk.Button(mainframe, text=chr(247), style="botones_restantes.TButton", command=lambda:ingresarValor("/"))
btn_multiplicar = ttk.Button(mainframe, text="x", style="botones_restantes.TButton", command=lambda:ingresarValor("x"))

btn_igual = ttk.Button(mainframe, text="=", style="botones_restantes.TButton", command=lambda:ingresarValor("="))
btn_raiz = ttk.Button(mainframe, text="√", style="botones_restantes.TButton", command=lambda:raizCuadrada())

#Declarando posicion de los botones
btn_parentesis1.grid(column=0,row=2, sticky=(W,E,N,S))
btn_parentesis2.grid(column=1, row=2, sticky=(W,E,N,S))
btn_borrar_todo.grid(column=2, row=2, sticky=(W,E,N,S))
btn_borrar.grid(column=3, row=2, sticky=(W,E,N,S))

btn7.grid(column=0,row=3, sticky=(W,E,N,S))
btn8.grid(column=1, row=3, sticky=(W,E,N,S))
btn9.grid(column=2, row=3, sticky=(W,E,N,S))
btn_dividir.grid(column=3, row=3, sticky=(W,E,N,S))

btn4.grid(column=0, row=4, sticky=(W,E,N,S))
btn5.grid(column=1, row =4, sticky=(W,E,N,S))
btn6.grid(column=2, row=4, sticky=(W,E,N,S))
btn_multiplicar.grid(column=3, row=4, sticky=(W,E,N,S))

btn1.grid(column=0, row=5, sticky=(W,E,N,S))
btn2.grid(column=1, row=5, sticky=(W,E,N,S))
btn3.grid(column=2, row=5,sticky=(W,E,N,S))
btn_suma.grid(column=3, row=5, sticky=(W,E,N,SE))

btn0.grid(column=0, row=6, columnspan=2, sticky=(W,E,N,S))
btn_punto.grid(column=2, row=6, sticky=(W,E,N,S))
btn_resta.grid(column=3, row=6, sticky=(W,E,N,S))

btn_igual.grid(column=0, row=7, columnspan=3, sticky=(W,E,N,S))
btn_raiz.grid(column=3, row=7, sticky=(W,E,N,S))

for child in mainframe.winfo_children():
    child.grid_configure(ipady=10, padx=1, pady=1)


root.bind("<Key>", escribirTeclado)
root.bind("<KeyPress-o>", darkMode)
root.bind("<KeyPress-c>", calmMode)
root.mainloop()