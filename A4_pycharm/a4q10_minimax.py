# Michael Angelo C. Adraincem
# 11208422 MCA655
# minimax.py

import a4q10_game_specific
import copy

class Node(object):
    def __init__(self, occupied, x, y):
        self.occupied = False
        self.x = x
        self.y = y

    def setOccupied(self, answer):
        self.occupied = answer

    def getOccupied(self):
        return self.occupied


class Tree(object):
    def __init__(self, root: Node):
        self.root = root

    def setRoot(self, newroot):
        self.root = newroot

    def getRoot(self):
        return self.root


class Minimax(object):
    import a4q1
    def __init__(self, tree: Tree, state:a4q10_game_specific.Game, search: a4q1.Search):
        self.tree = tree;
        self.state = state
        self.search = search

    def createTree(self, n):
        root = Node(False, 0, 0)
        self.tree = Tree(root)

    def mx(self, search: a4q1.Search, state: a4q10_game_specific.Game):
        best_score = -1
        cur_score = 0
        state_copy = copy.deepcopy(state)
        actions = search.actions(state_copy)
        for x in search.actions(state_copy):
            search.result(state_copy, actions)
            cur_score = min(search,state)
            if cur_score > best_score:
                best_score = cur_score
        return best_score

    def max(self, search: a4q1.Search, state: a4q10_game_specific.Game):
        state_copy = copy.deepcopy(state)
        if search.is_terminal(state_copy):
            if search.is_max_turn(state_copy):
                return -1
        else:
            best_score = -1
            cur_score = 0
            actions = search.actions(state_copy)
            for a in actions:
                search.result(state_copy, actions)
                cur_score = min(search,state)
                if cur_score > best_score:
                    best_score = cur_score
                return best_score

    def min(self, search: a4q1.Search, state: a4q10_game_specific.Game):
        state_copy = copy.deepcopy(state)
        if search.is_terminal(state_copy):
            if search.is_max_turn(state_copy):
                return 1
        else:
            best_score = 1
            cur_score = 0
            actions = search.actions(state_copy)
            for a in actions:
                search.result(state_copy, actions)
                cur_score = max(search,state)
                if cur_score < best_score:
                    best_score = cur_score
                return best_score



