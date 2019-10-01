#Projeto da disciplina de Inteligência Artificial «PUC-Campinas»

from searches.breadth import Breadth
from searches.depth import Depth
from searches.uniform_cost import Uniform_Cost

from services.read_file import Read
from services.prepare_data import Prepare_Data

cities = Read.readFile("input.txt")
start = ''
goal = ''

if not cities:
    print('This file is empty')
else:
    goal = cities.pop(len(cities)-1).split()
    start = cities.pop(len(cities)-1).split()
    goal = goal[0].replace(';', '')
    start = start[0].replace(';', '')

graph = Prepare_Data.dictionary_data(cities)

bfs = Breadth.bfs(graph, start, goal)
dfs = Depth.dfs(graph, start, goal)
ucs = Uniform_Cost.ucs(graph, start, goal)

print('Rota em Largura: ', bfs)
print('Rota em Profundidade: ', dfs)
print('Rota com Custo Uniforme: ', ucs, '--- Distância Total: ')

