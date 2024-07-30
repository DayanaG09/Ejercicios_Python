from modelo import Archivo
from controlador import Controlador
from vista import Interfaz

objModelo=Archivo()
objVista=Interfaz()
objControlador=Controlador(objVista,objModelo)

objVista.set_controlador(objControlador)
objControlador.iniciar()