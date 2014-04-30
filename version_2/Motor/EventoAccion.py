class EventoAccion(object):
    def __init__(self, tipoEvento, accion):
        self.__tipoEvento = tipoEvento
        self.__accion = accion
    # TIPO EVENTO
    def getTipoEvento(self):
        return self.__tipoEvento
    def setTipoEvento(self, tipoEvento):
        self.__tipoEvento = tipoEvento
    tipoEvento = property(getTipoEvento, setTipoEvento)
    # ACCION
    def getAccion(self):
        return self.__accion
    def setAccion(self, accion):
        self.__accion = accion
    accion = property(getAccion, setAccion)