import random


class Vertex(object):
    def __init__(self, word):
        self.word = word
        self.adjacent = {}  # nodes that it points to
        self.neighbors = []
        self.neighbors_weights = []

    def __str__(self):
        return self.word + ' '.join([node.value for node in self.adjacent.keys()])

    # adds an edge to the vertex we input with weight
    def add_edge_to(self, vertex, weight=0):
        self.adjacent[vertex] = weight

    # increments the weight of an edge
    def increment_edge(self, vertex):
        self.adjacent[vertex] = self.adjacent.get(vertex, 0) + 1

    def get_adjacent_nodes(self):
        return self.adjacent.keys()

    # initializes probability map
    def get_probability_map(self):
        for (vertex, weight) in self.adjacent.items():
            self.neighbors.append(vertex)
            self.neighbors_weights.append(weight)

    def next_word(self):
        # chooses randomly based on weights
        # will want to change
        return random.choices(self.neighbors, weights=self.neighbors_weights)[0]


class Graph(object):
    def __init__(self):
        self.vertices = {}

    # what are the values of all the vertices
    def get_vertex_values(self):
        return set(self.vertices.keys())

    def add_vertex(self, word):
        self.vertices[word] = Vertex(word)

    def get_vertex(self, word):
        if word not in self.vertices:
            self.add_vertex(word)
        return self.vertices[word]

    def get_next_word(self, current_vertex):
        return self.vertices[current_vertex.word].next_word()

    def generate_probability_mappings(self):
        for vertex in self.vertices.values():
            vertex.get_probability_map()
