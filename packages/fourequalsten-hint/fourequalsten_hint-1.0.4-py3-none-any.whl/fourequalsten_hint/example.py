from fourequalsten_hint import feth

foo1 = feth.solve("8556","+",0)
# foo1 is a string containing the first possible solution (and in general the simplest one)
# Here, foo1 = "8*5-5*6"

foo2 = feth.sovle("6031","+",1)
# foo2 is a list containing every possible solution for this proble
# Here, foo2 = ["6-(0-3-1)", "6-(0-1-3)", "3-(0-1-6)", "3-(0-6-1)", "1-(0-3-6)", "1-(0-6-3)"]

foo3 = feth.solve("8556","-",0)
# foo3 is an empty list, because there is no solution to this problem
# Here, foo3 = []

feth.fancy_solve()
# feth.fancy_solve() will guide the user with prints and inputs, but the concept remains the same
# 1. Ask for 4 digits
# 2. Ask for (potential) banned operators
# 3. Display the first solution, the number of possible solution and propose to display every solution
# 4. Propose to re-execute the program
