from tkinter import *
from math import * 
from cmath import sqrt #con math no puedes sqrt(-n)

#------- Config de la ventana ------

root = Tk()
root.title("Cal323")
root.resizable(False,False)
root.geometry("245x280+600+250")
root.iconbitmap("323factory.ico")
root.config(bg="darkred")

framelbl = Frame(root, bg="darkred")
framelbl.pack(side=TOP)

frame = Frame(root, bg="darkred")
#frame.pack()
frame.place(x=10,y=30)

#------------- Funciones -----------

def numPulsado(num):

	if len(numPantalla.get())<23:
	
		if num == 0:
			if numPantalla.get() != "":
				temp = numPantalla.get()
				
				if "0" in temp[0]:
					try:
						if "." in temp[1]:
							numPantalla.set(numPantalla.get() + str(num))
					
					except:
						pass

				else:
					numPantalla.set(numPantalla.get() + str(num))
			else:
				numPantalla.set(str(num))

		elif num == ".":
			if numPantalla.get() != "":

				yaEsta = False
				for x in numPantalla.get():
					if x == ".":
						yaEsta = True

				if yaEsta == False:
					numPantalla.set(numPantalla.get() + str(num))
		
		elif num == pi:
			if numPantalla.get() == "":
				numPantalla.set(str(num))

		elif num == e:
			if numPantalla.get() == "":
				numPantalla.set(str(num))

		else:
			if numPantalla.get() != "":
				temp = numPantalla.get()

				if "0" in temp[0]:
					try:
						if "." in temp[1]:
							numPantalla.set(numPantalla.get() + str(num))
						else:
							numPantalla.set(str(num)) #remplazamos el 0 por el número
					except:
						numPantalla.set(str(num)) #remplazamos el 0 por el número
				else:
					numPantalla.set(numPantalla.get() + str(num))
			else:
				numPantalla.set(str(num))

def borrarPantalla():
	numPantalla.set("")

def reset():
	numGuardado.set("")
	numPantalla.set("")
	lblInfo.set("")

def backPantalla():
	temp = numPantalla.get()
	temp = temp[0:-1]
	numPantalla.set(temp)

def porcentaje():
	if numGuardado.get() != "":

		if operadorGuardado.get() == "/":
			numTemp = float(numPantalla.get())/100
			lblInfo.set(lblInfo.get()+" "+str(numTemp)+" = ")

			if numPantalla.get() == "0":
				numPantalla.set("NaN") #Not a Number
			else:
				numTemp = float(numGuardado.get())/numTemp
				numPantalla.set(numTemp)

		elif operadorGuardado.get() == "x":
			numTemp = float(numPantalla.get())/100
			lblInfo.set(lblInfo.get()+" "+str(numTemp)+" = ")
			numTemp = float(numGuardado.get())*numTemp
			numPantalla.set(numTemp)

		elif operadorGuardado.get() == "-":
			numTemp = float(numGuardado.get())*float(numPantalla.get())/100
			lblInfo.set(lblInfo.get()+" "+str(numTemp)+" = ")
			numTemp = float(numGuardado.get())-numTemp
			numPantalla.set(numTemp)

		elif operadorGuardado.get() == "+":
			numTemp = float(numGuardado.get())*float(numPantalla.get())/100
			lblInfo.set(lblInfo.get()+" "+str(numTemp)+" = ")
			numTemp = float(numGuardado.get())+numTemp
			numPantalla.set(numTemp)

		operadorGuardado.set("")

def inverso():
	if numPantalla.get() != "":
		lblInfo.set("1 / "+numPantalla.get()+" =")
		temp = 1/float(numPantalla.get())
		numPantalla.set(temp)

def potencia():
	if numPantalla.get() != "":
		lblInfo.set(numPantalla.get()+"^2 =")
		temp = float(numPantalla.get())**2
		numPantalla.set(temp)

def raizCuadrada():
	if numPantalla.get() != "":
		lblInfo.set("sqrt("+numPantalla.get()+") =")
		temp = sqrt(float(numPantalla.get()))
		numPantalla.set(temp)

def dividir():
	if numPantalla.get() != "":
		if operadorGuardado.get() == "":
			numGuardado.set(numPantalla.get())
			numPantalla.set("")
			operadorGuardado.set("/")

			lblInfo.set(numGuardado.get()+" "+operadorGuardado.get())

		else:
			operadorAnterior.set("/")
			resultado()

