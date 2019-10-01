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
            queue = Uniform_Cost.sortQ(graph, queue)
            #pega o primeiro caminho (path) da fila
            path = queue.pop(0)
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


    def sortQ(graph, queue):
        ordenado = []
        ordenado.append(queue.pop())
        while queue:
            e = queue.pop()
            cost = Uniform_Cost.cost(graph, e)
            if cost > Uniform_Cost.cost(graph, ordenado[-1]):
                ordenado.append(e)
            else:
                for x in ordenado:
                    custo = Uniform_Cost.cost(graph, x)
                    if cost <= custo :
                        ordenado.insert(ordenado.index(x), e) 
                        break  
        return ordenado

    def cost(graph, queue):
        cost = 0
        for i in range(0,len(queue)-1):
                cost += graph[queue[i]][queue[i+1]]
        return cost