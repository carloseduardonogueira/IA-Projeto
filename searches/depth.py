class Depth:

    @staticmethod
    #busca em profundidade (Depth-First Search) entre cidade de origem e cidade de destino #LIFO
    def dfs(graph, start, goal):
        #uma pilha que se inicia com a cidade de origem
        stack = []
        stack.append([start])
        #enquanto a pilha não estiver vazia, fará tal processo
        while stack:
            #pega o primeiro caminho (path) da pilha
            path = stack.pop()
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
            #a pilha adiciona a rota
                for neighbour in neighbours: 
                    route = list(path)
                    route.append(neighbour)
                    stack.append(route)