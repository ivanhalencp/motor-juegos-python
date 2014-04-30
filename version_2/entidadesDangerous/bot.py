import Motor, pygame
from pygame.locals import *
from Motor import EntidadJuego, Rect

class Bot(EntidadJuego.EntidadJuego, object):
    def __init__(self, imagen, mundoFisico, controladorEventos, juego):
        EntidadJuego.EntidadJuego.__init__(self, imagen, mundoFisico)
        #self.posicion.set(150, 120)
        #self.crearAnimaciones()
        #self.registrarEventos()
        self.derechaPresionada = False
        self.izquierdaPresionada = False
        self.arribaPresionada = False
        self.abajoPresionada = False
        self.centrarFotogramas = True
        self.juego = juego
        self.__animaFueraEscena = False
        self.__graficaFueraEscena = False
        self.__logicaFueraEscena = True
        self.__aplicarFisicaFueraEscena = True
    def logica(self):
        # print "logica..."
        # CAIDA LIBRE
        self.velocidad.y += .05
        if self.mFisica.buscarColision("", "muro", True):
            self.velocidad.y = 0
        # MOVIMIENTO HORIZONTAL
        if self.derechaPresionada:
            #self.setAnimacionActiva("bot")
            self.mAnimaciones.invertirImagen = False
            self.velocidad.x = .5
            if self.mFisica.buscarColision("", "muro", True):
                self.velocidad.x = 0
        elif self.izquierdaPresionada:
            #self.setAnimacionActiva("bot")
            self.mAnimaciones.invertirImagen = True
            self.velocidad.x = -.5
            if self.mFisica.buscarColision("", "muro", True):
                self.velocidad.x = 0
        else:
            self.velocidad.x = 0
        # MOVIMIENTO VERTICAL
        #if self.arribaPresionada:
        #    self.setAnimacionActiva("bot")
        #    self.velocidad.y = -1
        #elif self.abajoPresionada:
        #    self.setAnimacionActiva("bot")
        #    self.velocidad.y = 1
        #else:
        #    self.velocidad.y = 0

        if self.velocidad.y == 0 and self.velocidad.x == 0:
            self.setAnimacionActiva("bot")

    def seguirEntidad(self, entidad):
        if (abs(round(entidad.posicion.x - self.posicion.x)) > 25):
            if (entidad.posicion.x > self.posicion.x):
                self.derechaPresionada = True
                self.izquierdaPresionada = False
            else:
                self.izquierdaPresionada = True
                self.derechaPresionada = False
        else:
            self.derechaPresionada = False
            self.izquierdaPresionada = False

    def crearAnimaciones(self):
        cuerpoChoque = Rect.Rect(-10, -14, 20, 28)
        # BOT
        self.crearAnimacion("bot")
        self.addFotogramaCuerpoChoque("bot_1", Rect.Rect(0, 64, 32, 32), cuerpoChoque)
        self.addFotogramaCuerpoChoque("bot_2", Rect.Rect(32, 64, 32, 32), cuerpoChoque)
        self.addFotogramaCuerpoChoque("bot_3", Rect.Rect(64, 64, 32, 32), cuerpoChoque)
        self.addFotogramaAnimacion("bot", "bot_1", 30)
        self.addFotogramaAnimacion("bot", "bot_2", 30)
        self.addFotogramaAnimacion("bot", "bot_3", 30)
        self.addFotogramaAnimacion("bot", "bot_2", 30)
        self.setAnimacionActiva("bot")    

    # -- GETS Y SETS --
    def getDerechaPresionada(self):
        return self.__derechaPresionada
    def setDerechaPresionada(self, param):
        self.__derechaPresionada = param
    derechaPresionada = property(getDerechaPresionada, setDerechaPresionada)
    def getIzquierdaPresionada(self):
        return self.__izquierdaPresionada
    def setIzquierdaPresionada(self, param):
        self.__izquierdaPresionada = param
    izquierdaPresionada = property(getIzquierdaPresionada, setIzquierdaPresionada)
    def getArribaPresionada(self):
        return self.__arribaPresionada
    def setArribaPresionada(self, param):
        self.__arribaPresionada = param
    arribaPresionada = property(getArribaPresionada, setArribaPresionada)
    def getAbajoPresionada(self):
        return self.__abajoPresionada
    def setAbajoPresionada(self, param):
        self.__abajoPresionada = param
    abajoPresionada = property(getAbajoPresionada, setAbajoPresionada)
    def getEstado(self):
        return self.__estado
    def setEstado(self, param):
        self.__estado = param
    estado = property(getEstado, setEstado)