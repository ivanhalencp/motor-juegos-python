import Fotograma

class Animacion(object):
    #__nombre (String)
    #__ciclica (Boolean)
    #__tiempoEsperaDefecto (Int)
    #__fotogramas []
    #__indiceFotogramaActivo (Int)
    #__accionPendiente(Funcion)
    def __init__ (self, nombre, tiempoEsperaDefecto, ciclica):
        self.__nombre = nombre
        self.__ciclica = ciclica
        self.__tiempoEsperaDefecto = 0
        self.__fotogramas = []
        self.__indiceFotogramaActivo = 0
        self.__indiceTiempoEspera = 0
        self.__tiempoEsperaAnterior = -1
        self.__accionPendiente = None
    def addFotograma(self, claveFCC, tiempoEspera = -1, accion = None):
        if tiempoEspera == -1:
            tiempoEspera = self.__tiempoEsperaDefecto
        # CREO NUEVO FOTOGRAMA
        fotograma = Fotograma.Fotograma(claveFCC, tiempoEspera, accion)
        # AGREGO A FOTOGRAMAS
        self.__fotogramas.append(fotograma)
    def getClaveFCCActivo(self):
        return self.fotogramas[self.indiceFotogramaActivo].claveFCC
    def animar(self):
        # SI ES LA PRIMERA VEZ QUE SE LLAMA AL METODO SETEO TIEMPO ESPERA ANTERIOR
        if (self.__tiempoEsperaAnterior == -1):
            self.__tiempoEsperaAnterior = self.fotogramas[self.indiceFotogramaActivo].tiempoEspera
        self.__indiceTiempoEspera += 1
        # SI SE CUMPLIO EL TIEMPO DE ANIMACION CAMBIO DE FOTOGRAMA
        if self.__indiceTiempoEspera >= self.__tiempoEsperaAnterior:
            # SI HAY ACCION PENDIENTE, LA LLAMO Y RESETEO LUEGO
            if self.__accionPendiente:
                self.__accionPendiente()
                self.__accionPendiente = None
            # SI TENGO ACCION SETEADA PARA ESTE FOTOGRAMA, LA SETEO COMO PENDIENTE PARA SER LLAMADA EN PROXIMO FOTOGRAMA
            if self.fotogramas[self.indiceFotogramaActivo].accion:
                self.__accionPendiente = self.fotogramas[self.indiceFotogramaActivo].accion
                # self.fotogramas[self.indiceFotogramaActivo].accion()
            # PASO AL FOTOGRAMA SIGUIENTE
            self.indiceFotogramaActivo += 1
            # SI LLEGO AL ULTIMO FOTOGRAMA VUELVO AL PRIMERO
            if self.indiceFotogramaActivo >= len(self.fotogramas):
                self.indiceFotogramaActivo = 0
            self.__tiempoEsperaAnterior = self.fotogramas[self.indiceFotogramaActivo].tiempoEspera
            self.__indiceTiempoEspera = 0

    # -- GETS Y SETS --
    def getNombre(self):
        return self.__nombre
    def setNombre(self, param):
        self.__nombre = param
    nombre = property(getNombre, setNombre)
    def getCiclica(self):
        return self.__ciclica
    def setCiclica(self, param):
        self.__ciclica = param
    ciclica = property(getCiclica, setCiclica)
    def getTiempoEsperaDefecto(self):
        return self.__tiempoEsperaDefecto
    def setTiempoEsperaDefecto(self, param):
        self.__tiempoEsperaDefecto = param
    tiempoEsperaDefecto = property(getTiempoEsperaDefecto, setTiempoEsperaDefecto)
    def getFotogramas(self):
        return self.__fotogramas
    def setFotogramas(self, param):
        self.__fotogramas = param
    fotogramas = property(getFotogramas, setFotogramas)
    def getIndiceFotogramaActivo(self):
        return self.__indiceFotogramaActivo
    def setIndiceFotogramaActivo(self, param):
        self.__indiceFotogramaActivo = param
    indiceFotogramaActivo = property(getIndiceFotogramaActivo, setIndiceFotogramaActivo)

