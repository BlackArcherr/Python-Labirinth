import random
from collections import namedtuple
from queue import Queue
from square import Square

Vertex = namedtuple('Vertex', 'square x y arrow')

def mark_start(start):
    start.start()
 
def mark_finish(last):
    last[0].finish()
 
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
 
def clean(last, current):
    if current[3] == 4:
        last[0].clear_left_bound()
        current[0].clear_right_bound()
    elif current[3] == 2:
        last[0].clear_right_bound()
        current[0].clear_left_bound()
    elif current[3] == 3:
        last[0].clear_lower_bound()
    else:
        current[0].clear_lower_bound()
 
def gen_graph(graph, length, width):
    for i in range(length):
        for j in range(width):
            if i > 0:
                graph.add((i * width + j, (i - 1) * width + j, 1))
                graph.add(((i - 1) * width + j, i * width + j, 3))
            if i < length - 1:
                graph.add((i * width + j, (i + 1) * width + j, 3))
                graph.add(((i + 1) * width + j, i * width + j, 1))
            if j > 0:
                graph.add((i * width + j, i * width + j - 1, 4))
                graph.add((i * width + j - 1, i * width + j, 2))
            if j < width - 1:
                graph.add((i * width + j, i * width + j + 1, 2))
                graph.add((i * width + j + 1, i * width + j, 4))
 
def span_tree_find(subset, number_squares):
    for i in range(len(number_squares)):
        if subset in number_squares[i]:
            return i
 
def span_tree_get_neighbours(current, field):
    neighbours = []
    for neib in get_neighbours(current[1], current[2], field):
        if neib.arrow == 3 and (current[0].lower_bound == " " or current[0].lower_bound == "?" or \
                                current[0].lower_bound == "!"):
            neighbours.append(neib)
        if neib.arrow == 1 and (neib.square.lower_bound == " " or neib.square.lower_bound == "!"):
            neighbours.append(neib)
        if neib.arrow == 4 and neib.square.right_bound == " ":
            neighbours.append(neib)
        if neib.arrow == 2 and neib.square.left_bound == " ":
            neighbours.append(neib)
    return neighbours
 
def span_tree_get_path(start, finish, field):
    current = (field[start[0]][start[1]], start[0], start[1])
    current[0].distance = 0
    current[0].marked = True
    path_queue = Queue()
    path_queue.put(current)
    path = []
    field[start[0]][start[1]].distance = 0
    while (current[1], current[2]) != finish:
        for neib in span_tree_get_neighbours(current, field):
            if not neib[0].marked:
                neib[0].marked = True
                path_queue.put(neib)
                neib[0].distance = current[0].distance + 1
        current = path_queue.get()
    while (current[1], current[2]) != start:
        for neib in span_tree_get_neighbours(current, field):
            if neib[0].distance == current[0].distance - 1:
                path.append((neib[1], neib[2]))
                current = neib
    path.append(finish)
    return path
 
def span_tree_gen(init_data):
    field = [[Square() for i in range(init_data[1])] for j in range(init_data[0])]
    random.seed(version=2)
    graph = set()
    gen_graph(graph, init_data[0], init_data[1])
    index_dict = {i * init_data[1] + j: (i, j) for i in range(init_data[0]) for j in range(init_data[1])}
    number_squares = [set([i * init_data[1] + j]) for i in range(init_data[0]) for j in range(init_data[1])]
    graph = list(graph)
    start = True
    path = []
    while len(graph) > 0 and len(number_squares) > 1:
        rand_edge = random.choice(graph)
        graph.remove(rand_edge)
        dom = span_tree_find(rand_edge[0], number_squares)
        ran = span_tree_find(rand_edge[1], number_squares)
        if dom == ran:
            continue
        number_squares[dom] = set.union(number_squares[ran], number_squares[dom])
        for i in range(ran, len(number_squares) - 1):
            number_squares[i] = number_squares[i + 1]
        number_squares.pop()
        indexes_0 = index_dict[rand_edge[0]]
        indexes_1 = index_dict[rand_edge[1]]
        if start:
            mark_start(field[indexes_0[0]][indexes_0[1]])
            path.append((indexes_0[0], indexes_0[1]))
            start = False
        clean(([field[indexes_0[0]][indexes_0[1]]]), ([field[indexes_1[0]][indexes_1[1]], \
                                                       0, 0, rand_edge[2]]))
    mark_finish(([field[indexes_1[0]][indexes_1[1]]]))
    start = path[0]
    path = span_tree_get_path(start, (indexes_1[0], indexes_1[1]), field)
    return field, path
 
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
