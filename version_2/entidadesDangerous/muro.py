import Motor, pygame
from pygame.locals import *
from Motor import EntidadJuego, Rect

class Muro(EntidadJuego.EntidadJuego, object):
    def __init__(self, imagen, mundoFisico):
        EntidadJuego.EntidadJuego.__init__(self, imagen, mundoFisico)        
        self.centrarFotogramas = True
    def logica(self):
        pass    
    def crearAnimaciones(self):
        cuerpoChoqueMuro = Rect.Rect(-10, -16, 20, 3)
        cuerpoChoqueSubEscalon = Rect.Rect(-10, 10, 20, 3)
        cuerpoChoqueEscalon = Rect.Rect(-10, -8, 20, 3)
        # MURO
        self.crearAnimacion("muro")
        self.addFotogramaCuerpoChoque("muro_1", Rect.Rect(0, 96, 32, 32), cuerpoChoqueMuro)
        self.addFotogramaAnimacion("muro", "muro_1", 30)
        # SUB ESCALON
        self.crearAnimacion("subEscalon")
        self.addFotogramaCuerpoChoque("subEscalon_1", Rect.Rect(32, 96, 32, 32), cuerpoChoqueSubEscalon)
        self.addFotogramaAnimacion("subEscalon", "subEscalon_1", 30)
        # ESCALON
        self.crearAnimacion("escalon")
        self.addFotogramaCuerpoChoque("escalon_1", Rect.Rect(64, 96, 32, 32), cuerpoChoqueEscalon)
        self.addFotogramaAnimacion("escalon", "escalon_1", 30)
        self.setAnimacionActiva("muro")