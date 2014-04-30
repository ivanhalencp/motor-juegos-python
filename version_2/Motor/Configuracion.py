class Configuracion(object):
    def __init__(self):
        #self.__anchoPantalla = 447
        #self.__altoPantalla = 195
        self.__anchoPantalla = 640
        self.__altoPantalla = 480
        self.__pantallaCompleta = False
        #self.__tiempoClock = 120
        self.__tiempoClock = 120
        self.__profundidadAutomatica = False

    # -- GETS Y SETS --
    def getAnchoPantalla(self):
        return self.__anchoPantalla
    def setAnchoPantalla(self, param):
        self.__anchoPantalla = param
    anchoPantalla = property(getAnchoPantalla, setAnchoPantalla)
    def getAltoPantalla(self):
        return self.__altoPantalla
    def setAltoPantalla(self, param):
        self.__altoPantalla = param
    altoPantalla = property(getAltoPantalla, setAltoPantalla)
    def getPantallaCompleta(self):
        return self.__pantallaCompleta
    def setPantallaCompleta(self, param):
        self.__pantallaCompleta = param
    pantallaCompleta = property(getPantallaCompleta, setPantallaCompleta)
    def getTiempoClock(self):
        return self.__tiempoClock
    def setTiempoClock(self, param):
        self.__tiempoClock = param
    tiempoClock = property(getTiempoClock, setTiempoClock)
    def getProfundidadAutomatica(self):
        return self.__profundidadAutomatica
    def setProfundidadAutomatica(self, param):
        self.__profundidadAutomatica = param
    profundidadAutomatica = property(getProfundidadAutomatica, setProfundidadAutomatica)