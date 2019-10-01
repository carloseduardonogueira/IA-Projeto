class Uniform_Cost:

    @staticmethod
    #busca de custo uniforme (Uniform Cost Search), utilizando o menor caminho entre cidades
    def ucs(graph, start, goal):
        #uma fila que se inicia com a cidade de origem
        queue = []
        queue.append([start])
        #enquanto a fila não estiver vazia, fará tal processo
        while queue:
            #print("Fila-->", queue)
            #pega o primeiro caminho (path) da fila
            path = queue.pop(0)
            print(path)
            #pega o último nó do caminho
            node = path[-1]
            #print('Node:', node)
            #caso o caminho tenha sido encontrado
            if node == goal:
                return path
            #neighbours (vizinhos) recebe o grafo a partir do nó atual
            elif node in graph:
                neighbours = graph[node] 
            #se um vizinho estiver no grafo de vizinhos
            #cria-se uma rota - através do caminho e adiciona tal vizinho a rota
            #a fila adiciona a rota
                for neighbour in neighbours: 
                    route = list(path)
                    route.append(neighbour)
                    queue.append(route)