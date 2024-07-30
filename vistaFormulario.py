import tkinter as ventana
from tkinter import messagebox

class Interfaz:
    def _init_(self):
        self.ventana=None
        self.datos=None
        self.controlador=None

    def set_controlador(self,controlador):
        self.controlador=controlador

    def crearVentana(self):
        self.ventana=ventana.Tk()
        self.ventana.title("MANEJO DE ARCHIVOS")
        self.ventana.geometry("800x800")
        self.contenedor=ventana.Frame(self.ventana)
        self.contenedor.config(bg="#bdd1de")
        self.contenedor.pack()
        #LABELS
        label=ventana.Label(self.contenedor,text="MANEJO DE ARCHIVOS")
        label.config(fg="#ffffff",font=("Times New Roman", 18, "bold"))
        label.pack(pady=10)
        label2=ventana.Label(self.contenedor,text="Bienvenido")
        label2.config(fg="#ffffff",font=("Times New Roman", 15))
        label2.pack(pady=10)
        labelArchivo=ventana.Label(self.contenedor,text="Escribe el nombre del archivo txt:")
        labelArchivo.pack(pady=5)
        self.archivo=ventana.StringVar()
        entryArchivo=ventana.Entry(self.contenedor,textvariable=self.archivo)
        entryArchivo.pack(pady=5)
        labelNombre=ventana.Label(self.contenedor,text="Ingresa tu nombre")
        labelNombre.config(fg="#ffffff",font=("Times New Roman", 12))
        labelNombre.pack(pady=5)
        self.nombre=ventana.StringVar()
        entryNombre=ventana.Entry(self.contenedor,textvariable=self.nombre)
        entryNombre.pack(pady=5)
        labelApellido=ventana.Label(self.contenedor, text="Ingresa tu apellido")
        labelApellido.config(fg="#ffffff",font=("Times New Roman", 12))
        labelApellido.pack(pady=5)
        self.apellido=ventana.StringVar()
        entryApellido=ventana.Entry(self.contenedor,textvariable=self.apellido)
        entryApellido.pack(pady=5)
        labelEdad=ventana.Label(self.contenedor, text="Cuantos años tienes")
        labelEdad.config(fg="#ffffff",font=("Times New Roman", 12))
        labelEdad.pack(pady=5)
        self.edad=ventana.StringVar()
        entryEdad=ventana.Entry(self.contenedor,textvariable=self.edad)
        entryEdad.pack(pady=5)
        labelDocumento=ventana.Label(self.contenedor, text="Numero de documento de identidad")
        labelDocumento.config(fg="#ffffff",font=("Times New Roman", 12))
        labelDocumento.pack(pady=5)
        self.documento=ventana.StringVar()
        entryDocumento=ventana.Entry(self.contenedor,textvariable=self.documento)
        entryDocumento.pack(pady=5)
        labelSexo=ventana.Label(self.contenedor, text="Sexo")
        labelSexo.config(fg="#ffffff",font=("Times New Roman", 12))
        labelSexo.pack(pady=5)
        self.sexo=ventana.StringVar()
        entrySexo=ventana.Entry(self.contenedor,textvariable=self.sexo)
        entrySexo.pack(pady=5)
        #BUTTOM
        botonGuardar=ventana.Button(self.contenedor,text="GUARDAR",command=self.crearArchivo)
        botonGuardar.pack(pady=5)

    def crearArchivo(self):
        try:
            nombre_archivo = self.archivo.get()
            nombre = self.nombre.get()
            apellido = self.apellido.get()
            edad = self.edad.get()
            documento = self.documento.get()
            sexo = self.sexo.get()
            self.controlador.guardarDatos(nombre_archivo, nombre, apellido, edad, documento, sexo)
            self.controlador.crearArchivo()
            msj=self.controlador.deserializar(nombre_archivo)
            messagebox.showinfo("¡Perfecto!", f"Su archivo se ha creado con éxito\nContenido: {msj}")
            
        except ValueError:
            messagebox.showerror("Error", "Por favor rellena todos los campos")
    
    def funcion_mainloop(self):
        self.ventana.mainloop()
