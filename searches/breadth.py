class Breadth:

    @staticmethod
    #busca em largura (Breadth-First Search) entre cidade de origem e cidade de destino #FIFO
    def bfs(graph, start, goal):
        #uma fila que se inicia com a cidade de origem
        queue = []
        queue.append([start])
        #enquanto a fila não estiver vazia, fará tal processo
        while queue:
            #pega o primeiro caminho (path) da fila
            path = queue.pop(0)
            #pega o último nó do caminho
            node = path[-1]
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