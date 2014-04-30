# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="ivo"
__date__ ="12/03/2011 18:22:22 PM"

from xml.dom import minidom
import Rect

def cargarAnimacionEntidad(archivoXML, entidad):
    # CARGAR ARCHIVO XML
    try:
        dom = minidom.parse(archivoXML)
        # -- CARGAR ANIMACIONES --
        animaciones = dom.getElementsByTagName("animacion")
        for animacion in animaciones:
            nombreAnimacion = animacion.getAttribute("nombre")
            entidad.crearAnimacion(nombreAnimacion)
        # -- CUERPOS CHOQUE --
        dictCC = {}
        cuerposChoque = dom.getElementsByTagName("cuerpoChoque")
        for cuerpoChoque in cuerposChoque:
            nombreCuerpoChoque = cuerpoChoque.getAttribute("nombre")
            x = int(cuerpoChoque.getAttribute("x"))
            y = int(cuerpoChoque.getAttribute("y"))
            ancho = int(cuerpoChoque.getAttribute("ancho"))
            alto = int(cuerpoChoque.getAttribute("alto"))
            dictCC[nombreCuerpoChoque] = Rect.Rect(x, y, ancho, alto)
        # -- CARGAR FOTOGRAMAS --
        fotogramas = dom.getElementsByTagName("fotograma")
        for fotograma in fotogramas:
            nombreFotograma = fotograma.getAttribute("nombre")
            nombreCuerpoChoque = fotograma.getAttribute("cuerpoChoque")
            x = int(fotograma.getAttribute("x"))
            y = int(fotograma.getAttribute("y"))
            ancho = int(fotograma.getAttribute("ancho"))
            alto = int(fotograma.getAttribute("alto"))
            entidad.addFotogramaCuerpoChoque(nombreFotograma, Rect.Rect(x, y, ancho, alto), dictCC[nombreCuerpoChoque])
        # -- CARGAR RELACION ANIMACION -> FOTOGRAMAS --
        fotoAnimaciones = dom.getElementsByTagName("fotoAnimacion")
        for fotoAnimacion in fotoAnimaciones:
            nombreAnimacion = fotoAnimacion.getAttribute("nombreAnimacion")
            nombreFotograma = fotoAnimacion.getAttribute("nombreFotograma")
            duracionFotograma = int(fotoAnimacion.getAttribute("duracion"))
            entidad.addFotogramaAnimacion(nombreAnimacion, nombreFotograma, duracionFotograma)
    except:
        print "Error al leer el archivo " + archivoXML

if __name__ == "__main__":
    print "## MODULO CON METODOS UTILITARIOS ##"