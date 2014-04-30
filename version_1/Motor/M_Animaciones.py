import Motor, pygame
from pygame.locals import *
from Motor import FotogramaCuerpoChoque, Animacion

class M_Animaciones(object):
    #__fotogramasCuerpoChoque (Diccionario)
    #__animaciones (Diccionario)
    #__tiempoEsperaDefecto (Int)
    #__imagen (Pygame Surface)
    #__fotogramaActivo (Int)
    #__animacionActiva (String (clave Animacion))
    def __init__(self, imagen):
        self.__fotogramasCuerpoChoque = {}
        self.__animaciones = {}
        self.__tiempoEsperaDefecto = 0
        self.__imagen = imagen
        self.__imagenInvertida = None
        self.__invertirImagen = False
        self.__fotogramaActivo = -1
        self.__animacionActiva = ""
        self.__centrarFotogramas = False
    def addFotogramaCuerpoChoque(self, clave, rectFotograma, rectCuerpoChoque):
        fcc = FotogramaCuerpoChoque.FotogramaCuerpoChoque(clave, rectFotograma, rectCuerpoChoque)
        self.__fotogramasCuerpoChoque[clave] = fcc
    def crearAnimacion(self, clave, tiempoEspera = -1, ciclica = True):
        if tiempoEspera == -1:
            tiempoEspera = self.__tiempoEsperaDefecto
        animacion = Animacion.Animacion(clave, tiempoEspera, ciclica)
        self.__animaciones[clave] = animacion
    def setAnimacionActiva(self, clave):
        if self.animaciones.has_key(clave):
            if self.animacionActiva != clave:
                self.animacionActiva = clave
                self.animaciones[self.animacionActiva].indiceFotogramaActivo = 0;
        else:
            print "ERROR(M_Animaciones -> setAnimacionActiva()): clave de animacion no definifa -> " + clave
    def addFotogramaAnimacion(self, claveAnimacion, claveFCC, tiempoEspera, accion = None):
        self.__animaciones[claveAnimacion].addFotograma(claveFCC, tiempoEspera, accion)
    def animar(self):
        if self.animacionActiva != "" and self.animaciones.has_key(self.animacionActiva):
            self.animaciones[self.animacionActiva].animar()
        else:
            print "ERROR(M_Animaciones -> animar()):  no hay animacion activa"
    def getCuerpoChoqueActivo(self):
        if self.animacionActiva != "" and self.animaciones.has_key(self.animacionActiva):
            cHActivo = self.fotogramasCuerpoChoque[self.animaciones[self.animacionActiva].getClaveFCCActivo()].rectCuerpoChoque
        else:
            print "ERROR(M_Animaciones -> getCuerpoChoqueActivo()):  no hay animacion activa"
            cHActivo = None
        return cHActivo
    def blit(self, screen, posicionPantalla):
        rectActivo = self.fotogramasCuerpoChoque[self.animaciones[self.animacionActiva].getClaveFCCActivo()].rectFotograma
        if not self.invertirImagen:
            if not self.centrarFotogramas:
                screen.blit(self.imagen, (posicionPantalla.x, posicionPantalla.y), (rectActivo.x, rectActivo.y, rectActivo.ancho, rectActivo.alto))
            else:
                screen.blit(self.imagen, (posicionPantalla.x - (rectActivo.ancho / 2), posicionPantalla.y - (rectActivo.alto / 2)), (rectActivo.x, rectActivo.y, rectActivo.ancho, rectActivo.alto))
        else:
            if self.imagenInvertida == None:
                self.imagenInvertida = pygame.transform.flip(self.imagen, True, False)
            if not self.centrarFotogramas:
                screen.blit(self.imagenInvertida, (posicionPantalla.x, posicionPantalla.y), (self.imagen.get_rect().width - rectActivo.x - rectActivo.ancho, rectActivo.y, rectActivo.ancho, rectActivo.alto))
            else:
                screen.blit(self.imagenInvertida, (posicionPantalla.x - (rectActivo.ancho / 2), posicionPantalla.y - (rectActivo.alto / 2)), (self.imagen.get_rect().width - rectActivo.x - rectActivo.ancho, rectActivo.y, rectActivo.ancho, rectActivo.alto))

    # -- GETS Y SETS --
    def getImagen(self):
        return self.__imagen
    def setImagen(self, imagen):
        self.__imagen = imagen
    imagen = property(getImagen, setImagen)
    def getImagenInvertida(self):
        return self.__imagenInvertida
    def setImagenInvertida(self, param):
        self.__imagenInvertida = param
    imagenInvertida = property(getImagenInvertida, setImagenInvertida)
    def getInvertirImagen(self):
        return self.__invertirImagen
    def setInvertirImagen(self, param):
        self.__invertirImagen = param
    invertirImagen = property(getInvertirImagen, setInvertirImagen)
    def getFotogramasCuerpoChoque(self):
        return self.__fotogramasCuerpoChoque
    def setFotogramasCuerpoChoque(self, param):
        self.__fotogramasCuerpoChoque = param
    fotogramasCuerpoChoque = property(getFotogramasCuerpoChoque, setFotogramasCuerpoChoque)
    def getAnimacionActiva(self):
        return self.__animacionActiva
    def propSetAnimacionActiva(self, param):
        self.__animacionActiva = param
    animacionActiva = property(getAnimacionActiva, propSetAnimacionActiva)
    def getFotogramaActivo(self):
        return self.__fotogramaActivo
    def setFotogramaActivo(self, param):
        self.__fotogramaActivo = param
    fotogramaActivo = property(getFotogramaActivo, setFotogramaActivo)
    def getAnimaciones(self):
        return self.__animaciones
    def setAnimaciones(self, param):
        self.__animaciones = param
    animaciones = property(getAnimaciones, setAnimaciones)
    def getTiempoEsperaDefecto(self):
        return self.__tiempoEsperaDefecto
    def setTiempoEsperaDefecto(self, param):
        self.__tiempoEsperaDefecto = param
    tiempoEsperaDefecto = property(getTiempoEsperaDefecto, setTiempoEsperaDefecto)    
    # FOTOGRAMAS CENTRADOS O NO
    def getCentrarFotogramas(self):
        return self.__centrarFotogramas
    def setCentrarFotogramas(self, param):
        self.__centrarFotogramas = param
    centrarFotogramas = property(getCentrarFotogramas, setCentrarFotogramas)