def multiplicar():
	if numPantalla.get() != "":
		if operadorGuardado.get() == "":
			numGuardado.set(numPantalla.get())
			numPantalla.set("")
			operadorGuardado.set("x")

			lblInfo.set(numGuardado.get()+" "+operadorGuardado.get())

		else:
			operadorAnterior.set("x")
			resultado()

def restar():
	if numPantalla.get() != "":
		if operadorGuardado.get() == "":
			numGuardado.set(numPantalla.get())
			numPantalla.set("")
			operadorGuardado.set("-")

			lblInfo.set(numGuardado.get()+" "+operadorGuardado.get())

		else:
			operadorAnterior.set("-")
			resultado()

def sumar():
	if numPantalla.get() != "":
		if operadorGuardado.get() == "":
			numGuardado.set(numPantalla.get())
			numPantalla.set("")
			operadorGuardado.set("+")

			lblInfo.set(numGuardado.get()+" "+operadorGuardado.get())

		else:
			operadorAnterior.set("+")
			resultado()


def resultado():
	if numGuardado.get() != "":
		
		if operadorGuardado.get() == "/":
			lblInfo.set(lblInfo.get()+" "+numPantalla.get()+" = ")

			if numPantalla.get() == "0":
				numPantalla.set("NaN") #Not a Number
			else:
				numTemp = float(numGuardado.get())/float(numPantalla.get())
				numPantalla.set(numTemp)

		elif operadorGuardado.get() == "x":
			lblInfo.set(lblInfo.get()+" "+numPantalla.get()+" = ")
			
			numTemp = float(numGuardado.get())*float(numPantalla.get())
			numPantalla.set(numTemp)

		elif operadorGuardado.get() == "-":
			lblInfo.set(lblInfo.get()+" "+numPantalla.get()+" = ")
			
			numTemp = float(numGuardado.get())-float(numPantalla.get())
			numPantalla.set(numTemp)

		elif operadorGuardado.get() == "+":
			lblInfo.set(lblInfo.get()+" "+numPantalla.get()+" = ")
			
			numTemp = float(numGuardado.get())+float(numPantalla.get())
			numPantalla.set(numTemp)

		elif operadorGuardado.get() == "mod":
			lblInfo.set(lblInfo.get()+" "+numPantalla.get()+" = ")
			
			numTemp = fmod(float(numGuardado.get()),float(numPantalla.get())) # fmod() is generally preferred when working with floats, while Python’s x % y is preferred when working with integers.
			numPantalla.set(numTemp)

		elif operadorGuardado.get() == "^":
			lblInfo.set(lblInfo.get()+numPantalla.get()+" = ")
			
			numTemp = float(numGuardado.get())**float(numPantalla.get())
			numPantalla.set(numTemp)

		elif operadorGuardado.get() == "GCD":
			lblInfo.set(lblInfo.get()+" & "+numPantalla.get()+" = ")
			try:
				numTemp = gcd(int(numGuardado.get()), int(numPantalla.get()))
				numPantalla.set(numTemp)
			except:
				numPantalla.set("NaN")


		operadorGuardado.set("")

		if operadorAnterior.get() == "/":
			operadorAnterior.set("")
			dividir()

		elif operadorAnterior.get() == "x":
			operadorAnterior.set("")
			multiplicar()

		elif operadorAnterior.get() == "-":
			operadorAnterior.set("")
			restar()

		elif operadorAnterior.get() == "+":
			operadorAnterior.set("")
			sumar()

		elif operadorAnterior.get() == "mod":
			operadorAnterior.set("")
			calcularMod()

		elif operadorAnterior.get() == "^":
			operadorAnterior.set("")
			potencia_xY()

		elif operadorAnterior.get() == "GCD":
			operadorAnterior.set("")
			calcularGCD()


def masMenos():
	if numPantalla.get() != "":

		if "-" in numPantalla.get():
			temp = numPantalla.get()
			temp = temp[1:len(temp)]
			numPantalla.set(temp)
		else:
			numPantalla.set("-"+numPantalla.get())


def calcularMod():
	if numPantalla.get() != "":
		if operadorGuardado.get() == "":
			numGuardado.set(numPantalla.get())
			numPantalla.set("")
			operadorGuardado.set("mod")

			lblInfo.set(numGuardado.get()+" "+operadorGuardado.get())

		else:
			operadorAnterior.set("mod")
			resultado()

def potencia_xY():
	if numPantalla.get() != "":
		if operadorGuardado.get() == "":
			numGuardado.set(numPantalla.get())
			numPantalla.set("")
			operadorGuardado.set("^")

			lblInfo.set(numGuardado.get()+operadorGuardado.get())

		else:
			operadorAnterior.set("^")
			resultado()

