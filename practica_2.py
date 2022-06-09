# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 14:12:21 2022

@author: HP EliteBook 2470p
"""

import tkinter as tk
from tkinter.messagebox import showinfo

ventana = tk.Tk()
ventana.geometry ("1080x400")
ventana.config(bg="Turquoise")

#Primera Fila

espacio = tk.Label(ventana, bg="Turquoise", fg="Turquoise")
espacio.grid (row = 0, column = 0)

texto1 = tk.Label(ventana, text="Latitud (°)=", bg="Turquoise", fg="gray20")
texto1.grid (row = 1, column = 0)

cuadro1 = tk.Entry(ventana, font = "Calibri 12", justify = "left")
cuadro1.grid (row = 1, column = 1)

texto2 = tk.Label(ventana, text="Longitud (°) =", bg="Turquoise", fg="gray20")
texto2.grid (row = 3, column = 0)

cuadro2 = tk.Entry(ventana, font = "Calibri 12", justify = "left")
cuadro2.grid (row = 3, column = 1)

#Segundaa Fila
espacio3 = tk.Label(ventana, bg="Turquoise", fg="Turquoise")
espacio3.grid (row = 1, column = 1)

texto3 = tk.Label(ventana, text="Latitud (°)=", bg="Turquoise", fg="gray20")
texto3.grid (row = 1, column = 2)

cuadro3 = tk.Entry(ventana, font = "Calibri 12", justify = "left")
cuadro3.grid (row = 1, column = 3)

texto4 = tk.Label(ventana, text="Longitud (°) =", bg="Turquoise", fg="gray20")
texto4.grid (row = 3, column = 2)

cuadro4 = tk.Entry(ventana, font = "Calibri 12", justify = "left")
cuadro4.grid (row = 3, column = 3)

texto5 = tk.Label(ventana, text="Min  =", bg="Turquoise", fg="gray20")
texto5.grid (row = 1, column = 4)

cuadro5 = tk.Entry(ventana, font = "Calibri 12", justify = "left")
cuadro5.grid (row = 1, column = 5)

texto6 = tk.Label(ventana, text="Seg =", bg="Turquoise", fg="gray20")
texto6.grid (row = 1, column = 6)

cuadro6 = tk.Entry(ventana, font = "Calibri 12", justify = "left")
cuadro6.grid (row = 1, column = 7)

texto7 = tk.Label(ventana, text="Min =", bg="Turquoise", fg="gray20")
texto7.grid (row = 3, column = 4)

cuadro7 = tk.Entry(ventana, font = "Calibri 12", justify = "left")
cuadro7.grid (row = 3, column = 5)

texto8 = tk.Label(ventana, text="Seg =", bg="Turquoise", fg="gray20")
texto8.grid (row = 3, column = 6)

cuadro8 = tk.Entry(ventana, font = "Calibri 12", justify = "left")
cuadro8.grid (row = 3, column = 7)

#Resultados
textoResult = tk.Text(ventana)
textoResult.grid(row = 11, column = 0, columnspan = 6)

def resultados_DD_a_DMS():
    textoResult.delete(1.0, tk.END)
    Latitud_1 = float(cuadro1.get())
    Longitud_1 = float(cuadro2.get())

#Conversion dd a dms
Conver = (Latitud_1*60)
textoResult.insert(tk.END, f"latitud_conversion = {latitud_conversion}\n\n")

Conver = (Longitud_1*60)
textoResult.insert(tk.END, f"longitud_conversion = {longitud_conversion}\n\n") 


   
def resultados_DMS_a_DD():
    textoResult.delete(1.0, tk.END)
    Latitud_2 = float(cuadro3.get())
    Longitud_2 = float(cuadro4.get())
    min_la = float(cuadro5.get())
    seg_la = float(cuadro6.get())
    min_lon = float(cuadro7.get())
    seg_lon = float(cuadro8.get())
    
  
    min_x = texto5/60 + MINUTOS

    grados_valor_x = round(((min_x)/60 + texto1 3)

    def gmd(grados_valor_x):    
        min_x = texto5/60 + texto6
        grados_valor_x = round(((min_x)/60 + texto1), 3)

#Ventana Emergente
def popup_showinfo():
    message ="¡finalizado!"
    showinfo(message)
    
#Botón de Cálculo DD A DMS
boton_calculo = tk.Button(text = "Convertir de DD a DMS", font= 'Cambria 11', command = resultados_DD_a_DMS)
boton_calculo.grid(row = 10, column = 1, columnspan = 1)

#Botón de Cálculo DMS A DD
boton_calculo = tk.Button(text = "Convertir de DMS a DD", font= 'Cambria 11', command = resultados_DMS_a_DD)
boton_calculo.grid(row = 10, column = 2, columnspan = 2)

#Título 
ventana.title("Conversor de Coordenadas por Bryan Martinez")

ventana.mainloop()