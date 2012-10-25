import pygraphviz as pgv

G = pgv.AGraph()
G.add_node('a')
G.add_edge('b','c')
G.add_edge('c','d', 'e')
print G

G.layout() # default to neato
G.draw('file.png')
