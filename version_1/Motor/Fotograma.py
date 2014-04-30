class Fotograma(object):
    #__claveFCC (String)
    #__tiempoEspera (int)
    def __init__(self, claveFCC, tiempoEspera, accion = None):
        self.__claveFCC = claveFCC
        self.__tiempoEspera = tiempoEspera
        self.__accion = accion

    # -- GETS Y SETS --
    # CLAVE FOTOGRAMACC
    def getClaveFCC(self):
        return self.__claveFCC
    def setClaveFCC(self, param):
        self.__claveFCC = param
    claveFCC = property(getClaveFCC, setClaveFCC)
    # TIEMPO DE ESPERA DEL FOTOGRAMA
    def getTiempoEspera(self):
        return self.__tiempoEspera
    def setTiempoEspera(self, param):
        self.__tiempoEspera = param
    tiempoEspera = property(getTiempoEspera, setTiempoEspera)
    # ACCION (FUNCION DE CALLBACK AL LLEGAR AL FOTOGRAMA)
    def getAccion(self):
        return self.__accion
    def setAccion(self, param):
        self.__accion = param
    accion = property(getAccion, setAccion)
