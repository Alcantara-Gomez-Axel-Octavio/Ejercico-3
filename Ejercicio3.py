from tkinter import *
from tkinter import ttk
import tkinter as ttk



# Crear ventana principal
root = Tk()

# Crear frame principal
main_frame = ttk.Frame(root, width=200, height=200, bg="#141414")
main_frame.pack()

# Frame 1 (blanco)
frame1 = ttk.Frame(main_frame, width=693, height=100, bg="white", relief="raised")
frame1.grid(column=0, row=0)

ttk.Label(frame1, text="      ", bg="white", foreground="white").grid(column=0, row=0, padx=400)
    
    #Frame azul.
frameAzul = ttk.Frame(frame1, width=693, height=100, bg="#0c747c", relief="raised")
frameAzul.grid(column=0, row=1)

imagen2 = PhotoImage(file= 'LineasMenu.png')
imagen2_reducida = imagen2.subsample(30, 30) # La imagen se reducirá a la mitad en ambas direcciones (horizontal y vertical)
etqImagen2 = ttk.Button(frameAzul,bg="#0c747c",activebackground="#0c747c")
etqImagen2.grid(column=0, row=0, padx=10)
etqImagen2['image']=imagen2_reducida
etqImagen2.config(borderwidth=0, highlightthickness=0)

ttk.Label(frameAzul, text="SPAI 4.0", font=("Arial", 16, "bold"), bg="#0c747c", foreground="white").grid(column=1, row=0, pady=10,sticky=(W))
ttk.Label(frameAzul, text=" ", bg="#0c747c", foreground="white").grid(column=2, row=0, padx=580, pady=10,sticky=(W))

# Frame 2 (Negro)
frame2 = ttk.Frame(main_frame, bg="#141414")
frame2.grid(column=0, row=1)

    #Frame 3 (Izquierdo)
frame3 = ttk.Frame(frame2, bg="#141414")
frame3.grid(column=0, row=0, pady=3)

        #Frame 3.1(A)
frame311 = ttk.Frame(frame3, bg="#343434")
frame311.grid(column=0, row=0, padx=3)

ttk.Label(frame311, text="Indicadores Digitales", bg="#343434", foreground="#0c747c", font=("Arial", 12, "bold")).grid(column=0, row=0, pady=10,columnspan=2)


ttk.Label(frame311, text=" Linea 1:         ", bg="#343434", foreground="white", font=("Arial", 12)).grid(column=0, row=1)
ttk.Label(frame311, text=" Linea 2:         ", bg="#343434", foreground="white", font=("Arial", 12)).grid(column=0, row=2)
ttk.Label(frame311, text=" Linea 1:         ", bg="#343434", foreground="white", font=("Arial", 12)).grid(column=0, row=3)
ttk.Label(frame311, text=" Gabinete: ", bg="#343434", foreground="white", font=("Arial", 12)).grid(column=0, row=4,sticky=(W))
ttk.Label(frame311, text=" Alarma:        ", bg="#343434", foreground="white", font=("Arial", 12)).grid(column=0, row=5)
ttk.Label(frame311, text=" Alarma2:        ", bg="#343434", foreground="white", font=("Arial", 12)).grid(column=0, row=6)


ttk.Label(frame311, text="On", bg="#343434", foreground="white", font=("Arial", 12, "bold")).grid(column=1, row=1)
ttk.Label(frame311, text="On", bg="#343434", foreground="white", font=("Arial", 12, "bold")).grid(column=1, row=2)
ttk.Label(frame311, text="On", bg="#343434", foreground="white", font=("Arial", 12, "bold")).grid(column=1, row=3)
ttk.Label(frame311, text="Abierto", bg="#343434", foreground="white", font=("Arial", 12, "bold")).grid(column=1, row=4,sticky=(W))
ttk.Label(frame311, text="On", bg="#343434", foreground="white", font=("Arial", 12, "bold")).grid(column=1, row=5)
ttk.Label(frame311, text="Off", bg="#343434", foreground="white", font=("Arial", 12, "bold")).grid(column=1, row=6)

