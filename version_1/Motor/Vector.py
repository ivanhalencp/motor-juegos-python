class Vector(object):
    __x = 0
    __y = 0
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    def set(self, x, y):
        self.__x = x
        self.__y = y
    def addVector(self, vector):
        self.__x += vector.x
        self.__y += vector.y
    def susVector(self, vector):
        self.__x -= vector.x
        self.__y -= vector.y
    def getCopy(self):
        vCopy = Vector(self.__x, self.__y)
        return vCopy
    def multEscalar(self, razon):
        self.__x *= razon
        self.__y *= razon
    def modulo(self):
        # Estudiar mas matematica en python para esto...
        pass
    def invertir(self):
        self.__x *= -1
        self.__y *= -1
    def invertirX(self):
        self.__x *= -1
    def invertirY(self):
        self.__y *= -1

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