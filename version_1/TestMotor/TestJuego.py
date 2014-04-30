import os, pygame, Motor, Guy
from pygame.locals import *
from Motor import Vector, Constantes, MundoFisico, ControladorEventos, Configuracion, Juego, Jugador, Rect, EntidadJuego

class TestJuego(Juego.Juego, object):
    def __init__(self):
        Juego.Juego.__init__(self)
    def crearMundo(self):
        # SETEO LIMITES DENTRO DE LOS CUALES SE PUEDE MOVER EL PERSONAJE
        self.mundoFisico.limites.setRect(30, 140, 400, 60)
        # CARGO IMAGENES
        img_fondo = self.cargarImagen("../Data", "FondoFF2.gif")
        img_guy = self.cargarImagen("../Data", "Guy.gif", -1)
        # ESCENARIO
        self.mEscenarios.set(img_fondo, Rect.Rect(0, 0, 10, 10))
        # GUY
        guy = Guy.Guy(img_guy, self.mundoFisico, self.controladorEventos)
        self.addEntidad(guy)
        # GUY COMO OBJETIVO DE LA CAMARA
        self.mEscenarios.objetivo = guy;
        self.mEscenarios.ajusteCamara = Vector.Vector(-200, -100)
        self.mEscenarios.limitesCamara = Rect.Rect(0, 0, 900, 200)
        self.mEscenarios.velocidadCamara.set(.5, .5)
        self.mEscenarios.activarCamara()
    def registrarEventos(self):
        # GENERAL JUEGO
        self.controladorEventos.addListener(QUIT, self.terminar)
        self.controladorEventos.addListenerTeclado(KEYDOWN, K_ESCAPE, self.terminar)
    def logica(self):
        # TEST EFECTO FONDO
        if self.mEscenarios.ventana.ancho < 450:
            self.mEscenarios.ventana.ancho += 5
        if self.mEscenarios.ventana.alto < 200:
            self.mEscenarios.ventana.alto += 5
        self.mundoFisico.limites.x = self.mEscenarios.ventana.x + 30

# TEST DEL JUEGO
test = TestJuego()
test.buclePrincipal()