imagen2 = PhotoImage(file= 'Punto.png')
imagen2_reducida = imagen2.subsample(2, 2) # La imagen se reducirá a la mitad en ambas direcciones (horizontal y vertical)
etqImagen2 = ttk.Button(frame311,bg="#482525",activebackground="#482525")
etqImagen2.grid(column=2, row=1, pady=10, padx=15)
etqImagen2['image']=imagen2_reducida
etqImagen2.config(borderwidth=0, highlightthickness=0)

imagen3 = PhotoImage(file= 'Punto.png')
imagen3_reducida = imagen3.subsample(2, 2) # La imagen se reducirá a la mitad en ambas direcciones (horizontal y vertical)
etqImagen3 = ttk.Button(frame311,bg="#482525",activebackground="#482525")
etqImagen3.grid(column=2, row=2, pady=10, padx=15)
etqImagen3['image']=imagen3_reducida
etqImagen3.config(borderwidth=0, highlightthickness=0)

imagen4 = PhotoImage(file= 'Punto.png')
imagen4_reducida = imagen4.subsample(2, 2) # La imagen se reducirá a la mitad en ambas direcciones (horizontal y vertical)
etqImagen4 = ttk.Button(frame311,bg="#482525",activebackground="#482525")
etqImagen4.grid(column=2, row=3, pady=10, padx=15)
etqImagen4['image']=imagen4_reducida
etqImagen4.config(borderwidth=0, highlightthickness=0)

imagen5 = PhotoImage(file= 'PuntoR.png')
imagen5_reducida = imagen5.subsample(2, 2) # La imagen se reducirá a la mitad en ambas direcciones (horizontal y vertical)
etqImagen5 = ttk.Button(frame311,bg="#482525",activebackground="#482525")
etqImagen5.grid(column=2, row=4, pady=10, padx=15)
etqImagen5['image']=imagen5_reducida
etqImagen5.config(borderwidth=0, highlightthickness=0)

imagen6 = PhotoImage(file= 'PuntoR.png')
imagen6_reducida = imagen6.subsample(2, 2) # La imagen se reducirá a la mitad en ambas direcciones (horizontal y vertical)
etqImagen6 = ttk.Button(frame311,bg="#482525",activebackground="#482525")
etqImagen6.grid(column=2, row=5, pady=10, padx=15)
etqImagen6['image']=imagen6_reducida
etqImagen6.config(borderwidth=0, highlightthickness=0)

imagen7 = PhotoImage(file= 'Punto.png')
imagen7_reducida = imagen7.subsample(2, 2) # La imagen se reducirá a la mitad en ambas direcciones (horizontal y vertical)
etqImagen7 = ttk.Button(frame311,bg="#482525",activebackground="#482525")
etqImagen7.grid(column=2, row=6, pady=10, padx=15)
etqImagen7['image']=imagen7_reducida
etqImagen7.config(borderwidth=0, highlightthickness=0)


        #Frame 3.2
frame32 = ttk.Frame(frame3, bg="#343434")
frame32.grid(column=2, row=0)

ttk.Label(frame32, text="Temperatura", bg="#343434", foreground="#0c747c", font=("Arial", 12, "bold")).grid(column=0, row=0, pady=10, sticky=(W))
ttk.Label(frame32, text="Temperatura 1:", bg="#343434", foreground="white", font=("Arial", 12)).grid(column=0, row=1, pady=13, padx=34)
ttk.Label(frame32, text="Temperatura 2:", bg="#343434", foreground="white", font=("Arial", 12)).grid(column=1, row=1, pady=17, padx=33)

imagen8 = PhotoImage(file= 'MedidorVerde.png')
imagen8_reducida = imagen8.subsample(3, 3) # La imagen se reducirá a la mitad en ambas direcciones (horizontal y vertical)
etqImagen8 = ttk.Button(frame32,bg="#482525",activebackground="#482525")
etqImagen8.grid(column=0, row=2, padx=30)
etqImagen8['image']=imagen8_reducida
etqImagen8.config(borderwidth=0, highlightthickness=0)

imagen9 = PhotoImage(file= 'MedidorAmarillo.png')
imagen9_reducida = imagen9.subsample(3, 3) # La imagen se reducirá a la mitad en ambas direcciones (horizontal y vertical)
etqImagen9 = ttk.Button(frame32,bg="#482525",activebackground="#482525")
etqImagen9.grid(column=1, row=2, padx=30)
etqImagen9['image']=imagen9_reducida
etqImagen9.config(borderwidth=0, highlightthickness=0)

