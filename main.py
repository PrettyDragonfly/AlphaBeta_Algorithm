from tree import build_tree
from tree import draw_tree
from numpy import inf
from Minimax_AlphaBeta import minimax_alphabeta as mmab

if __name__ == '__main__':
    # Building the tree from reading the file
    g = build_tree()

    # Calling the function with the root and height as parameters
    res = mmab(g.vertices[0],4, -inf, inf, True)

    # Console display of the root at the end of the execution
    print("The value of the root is " + str(res) + ".")

    # Creation of the graph in draw.png
    draw_tree(g)