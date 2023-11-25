from tkinter import Tk, Button, Entry, Label

# Funciones para realizar las operaciones

def sumar():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    resultado = num1 + num2
    label_resultado.config(text="Resultado: " + str(resultado))

def restar():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    resultado = num1 - num2
    label_resultado.config(text="Resultado: " + str(resultado))

def multiplicar():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    resultado = num1 * num2
    label_resultado.config(text="Resultado: " + str(resultado))

def dividir():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    if num2 != 0:
        resultado = num1 / num2
        label_resultado.config(text="Resultado: " + str(resultado))
    else:
        label_resultado.config(text="Error: No se puede dividir entre cero")

# Crear la ventana de la calculadora
ventana = Tk()
ventana.title("Calculadora")

# Crear los elementos de la interfaz
label_num1 = Label(ventana, text="Número 1:")
label_num1.grid(row=0, column=0)

entry_num1 = Entry(ventana)
entry_num1.grid(row=0, column=1)

label_num2 = Label(ventana, text="Número 2:")
label_num2.grid(row=1, column=0)

entry_num2 = Entry(ventana)
entry_num2.grid(row=1, column=1)

btn_sumar = Button(ventana, text="Sumar", command=sumar)
btn_sumar.grid(row=2, column=0)

btn_restar = Button(ventana, text="Restar", command=restar)
btn_restar.grid(row=2, column=1)

btn_multiplicar = Button(ventana, text="Multiplicar", command=multiplicar)
btn_multiplicar.grid(row=3, column=0)

btn_dividir = Button(ventana, text="Dividir", command=dividir)
btn_dividir.grid(row=3, column=1)

label_resultado = Label(ventana, text="Resultado:")
label_resultado.grid(row=4, column=0, columnspan=2)

# Ejecutar el bucle principal de la ventana
ventana.mainloop()