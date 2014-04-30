import Motor, pygame
from pygame.locals import *
from Motor import EntidadJuego, Rect

class Escalera(EntidadJuego.EntidadJuego, object):
    def __init__(self, imagen, mundoFisico):
        EntidadJuego.EntidadJuego.__init__(self, imagen, mundoFisico)        
        self.centrarFotogramas = True
    def logica(self):
        pass    
    def crearAnimaciones(self):
        cuerpoChoque = Rect.Rect(-16, -16, 32, 32)        
        # ESCALERA
        self.crearAnimacion("comun")
        self.addFotogramaCuerpoChoque("comun_1", Rect.Rect(0, 128, 32, 32), cuerpoChoque)
        self.addFotogramaAnimacion("comun", "comun_1", 30)
        # ESCALERA MURO
        self.crearAnimacion("muro")
        self.addFotogramaCuerpoChoque("muro_1", Rect.Rect(32, 128, 32, 32), cuerpoChoque)
        self.addFotogramaAnimacion("muro", "muro_1", 30)
