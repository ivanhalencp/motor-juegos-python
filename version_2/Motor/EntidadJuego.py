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
        # ACCIONES FUERA ESCENA
        self.__logicaFueraEscena = True
        self.__animarFueraEscena = False
        self.__aplicarFisicaFueraEscena = True
        self.__graficarFueraEscena = False
        # SI EL JUEGO MANEJA CAPAZ, EL ID DE LA CAPA A LA QUE PERTENEC LA ENTIDAD
        self.__idCapa = -1

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
    # ANIMAR:
    # CAMBIA AL SIGUIENTE FOTOGRAMA DE LA ANIMACION ACTIVA
    def animar(self):
        # CORRER ANIMACION
        self.mAnimaciones.animar()        
    # APLICAMOS FISICA PARA EL MOVIMIENTO
    def aplicarFisica(self):
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
    # ID TIPO
    def getIdTipo(self):
        return self.__idTipo
    def setIdTipo(self, param):
        self.__idTipo = param
    idTipo = property(getIdTipo, setIdTipo)
    # PROFUNDIDAD
    def getProfundidad(self):
        return self.__profundidad
    def setProfundidad(self, param):
        self.__profundidad = param
    profundidad = property(getProfundidad, setProfundidad)
    # LOGICA FUERA ESCENA
    def getLogicaFueraEscena(self):
        return self.__logicaFueraEscena
    def setLogicaFueraEscena(self, param):
        self.__logicaFueraEscena = param
    logicaFueraEscena = property(getLogicaFueraEscena, setLogicaFueraEscena)
     # GRAFICAR FUERA ESCENA
    def getGraficarFueraEscena(self):
        return self.__graficarFueraEscena
    def setGraficarFueraEscena(self, param):
        self.__graficarFueraEscena = param
    graficarFueraEscena = property(getGraficarFueraEscena, setGraficarFueraEscena)
     # ANIMAR FUERA ESCENA
    def getAnimarFueraEscena(self):
        return self.__animarFueraEscena
    def setAnimarFueraEscena(self, param):
        self.__animarFueraEscena = param
    animarFueraEscena = property(getAnimarFueraEscena, setAnimarFueraEscena)
     # APLICAR FISICA FUERA ESCENA
    def getAplicarFisicaFueraEscena(self):
        return self.__aplicarFisicaFueraEscena
    def setAplicarFisicaFueraEscena(self, param):
        self.__aplicarFisicaFueraEscena = param
    aplicarFisicaFueraEscena = property(getAplicarFisicaFueraEscena, setAplicarFisicaFueraEscena)
    # ID CAPA
    def getIdCapa(self):
        return self.__idCapa
    def setIdCapa(self, param):
        self.__idCapa = param
    idCapa = property(getIdCapa, setIdCapa)