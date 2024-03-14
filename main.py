from sympy.solvers import solve
from sympy import Symbol
import math


# equation using one of more of the symbols
# attempt(values) tries to solve the equation for the None value
class Equation:
    def __init__(self, equation, alphabet):
        self.equation = equation

        # parse the symbols
        self.symbols = []
        for s in alphabet:
            if s in equation:
                self.symbols.append(s)


    def attempt(self, values:dict):
        # replace the symbols with their values
        eq = self.equation

        # make sure the equation is solvable (only one unknown symbol)
        if len(self.symbols) - sum([1 for s in self.symbols if values[s] is not None]) != 1:
            return

        # extract only the relevant symbols
        my_values = {k: v for k, v in values.items() if k in self.symbols}

        solve_for = None
        for k, v in my_values.items():
            if v is None:
                solve_for = k
            else:
                eq = eq.replace(k, str(v))

        # solve the equation
        if solve_for:
            # parse the equation to match sympy's syntax
            eq = eq.replace("=", "-(") + ")"

            # solve the equation
            result = solve(eq, solve_for)
            if len(result) == 1:
                return solve_for, result[0]


if __name__ == '__main__':

    # ask user to list all symbols separated by a space
    alphabet = input("Enter all symbols separated by a space: ").split()

    # ask user for the value of each symbol
    values = {}
    for s in alphabet:
        values[s] = None
        val = input(f"Enter value for {s} (leave blank if unknown): ")
        if val:
            values[s] = int(val)

    # ask user for the equations
    global_equations = []
    while True:
        eq = input("Enter equation (leave blank to stop): ")
        if not eq:
            break
        global_equations.append(eq)

    # solve the equations
    print("Solving equations...")

    while True:
        flag = False
        for e in global_equations:
            e = Equation(e, alphabet)
            result = e.attempt(values)
            if result:
                values[result[0]] = result[1]
                print("Solved", result[0], "=", result[1])
                flag = True
        if not flag:
            break

        if all([v is not None for v in values.values()]):
            break

    if not all([v is not None for v in values.values()]):
        print("Could not solve the provided system. Make sure you entered all known values and equations correctly.")
    else:
        print("\nSolved system:")
        for k, v in values.items():
            if k == "W":
                k = "S"
            print(f"{k} = {v}")

