# Michael Angelo C. Adraincem
# MCA655 11208422

import Problem
import Machine
import itertools
import a2q6_rmse


# random_search
# Parameters: Problem, Iteration limit
# Returns: Best guess result
def random_search(problem,limit):
    # Best Guess Equation - random state
    best_guess = problem.result(problem.a_state)
    # Best Guess Result
    bgr = Machine.machine_exec(best_guess.operand)
    guess = None
    gr = 0
    i = 1

    while i < limit:
        # Call get_neighbor class
        guess = get_neighbour(best_guess, problem, limit)
        gr = Machine.machine_exec(guess.operand)

        if is_closer(gr, bgr, problem.target):
            best_guess = guess
            bgr = gr
        i += 1
    print(best_guess.operand)
    return bgr


# get_neighbour
# Parameters: guess, best_guess
# Returns: returns best guess neighbor
def get_neighbour(best_guess, problem, limit):
    i = 0
    c = 0
    guess = None

    while guess is None and c < limit:
        attempt = problem.result(problem.a_state)
        for x, y in zip(attempt.operand, best_guess.operand):
            operator_g = x[0]
            operator_b = y[0]
            if operator_b == operator_g:
                i += 1
        if len(best_guess.operand) - i == 1:
            guess = attempt
            break
        else:
            guess = attempt
            break
        i = 0
        c += 1

    return guess


# is_closer
# Parameters: guess, best, target
# Returns: returns True if guess is better, False otherwise
def is_closer(guess, best, target):
    # Objective Function
    result = min(guess, best, key=lambda v: abs(target-v))

    if result == guess:
        return True
    else:
        return False


# test
# Parameters: test number, target, numberlist, iteration limit
# Post: displays results
# Returns: nothing
def test(i, target, number, limit):
    print("**************************Test", i , "*************************")
    t = Problem.Problem(target,number)
    print("Target is: ", target)
    print("Result is: ")
    result = (random_search(t, limit))
    print(result)
    print("**********************End of Test", i, "**********************\n")
    return a2q6_rmse.err(result, target)


def main():
    # Iteration Limit: 10000
    test(1, 2.74161e+05, [344, 397, 152, 307, 217], 1000)
    test(2, 9.07000e+02, [117, 305, 329, 343, 444], 1000)
    test(3, 1.27500e+03, [310, 195, 382, 213, 118], 1000)
    test(4, -7.01300e+03, [474, 131, 301, 194, 478], 1000)
    test(5, 1.44000e+02, [392, 142, 354, 482, 106], 1000)



