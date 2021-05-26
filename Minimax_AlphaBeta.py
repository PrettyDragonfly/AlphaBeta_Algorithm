from numpy import inf


def minimax_alphabeta(position, depth, alpha, beta, maximizingPlayer):
    position.alpha = alpha
    position.beta = beta
    position.visited = True
    if depth == 0:
        print("Node " + str(position.id) + "\nData : " + str(position.data) + "\n")
        return position.data

    # for the allied player
    if maximizingPlayer:
        position.color = "green"
        position.shape = "square"
        maxEval = -inf
        for child in position.children:
            res = minimax_alphabeta(child, depth - 1, alpha, beta, False)
            maxEval = max(maxEval, res)
            alpha = max(alpha, res)
            position.alpha = alpha
            position.beta = beta
            if beta <= alpha:
                break
        position.data = maxEval
        print("Node " + str(position.id) + "\nData : " + str(position.data)
              + "\nAlpha : " + str(position.alpha) + "\nBéta : " + str(position.beta) + "\n")
        return maxEval

    # for the adversary
    else:
        position.color = "red"
        position.shape = "circle"
        minEval = inf
        for child in position.children:
            res = minimax_alphabeta(child, depth - 1, alpha, beta, True)
            minEval = min(minEval, res)
            beta = min(beta, res)
            position.alpha = alpha
            position.beta = beta
            if beta <= alpha:
                break
        position.data = minEval
        print("Node " + str(position.id) + "\nData : " + str(position.data)
              + "\nAlpha : " + str(position.alpha) + "\nBéta : " + str(position.beta) + "\n")
        return minEval
