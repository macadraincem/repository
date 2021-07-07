# Michael Angelo C. Adraincem
# MCA655 11208422
# Problem.py

import State
import Machine
import random

class Problem(object):
    action_start = "load "
    action_ADD = "ADD "
    action_MUL = "MUL "
    action_SUB = "SUB "
    action_DIV = "DIV "
    action_NOP = "NOP "

    def __init__(self, target=None, number=None):
        self.target = target
        self.number = number
        self.a_state = State.State(target, [], number)

    def random_start(self,target, mlist, state):
        newstate = State.State(target, [], mlist)

        mlist=[]
        while len(mlist) < len(state.number):
            r = random.randint(1,5)
            mlist.append(r)

        z = 0
        for x in mlist:
            if mlist[z] == 1:
                newstate.operand.append(['NOP', newstate.number[z]])
            elif mlist[z] == 2:
                newstate.operand.append(['ADD', newstate.number[z]])
            elif mlist[z] == 3:
                newstate.operand.append(['SUB', newstate.number[z]])
            elif mlist[z] == 4:
                newstate.operand.append(['MUL', newstate.number[z]])
            elif mlist[z] == 5:
                newstate.operand.append(['DIV', newstate.number[z]])
            else:
                print("unknown operator")
            z += 1
        return newstate

    def is_goal(self, a_state: State.State):
        return a_state.target == self.target

    def result(self, a_state: State.State):
        seq = self.random_start(a_state.target, a_state.number, a_state)
        return seq


