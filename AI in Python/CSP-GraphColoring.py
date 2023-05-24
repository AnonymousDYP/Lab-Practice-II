class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    # Function for checking the safety of assigning a color to a vertex.
    def is_safe(self, v, color, c):
        for i in range(self.V):
            if self.graph[v][i] == 1 and color[i] == c:
                return False
        return True

    # Performing graph coloring algorithm
    def graph_coloring(self, m):
        color = [-1] * self.V
        color[0] = 0
        if not self.graph_coloring_util(m, color, 1):
            print("Solution does not exist.")
        else:
            print("Graph coloring solution:")
            print(color)

    # Recursive function that implements backtracking and brach & bound techniques.
    def graph_coloring_util(self, m, color, v):
        if v == self.V:
            return True
        for c in range(m):
            if self.is_safe(v, color, c):
                color[v] = c
                if self.graph_coloring_util(m, color, v + 1):
                    return True
                color[v] = -1
        return False

if __name__ == '__main__':
    g = Graph(4)
    # pre-defined graph
    g.graph = [
        [0, 1, 1, 1],
        [1, 0, 1, 0],
        [1, 1, 0, 1],
        [1, 0, 1, 0]
    ]
    # Number of colors to be used
    num_colors = int(input("Enter number of colors : "))  
    g.graph_coloring(num_colors)
