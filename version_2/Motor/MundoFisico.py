import Motor
from Motor import Rect

class MundoFisico(object):
    def __init__(self):
        self.__limites = Rect.Rect(0, 0, 0, 0)
        self.__eventosChoque = {}
        self.__objetosFisicos = []
    # NUEVO LISTENER PARA EVENTO DE CHOQUES
    def addEventoChoque(self, entidad, accion = None):
        self.eventosChoque[entidad] = accion
    # NUEVO OBJETO AL MUNDO FISICO
    def addObjetoFisico(self, entidad):
        self.objetosFisicos.append(entidad)
    # RECORRER EL MUNDO BUSCANDO CHOQUES
    def chequearChoques(self):
        # PARA CADA ELEMENTO DEL MUNDO FISICO
        for obj in (self.objetosFisicos):
            # SI TIENE UN EVENTO DE CHOQUE DEFINIDO
            if self.eventosChoque.has_key(obj):
                obj.mFisica.colisionesActuales = []
                obj.mFisica.entidadesCercanas = []
                # PARA CADA ELEMENTO DEL MUNDO FISICO...
                for otroObj in (self.objetosFisicos):
                    # ...DISTINO DEL PRIMERO
                    if obj != otroObj and obj.mFisica.getDistanciaAEntidad(otroObj) < 50:
                        obj.mFisica.entidadesCercanas.append(otroObj)
                        # ME QUEDO CON SUS CUERPOS DE CHOQUE
                        cCObj = obj.mFisica.getCuerpoChoqueAbsoluto()
                        cCObjSiguiente = obj.mFisica.getCuerpoChoqueAbsolutoSiguiente()
                        cCOtroObj = otroObj.mFisica.getCuerpoChoqueAbsoluto()
                        # SI HAY INTERSECCION, LLAMO A LA ACCION REGISTRADA Y LE PASO EL OBJETO CON EL CUAL
                        # ESTA CHOCANDO
                        if cCObj.intersect(cCOtroObj):
                            obj.mFisica.colisionesActuales.append(otroObj)
                            if self.eventosChoque[obj] != None:
                                self.eventosChoque[obj](obj, otroObj)

    # -- GETS Y SETS --
    # LIMITES
    def getLimites(self):
        return self.__limites
    def setLimites(self, param):
        self.__limites = param
    limites = property(getLimites, setLimites)
    # EVENTOS DE CHOQUE
    def getEventosChoque(self):
        return self.__eventosChoque
    def setEventosChoque(self, param):
        self.__eventosChoque = param
    eventosChoque = property(getEventosChoque, setEventosChoque)
    # OBJETOS EN MUNDO FISICO
    def getObjetosFisicos(self):
        return self.__objetosFisicos
    def setObjetosFisicos(self, param):
        self.__objetosFisicos = param
    objetosFisicos = property(getObjetosFisicos, setObjetosFisicos)