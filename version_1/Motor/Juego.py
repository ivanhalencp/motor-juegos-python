import os, pygame, Motor
from pygame.locals import *
from Motor import Constantes, MundoFisico, ControladorEventos, Configuracion, M_Escenarios, EntidadJuego

class Juego(object):
    def __init__(self):
        # CONSTANTES
        self.__estado = Constantes.INICIALIZANDO
        # CONTROLADOR DE EVENTOS
        self.__controladorEventos = ControladorEventos.ControladorEventos(pygame)
        # MUNDO FISICO
        self.__mundoFisico = MundoFisico.MundoFisico()
        # ENTIDADES JUEGO
        self.__entidades = []
        # OBJETO DISPLAY DE PYGAME
        self.__pantalla = None
        # MANEJADOR DE ESCENARIOS
        self.__mEscenarios = M_Escenarios.M_Escenarios()
        # CONFIGURACION
        self.__configuracion = Configuracion.Configuracion()
        # CLOCK DE PYGAME
        self.__clock = pygame.time.Clock()
    # - AGREGAR NUEVA ENTIDAD
    # - LE ASIGNO PROFUNDIDAD
    def addEntidad(self, entidad):
        entidad.profundidad = len(self.entidades)
        self.entidades.append(entidad)
    # CREACION Y REGISTRO DE OBJETOS AL MUNDO FISICO
    # (SOBREESCRIBIR ESTE METODO)
    def crearMundo(self):
        pass
    # REGISTRAMOS TODOS LOS EVENTOS
    # (SOBREESCRIBIR ESTE METODO)
    def registrarEventos(self):
        pass
    def inicializarPygame(self):
        # INICIALIZAR PYGAME
        pygame.init()
        # INICIALIZAR DISPLAY
        if self.configuracion.pantallaCompleta:
            self.pantalla = pygame.display.set_mode((self.configuracion.anchoPantalla, self.configuracion.altoPantalla), FULLSCREEN)
        else:
            self.pantalla = pygame.display.set_mode((self.configuracion.anchoPantalla, self.configuracion.altoPantalla))
        # TITULO DE VENTANA EN CASO DE QUE SEA VENTANA
        pygame.display.set_caption("JUEGO")
    # SE INICIALIZA TODO LO NECESARIO PARA EL JUEGO
    def inicializar(self):
        print "JUEGO -> SE INICIALIZA EL JUEGO"
        # INICIALIZAR PYGAME
        self.inicializarPygame()
        # CREAR MUNDO
        self.crearMundo()
        # REGISTRAR EVENTOS
        self.registrarEventos()
        # PASAR A ESTADO JUGANDO
        self.estado = Constantes.JUGANDO
        print "JUEGO -> JUGANDO..."
    # LLAMA A LA LOGICA DE CADA ENTIDAD
    def logicaEntidades(self):
        for entidad in (self.entidades):
            if entidad.activo:
                entidad.logica()
    # RECALCULAR PRORFUNDIDADES SEGUN LA COORDENADA Y DE LA ENTIDAD
    def calcularProfundidadEntidades(self):
        cantidadEntidades = len(self.entidades)
        itBase = 0
        it = 0
        while (itBase < cantidadEntidades - 1):
            while (it < cantidadEntidades - 1):
                if self.swapProfundidadEntidades(self.entidades[it], self.entidades[it + 1]):
                    self.entidades[it], self.entidades[it + 1] = self.entidades[it + 1], self.entidades[it]
                it = it + 1
            itBase = itBase + 1
    # DEVUELVE TRUE O FALSE INDICANDO SI ES NECESARIO HACER UN SWAP DE PROFUNDIDAD
    def swapProfundidadEntidades(self, entidadA, entidadB):
        resultado = False
        if entidadA.posicion.y > entidadB.posicion.y:
            resultado = True
        return resultado
    # ANIMAR ENTIDADES
    def animar(self):
        for entidad in (self.entidades):
            if entidad.activo:
                entidad.animar()
    # GRAFICAR TODO
    def graficar(self):
        # GRAFICAR FONDO
        ajustePosicion = self.mEscenarios.logicaCamara()
        self.mEscenarios.blit(self.pantalla)
        # GRAFICAR ENTIDADES JUEGO
        for entidad in (self.entidades):
            if entidad.activo:
                # SI LA CAMARA SE MOVIO ENTONCES AJUSTO POSICION DE CADA ENTIDAD
                entidad.blit(self.pantalla, ajustePosicion)
        # VOLCAR TODO A PANTALLA
        pygame.display.update()
    # LOGICA PROPIA DE CADA JUEGO
    # (SOBREESCRIBIR ESTE METODO)
    def logica(self):
        pass
    # BUCLE JUGAR
    def jugar(self):
        # LLAMO A LOGICA PROPIA DEL JUEGO
        self.logica()
        # CHEQUEO EVENTOS REGISTRADOS Y NOTIFICO A LISTENERS
        self.controladorEventos.notificarListeners()
        # CHEQUEO CHOQUES DE LOS OBJETOS REGISTRADOS EN EL MUNDO FISICO
        self.mundoFisico.chequearChoques()
        # LLAMAR LOGICA DE CADA ENTIDAD
        self.logicaEntidades()
        # PROFUNDIDAD ENTIDADES (SI ESTA ACTIVADO EN LA CONFIGURACION)
        if self.configuracion.profundidadAutomatica:
            self.calcularProfundidadEntidades()
        # ANIMAR ENTIDADES
        self.animar()
        # GRAFICAR TODO
        self.graficar()
    # PASO ESTADO DEL JUEGO A TERMINADO
    def terminar(self, evento):
        print "JUEGO -> TERMINADO"
        self.estado = Constantes.TERMINADO
    # BUCLE PRINCIPAL DEL JUEGO
    def buclePrincipal(self):
        while (self.estado != Constantes.TERMINADO):
            # TIEMPO DE ESPERA
            self.clock.tick(self.configuracion.tiempoClock)
            if self.estado == Constantes.INICIALIZANDO:
                self.inicializar()
            elif self.estado == Constantes.JUGANDO:
                self.jugar()
    # UTILITARIOS
    # CARGAR UNA IMAGEN
    def cargarImagen(self, directorio, nombreArchivo, colorTransparente = None):
        nombreCompleto = os.path.join(directorio, nombreArchivo)
        try:
            imagen = pygame.image.load(nombreCompleto)
        except pygame.error, message:
            print 'ERROR: Imposible cargar archivo de imagen: ', nombreCompleto
            raise SystemExit, message
        imagen = imagen.convert()
        if colorTransparente is not None:
            if colorTransparente is -1:
                colorTransparente = imagen.get_at((0,0))
            imagen.set_colorkey(colorTransparente, RLEACCEL)
        return imagen
    # MANEJO DE AUDIO
    # -- CARGAR MUSICA PARA FONDO --
    def cargarMusicaFondo(self, directorio, nombreArchivo):
        nombreCompleto = os.path.join(directorio, nombreArchivo)
        try:
            pygame.mixer.music.load(nombreCompleto)
        except pygame.error, message:
            print 'ERROR: Imposible cargar archivo de audio: ', nombreCompleto
            raise SystemExit, message
    # -- COMENZAR LA REPRODUCCION --
    def tocarMusicaFondo(self):
        pygame.mixer.music.play()
    # -- CARGAR UN SONIDO --
    def cargarAudio(self, directorio, nombreArchivo):
        nombreCompleto = os.path.join(directorio, nombreArchivo)
        try:
            sonido = pygame.mixer.Sound(nombreCompleto)
        except pygame.error, message:
            print 'ERROR: Imposible cargar archivo de audio: ', nombreCompleto
            raise SystemExit, message
        return sonido

    # -- GETS Y SETS --
    # ESTADO
    def getEstado(self):
        return self.__estado
    def setEstado(self, param):
        self.__estado = param
    estado = property(getEstado, setEstado)
    # CONTROLADOR EVENTOS
    def getControladorEventos(self):
        return self.__controladorEventos
    def setControladorEventos(self, param):
        self.__controladorEventos = param
    controladorEventos = property(getControladorEventos, setControladorEventos)
    # MUNDO FISICO
    def getMundoFisico(self):
        return self.__mundoFisico
    def setMundoFisico(self, param):
        self.__mundoFisico = param
    mundoFisico = property(getMundoFisico, setMundoFisico)
    # MANEJADOR ESCENARIOS
    def getMEscenarios(self):
        return self.__mEscenarios
    def setMEscenarios(self, param):
        self.__mEscenarios = param
    mEscenarios = property(getMEscenarios, setMEscenarios)
    # ENTIDADES (CONJUNTO DE ENTIDADES JUEGO)
    def getEntidades(self):
        return self.__entidades
    def setEntidades(self, param):
        self.__entidades = param
    entidades = property(getEntidades, setEntidades)
    # PANTALLA
    def getPantalla(self):
        return self.__pantalla
    def setPantalla(self, param):
        self.__pantalla = param
    pantalla = property(getPantalla, setPantalla)
    # CONFIGURACION
    def getConfiguracion(self):
        return self.__configuracion
    def setConfiguracion(self, param):
        self.__configuracion = param
    configuracion = property(getConfiguracion, setConfiguracion)
    # CLOCK
    def getClock(self):
        return self.__clock
    def setClock(self, param):
        self.__clock = param
    clock = property(getClock, setClock)