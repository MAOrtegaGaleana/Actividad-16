from algoritmos import distancia_euclidiana

class Particula:
    def __init__(self, identificacion=0, origenx=0, origeny=0, destinox=0, destinoy=0, velocidad=0, red=0, green=0, blue=0,d=0.0):
        self.__identificacion = identificacion
        self.__origenx = origenx
        self.__origeny = origeny
        self.__destinox = destinox
        self.__destinoy = destinoy
        self.__velocidad = velocidad
        self.__red = red
        self.__green = green 
        self.__blue = blue
        self.__d = distancia_euclidiana(origenx,destinox,origeny,destinoy)

    def __str__(self):
        return(
            'ID: ' + str(self.__identificacion) + '\n' +
            'Origen en x: ' + str(self.__origenx) + '\n' +
            'Origen en y: ' + str(self.__origeny) + '\n' +
            'Destino en x: ' + str(self.__destinox) + '\n' +
            'Destino en y: ' + str(self.__destinoy) + '\n' +
            'Velocidad: ' + str(self.__velocidad) + '\n' +
            'Red: ' + str(self.__red) + '\n' +
            'Green: ' + str(self.__green) + '\n' +
            'Blue: ' + str(self.__blue) + '\n' +
            'Distancia: ' + str(self.__d) + '\n\n'
        )

    @property
    def identificacion(self):
        return self.__identificacion

    @property
    def origenx(self):
        return self.__origenx
    
    @property
    def origeny(self):
        return self.__origeny

    @property
    def destinox(self):
        return self.__destinox
    
    @property
    def destinoy(self):
        return self.__destinoy

    @property
    def velocidad(self):
        return self.__velocidad

    @property
    def red(self):
        return self.__red

    @property
    def green(self):
        return self.__green

    @property
    def blue(self):
        return self.__blue
    
    @property
    def d(self):
        return self.__d

    def to_dict(self):
        return{
            "identificacion": self.__identificacion,
            "origenx": self.__origenx,
            "origeny": self.__origeny,
            "destinox": self.__destinox,
            "destinoy": self.__destinoy,
            "velocidad": self.__velocidad,
            "red": self.__red,
            "blue": self.__blue,
            "green": self.__green
        }