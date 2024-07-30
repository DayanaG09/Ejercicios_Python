class Controlador:
    def __init__(self,objVista,objModelo):
        self.objVista=objVista
        self.objModelo=objModelo
        
    def guardarDatos(self,nombreArchivo,nombre,apellido,edad,documento,sexo):
        self.objModelo.guardarDatos(nombreArchivo,nombre,apellido,edad,documento,sexo)

    def crearArchivo(self):
        datoUsuario=self.objModelo.get_listaUsuarios()
        datoTitulo=self.objModelo.get_nombreArchivo()
        archivoCreado=self.objModelo.crearArchivo(datoUsuario,datoTitulo)
        self.objModelo.leerArchivo(archivoCreado)
    
    def deserializar(self,datoTitulo):
        auxDatoCreado=self.objModelo.deserializar(datoTitulo)
        return auxDatoCreado
        
    def iniciar(self):
        self.objVista.crearVentana()
        self.objVista.funcion_mainloop()