import Motor
from Motor import EntidadJuego

class Jugador(EntidadJuego.EntidadJuego, object):
    def __init__(self, imagen, mundoFisico, controladorEventos):
        # INICIALIZO ENTIDAD JUEGO
        EntidadJuego.EntidadJuego.__init__(self, imagen, mundoFisico)
        # REFERENCIA AL CONTROLADOR DE EVENTOS
        self.__controladorEventos = controladorEventos
        # INICIALIZO VALORES JUGADOR
        self.__energia = 0
        self.__vidas = 0
        self.__creditos = 0
        self.__puntos = 0

    # -- GETS Y SETS --
    def getEnergia(self):
        return self.__energia
    def setEnergia(self, param):
        self.__energia = param
    energia = property(getEnergia, setEnergia)
    def getVidas(self):
        return self.__vidas
    def setVidas(self, param):
        self.__vidas = param
    vidas = property(getVidas, setVidas)
    def getCreditos(self):
        return self.__creditos
    def setCreditos(self, param):
        self.__creditos = param
    creditos = property(getCreditos, setCreditos)
    def getPuntos(self):
        return self.__puntos
    def setPuntos(self, param):
        self.__puntos = param
    puntos = property(getPuntos, setPuntos)
    # CONTROLADOR DE EVENTOS
    def getControladorEventos(self):
        return self.__controladorEventos
    def setControladorEventos(self, param):
        self.__controladorEventos = param
    controladorEventos = property(getControladorEventos, setControladorEventos)
