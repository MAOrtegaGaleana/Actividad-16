from particula import Particula
import json
from collections import deque
from pprint import pprint, pformat

class Particulas:
    def __init__(self):
        self.__particulas = []
        self.__diccionario = {}
        self.__grafo = {}

    def agregar_final(self,particula:Particula):
        self.__particulas.append(particula)

    def agregar_inicio(self,particula:Particula):
        self.__particulas.insert(0,particula)

    def mostrar(self):
        for particula in self.__particulas:
            print(particula)

    def __str__(self):
        return "".join(
            str(particula) for particula in self.__particulas
        )

    def __len__(self):
        return len(self.__particulas)
    
    def __iter__(self):
        self.cont = 0
        return self

    def __next__(self):
        if self.cont < len(self.__particulas):
            particula = self.__particulas[self.cont]
            self.cont +=1
            return particula
        else:
            raise StopIteration

    def guardar(self,ubicacion):
        try:
            with open(ubicacion, 'w') as archivo:
                lista = [particula.to_dict() for particula in self.__particulas]
                print(lista)
                json.dump(lista, archivo, indent=5)
            return 1
        except:
            return 0

    def abrir(self, ubicacion):
        try:
            with open(ubicacion, 'r') as archivo:
                lista = json.load(archivo)
                self.__particulas = [Particula(**particula) for particula in lista]
            return 1
        except:
            return 0

    def ordenarid(self):
        self.__particulas.sort(key= lambda particula: particula.identificacion)

    def ordenardistancia(self):
        self.__particulas.sort(key= lambda particula: particula.d,reverse=True)

    def ordenarvelocidad(self):
        self.__particulas.sort(key= lambda particula: particula.velocidad)


    def mostrar_diccionario(self):
        for particula in self.__particulas:
            origin = (particula.origenx,particula.origeny)
            destination = (particula.destinox,particula.destinoy)
            arista_origin = (particula.destinox,particula.destinoy,particula.d)
            arista_destination = (particula.origenx,particula.origeny,particula.d)

            if origin in self.__diccionario:
                self.__diccionario[origin].append(arista_origin)
            else:
                self.__diccionario[origin] = [arista_origin]

            if destination in self.__diccionario:
                self.__diccionario[destination].append(arista_destination)
            else:
                self.__diccionario[destination] = [arista_destination]
                
        str = pformat(self.__diccionario, width=40, indent=1)
        print(str)
        return str
        
    def recorrido_profundidad(self, origen):
        visitados = deque()
        pila = deque()
        recorrido = deque()

        visitados.append(origen)
        pila.append(origen)

        while len (pila) > 0:

            vertice = pila[-1]
            recorrido.append(vertice)
            pila.pop()
            adyacentes = self.__grafo[vertice]
            for i in adyacentes:
                ady = i
                if ady not in visitados:
                    visitados.append(ady)
                    pila.append(ady)
        return recorrido

    def recorrido_amplitud(self, origen):
        visitados = deque()
        cola = deque()
        recorrido = deque()

        visitados.append(origen)
        cola.append(origen)

        while len (cola) > 0:

            vertice = cola[0]
            recorrido.append(vertice)
            del cola[0]
            adyacentes = self.__grafo[vertice]
            for i in adyacentes:
                ady = i
                if ady not in visitados:
                    visitados.append(ady)
                    cola.append(ady)
        return recorrido

    def peso(self):
        self.__grafo = self.__diccionario.copy()
        for i in self.__diccionario:
            self.__grafo[i] = [x[:2] for x in self.__diccionario[i]]
        