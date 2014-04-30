from pygame.locals import *
from Motor import Vector, Juego, Rect, Util
from entidadesDangerous import hero, bot, muro, escalera

class Dangerous(Juego.Juego, object):
    def __init__(self):
        Juego.Juego.__init__(self)
        self.img_tile = None
        self.hero = None
        self.bot = None
        self.bots = []
    def crearMundo(self):
        # SETEO LIMITES DENTRO DE LOS CUALES SE PUEDE MOVER EL PERSONAJE
        self.mundoFisico.limites.setRect(0, 0, 800, 600)
        # CARGO IMAGENES
        img_fondo = self.cargarImagen("dangerousData", "bg_1.png")
        self.img_tile = self.cargarImagen("dangerousData", "tile_hero.png", -1)
        # MAPA
        Util.cargarMapa("dangerousData/mapa_0.map", self.ubicarEntidadMapa)
        # ESCENARIO
        self.mEscenarios.set(img_fondo, Rect.Rect(0, 0, 640, 480))
        # NUESTRO HEROE COMO OBJETIVO DE LA CAMARA
        self.mEscenarios.objetivo = self.hero;
        self.mEscenarios.ajusteCamara = Vector.Vector(-320, -240)
        self.mEscenarios.limitesCamara = Rect.Rect(0, 0, 800, 600)
        self.mEscenarios.velocidadCamara.set(1, 1)
        self.mEscenarios.activarCamara()
    def ubicarEntidadMapa(self, x, y, idEntidad):
        realX = (x * 32) + 16
        realY = (y * 32) + 16
        if idEntidad == "M" or idEntidad == "p" or idEntidad == "P":
            tmp_muro = muro.Muro(self.img_tile, self.mundoFisico)
            tmp_muro.posicion.set(realX, realY)
            tmp_muro.crearAnimaciones()
            tmp_muro.id = "muro" + str(len(self.entidades))
            tmp_muro.idTipo = "muro"
            if idEntidad == "M":
                tmp_muro.setAnimacionActiva("muro")
            elif idEntidad == "p":
                tmp_muro.setAnimacionActiva("subEscalon")
            else:
                tmp_muro.setAnimacionActiva("escalon")
            self.addEntidad(tmp_muro, 0)
            self.mundoFisico.addObjetoFisico(tmp_muro)
        elif idEntidad == "H":
            # HERO
            self.hero =  hero.Hero(self.img_tile, self.mundoFisico, self.controladorEventos, self)
            self.hero.posicion.set(realX, realY)
            self.hero.crearAnimaciones()
            self.hero.registrarEventos(K_RIGHT, K_LEFT, K_UP, K_DOWN, K_p)
            self.hero.id = "hero"
            self.hero.idTipo = "hero"
            self.addEntidad(self.hero, 1)
            self.mundoFisico.addObjetoFisico(self.hero)
            self.mundoFisico.addEventoChoque(self.hero)
        elif idEntidad == "B":
             # BOT
            tmp_bot =  bot.Bot(self.img_tile, self.mundoFisico, self.controladorEventos, self)
            tmp_bot.posicion.set(realX, realY)
            tmp_bot.crearAnimaciones()
            tmp_bot.id = "bot"
            tmp_bot.idTipo = "bot"
            self.addEntidad(tmp_bot, 1)
            self.mundoFisico.addObjetoFisico(tmp_bot)
            self.mundoFisico.addEventoChoque(tmp_bot)
            self.bots.append(tmp_bot)
        elif idEntidad == "E" or idEntidad == "N":
            tmp_escalera = escalera.Escalera(self.img_tile, self.mundoFisico)
            tmp_escalera.posicion.set(realX, realY)
            tmp_escalera.crearAnimaciones()
            if idEntidad == "E":
                tmp_escalera.setAnimacionActiva("comun")
            else:
                tmp_escalera.setAnimacionActiva("muro")
            tmp_escalera.id = "escalera"
            tmp_escalera.idTipo = "escalera"
            self.addEntidad(tmp_escalera)
            self.mundoFisico.addObjetoFisico(tmp_escalera)
        
    def registrarEventos(self):
        # GENERAL JUEGO
        self.controladorEventos.addListener(QUIT, self.terminar)
        self.controladorEventos.addListenerTeclado(KEYDOWN, K_ESCAPE, self.terminar)
        self.controladorEventos.addListenerTeclado(KEYDOWN, K_1, self.cambiarCamara)
        #self.controladorEventos.addListenerTeclado(KEYDOWN, K_p, self.reproducirGolpe)
    def cambiarCamara(self, evento):
        self.mEscenarios.objetivo = self.bot
    def manejarChoques(self, quien, conQuien):
        #print "Choca " + quien.id + " con " + conQuien.id
        pass
    def logica(self):        
        for bot in self.bots:
            bot.seguirEntidad(self.hero)

# TEST DEL JUEGO
if __name__ == '__main__':
    juego = Dangerous()
    juego.buclePrincipal()