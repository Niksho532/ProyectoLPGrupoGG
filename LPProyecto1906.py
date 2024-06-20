# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 17:33:47 2024

@author: Personal
"""

import tkinter as tk
from tkinter import filedialog
import csv

# Variables globales
archivo = ""

# Cifrado César
def CifradoCesar(texto, desplazamiento):
    def EncriptarCaracter(char):
        if char.isalpha():
            valor = 65 if char.isupper() else 97
            return chr((ord(char) - valor + desplazamiento) % 26 + valor) #Se aplica la formula del cifrado cesar
        else:       
            return char
    resultado = "".join(map(EncriptarCaracter, texto))
    return resultado

"""def escribir_csv_con_cifrado(nombre_archivo, TextoCifrado, desplazamiento):
    #texto_cifrado = CifradoCesar(texto, desplazamiento)
    
    with open(nombre_archivo, mode='w', newline='') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        
        # Escribir contenido
        escritor_csv.writer(TextoCifrado)"""

# Cifrado Affine
def CifradoAffine(texto, a, b):
    def EncriptarCaracter(char):
        if char.isalpha():
            valor = 65 if char.isupper() else 97
            return chr(((a * (ord(char) - valor) + b) % 26) + valor) #Se aplica la formula del cifrado Affine
        else:
            return char

    resultado = "".join(map(EncriptarCaracter, texto)) #Con map se encripta cada caracter del texto y luego con join se junta en una sola cadena sin espacios
    return resultado

# Cifrado Mixto (Affine seguido de César)
def CifradoMixto(texto, a, b, desplazamiento):
    textoAffine = CifradoAffine(texto, a, b)
    return CifradoCesar(textoAffine, desplazamiento)

# Selección de archivo
def SelecArchivo():
    global archivo
    archivo = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if archivo:
        MostrarConten(archivo)

# Aplicar cifrado César
def Cesar():
    if archivo:
        texto = ObtenerTexto(archivo)
        TextoCifrado = CifradoCesar(texto, 3)  # Usando un desplazamiento de 3
        MostrarTextoCifrado(TextoCifrado)
        #escribir_csv_con_cifrado('TextoCesar', TextoCifrado, 3)
        #archivoCesar = open("ArchivoCesar.csv","w")
        #archivoCesar.write(TextoCifrado)
        #archivoCesar.close()

# Aplicar cifrado Affine
def Affine():
    if archivo:
        texto = ObtenerTexto(archivo)
        TextoCifrado = CifradoAffine(texto, 5, 8)  # Usando a=5 y b=8
        MostrarTextoCifrado(TextoCifrado)

# Aplicar cifrado Mixto
def Mixto():
    if archivo:
        texto = ObtenerTexto(archivo)
        TextoCifrado = CifradoMixto(texto, 5, 8, 3)  # Usando a=5, b=8 y desplazamiento=3
        MostrarTextoCifrado(TextoCifrado)

# Mostrar contenido del archivo
def MostrarConten(archivo):
    try:
        with open(archivo, newline='', encoding='utf-8') as archivocsv:
            red = csv.reader(archivocsv)
            
            contenidocsv = ""
            for row in red:
                contenidocsv += " ".join(row) + "\n"
                
            # Mostrar el contenido del CSV en la caja de texto
            cajatext.delete(1.0, tk.END)
            cajatext.insert(tk.END, contenidocsv)
    except Exception as e:
        cajatext.delete(1.0, tk.END)
        cajatext.insert(tk.END, f"Ocurrio un error al leer el archivo: {e}")

# Obtener texto del archivo
def ObtenerTexto(archivo):
    try:
        with open(archivo, newline='', encoding='utf-8') as archivocsv:
            red = csv.reader(archivocsv)
            contenidocsv = ""
            for row in red:
                contenidocsv += " ".join(row) + "\n"
            return contenidocsv
    except Exception as e:
        return f"Ocurrio un error al leer el archivo: {e}"

# Mostrar texto cifrado
def MostrarTextoCifrado(texto):
    cajatext2.delete(1.0, tk.END)
    cajatext2.insert(tk.END, texto)


#Interfaz grafica

ventana= tk.Tk()
ventana.geometry("500x500")
ventana.title("Ventana Principal")

msg = tk.Label(ventana, text="Proyecto Lenguajes de Programacion 2024-1")
msg.pack()

lbl = tk.Label(ventana, text='Seleccione un archivo .csv')
lbl.place(x=178, y=40)

#botonSeleccionar
botonSelec = tk.Button(ventana, text='Seleccionar', bg="orange", command=SelecArchivo)
botonSelec.place(x=210, y=60)

#botonCesar
botonCesar = tk.Button(ventana, text='Cesar', command=Cesar)
botonCesar.place(x=120, y=110)

#botonAffine
botAffine = tk.Button(ventana, text='Affine', command=Affine)
botAffine.place(x=225, y=110)

#botonMixto
botMixto = tk.Button(ventana, text='Mixto', command=Mixto)
botMixto.place(x=320, y=110)

#caja de texto izquierda
cajatext = tk.Text(ventana, width=24, wrap=tk.NONE, height=16, bg="white")
cajatext.place(x=50, y=160)

scrolY1 = tk.Scrollbar(ventana, orient="vertical", command=cajatext.yview)
scrolY1.pack(side="right", fill="y")
cajatext.config(yscrollcommand=scrolY1.set)

scrolX1 = tk.Scrollbar(ventana, orient="horizontal", command=cajatext.xview)
scrolX1.pack(side="bottom", fill="x")
cajatext.config(xscrollcommand=scrolX1.set)

#caja de texto derecha
cajatext2 = tk.Text(ventana, width=24, wrap=tk.NONE, height=16, bg="white")
cajatext2.place(x=250, y=160)

scrolY2 = tk.Scrollbar(ventana, orient="vertical", command=cajatext2.yview)
scrolY2.pack(side="right", fill="y")
cajatext2.config(yscrollcommand=scrolY2.set)

scrolX2 = tk.Scrollbar(ventana, orient="horizontal", command=cajatext2.xview)
scrolX2.pack(side="bottom", fill="x")
cajatext2.config(xscrollcommand=scrolX2.set)

ventana.mainloop()
