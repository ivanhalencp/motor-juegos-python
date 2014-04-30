import Motor
from Motor import Vector
class M_Escenarios(object):
    def __init__(self):
        self.__manejaScroll = False
        self.__imagen = None
        self.__ventana = None
        self.__estadoCamara = "pausada"
        self.__limitesCamara = None
        self.__origenVentana = Vector.Vector(0, 0)
        self.__velocidadCamara = Vector.Vector(1, 1)
    # SETEAR IMAGEN Y VENTANA
    def set(self, imagen, ventana):
        self.__imagen = imagen
        self.__ventana = ventana
    # ACTIVAR CAMARA
    def activarCamara(self):
        self.estadoCamara = "activa"
    # PAUSAR CAMARA
    def pausarCamara(self):
        self.estadoCamara = "pausada"
    # SI LA CAMARA ESTA ACTIVA ACTUALIZO SEGUN POSICION DEL OBJETIVO
    def logicaCamara(self):
        if self.estadoCamara == "activa":
            self.actualizarCamara()
        return Vector.Vector(self.ventana.x, self.ventana.y)
    def actualizarCamara(self):
        nuevaPosicionVentana = self.objetivo.posicion.getCopy()
        nuevaPosicionVentana.addVector(self.ajusteCamara)
        #xPosible, yPosible = self.esPosicionValida(nuevaPosicionVentana)
        desplazamientoCamara = Vector.Vector(0, 0)
        # EJE X
        if self.ventana.x < nuevaPosicionVentana.x:
            desplazamientoCamara.x = self.velocidadCamara.x
        elif self.ventana.x > nuevaPosicionVentana.x:
            desplazamientoCamara.x = self.velocidadCamara.x * -1
        # EJE Y
        if self.ventana.y < nuevaPosicionVentana.y:
            desplazamientoCamara.y = self.velocidadCamara.y
        elif self.ventana.y > nuevaPosicionVentana.y:
            desplazamientoCamara.y = self.velocidadCamara.x * -1
        # SI LA CAMARA PUEDE MOVERSE, ACTUALIZO
        nuevaPosicionVentana.x = self.ventana.x + desplazamientoCamara.x
        nuevaPosicionVentana.y = self.ventana.y + desplazamientoCamara.y
        xPosible, yPosible = self.esPosicionValida(nuevaPosicionVentana)
        if xPosible:
            self.ventana.addVector(Vector.Vector(desplazamientoCamara.x, 0))
        if yPosible:
            self.ventana.addVector(Vector.Vector(0, desplazamientoCamara.y))
    def esPosicionValida(self, posicion):
        xPosible = False
        yPosible = False
        if self.limitesCamara == None:
            xPosible = True
            yPosible = True
        else:
            if (posicion.x > self.limitesCamara.x) and (posicion.x + self.ventana.ancho < self.limitesCamara.x + self.limitesCamara.ancho):
                xPosible = True
            if (posicion.y > self.limitesCamara.y) and (posicion.y + self.ventana.alto < self.limitesCamara.y + self.limitesCamara.alto):
                yPosible = True
        return xPosible, yPosible
    # BLIT
    def blit(self, screen):
        screen.blit (self.imagen, (self.origenVentana.x, self.origenVentana.y), (self.ventana.x, self.ventana.y, self.ventana.ancho, self.ventana.alto))

    # -- GETS Y SETS --
    # IMAGEN (PYGAME SURFACE)
    def getImagen(self):
        return self.__imagen
    def setImagen(self, param):
        self.__imagen = param
    imagen = property(getImagen, setImagen)
    # VENTANA (RECT)
    def getVentana(self):
        return self.__ventana
    def setVentana(self, param):
        self.__ventana = param
    ventana = property(getVentana, setVentana)
    # MANEJA SCROLL (BOOLEAN)
    def getManejaScroll(self):
        return self.__manejaScroll
    def setManejaScroll(self, param):
        self.__manejaScroll = param
    manejaScroll = property(getManejaScroll, setManejaScroll)
    # ESTADO CAMARA (ACTIVA O PAUSADA)
    def getEstadoCamara(self):
        return self.__estadoCamara
    def setEstadoCamara(self, param):
        self.__estadoCamara = param
    estadoCamara = property(getEstadoCamara, setEstadoCamara)
    # OBJETIVO (ENTIDADJUEGO)
    def getObjetivo(self):
        return self.__objetivo
    def setObjetivo(self, param):
        self.__objetivo = param
    objetivo = property(getObjetivo, setObjetivo)
    # AJUSTE CAMARA (VECTOR)
    def getAjusteCamara(self):
        return self.__ajusteCamara
    def setAjusteCamara(self, param):
        self.__ajusteCamara = param
    ajusteCamara = property(getAjusteCamara, setAjusteCamara)
    # LIMITES CAMARA (RECT)
    def getLimitesCamara(self):
        return self.__limitesCamara
    def setLimitesCamara(self, param):
        self.__limitesCamara = param
    limitesCamara = property(getLimitesCamara, setLimitesCamara)
    # PUNTO 0RIGEN DE LA VENTANA POR DEFECTO (0, 0)
    def getOrigenVentana(self):
        return self.__origenVentana
    def setOrigenVentana(self, param):
        self.__origenVentana = param
    origenVentana = property(getOrigenVentana, setOrigenVentana)
    # VELOCIDAD DE MOVIMIENTO DE LA CAMARA
    def getVelocidadCamara(self):
        return self.__velocidadCamara
    def setVelocidadCamara(self, param):
        self.__velocidadCamara = param
    velocidadCamara = property(getVelocidadCamara, setVelocidadCamara)