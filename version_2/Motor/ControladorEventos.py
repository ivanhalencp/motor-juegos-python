import Motor, pygame
from pygame.locals import *
from Motor import EventoTecladoAccion, EventoAccion

class ControladorEventos(object):
    __listenersTeclado = []
    __listeners = []
    def __init__(self, pygame):
        self.__pygame = pygame
    def addListenerTeclado(self, evento, key, accion):
        eventoTecladoAccion = EventoTecladoAccion.EventoTecladoAccion(evento, key, accion)
        self.__listenersTeclado.append(eventoTecladoAccion)
    def addListener(self, evento, accion):
        eventoAccion = EventoAccion.EventoAccion(evento, accion)
        self.__listeners.append(eventoAccion)
    def notificarListeners(self):
        if len(self.__listenersTeclado) > 0:
            # RECORRO EVENTOS DE TECLADO
            for event in self.__pygame.event.get([KEYDOWN, KEYUP]):
                # RECORRO OBJETOS REGISTRADOS PARA ESCUCHAR EVENTOS
                for listener in self.__listenersTeclado:
                    # SI EL TIPO DE EVENTO ES EL QUE EL OBJETO ESCUCHA LLAMO A
                    # LA ACCION REGISTRADA
                    if (event.type == listener.tipoEvento) and (event.key == listener.key):
                        listener.accion(event)
        if len(self.__listeners) > 0:
            # RECORRO RESTO DE LOS EVENTOS
            for event in self.__pygame.event.get():
                # RECORRO OBJETOS REGISTRADOS PARA ESCUCHAR EVENTOS
                for listener in self.__listeners:
                    # SI EL TIPO DE EVENTO ES EL QUE EL OBJETO ESCUCHA LLAMO A
                    # LA ACCION REGISTRADA
                    if event.type == listener.tipoEvento:
                        listener.accion(event)
