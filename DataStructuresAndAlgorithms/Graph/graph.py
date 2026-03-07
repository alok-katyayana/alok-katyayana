"""
   This Module Consists of class for Graph
"""

class Graph:
    """
       This is an abstraction of Graph data structure,
       built using list
    """
    def __init__(self):
        self.adj_list = {}

    def print_graph(self):
        """
           Print the whole Graph
        """
        for vertex, edges in self.adj_list.items():
            print(vertex, ":", edges)

    def add_vertex(self,vertex):
        """
           Add a net vertex.
        """
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
            return True

        return False

    def add_edge(self, v1, v2):
        """
           Add and edge between two vertex
        """
        if v1 in self.adj_list and v2 in self.adj_list:
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True

        return False

    def remove_edge(self, v1, v2):
        """
           Removes the edges between two vertex
        """
        if v1 in self.adj_list and v2 in self.adj_list:
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True

        return False

    def remove_vertex(self, v):
        """
           Removes a vertex.
        """
        adjs = self.adj_list.pop(v, None)
        if adjs is None:
            return False
        for elm in adjs:
            self.adj_list[elm].remove(v)

        return True




if __name__ == "__main__":
    myg = Graph()

    myg.print_graph()

    myg.add_vertex("Whole")
    myg.add_vertex("number")
    myg.add_vertex("value")
    myg.add_edge("Whole", "number")
    myg.add_edge("value", "number")
    myg.print_graph()
    myg.add_vertex("Rational")
    myg.add_edge("Whole", "Rational")
    myg.print_graph()
    print("Removing an Vertex")
    myg.remove_vertex("value")
    myg.print_graph()
