import json

class Archivo:
    def __init__(self):
        self.nombreArchivo=None
        self.usuario=None
        self.listaUsuarios=[]

    def get_usuario(self):
        return self.usuario
    def get_nombreArchivo(self):
        return self.nombreArchivo
    def get_listaUsuarios(self):
        return self.listaUsuarios
    
    def set_usuario(self,nombre,apellido,edad,documento,sexo):
        self.usuario=[nombre,apellido,edad,documento,sexo]
        self.listaUsuarios.append(self.usuario)
    def set_nombreArchivo(self,auxNombre):
        self.nombreArchivo=auxNombre

    def guardarDatos(self,nombreArchivo,nombre,apellido,edad,documento,sexo):
        self.set_usuario(nombre,apellido,edad,documento,sexo)
        self.set_nombreArchivo(nombreArchivo)

    def crearArchivo(self,usuario,datoTitulo):
        nombreArchivo=datoTitulo+".txt"
        with open(nombreArchivo, "w") as archivo:
            json.dump(usuario,archivo)
        return nombreArchivo
    
    def leerArchivo(self,auxArchivo):
        with open(auxArchivo,"r") as archivo:
            datoContenido=archivo.read()
            print(datoContenido)
            archivo.close()
            
    def deserializar(self,nombreArchivo):
        with open(nombreArchivo+".txt","r") as archivo:
            datoCreado=json.load(archivo)
        return datoCreado