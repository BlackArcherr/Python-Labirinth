import random
from collections import namedtuple
from queue import Queue
from square import Square
import graph
import auxiliary_func

Vertex = namedtuple('Vertex', 'square x y arrow')
Element = namedtuple('Element', 'x y arrow')
class Square:
    lower_bound = "_"
    left_bound = "|"
    right_bound = "|"
    marked = False
    distance = 0
    lower_bound_with_end = "\u0332!"
    lower_bound_with_start = "\u0332?"
    lower_bound_with_path = "\u0332*"
    
    def __str__(self):
        return self.left_bound + self.lower_bound + self.right_bound
        
    def path_mark(self):
        if self.lower_bound == self.lower_bound_with_end or \
                self.lower_bound == lower_bound_with_start or \
                self.lower_bound == "!" or self.lower_bound == "?":
            pass
        else:
            if self.lower_bound == "_":
                self.lower_bound = self.lower_bound_with_path
            elif self.lower_bound == " ":
                self.lower_bound = "*"
                
    def start(self):
        self.lower_bound = self.lower_bound_with_start

    def finish(self):
        if self.lower_bound == "_":
            self.lower_bound = self.lower_bound_with_end
        else:
            self.lower_bound = "?"
    def clear_left_bound(self):
        self.left_bound = " "

    def clear_right_bound(self):
        self.right_bound = " "
       
    def clear_lower_bound(self):
        if self.lower_bound == self.lower_bound_with_end:
            self.lower_bound = "!"
        elif self.lower_bound == self.lower_bound_with_start:
            self.lower_bound = "?"
        else:
            self.lower_bound = " "
  


def initial():
    print("How width must have a maze?")
    width = int(input())
    print("How length must have a maze?")
    length = int(input())
    init_data = (length, width)
    return init_data

def mark_start(start):
    start.start()

def mark_finish(last):
    last[0].finish()


def get_neighbours(i, j, field):
    neighbours = []
    if i > 0:
        neighbours.append(Vertex(field[i - 1][j], i - 1, j, 1))
    if i < len(field) - 1:
        neighbours.append(Vertex((field[i + 1][j], i + 1, j, 3))
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
        
        
        def span_tree_find(subset, list_of_id_sets):
    for i in range(len(list_of_id_sets)):
        if subset in list_of_id_sets[i]:
            return i

               
def clear_border(last, current):
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
                
def span_tree_get_neighbours(current, field):
    neighbours = []
    for el in get_neighbours(current[0], current[1], field):
        if el.arrow == 3 and (current[0].lower_bound == " " or current[0].lower_bound == "?" or current[0].lower_bound == "!"):
            neighbours.append(el)
        if el.arrow == 1 and (el.field_element.lower_bound == " " or el.field_element.lower_bound == "!"):
            neighbours.append(el)
        if el.arrow == 4 and el.field_element.right_bound == " ":
            neighbours.append(el)
        if el.arrow == 2 and el.field_element.left_bound == " ":
            neighbours.append(el)
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
        for el in span_tree_get_neighbours(current, field):
            if not el[0].marked:
                el[0].marked = True
                path_queue.put(el)
                el[0].distance = current[0].distance + 1
        current = path_queue.get()
    while (current[1], current[2]) != start:
        for el in span_tree_get_neighbours(current, field):
            if el[0].distance == current[0].distance - 1:
                path.append((el[1], el[2]))
                current = el
    path.append(finish)
    return path

def span_tree_gen(init_data):
    field = [[Square() for i in range(init_data[1])] for j in range(init_data[0])]
    random.seed(version=2)
    graph = set()
    gen_graph(graph, init_data[0], init_data[1])
    index_dict = {i * init_data[1] + j: (i, j) for i in range(init_data[0]) for j in range(init_data[1])}
    list_of_id_sets = [set([i * init_data[1] + j]) for i in range(init_data[0]) for j in range(init_data[1])]
    graph = list(graph)
    start = True
    path = []
    while len(graph) > 0 and len(list_of_id_sets) > 1:
        current_edge = random.choice(graph)
        graph.remove(current_edge)
        dom = span_tree_find(current_edge[0], list_of_id_sets)
        ran = span_tree_find(current_edge[1], list_of_id_sets)
        if dom == ran:
            continue
        list_of_id_sets[dom] = set.union(list_of_id_sets[ran], list_of_id_sets[dom])
        for i in range(ran, len(list_of_id_sets) - 1):
            list_of_id_sets[i] = list_of_id_sets[i + 1]
        list_of_id_sets.pop()
        indexes_0 = index_dict[current_edge[0]]
        indexes_1 = index_dict[current_edge[1]]
        if start:
            mark_start(field[indexes_0[0]][indexes_0[1]])
            path.append((indexes_0[0], indexes_0[1]))
            start = False
        clear_border(([field[indexes_0[0]][indexes_0[1]]]), ([field[indexes_1[0]][indexes_1[1]],
                                                                0, 0, current_edge[2]]))
    mark_finish(([field[indexes_1[0]][indexes_1[1]]]))
    start = path[0]
    path = span_tree_get_path(start, (indexes_1[0], indexes_1[1]), field)
    return field, path
    
    
init_data = initial()
lab, path = span_tree_gen(init_data)
print(" _ " * len(lab[0]))
for i in range(len(lab)):
    for j in range(len(lab[i])):
        print(lab[i][j], end="")
    print()
print("Mark path? Yes or No")
if input() == "Yes":
    mark_path(lab, path)
