import Motor
from Motor import Vector

class Rect(object):
    __x = 0
    __y = 0
    __ancho = 0
    __alto = 0
    def __init__(self, x, y, ancho, alto):
        self.__x = x
        self.__y = y
        self.__ancho = ancho
        self.__alto = alto
    def setRect(self, x, y, ancho, alto):
        self.__x = x
        self.__y = y
        self.__ancho = ancho
        self.__alto = alto
    def addVector(self, vector):
        self.__x += vector.x
        self.__y += vector.y
    def getCopy(self):
        rCopy = Rect(self.__x, self.__y, self.__ancho, self.__alto)
        return rCopy
    def getVertices(self):
        pareja_si = (self.__x, self.__y)
        pareja_sd = (self.__x + self.__ancho, self.__y)
        pareja_ii = (self.__x, self.__y + self.__alto)
        pareja_id = (self.__x + self.__ancho, self.__y + self.__alto)
        vertices = (pareja_si, pareja_sd, pareja_ii, pareja_id)
        return vertices
    def getCentro(self):
        centro = Vector.Vector((self.x + (self.ancho/2)), (self.y + (self.alto/2)))
        return centro
    def intersect(self, rect, nivel = -1):
        # USO NIVEL PARA IMPEDIR RECURSION INFINITA
        resultado = False
        for vertice in rect.getVertices():
            if self.checkIn(vertice[0], vertice[1]):
                resultado = True
        if nivel == -1 and resultado == False:
            resultado = rect.intersect(self, 0)
        return resultado
    def checkIn(self, x, y):
        resultado = False
        if x >= self.__x and x <= (self.__x + self.__ancho):
            if y >= self.__y and y <= (self.__y + self.__alto):
                resultado = True
        return resultado

    # -- GETS Y SETS --
    # X
    def getX(self):
        return self.__x
    def setX(self, x):
        self.__x = x
    x = property(getX, setX)
    # Y
    def getY(self):
        return self.__y
    def setY(self, y):
        self.__y = y
    y = property(getY, setY)
    # ANCHO
    def getAncho(self):
        return self.__ancho
    def setAncho(self, ancho):
        self.__ancho = ancho
    ancho = property(getAncho, setAncho)
    # ALTO
    def getAlto(self):
        return self.__alto
    def setAlto(self, alto):
        self.__alto = alto
    alto = property(getAlto, setAlto)