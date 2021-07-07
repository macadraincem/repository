# Michael Angelo C. Adraincem
# MCA655 11208422
# State.py

import random


class State(object):
    def __init__(self,target,operand,number):
        self.target = target
        self.operand = operand
        self.number = number

    def __str__(self):
        if self.target is None:
            return '<Initial state,' + str(self.number) + '>'
        else:
            return '<' + str(self.target) + ' ' + self.operand + ' ' + str(self.number) + '>'

    def used(self,c):
        #Check if value c appears as a choice
        return c not in self.choices

    def expression(self):
        return self.expr
