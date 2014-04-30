import Motor
from Motor import Vector, Rect

class M_Fisica(object):
    #__posicion = (Vector)
    #__velocidad = (Vector)
    #__celeracion = (Vector)
    #__cuerpoChoque = (Rect)
    #__mundoFisico = (MundoFisico)
    def __init__(self, posicion, mundoFisico):
        self.__posicion = posicion
        self.__cuerpoChoque = None
        self.__velocidad = Vector.Vector(0, 0)
        self.__aceleracion = Vector.Vector(0, 0)
        self.__focalizarMovimiento = True
        # REFERENCIA AL MUNDO FISICO
        self.__mundoFisico = mundoFisico
    def addVector(self, vector):
        self.posicion.addVector(vector)
    def getCuerpoChoqueAbsoluto(self):
        cuerpoChoqueAbsoluto = self.cuerpoChoque.getCopy()
        cuerpoChoqueAbsoluto.addVector(self.posicion)
        return cuerpoChoqueAbsoluto
    def aplicar(self, focalizarEn = ""):
        self.velocidad.addVector(self.aceleracion)
        if focalizarEn == "":
            self.posicion.addVector(self.velocidad)
        elif focalizarEn == "x":
            velocidadX = self.velocidad.getCopy()
            velocidadX.y = 0
            self.posicion.addVector(velocidadX)
        elif focalizarEn == "y":
            velocidadY = self.velocidad.getCopy()
            velocidadY.x = 0
            self.posicion.addVector(velocidadY)
    def getPosicionSiguiente(self, focalizarEn = ""):
        posicionSiguiente = self.posicion.getCopy()
        velocidadSiguiente = self.velocidad.getCopy()
        velocidadSiguiente.addVector(self.aceleracion)
        # FOCALIZO EL MOVIMIENTO EN UN SOLO EJE
        if focalizarEn == "x":
            # SI ES EN X, ANULO COMPONENTE Y
            velocidadSiguiente.y = 0
        elif focalizarEn == "y":
            # SI ES EN Y, ANULO COMPONENTE X
            velocidadSiguiente.x = 0
        posicionSiguiente.addVector(velocidadSiguiente)
        return posicionSiguiente
    def getCuerpoChoqueAbsolutoSiguiente(self, focalizarEn = ""):
        posicionSiguiente = self.getPosicionSiguiente(focalizarEn)
        cuerpoChoqueAbsolutoSiguiente = self.cuerpoChoque.getCopy()
        cuerpoChoqueAbsolutoSiguiente.addVector(posicionSiguiente)
        return cuerpoChoqueAbsolutoSiguiente
    def intentarAvanzar(self):
        movimientoPosible = False
        if self.esMovimientoPosible():
            self.aplicar()
            movimientoPosible= True
        elif self.focalizarMovimiento:
            if self.esMovimientoPosible("x"):
                self.aplicar("x")
                movimientoPosible= True
            elif self.esMovimientoPosible("y"):
                self.aplicar("y")
                movimientoPosible= True
        return movimientoPosible
    def esMovimientoPosible(self, focalizarEn = ""):
        # OBTENGO CUERPO DE CHOQUE SIGUIENTE
        cuerpoChoqueAbsolutoSiguiente = self.getCuerpoChoqueAbsolutoSiguiente(focalizarEn)
        movimientoPosible = False
        # LIMITES DEL MUNDO FISICO
        # COORDENADAS DEL LIMITE SUPERIOR IZQUIERDO (SI)
        si_x = self.mundoFisico.limites.x
        si_y = self.mundoFisico.limites.y
        # COORDENADAS DEL LIMITE INFERIOR DERECHO (ID)
        id_x = si_x + self.mundoFisico.limites.ancho
        id_y = si_y + self.mundoFisico.limites.alto
        if cuerpoChoqueAbsolutoSiguiente.x >= si_x and cuerpoChoqueAbsolutoSiguiente.y >= si_y:
            if cuerpoChoqueAbsolutoSiguiente.x + self.cuerpoChoque.ancho <= id_x and cuerpoChoqueAbsolutoSiguiente.y + self.cuerpoChoque.alto <= id_y:
                movimientoPosible = True
        return movimientoPosible

    # -- GETS Y SETS --
    # POSICION
    def getPosicion(self):
        return self.__posicion
    def setPosicion(self, posicion):
        self.__posicion = posicion
    posicion = property(getPosicion, setPosicion)
    # VELOCIDAD
    def getVelocidad(self):
        return self.__velocidad
    def setVelocidad(self, velocidad):
        self.__velocidad = velocidad
    velocidad = property(getVelocidad, setVelocidad)
    # ACELERACION
    def getAceleracion(self):
        return self.__aceleracion
    def setAceleracion(self, param):
        self.__aceleracion = param
    aceleracion = property(getAceleracion, setAceleracion)
    # CUERPO CHOQUE
    def getCuerpoChoque(self):
        return self.__cuerpoChoque
    def setCuerpoChoque(self, cuerpoChoque):
        self.__cuerpoChoque = cuerpoChoque
    cuerpoChoque = property(getCuerpoChoque, setCuerpoChoque)
    # MUNDO FISICO
    def getMundoFisico(self):
        return self.__mundoFisico
    def setMundoFisico(self, param):
        self.__mundoFisico = param
    mundoFisico = property(getMundoFisico, setMundoFisico)
    # FOCALIZAR MOVIMIENTO, SI EL MOVIMIENTO NO ES POSIBLE CON UN VECTOR CON COMPONENTES X, Y ...
    # ...ENTONCES INTENTA MOVER EN X O EN Y
    def getFocalizarMovimiento(self):
        return self.__focalizarMovimiento
    def setFocalizarMovimiento(self, param):
        self.__focalizarMovimiento = param
    focalizarMovimiento = property(getFocalizarMovimiento, setFocalizarMovimiento)