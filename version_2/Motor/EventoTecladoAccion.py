class EventoTecladoAccion(object):
    def __init__(self, tipoEvento, key, accion):
        self.__tipoEvento = tipoEvento
        self.__key = key
        self.__accion = accion
    # TIPO EVENTO
    def getTipoEvento(self):
        return self.__tipoEvento
    def setTipoEvento(self, tipoEvento):
        self.__tipoEvento = tipoEvento
    tipoEvento = property(getTipoEvento, setTipoEvento)
    # KEY
    def getKey(self):
        return self.__key
    def setKey(self, key):
        self.__key = key
    key = property(getKey, setKey)
    # ACCION
    def getAccion(self):
        return self.__accion
    def setAccion(self, accion):
        self.__accion = accion
    accion = property(getAccion, setAccion)