frame321 = ttk.Frame(frame32, bg="#343434")
frame321.grid(column=0, row=3, columnspan=2, pady=3)

ttk.Label(frame321, text="\nTemp. Agua:", bg="#343434", foreground="white", font=("Arial", 10)).grid(column=0, row=3, pady=20, sticky=(E,S))
ttk.Label(frame321, text="58ºC ", bg="#343434", foreground="white", font=("Arial", 10, "bold")).grid(column=1, row=3, pady=20, sticky=(W,S))
ttk.Label(frame321, text="Temp. Ambiente:", bg="#343434", foreground="white", font=("Arial", 10)).grid(column=0, row=4, pady=12, sticky=(E))
ttk.Label(frame321, text="32ºC ", bg="#343434", foreground="white", font=("Arial", 10, "bold")).grid(column=1, row=4, pady=12, sticky=(W))

        #Frame 3,3
frame33 = ttk.Frame(frame2, bg="#141414")
frame33.grid(column=0, row=1)


            #Frame 3,31
frame331 = ttk.Frame(frame33, bg="#343434")
frame331.grid(column=0, row=0, padx=3)


ttk.Label(frame331, text="\nVelocidad bomba:", bg="#343434", foreground="white", font=("Arial", 12, "bold")).grid(column=0, row=0, pady=18, padx=70)

imagen10 = PhotoImage(file= 'MedidorRojo.png')
imagen10_reducida = imagen10.subsample(2, 2) # La imagen se reducirá a la mitad en ambas direcciones (horizontal y vertical)
etqImagen10 = ttk.Button(frame331,bg="#482525",activebackground="#482525")
etqImagen10.grid(column=0, row=1, pady=28)
etqImagen10['image']=imagen10_reducida
etqImagen10.config(borderwidth=0, highlightthickness=0)

            #Frame 3,32
frame332 = ttk.Frame(frame33, bg="#343434")
frame332.grid(column=1, row=0)


ttk.Label(frame332, text="Nivel del tanque:", bg="#343434", foreground="#0c747c", font=("Arial", 12, "bold")).grid(column=0, row=0, pady=12,sticky=(W))

imagen11 = PhotoImage(file= 'MedidorAzul.png')
imagen11_reducida = imagen11.subsample(2, 2) # La imagen se reducirá a la mitad en ambas direcciones (horizontal y vertical)
etqImagen11 = ttk.Button(frame332,bg="#482525",activebackground="#482525")
etqImagen11.grid(column=0, row=1, padx=52, pady=16,sticky=(N))
etqImagen11['image']=imagen11_reducida
etqImagen11.config(borderwidth=0, highlightthickness=0)

ttk.Label(frame332, text="       ", bg="#343434", foreground="#0c747c", font=("Arial", 12, "bold")).grid(column=1, row=0, pady=12 )
    
    
    # Frame 4 (Derecho)
frame4 = ttk.Frame(frame2, bg="#343434")
frame4.grid(column=1, row=0,rowspan=2, padx=3,sticky=(N))

ttk.Label(frame4, text="Produccion ", bg="#343434", foreground="#0c747c", font=("Arial", 12, "bold")).grid(column=0, row=0, pady=12, sticky=(W))

imagen12 = PhotoImage(file= 'Grafica.png')
imagen11_reducida12 = imagen12.subsample(2, 2)
etqImagen = ttk.Label(frame4)
etqImagen.grid(column=0, row=1)
etqImagen["image"]  = imagen11_reducida12
etqImagen.config(borderwidth=0, highlightthickness=0)

ttk.Label(frame4, text="\n\n\n                                        50 ", bg="#343434", foreground="white", font=("Arial", 10, "bold")).grid(column=0, row=2, pady=12)
ttk.Label(frame4, text="\n\n\nPiezas producidas:", bg="#343434", foreground="white", font=("Arial", 10)).grid(column=0, row=2, pady=12)

ttk.Label(frame4, text="                                         12", bg="#343434", foreground="white", font=("Arial", 10, "bold")).grid(column=0, row=3, pady=12)
ttk.Label(frame4, text="Piezas defectuosas:", bg="#343434", foreground="white", font=("Arial", 10)).grid(column=0, row=3, pady=12)

root.mainloop()
