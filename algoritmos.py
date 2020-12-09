import math

def distancia_euclidiana(origenx,destinox,origeny,destinoy):
    s = round(math.sqrt((destinox-origenx)**2+(destinoy-origeny)**2))
    return(s)
