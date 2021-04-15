import random
from collections import namedtuple
from queue import Queue
from square import Square
import graph

Vertex = namedtuple('Vertex', 'square x y arrow')

def get_neighbours(i, j, field):
    neighbours = []
    if i > 0:
        neighbours.append(Vertex(field[i - 1][j], i - 1, j, 1))
    if i < len(field) - 1:
        neighbours.append(Vertex(field[i + 1][j], i + 1, j, 3))
    if j > 0:
        neighbours.append(Vertex(field[i][j - 1], i, j - 1, 4))
    if j < len(field[0]) - 1:
        neighbours.append(Vertex(field[i][j + 1], i, j + 1, 2))
    return neighbours


def visited(neighbours):
    for i in neighbours:
        if not i[0].marked:
            return False
    return True
    
def mark_path(field, path):
    for i in range(len(path)):
        field[path[i][0]][path[i][1]].path_mark()
    print(" _ " * len(lab[0]))
    for i in range(len(field)):
        for j in range(len(field[i])):
            print(field[i][j], end="")
        print() 
    
print("How width must have a Labirinth?")
width = int(input())
print("How length must have a Labirinth?")
length = int(input())
init_data = (length, width)
lab, path = span_tree_gen(init_data)
print(" _ " * len(lab[0]))
for i in range(len(lab)):
    for j in range(len(lab[i])):
        print(lab[i][j], end="")
    print()
print("Mark path? Yes or No")
if input() == "Yes":
    mark_path(lab, path)
