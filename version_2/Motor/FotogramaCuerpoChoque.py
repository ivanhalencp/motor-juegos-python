class FotogramaCuerpoChoque(object):
    #__clave (String)
    #__rectFotograma (Rect)
    #__rectCuerpoChoque (Rect)
    def __init__(self, clave, rectFotograma, rectCuerpoChoque):
        self.__clave = clave
        self.__rectFotograma = rectFotograma
        self.__rectCuerpoChoque = rectCuerpoChoque

    # -- GETS Y SETS --
    def getClave(self):
        return self.__clave
    def setClave(self, param):
        self.__clave = param
    clave = property(getClave, setClave)
    def getRectFotograma(self):
        return self.__rectFotograma
    def setRectFotograma(self, param):
        self.__rectFotograma = param
    rectFotograma = property(getRectFotograma, setRectFotograma)
    def getRectCuerpoChoque(self):
        return self.__rectCuerpoChoque
    def setRectCuerpoChoque(self, param):
        self.__rectCuerpoChoque = param
    rectCuerpoChoque = property(getRectCuerpoChoque, setRectCuerpoChoque)