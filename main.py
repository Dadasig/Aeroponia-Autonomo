from tkinter import *
from tkinter import ttk, messagebox
import tkinter as tk
#import tkinter as tkFont
from tkinter import font
#from PIL import ImageTk#
from PIL import Image
import time, os

class Window(Frame):
    def __init__(self, master=None):     
        Frame.__init__(self, master)                
        self.master = master
        self.menus()
        self.componentes()
        self.botones()
        #self.master.iconbitmap('la.ico')
        self.master.resizable(False,False)
        self.master.title('Control de Accesos')
        self.master.geometry("1100x500")
        self.master.config(bg="white")
        self.master.config(relief="ridge")

    def componentes(self):
        self.text = Label(text="Sistema de Control de Accesos LabSoL", bg="white", font=helv36, justify=("center"))
        self.text.place(x=140,y=10)
        self.label = Label(text="", bg="white", fg="Black", font=helv35, justify=("center"))
        self.label.place(x=455, y=310)
        self.update_clock()

    def botones(self):
        self.btn = Button(text="Registro", bg="white", bd=2, background="black", foreground="#FFFFFF", font=helv34, justify=("center"), command=self.registro)
        self.btn.place(x=400,y=390)
        self.btn = Button(text="Accesar", bg="white", bd=2, background="black", foreground="#FFFFFF", font=helv34, justify=("center"), command=self.reconocer)
        self.btn.place(x=510,y=390)
        self.btn = Button(text="Entrenar", bg="white", bd=2, background="black", foreground="#FFFFFF", font=helv34, justify=("center"), command=self.entrenar)
        self.btn.place(x=640,y=390)

    def menus(self):
        menu = Menu(self.master)
        self.master.config(menu=menu)
        Archivo = Menu()
        Archivo.add_separator()
        Archivo.add_command(label='Ver Registro')
        Archivo.add_separator
        Archivo.add_command(label='Modificar Registro')
        Archivo.add_separator
        Archivo.add_command(label='Eliminar Registro')
        Archivo.add_command(label="Salir", command=self.client_exit)
        menu.add_cascade(label="Archivo", menu=Archivo)
        ayuda = Menu()
        ayuda.add_command(label="Ayuda", command=self.ayuda)
        ayuda.add_command(label="Acerca de...", command=self.acerca)
        ayuda.add_separator()
        menu.add_cascade(label="Ayuda", menu=ayuda)
        menu.add_command(label="Salir", command=self.client_exit)

    def client_exit(self):
        exit()
    def acerca(self):
        messagebox.showinfo('Acerca de...', 'Version: Beta.\n Fecha: 08/11/2019.\n Laboratorio de Software Libre, Zac. \n Desarrollado con  Herramientas Open Source. \n Desarrolladores: 1 Jose Jimenez 2 Miguel Garcia 3 Gustavo Escalante. ') 
    def ayuda(self):
        messagebox.showinfo('Ayuda', 'contacto directo laboratorio de sofftware libre')    

    def update_clock(self):
        now = time.strftime("%H:%M:%S" )
        self.label.configure(text=now, )
        self.after(1000, self.update_clock)   
    
    def reconocer(self):
        os.system('python3 detectar_identificar_rostros.py')
    def entrenar(self):
        os.system('python3 entrenamiento.py')
    def registro(self):
        os.system('python3 interfaz.py')
root = Tk()

helv36 = font.Font(family='Helvetica', size=32, weight='bold')
helv35 = font.Font(family='Helvetica', size=45, weight='bold')
helv34= font.Font(family='Helvetica', size=12, weight='bold')

#im=Image.open("labsol.png")
#photo=ImageTk.PhotoImage(im)  
cv = tk.Canvas(bg="white",  width=600, height=232)  
#cv.create_image(2, 5, image=photo, anchor='nw')
#cv.place(x=255, y=60)

app = Window(root)
root.after(1000, app.update_clock)
root.mainloop() 
