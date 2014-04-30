from pygame.locals import *
from Motor import Vector, Juego, Rect, Util
from TestMotor import Guy

class TestJuego(Juego.Juego, object):
    def __init__(self):
        Juego.Juego.__init__(self)
    def crearMundo(self):
        # SETEO LIMITES DENTRO DE LOS CUALES SE PUEDE MOVER EL PERSONAJE
        self.mundoFisico.limites.setRect(30, 140, 400, 60)
        # CARGO MUSICA DE FONDO
        #self.cargarMusicaFondo("Data", "MusicaFondo1.mp3")
        #self.tocarMusicaFondo()
        # CARGAR SONIDO PARA GOLPES
        self.sonidoGolpe = self.cargarAudio("Data", "Golpe.ogg")
        # CARGO IMAGENES
        img_fondo = self.cargarImagen("Data", "FondoFF2.gif")
        img_guy = self.cargarImagen("Data", "Guy.gif", -1)
        # ESCENARIO
        self.mEscenarios.set(img_fondo, Rect.Rect(0, 0, 10, 10))
        # GUY
        guy = Guy.Guy(img_guy, self.mundoFisico, self.controladorEventos)
        Util.cargarAnimacionEntidad("Data/Guy.xml", guy)
        guy.crearAnimaciones()
        guy.registrarEventos(K_RIGHT, K_LEFT, K_UP, K_DOWN, K_p)
        guy.id = "GUY_1"
        self.addEntidad(guy)
        self.mundoFisico.addObjetoFisico(guy)
        self.mundoFisico.addEventoChoque(guy, self.choqueGuy)
        # GUY 2
        self.guy_2 = Guy.Guy(img_guy, self.mundoFisico, self.controladorEventos)
        Util.cargarAnimacionEntidad("Data/Guy.xml", self.guy_2)
        self.guy_2.crearAnimaciones()
        self.guy_2.registrarEventos(K_d, K_a, K_w, K_s, K_o)
        self.guy_2.id = "GUY_2"
        self.addEntidad(self.guy_2)
        self.mundoFisico.addObjetoFisico(self.guy_2)
        self.mundoFisico.addEventoChoque(self.guy_2, self.choqueGuy)
        # GUY 3
        guy_3 = Guy.Guy(img_guy, self.mundoFisico, self.controladorEventos)
        Util.cargarAnimacionEntidad("Data/Guy.xml", guy_3)
        guy_3.crearAnimaciones()
        guy_3.registrarEventos(K_h, K_f, K_t, K_g, K_i)
        guy_3.id = "GUY_3"
        self.addEntidad(guy_3)
        self.mundoFisico.addObjetoFisico(guy_3)
        self.mundoFisico.addEventoChoque(guy_3, self.choqueGuy)
        # GUY COMO OBJETIVO DE LA CAMARA
        self.mEscenarios.objetivo = guy;
        self.mEscenarios.ajusteCamara = Vector.Vector(-200, -120)
        self.mEscenarios.limitesCamara = Rect.Rect(0, 0, 900, 200)
        self.mEscenarios.velocidadCamara.set(1, 1)
        self.mEscenarios.activarCamara()
    def registrarEventos(self):
        # GENERAL JUEGO
        self.controladorEventos.addListener(QUIT, self.terminar)
        self.controladorEventos.addListenerTeclado(KEYDOWN, K_ESCAPE, self.terminar)
        self.controladorEventos.addListenerTeclado(KEYDOWN, K_1, self.cambiarCamara)
        self.controladorEventos.addListenerTeclado(KEYDOWN, K_p, self.reproducirGolpe)
    def reproducirGolpe(self, evento):
        self.sonidoGolpe.play()
    def cambiarCamara(self, evento):
        self.mEscenarios.objetivo = self.guy_2
    def choqueGuy(self, quien, conQuien):
        # print "Choca " + quien.id + " con " + conQuien.id
        pass
    def logica(self):
        # TEST EFECTO FONDO
        if self.mEscenarios.ventana.ancho < 450:
            self.mEscenarios.ventana.ancho += 5
        if self.mEscenarios.ventana.alto < 200:
            self.mEscenarios.ventana.alto += 5
        self.mundoFisico.limites.x = self.mEscenarios.ventana.x + 30

# TEST DEL JUEGO
if __name__ == '__main__':
    test = TestJuego()
    test.buclePrincipal()
