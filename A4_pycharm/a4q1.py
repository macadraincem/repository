# Michael Angelo C. Adraincem
# 11208422 MCA655
# a4q1.py

import a4q10_game_specific
import copy



class Search(object):
    def __init__(self, state: a4q10_game_specific.Game, size):
        self.state = a4q10_game_specific.Game("", size, 0)
        self.size = size

    def createGame(self):
        return self.state.createBoard()

    def is_terminal(self, state :a4q10_game_specific.Game):
        column = len(state.nqueen)
        if state.size == column:
            return True
        elif state.isNqueen():
            return True
        elif column < state.size:
            ctr = 0
            for a in range(0,state.size):
                if state.checkHorizontal(a,column-1):
                    if state.checkVertical(a, column-1):
                        if state.checkDiagonal(a, column-1):
                            ctr = ctr + 1
            if ctr == 0:
                return True
            else:
                return False

        else:
            return False

    def utility(self, state: a4q10_game_specific.Game):
        import a4q10_minimax
        if self.is_terminal(state):
            x = a4q10_minimax.Minimax("",state,self)
            return x.mx(self,state)
        else:
            print("not a terminal state")

    def actions(self, state: a4q10_game_specific.Game):
        actions = []
        column = len(state.nqueen)

        for a in range(0, state.size):
            if state.checkHorizontal(a, column):
                if state.checkVertical(a, column):
                    if state.checkDiagonal(a, column):
                        actions.append([a, column])
        return actions

    def result(self, state: a4q10_game_specific.Game, action):
        new_state = copy.deepcopy(state)

        new_state.putQueen(action[0][0], action[0][1])
        return new_state

    def is_max_turn(self,state: a4q10_game_specific.Game):
        if len(state.nqueen) == 0:
            return True
        elif len(state.nqueen) % 2 == 0:
            return True
        elif len(state.nqueen) % 2 == 1:
            return False

    def is_min_turn(self, state: a4q10_game_specific.Game):
        return not self.is_max_turn(state)

    def simulate(self, state:a4q10_game_specific.Game):
        self.createGame()
        for a in range(0,state.size):
            actions = self.actions(state)
            state = self.result(state, actions)
            if self.is_terminal(state):
                print(self.utility(state))
                break
        state.__str__()



def main():
    test = Search("",4)
    test.simulate(test.state)
    test.actions(test.state)


main()