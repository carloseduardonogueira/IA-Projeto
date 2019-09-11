#leitura do arquivo
def readFile(file):
    file = open(file, 'r')
    fcontent = file.readlines()
    file.close()
    return fcontent

#cria um dicionário com uma lista de vizinhos para cada cidade
def prepareData(data):
    D = {}
    for n in range(0, len(data)):
        key, value = data[n].split()
        key = key.replace(',','')
        value = value.replace(';','')
        if key not in D:
            D[key]=[value]
        else:
            D[key].append(value)
    return D

#faz a busca em largura
def largura(grafo, origem, destino):
    fila = []
    fila.append([origem])
    while fila:
        rota = fila.pop(0) #pega o primeiro elemento da fila
        no = rota[-1] #pega o ultimo elemento da rota
        if no == destino: #verifica se já chegou ao destino
            return rota
        vizinhos = grafo[no] #pega os vizinhos do no
        for vizinho in vizinhos:
            novaRota = list(rota) #cria uma lista com a rota
            novaRota.append(vizinho) #adiciona o vizinho na lista criada
            fila.append(novaRota) #adiciona a lista criada na fila
 

#programa principal
cidades = readFile('c:/Users/Carlos Eduardo/Desktop/arquivo.txt')
origem = ""
destino = ""
if not cidades:
    print("Arquivo em branco")
else:
    destino = cidades.pop(len(cidades)-1).split()
    origem = cidades.pop(len(cidades)-1).split()
    destino = destino[0].replace(';','')
    origem = origem[0].replace(';','')
grafo = prepareData(cidades)
largura = largura(grafo, origem, destino)
print('Rota ->', largura)
