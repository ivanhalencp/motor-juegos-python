import Motor, pygame
from pygame.locals import *
from Motor import Jugador, Rect

class Guy(Jugador.Jugador, object):
    def __init__(self, imagen, mundoFisico, controladorEventos):
        Jugador.Jugador.__init__(self, imagen, mundoFisico, controladorEventos)
        self.posicion.set(200, 120)
        #self.crearAnimaciones()
        #self.registrarEventos()
        self.derechaPresionada = False
        self.izquierdaPresionada = False
        self.arribaPresionada = False
        self.abajoPresionada = False
        self.centrarFotogramas = True
    def logica(self):
        # MOVIMIENTO HORIZONTAL
        if self.derechaPresionada:
            self.setAnimacionActiva("caminando")
            self.mAnimaciones.invertirImagen = False
            self.velocidad.x = 1
        elif self.izquierdaPresionada:
            self.setAnimacionActiva("caminando")
            self.mAnimaciones.invertirImagen = True
            self.velocidad.x = -1
        else:
            self.velocidad.x = 0
        # MOVIMIENTO VERTICAL
        if self.arribaPresionada:
            self.setAnimacionActiva("caminando")
            self.velocidad.y = -1
        elif self.abajoPresionada:
            self.setAnimacionActiva("caminando")
            self.velocidad.y = 1
        else:
            self.velocidad.y = 0

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
    def upUp(self, evento):
        self.arribaPresionada = False
    def downDown(self, evento):
        self.abajoPresionada = True
    def upDown(self, evento):
        self.abajoPresionada = False
    def crearAnimaciones(self):
        cuerpoChoquePies = Rect.Rect(4, 40, 48, 16)
        # PARADO
        ''' self.crearAnimacion("parado")
        self.crearAnimacion("pegando")
        self.crearAnimacion("caminando") 
        self.addFotogramaCuerpoChoque("parado_1", Rect.Rect(54, 5, 56, 96), cuerpoChoquePies)
        self.addFotogramaCuerpoChoque("parado_2", Rect.Rect(115, 5, 56, 96), cuerpoChoquePies)
        self.addFotogramaCuerpoChoque("parado_3", Rect.Rect(173, 5, 56, 96), cuerpoChoquePies)
        self.addFotogramaAnimacion("parado", "parado_1", 30)
        self.addFotogramaAnimacion("parado", "parado_2", 30)
        self.addFotogramaAnimacion("parado", "parado_3", 30) '''
        self.setAnimacionActiva("parado")
        # CAMINANDO
        #self.crearAnimacion("caminando")
        self.addFotogramaCuerpoChoque("caminando_1", Rect.Rect(35, 312, 56, 96), cuerpoChoquePies)
        self.addFotogramaCuerpoChoque("caminando_2", Rect.Rect(88, 312, 56, 96), cuerpoChoquePies)
        self.addFotogramaCuerpoChoque("caminando_3", Rect.Rect(140, 312, 40, 96), cuerpoChoquePies)
        self.addFotogramaCuerpoChoque("caminando_4", Rect.Rect(176, 312, 40, 96), cuerpoChoquePies)
        self.addFotogramaCuerpoChoque("caminando_5", Rect.Rect(221, 312, 56, 96), cuerpoChoquePies)
        self.addFotogramaCuerpoChoque("caminando_6", Rect.Rect(74, 415, 56, 96), cuerpoChoquePies)
        self.addFotogramaCuerpoChoque("caminando_7", Rect.Rect(136, 413, 40, 96), cuerpoChoquePies)
        self.addFotogramaCuerpoChoque("caminando_8", Rect.Rect(176, 413, 40, 96), cuerpoChoquePies)
        self.addFotogramaAnimacion("caminando", "caminando_1", 15)
        self.addFotogramaAnimacion("caminando", "caminando_2", 15)
        self.addFotogramaAnimacion("caminando", "caminando_3", 15)
        self.addFotogramaAnimacion("caminando", "caminando_4", 15)
        self.addFotogramaAnimacion("caminando", "caminando_5", 15)
        self.addFotogramaAnimacion("caminando", "caminando_6", 15)
        self.addFotogramaAnimacion("caminando", "caminando_7", 15)
        self.addFotogramaAnimacion("caminando", "caminando_8", 15)
        # PEGANDO
        #self.crearAnimacion("pegando")
        self.addFotogramaCuerpoChoque("pegando_1", Rect.Rect(78, 105, 56, 96), cuerpoChoquePies)
        self.addFotogramaCuerpoChoque("pegando_2", Rect.Rect(139, 105, 70, 96), cuerpoChoquePies)
        self.addFotogramaAnimacion("pegando", "pegando_1", 25)
        self.addFotogramaAnimacion("pegando", "pegando_2", 25)
        self.addFotogramaAnimacion("pegando", "pegando_1", 25, self.finPegando)

    def pegar(self, evento):
        self.setAnimacionActiva("pegando")
    def finPegando(self):
        self.setAnimacionActiva("caminando")

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