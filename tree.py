import pygraphviz as pg
import xlrd


class TreeNode:
    def __init__(self, data, id):
        self.data = data
        self.id = id
        self.children = []
        self.alpha = None
        self.beta = None
        self.color = "black"
        self.shape = "square"
        self.visited = False

    def add_child(self, child):
        child.parent = self
        self.children.append(child)


class Graph:
    def __init__(self):
        self.vertices = list()
        self.edges = list()

    def add_vertex(self, vertex):
        self.vertices.append(vertex)

    def add_edges(self, vertex1, vertex2):
        self.edges.append((vertex1, vertex2))


def build_tree():
    g = Graph()

    # Open the xls file containing the base data
    workbook = xlrd.open_workbook(r"Graphe.xls")

    # get sheet using its name
    # sheet = workbook.sheet_by_name("Sheet")

    # Getting the first sheet
    sheet = workbook.sheet_by_index(0)

    # Print all sheet names
    # print(sh.name)

    # header = sheet.row_values(0, start_colx=0, end_colx=None)

    nbVertices = int(sheet.cell(0, 1).value)

    for cur_row in range(2, int(nbVertices + 1)):
        dataTemp = sheet.cell(cur_row, 1).value
        if dataTemp != 'None':
            temp = TreeNode(int(sheet.cell(cur_row, 1).value), int(sheet.cell(cur_row, 0).value))
        else:
            temp = TreeNode(None, int(sheet.cell(cur_row, 0).value))
        g.vertices.append(temp)

        if temp.id != 1:
            idpere = int(sheet.cell(cur_row, 2).value)
            g.vertices[idpere - 1].add_child(temp)
            g.edges.append((g.vertices[idpere - 1], temp))

    return g


def draw_tree(g):
    A = pg.AGraph(directed=False, strict=True, bgcolor="darkgrey")

    # Add the nodes to the graph
    for node in g.vertices:
        if not node.visited:
            if node.data is not None:
                # it's a leaf
                A.add_node('/' + '\ndata: ' + str(node.data) + '\nid: ' + str(node.id), shape="circle", color="blue")
            else:
                A.add_node('/' + '\nid: ' + str(node.id), shape="circle", color="blue")
        else:
            A.add_node('data: ' + str(node.data) + '\nalpha: ' + str(node.alpha) +
                       '\nbeta: ' + str(node.beta) + '\nid: ' + str(node.id), color=node.color, shape=node.shape)

    # Add the edges
    for edge in g.edges:
        # If the first node is not visited, nor the second one, it is necessary to check if it is a leaf
        if edge[0].visited is False:
            # it's a leaf
            if edge[1].data is not None:
                A.add_edge('/' + '\nid: ' + str(edge[0].id),
                           '/' + '\ndata: ' + str(edge[1].data) + '\nid: ' + str(edge[1].id))
            else:
                A.add_edge('/' + '\nid: ' + str(edge[0].id), '/' + '\nid: ' + str(edge[1].id))
        elif edge[0].visited is True and edge[1].visited is False:
            if edge[1].data is not None:
                # it's a leaf
                A.add_edge('data: ' + str(edge[0].data) + '\nalpha: ' + str(edge[0].alpha) +
                           '\nbeta: ' + str(edge[0].beta) + '\nid: ' + str(edge[0].id),
                           '/' + '\ndata: ' + str(edge[1].data) + '\nid: ' + str(edge[1].id))
            else:
                A.add_edge('data: ' + str(edge[0].data) + '\nalpha: ' + str(edge[0].alpha) +
                           '\nbeta: ' + str(edge[0].beta) + '\nid: ' + str(edge[0].id),
                           '/' + '\nid: ' + str(edge[1].id))
        else:
            A.add_edge('data: ' + str(edge[0].data) + '\nalpha: ' + str(edge[0].alpha) +
                       '\nbeta: ' + str(edge[0].beta) + '\nid: ' + str(edge[0].id),
                       'data: ' + str(edge[1].data) + '\nalpha: ' + str(edge[1].alpha) +
                       '\nbeta: ' + str(edge[1].beta) + '\nid: ' + str(edge[1].id))

    A.write('draw.dot')
    A.layout(prog='dot')
    A.draw("draw.png")