import math,random,copy,os

def distancesFromCoords():
    f = open('berlin52.tsp')
    data = [line.replace("\n","").split(" ")[1:] for line in f.readlines()[6:58]]
    coords =  list(map(lambda x: [float(x[0]),float(x[1])], data))
    distances = []
    for i in range(len(coords)):
        row = []
        for j in range(len(coords)):
            row.append(math.sqrt((coords[i][0]-coords[j][0])**2 + (coords[i][1]-coords[j][1])**2))
        distances.append(row)
    return distances

def calcularCosto(camino):
    costo = 0
    for i in range(len(camino)-1):
        costo += distancias[camino[i]][camino[i+1]] 
    return costo

def generarCaminoNuevo(camino):
    caminoNuevo = copy.deepcopy(camino)    
    caminoNuevo.pop(0)
    caminoNuevo.pop()

    x1 = 0
    x2 = 0
    while x1 == x2:
        x1 = random.choice(caminoNuevo)
        x2 = random.choice(caminoNuevo)

    i = caminoNuevo.index(x1)
    j = caminoNuevo.index(x2)

    aux = caminoNuevo[i]
    caminoNuevo[i]=caminoNuevo[j]
    caminoNuevo[j]=aux

    caminoNuevo.insert(0,camino[0])
    caminoNuevo.append(camino[0])
    #print(caminoNuevo)
    return caminoNuevo

def recocidoSimulado(camino,T,alfa):
    #caminoNuevo = []
    iteracion = 0
    print(camino)

    while (T >= 0.1):
        iteracion += 1
        caminoNuevo = generarCaminoNuevo(camino)
        costoCaminoNuevo = calcularCosto(caminoNuevo)
        #print("Costo camino nuevo: ",costoCaminoNuevo)
        costoCamino = calcularCosto(camino)
        #print("Costo camino: ",costoCamino)
        if costoCaminoNuevo < costoCamino:
            camino = copy.deepcopy(caminoNuevo)
            T *= alfa
        else:
            factorDeEnfriamiento=random.uniform(0.8,0.99)
            if factorDeEnfriamiento < math.exp(-((costoCaminoNuevo - costoCamino)/ T)):
                camino = copy.deepcopy(caminoNuevo)
                T *= alfa        
        print("Iteracion: ",iteracion,"\nT: ",T,"\nZ: ",costoCamino,"\nZ':",costoCaminoNuevo)
        print("\n")
    print("Mejor ruta",camino)
    print("Mejor solucion:",costoCamino)

if __name__ == '__main__':
    distancias = distancesFromCoords()
    #print(distancias)
    camino = [i for i in range(52)]
    random.shuffle(camino)
    camino.append(camino[0])
    
    caminoNuevo = []
    T = 10000
    alfa = 0.9999
    recocidoSimulado(camino,T,alfa)