def calcularGCD():
	if numPantalla.get() != "":
		if operadorGuardado.get() == "":
			numGuardado.set(numPantalla.get())
			numPantalla.set("")
			operadorGuardado.set("GCD")

			lblInfo.set(operadorGuardado.get()+":"+numGuardado.get())

		else:
			operadorAnterior.set("GCD")
			resultado()



def calcularFactorial():
	if numPantalla.get() != "":
		lblInfo.set(numPantalla.get()+"! =")
		try:
			temp = factorial(int(numPantalla.get()))
			numPantalla.set(temp)
		except ValueError:
			numPantalla.set("NaN")

def logaritmo():
	if numPantalla.get() != "":
		lblInfo.set("log("+numPantalla.get()+") =")
		temp = log10(float(numPantalla.get()))
		numPantalla.set(temp)

def logNeperiano():
	if numPantalla.get() != "":
		lblInfo.set("ln("+numPantalla.get()+") =")
		temp = log(float(numPantalla.get()), e)
		numPantalla.set(temp)

def calcularSin():
	if numPantalla.get() != "":
		lblInfo.set("["+txtRadDeg.get()+"]  sin("+numPantalla.get()+") =")
		if txtRadDeg.get()=="DEG":
			temp = sin(radians(float(numPantalla.get())))
		else:
			temp = sin(float(numPantalla.get()))
		numPantalla.set(temp)

def calcularCos():
	if numPantalla.get() != "":
		lblInfo.set("["+txtRadDeg.get()+"]  cos("+numPantalla.get()+") =")
		if txtRadDeg.get()=="DEG":
			temp = cos(radians(float(numPantalla.get())))
		else:
			temp = cos(float(numPantalla.get()))
		numPantalla.set(temp)

def calcularTan():
	if numPantalla.get() != "":
		lblInfo.set("["+txtRadDeg.get()+"]  tan("+numPantalla.get()+") =")
		if txtRadDeg.get()=="DEG":
			temp = tan(radians(float(numPantalla.get())))
		else:
			temp = tan(float(numPantalla.get()))
		numPantalla.set(temp)

def changeRadDeg():
	if txtRadDeg.get() == "RAD":
		txtRadDeg.set("DEG")
	else:
		txtRadDeg.set("RAD")


#----- Variables de Texto -----

numGuardado = StringVar()
operadorGuardado = StringVar() #global operardor
operadorAnterior = StringVar()

#------------- Info ----------- row 0

lblInfo = StringVar()
lblInfo.set("323factory.com\n(máximo 23 carácteres)")
lbl = Label(framelbl, textvariable = lblInfo, fg="white", bg="darkred", justify = "center")
lbl.grid(row=0, column=0, padx=0)
lbl.config(font=("Courier New",8), wraplength=250)

#------------- Pantalla ----------- row 1

numPantalla = StringVar()

pantalla = Entry(frame, textvariable = numPantalla, state="disabled")
pantalla.grid(row=1, column=0, padx=0, pady=10, columnspan=6)
pantalla.config(disabledbackground="white",disabledforeground="darkred", width=28, font=("Courier New",10),justify="right")

#------------ Fila Vars -----------

wdh = 4 # width
pdy = 5 # pady

#------------- Fila 2 -------------
rw = 2

btnGCD = Button(frame, text="GCD", width=wdh, pady=pdy, command=lambda:calcularGCD()) #greatest common divisor
btnMod = Button(frame, text="mod", width=wdh, pady=pdy, command=lambda:calcularMod())
btnPor = Button(frame, text="%", width=wdh, pady=pdy, command=lambda:porcentaje())
btnCE = Button(frame, text="CE", width=wdh, pady=pdy, command=lambda:borrarPantalla())
btnC  = Button(frame, text="C", width=wdh, pady=pdy, command=lambda:reset()) #+ borrar guardado
btnBa = Button(frame, text="<<", width=wdh, pady=pdy, command=lambda:backPantalla())

btnGCD.grid(row=rw, column=0)
btnMod.grid(row=rw, column=1)
btnPor.grid(row=rw, column=2)
btnCE.grid(row=rw, column=3)
btnC.grid(row=rw, column=4)
btnBa.grid(row=rw, column=5)

#------------- Fila 3 -------------
rw = 3
txtRadDeg = StringVar()
txtRadDeg.set("RAD")

