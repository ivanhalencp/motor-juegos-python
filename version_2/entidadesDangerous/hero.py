import Motor, pygame
from pygame.locals import *
from Motor import Jugador, Rect

class Hero(Jugador.Jugador, object):
    def __init__(self, imagen, mundoFisico, controladorEventos, juego):
        Jugador.Jugador.__init__(self, imagen, mundoFisico, controladorEventos)
        self.juego = juego
        self.derechaPresionada = False
        self.izquierdaPresionada = False
        self.arribaPresionada = False
        self.abajoPresionada = False
        self.centrarFotogramas = True
    def logica(self):
        # CAIDA LIBRE
        self.velocidad.y += .05
        if self.mFisica.buscarColision("", "muro", True):
            self.velocidad.y = 0
            if self.mAnimaciones.animacionActiva == "cayendo":
                self.setAnimacionActiva("parado");
        elif self.velocidad.y > 4:
            self.setAnimacionActiva("cayendo");
        # MOVIMIENTO HORIZONTAL
        # CAMINANDO DERECHA
        if self.derechaPresionada:
            if self.mAnimaciones.animacionActiva != "cayendo":
                self.setAnimacionActiva("caminando")
            self.mAnimaciones.invertirImagen = False
            self.velocidad.x = 1
            if self.mFisica.buscarColision("", "muro", True):
                self.velocidad.x = 0
        # CAMINANDO IZQUIERDA
        elif self.izquierdaPresionada:
            if self.mAnimaciones.animacionActiva != "cayendo":
                self.setAnimacionActiva("caminando")
            self.mAnimaciones.invertirImagen = True
            self.velocidad.x = -1
            if self.mFisica.buscarColision("", "muro", True):
                self.velocidad.x = 0
        else:
            self.velocidad.x = 0
        # MOVIMIENTO VERTICAL
        #if self.arribaPresionada:
        #    self.setAnimacionActiva("en_escalera")
        #    self.velocidad.y = -1
        #elif self.abajoPresionada:
        #    self.setAnimacionActiva("cayendo")
        #    self.velocidad.y = 1
        #else:
        #    self.velocidad.y = 0
        # SI LAS VELOCIDADES SON 0 SETEO ANIMACION PARADO
        if self.velocidad.y == 0 and self.velocidad.x == 0 and self.mAnimaciones.animacionActiva != "pegando":
            self.setAnimacionActiva("parado")

    def registrarEventos(self, derecha, izquierda, arriba, abajo, fuego):
        self.controladorEventos.addListenerTeclado(KEYDOWN, derecha, self.downDerecha)
        self.controladorEventos.addListenerTeclado(KEYUP, derecha, self.upDerecha)
        self.controladorEventos.addListenerTeclado(KEYDOWN, izquierda, self.downIzquierda)
        self.controladorEventos.addListenerTeclado(KEYUP, izquierda, self.upIzquierda)
        self.controladorEventos.addListenerTeclado(KEYDOWN, arriba, self.downUp)
        self.controladorEventos.addListenerTeclado(KEYUP, arriba, self.upUp)
        self.controladorEventos.addListenerTeclado(KEYDOWN, abajo, self.downDown)
        self.controladorEventos.addListenerTeclado(KEYUP, abajo, self.upDown)
        self.controladorEventos.addListenerTeclado(KEYDOWN, fuego, self.pegar)
    def downDerecha(self, evento):
        self.derechaPresionada = True
    def upDerecha(self, evento):
        self.derechaPresionada = False
    def downIzquierda(self, evento):
        self.izquierdaPresionada = True
    def upIzquierda(self, evento):
        self.izquierdaPresionada = False
    def downUp(self, evento):
        self.arribaPresionada = True
        if self.velocidad.y == 0:
            self.velocidad.y = -2.25
    def upUp(self, evento):
        self.arribaPresionada = False
    def downDown(self, evento):
        self.abajoPresionada = True
    def upDown(self, evento):
        self.abajoPresionada = False
    def crearAnimaciones(self):
        cuerpoChoque = Rect.Rect(-10, -14, 20, 28)
        # PARADO
        self.crearAnimacion("parado")
        self.addFotogramaCuerpoChoque("parado_1", Rect.Rect(0, 0, 32, 32), cuerpoChoque)
        self.addFotogramaCuerpoChoque("parado_2", Rect.Rect(32, 0, 32, 32), cuerpoChoque)
        self.addFotogramaAnimacion("parado", "parado_1", 30)
        self.addFotogramaAnimacion("parado", "parado_2", 30)
        self.setAnimacionActiva("parado")
        # CAMINANDO
        self.crearAnimacion("caminando")
        self.addFotogramaCuerpoChoque("caminando_1", Rect.Rect(64, 0, 32, 32), cuerpoChoque)
        self.addFotogramaCuerpoChoque("caminando_2", Rect.Rect(96, 0, 32, 32), cuerpoChoque)
        self.addFotogramaAnimacion("caminando", "caminando_1", 30)
        self.addFotogramaAnimacion("caminando", "caminando_2", 30)
        # EN LA ESCALERA
        self.crearAnimacion("en_escalera")
        self.addFotogramaCuerpoChoque("en_escalera_1", Rect.Rect(128, 0, 32, 32), cuerpoChoque)
        self.addFotogramaCuerpoChoque("en_escalera_2", Rect.Rect(160, 0, 32, 32), cuerpoChoque)
        self.addFotogramaAnimacion("en_escalera", "en_escalera_1", 30)
        self.addFotogramaAnimacion("en_escalera", "en_escalera_2", 30)
        # CAYENDO
        self.crearAnimacion("cayendo")
        self.addFotogramaCuerpoChoque("cayendo_1", Rect.Rect(192, 0, 32, 32), cuerpoChoque)
        self.addFotogramaCuerpoChoque("cayendo_2", Rect.Rect(224, 0, 32, 32), cuerpoChoque)
        self.addFotogramaAnimacion("cayendo", "cayendo_1", 30)
        self.addFotogramaAnimacion("cayendo", "cayendo_2", 30)       
    def pegar(self, evento):
        self.setAnimacionActiva("pegando")
    def finPegando(self):
        self.setAnimacionActiva("parado")

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