import Motor
from Motor import Rect, Vector, M_Animaciones, M_Fisica

class EntidadJuego(object):
    #__mAnimaciones (M_Animaciones)
    #__mFisica = (M_Fisica)
    #__posicion (Vector)
    #__cuerpoChoqueDefecto (Rect)
    def __init__(self, imagen, mundoFisico):
        self.__posicion = Vector.Vector(0, 0)
        self.__cuerpoChoqueDefecto = Rect.Rect(0, 0, 0, 0)
        self.__activo = True
        # MANEJADOR FISICA
        self.__mFisica = M_Fisica.M_Fisica(self.__posicion, mundoFisico)
        self.__mFisica.cuerpoChoque = self.cuerpoChoqueDefecto
        # MANEJADOR ANIMACIONES
        self.__mAnimaciones = M_Animaciones.M_Animaciones(imagen)

    # GRAFICOS / ANIMACIONES
    def addFotogramaCuerpoChoque(self, clave, rectFotograma, rectCuerpoChoque = None):
        if rectCuerpoChoque == None:
            rectCuerpoChoque = self.__cuerpoChoqueDefecto
        self.mAnimaciones.addFotogramaCuerpoChoque(clave, rectFotograma, rectCuerpoChoque)
    def crearAnimacion(self, clave, tiempoEspera = -1, ciclica = True):
        self.mAnimaciones.crearAnimacion(clave, tiempoEspera = -1, ciclica = True)
    def setAnimacionActiva(self, clave):
        self.mAnimaciones.setAnimacionActiva(clave)
    def addFotogramaAnimacion(self, claveAnimacion, claveFCC, tiempoEspera, accion = None):
        self.mAnimaciones.addFotogramaAnimacion(claveAnimacion, claveFCC, tiempoEspera, accion)
    def blit(self, screen, ajustePosicion = None):
        # AJUSTE DE POSICION SEGUN POSICION DE PANTALLA
        if ajustePosicion == None:
            ajustePosicion = Vector.Vector(0, 0)
        posicionReal = self.mFisica.posicion.getCopy()
        posicionReal.susVector(ajustePosicion)
        self.mAnimaciones.blit(screen, posicionReal)
    # FISICA
    def getCuerpoChoqueAbsoluto(self):
        return self.mFisica.getCuerpoChoqueAbsoluto()
    # GENERAL
    def animar(self):
        # CORRER ANIMACION
        self.mAnimaciones.animar()
        # ACTUALIZO CUERPO DE CHOQUE ACTIVO LUEGO DEL CAMBIO DE FRAME(ANIMACION)
        self.mFisica.cuerpoChoque = self.mAnimaciones.getCuerpoChoqueActivo()
        # APLICO FISICA
        self.mFisica.intentarAvanzar()

    # LOGICA PROPIA DE CADA ENTIDAD
    # (SOBREESCRIBIR ESTE METODO)
    def logica(self):
        pass

    # -- GETS Y SETS --
    # MANEJADOR ANIMACIONES
    def getMAnimaciones(self):
        return self.__mAnimaciones
    def setMAnimaciones(self, param):
        self.__mAnimaciones = param
    mAnimaciones = property(getMAnimaciones, setMAnimaciones)
    # MANEJADOR FISICA
    def getMFisica(self):
        return self.__mFisica
    def setMFisica(self, param):
        self.__mFisica = param
    mFisica = property(getMFisica, setMFisica)
    # ACTIVO
    def getActivo(self):
        return self.__activo
    def setActivo(self, param):
        self.__activo = param
    activo = property(getActivo, setActivo)
    # POSICION
    def getPosicion(self):
        return self.__mFisica.posicion
    def setPosicion(self, param):
        self.__mFisica.posicion = param
    posicion = property(getPosicion, setPosicion)
    # DIRECCION
    def getVelocidad(self):
        return self.__mFisica.velocidad
    def setVelocidad(self, velocidad):
        self.__mFisica.velocidad = velocidad
    velocidad = property(getVelocidad, setVelocidad)
    # CUERPO DE CHOQUE X DEFECTO
    def getCuerpoChoqueDefecto(self):
        return self.__cuerpoChoqueDefecto
    def setCuerpoChoqueDefecto(self, param):
        self.__cuerpoChoqueDefecto = param
    cuerpoChoqueDefecto = property(getCuerpoChoqueDefecto, setCuerpoChoqueDefecto)
    # CUERPO DE CHOQUE ACTIVO (SOLO LECTURA)
    def getCuerpoChoque(self):
        return self.mAnimaciones.getCuerpoChoqueActivo()
    cuerpoChoque = property(getCuerpoChoque)
    # FOTOGRAMAS CENTRADOS O NO
    def getCentrarFotogramas(self):
        return self.__mAnimaciones.centrarFotogramas
    def setCentrarFotogramas(self, param):
        self.__mAnimaciones.centrarFotogramas = param
    centrarFotogramas = property(getCentrarFotogramas, setCentrarFotogramas)
    # ID
    def getId(self):
        return self.__id
    def setId(self, param):
        self.__id = param
    id = property(getId, setId)
    # PROFUNDIDAD
    def getProfundidad(self):
        return self.__profundidad
    def setProfundidad(self, param):
        self.__profundidad = param
    profundidad = property(getProfundidad, setProfundidad)