btnRadDeg = Button(frame, textvariable=txtRadDeg, width=wdh, pady=pdy, command=lambda:changeRadDeg())
btnPotxY = Button(frame, text="x^Y", width=wdh, pady=pdy, command=lambda:potencia_xY())
btnInv  = Button(frame, text="1/x", width=wdh, pady=pdy, command=lambda:inverso())
btnPot = Button(frame, text="x^2", width=wdh, pady=pdy, command=lambda:potencia())
btnRai = Button(frame, text="sqrt", width=wdh, pady=pdy, command=lambda:raizCuadrada())
btnDi = Button(frame, text="/", width=wdh, pady=pdy, command=lambda:dividir())

btnRadDeg.grid(row=rw, column=0)
btnPotxY.grid(row=rw, column=1)
btnInv.grid(row=rw, column=2)
btnPot.grid(row=rw, column=3)
btnRai.grid(row=rw, column=4)
btnDi.grid(row=rw, column=5)

#------------- Fila 4 -------------
rw = 4

btne = Button(frame, text="e", width=wdh, pady=pdy, command=lambda:numPulsado(e))
btnPi = Button(frame, text="Pi", width=wdh, pady=pdy, command=lambda:numPulsado(pi))
btn7 = Button(frame, text="7", width=wdh, pady=pdy, command=lambda:numPulsado(7))
btn8 = Button(frame, text="8", width=wdh, pady=pdy, command=lambda:numPulsado(8))
btn9 = Button(frame, text="9", width=wdh, pady=pdy, command=lambda:numPulsado(9))
btnX = Button(frame, text="X", width=wdh, pady=pdy, command=lambda:multiplicar())

btne.grid(row=rw, column=0)
btnPi.grid(row=rw, column=1)
btn7.grid(row=rw, column=2)
btn8.grid(row=rw, column=3)
btn9.grid(row=rw, column=4)
btnX.grid(row=rw, column=5)

#------------- Fila 5 -------------
rw = 5

btnSin = Button(frame, text="sin", width=wdh, pady=pdy, command=lambda:calcularSin())
btnFact = Button(frame, text="n!", width=wdh, pady=pdy, command=lambda:calcularFactorial())
btn4  = Button(frame, text="4", width=wdh, pady=pdy, command=lambda:numPulsado(4))
btn5  = Button(frame, text="5", width=wdh, pady=pdy, command=lambda:numPulsado(5))
btn6  = Button(frame, text="6", width=wdh, pady=pdy, command=lambda:numPulsado(6))
btnMe = Button(frame, text="-", width=wdh, pady=pdy, command=lambda:restar())

btnSin.grid(row=rw, column=0)
btnFact.grid(row=rw, column=1)
btn4.grid(row=rw, column=2)
btn5.grid(row=rw, column=3)
btn6.grid(row=rw, column=4)
btnMe.grid(row=rw, column=5)


#------------- Fila 6 -------------
rw = 6

btnCos = Button(frame, text="cos", width=wdh, pady=pdy, command=lambda:calcularCos())
btnLog = Button(frame, text="Log", width=wdh, pady=pdy, command=lambda:logaritmo()) 
btn1  = Button(frame, text="1", width=wdh, pady=pdy, command=lambda:numPulsado(1))
btn2  = Button(frame, text="2", width=wdh, pady=pdy, command=lambda:numPulsado(2))
btn3  = Button(frame, text="3", width=wdh, pady=pdy, command=lambda:numPulsado(3))
btnMas = Button(frame, text="+", width=wdh, pady=pdy, command=lambda:sumar())

btnCos.grid(row=rw, column=0)
btnLog.grid(row=rw, column=1)
btn1.grid(row=rw, column=2)
btn2.grid(row=rw, column=3)
btn3.grid(row=rw, column=4)
btnMas.grid(row=rw, column=5)


#------------- Fila 7 -------------
rw = 7

btnTan = Button(frame, text="tan", width=wdh, pady=pdy, command=lambda:calcularTan())
btnLn = Button(frame, text="ln", width=wdh, pady=pdy, command=lambda:logNeperiano())
btnMm = Button(frame, text="+/-", width=wdh, pady=pdy, command=lambda:masMenos())
btn0  = Button(frame, text="0", width=wdh, pady=pdy, command=lambda:numPulsado(0))
btnP  = Button(frame, text=".", width=wdh, pady=pdy, command=lambda:numPulsado("."))
btnIg = Button(frame, text="=", width=wdh, pady=pdy, command=lambda:resultado())

btnTan.grid(row=rw, column=0)
btnLn.grid(row=rw, column=1)
btnMm.grid(row=rw, column=2)
btn0.grid(row=rw, column=3)
btnP.grid(row=rw, column=4)
btnIg.grid(row=rw, column=5)

#------------- end
root.mainloop()
