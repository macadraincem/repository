# Michael Angelo C. Adraincem
# MCA655 11208422

import Problem
import Machine
import a2q6_rmse


# random_guessing
# Parameters: Problem, Iteration limit
# Returns: Best guess result
def random_guessing(problem,limit):
    # Best Guess Equation - random state
    best_guess = problem.result(problem.a_state)
    # Best Guess Result
    bgr = Machine.machine_exec(best_guess.operand)
    i = 1

    while i < limit:
        # Guess Equation
        guess = problem.result(problem.a_state)
        # Guess Result
        gr = Machine.machine_exec(guess.operand)
        if is_closer(gr, bgr, problem.target):
            best_guess = guess
            bgr = gr
        i += 1
    print(best_guess.operand)
    return bgr


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
# Returns: err value
def test(i, target, number, limit):
    print("**************************Test", i , "*************************")
    t = Problem.Problem(target,number)
    print("Target is: ", target)
    print("Result is: ")
    result = random_guessing(t, limit)
    print(result)
    print("**********************End of Test", i, "**********************\n")
    return a2q6_rmse.err(result, target)

def main():
    # Iteration Limit: 1000
    test(1, 2.74161e+05, [344, 397, 152, 307, 217], 1000)
    test(2, 9.07000e+02, [117, 305, 329, 343, 444], 1000)
    test(3, 1.27500e+03, [310, 195, 382, 213, 118], 1000)
    test(4, -7.01300e+03, [474, 131, 301, 194, 478], 1000)
    test(5, 1.44000e+02, [392, 142, 354, 482, 106], 1000)



