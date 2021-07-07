# Michael Angelo C. Adraincem
# MCA655 11208422
# Machine.py

def machine_exec(seq):
    register = 0.0
    for instruction in seq:
        operator = instruction[0]
        operand = instruction[1]

        if operator == "ADD":
            register += operand
        elif operator == "SUB":
            register -= operand
        elif operator == "MUL":
            register *= operand
        elif operator == "DIV":
            register = register / operand
        elif operator == "NOP":
            pass
        else:
            print('unknown operator', operator)
    return register
