# Author : Cheewy
# Filename : feth.py

# List of usable functions : 
#   - fancy_solve()
#   - solve(input_nb,input_op,all_solutions)

# List of other functions :
#   - decompose(input,x)
#   - research(pattern,current_nb,operator_list)
#   - str_calcul(pattern)
#   - clean_par(pattern)
#   - par_pattern(x,pattern)

# Usable function : Fancy display for solving the enigma
def fancy_solve():
    import os

    missing_operator = []
    current_nb = []

    # While the user don't quit (ask at the end)
    cont = "1"
    while(cont == "1"):
        # Clear the terminal
        os.system('cls')
        
        # Asking the 4 digits and calls decompose() to verify the input
        input_str = str(input("Enter the 4 enigma's digits : "))
        while(decompose(input_str,0) == []):
            input_str = str(input("Enter the 4 enigma's digits : "))

        # For display purpose (after the solving)
        tmp_digits = input_str
        
        #  Transform the string into a 4 element list
        current_nb = list(input_str)

        # Same steps for the banned operators (up to line 45)
        input_str = str(input("Enter the banned operators (Press Enter if there's none) : "))
        while(decompose(input_str,1) == []):
            input_str = str(input("Enter the banned operators (Press Enter if there's none) : "))

        tmp_banop = input_str
        missing_operator = list(input_str)

        
        operator_list = ["+","-","*","/"]

        # Delete the banned operators from the above list
        if missing_operator != ["none"]:
            for i in missing_operator:
                operator_list.remove(i)

        # Transform the 4 strings of the current_nb list into ints
        for k in range(len(current_nb)):
            current_nb[k] = int(current_nb[k])
            
        # Generate the pattern dictionnary, which is the lung of the program. Consist of :
        #   - Every opening and closing parenthesis, with a 0 or a 1, depending if there's one or not
        #   - Every position for the numbers of the enigma (containing one of the numbers)
        #   - Every position for the operators of the enigma (containing one of the allowed operators)
        pattern = {"par_ou1" : 0, "num1" : -1, "op1" : 0, "par_ou2" : 0, "num2" : -1, "par_fe1" : 0, "op2" : 0, "par_ou3" : 0, "num3"  : -1, "par_fe2" : 0, "op3" : 0, "num4" : -1, "par_fe3" : 0}

        # Calls the research() function, which will send the result(s) of the enigma
        solution = research(pattern,current_nb,operator_list)
      
        # Fancy display...
        os.system('cls')
        print("Digits : " + tmp_digits)
        if(missing_operator == ["none"]):
            print("Banned operators : none")
        else:
            print("Banned operators : " + tmp_banop)
        if(solution == []):
            print("No solution found. You enter wrong values or there is no solution.")
        else:
            print("We found [ " + str(len(solution)) + " ] solutions !")
            if(len(solution) == 1):
                print("Here it is :")
                print("")
                print(solution[0])
            else:
                print("Here is one : ")
                print("")
                print(solution[0])
                print("")
                print("Would you like to see all the answers ?")

                # Propose to display every solution (0 for yes, Enter to skip)
                display_all = str(input("(Press Enter to skip, 0 to display all possible solutions) : "))
                while(display_all != "" and display_all != "0"):
                    display_all = str(input("(Press Enter to skip, 0 to display all possible solutions) : "))

                print("")
                
                # Display every solution if desired
                if(display_all == "0"):
                    for k in range(len(solution)):
                        print("Solution n°"+str(k+1)+" : "+solution[k])

        print("\n\n\n")
           
        # Propose to re-execute the program
        cont = str(input("Would you like to continue ? (1 for YES, 0 for NO) : "))
        while(cont not in ["1","0"]):
            print("Please enter either 0 or 1.")
            cont = str(input("Would you like to continue ? (1 for YES, 0 for NO) : "))

    print("\n\n\n")
    # Being kind <3
    print("Thanks for using my program <3\n\n\tby Cheewy")
    print("\n\n\n")

# Usable function : Return different forms of answer for the enigma
def solve(input_nb,input_op,all_solutions):
    # Check the inputs and put them in a list (one element for each character)
    current_nb = decompose(input_nb,0)
    missing_operator = decompose(input_op,1)

    # If both numbers and operators are valid
    if(current_nb != [] and missing_operator != []):
        operator_list = ["+","-","*","/"]

        # Removing banned operators
        if missing_operator != ["none"]:
            for i in missing_operator:
                operator_list.remove(i)

        # Same as the fancy_solve() (up to line 133)
        for k in range(len(current_nb)):
            current_nb[k] = int(current_nb[k])

        # Go to line 59 for more details
        pattern = {"par_ou1" : 0, "num1" : -1, "op1" : 0, "par_ou2" : 0, "num2" : -1, "par_fe1" : 0, "op2" : 0, "par_ou3" : 0, "num3"  : -1, "par_fe2" : 0, "op3" : 0, "num4" : -1, "par_fe3" : 0}

        solution = research(pattern,current_nb,operator_list)
        
        # If only one solution is desired, return the first solution    
        if(all_solutions == 0 and solution != []):
            return solution[0]

        # If all the solutions are desired, return a list of every possible solution
        elif(all_solutions == 1 and solution != []):
            return solution
        # If there's no solution, return an empty list
        else:
            return []

# Checking the inputs and returning them in form of lists
def decompose(input,x):
    # Initializations...
    number_list = ["0","1","2","3","4","5","6","7","8","9"]
    operator_list = ["+","-","*","/"]
    # Default result (invalid one, if the input is correct, it will return something else)
    res = []

    # Checking the type
    if(type(input) != str):
        print("ERROR : Wrong type ! You need to enter a string.")
    else:
        # If the input is the string of 4 digits
        if(x == 0):
            # Testing length
            if(len(input) != 4):
                print("ERROR : You need to enter 4 numbers.")
            else:
                inc = 1
                valid = 1
                # Testing the validity of every character
                for i in input:
                    if(i not in number_list):
                        valid = 0
                        print("ERROR : The character n°"+str(inc)+" is invalid.")
                    inc += 1
                # Returning the good list
                if(valid == 1):
                    res = [input[0],input[1],input[2],input[3]]
        # If the input is the string of banned operators
        elif(x == 1):
            # If 4 operators or more are banned
            if(len(input)>len(operator_list)-1):
                print("ERROR : You banned too many operators !")
            else:
                inc = 1
                valid = 1
                # Testing the validity of every character
                for i in input:
                    if(i not in operator_list):
                        valid = 0
                        print("ERROR : The character n°"+str(inc)+" is invalid.")
                    inc += 1
                if(valid == 1):
                    # If no operators are banned, return a valid result
                    if(len(input) == 0):
                        res = ["none"]
                    else:
                        # Return every banned operators in a list
                        for i in input:
                            res.append(i)
        else:
            # If the 'x' input isn't for numbers (0) or banned operators (1)
            print("ERROR : The input is neither 4 numbers or the list of banned operators.")
    
    return res

# Calculating every solution of the enigma
def research(pattern,current_nb,operator_list):
    # Initializations...
    nb_par = nb_signe = nb_chiffre = no_swap = 0
    solution = []

    # For every possible parenthesis pattern :
    while(nb_par <= 5):
        # For every possible number switch
        nb_chiffre = 0
        while(nb_chiffre < 24):
            no_swap = 0
            nb_signe = 0
            # Initializing the numbers at the beginning
            if(nb_par == 0 and nb_signe == 0 and nb_chiffre == 0):
                pattern["num1"] = current_nb[0]
                pattern["num2"] = current_nb[1]
                pattern["num3"] = current_nb[2]
                pattern["num4"] = current_nb[3]
            else:
                # From this line up to the 253th, we're just swapping numbers in order to generate every possible combinaison

                # Every 6 test, change the first number
                if(nb_chiffre%6 == 0):
                    # If swapping the values changes something (no duplicates), swap
                    if(pattern["num1"] != pattern["num" + str((nb_chiffre//6)+1)] or nb_chiffre == 0):
                        pattern["num1"], pattern["num" + str((nb_chiffre//6)+1)] = pattern["num" + str((nb_chiffre//6)+1)], pattern["num1"]
                    else:
                        # Else don't swap and don't calculate
                        no_swap = 1
                else:
                    # If the first number didn't change and the number of swaps already checked is odd, swap the 3rd and the 4th digits
                    if(nb_chiffre%2 == 1):
                        # If swapping the values changes something (no duplicates), swap
                        if(pattern["num3"] != pattern["num4"]):
                            pattern["num3"], pattern["num4"] = pattern["num4"], pattern["num3"]
                        else:
                            # Else don't swap and don't calculate
                            no_swap = 1
                    # If the first number didn't change and the number of swaps already checked is even, swap the 2nd and the 4th digits
                    else:
                        # If swapping the values changes something (no duplicates), swap
                        if(pattern["num2"] != pattern["num4"]):
                            pattern["num2"], pattern["num4"] = pattern["num4"], pattern["num2"]
                        else:
                            # Else don't swap and don't calculate
                            no_swap = 1

            # If numbers swapped (in order to not check again if you wanted to swap similar numbers)
            if(no_swap == 0):
                # For every swap of numbers and every parenthesis pattern, check every possible operator combinaison
                while(nb_signe < len(operator_list)**3):
                    # Changing the possible operator combinaison every iteration
                    pattern["op1"] = operator_list[nb_signe//len(operator_list)**2]
                    pattern["op2"] = operator_list[(nb_signe//len(operator_list))%len(operator_list)]
                    pattern["op3"] = operator_list[nb_signe%len(operator_list)]
                
                    # Calculating the outputed pattern
                    try:
                        # Transforming the pattern into a string and calculating it thanks to the eval() function
                        res = eval(str_calcul(pattern))
                    # If there is a division by zero, return 0 (!= of 10 so it won't count)
                    except ZeroDivisionError:
                        res = 0

                    # If the pattern is a solution, save it into the 'solution' list
                    if(res == 10):
                        solution.append(str_calcul(pattern))
                    # Just iterating every while condition
                    nb_signe += 1
            nb_chiffre += 1
        nb_par += 1

        # Changing the pattern of the parenthesis (for every iteration of the first while)
        pattern = par_pattern(nb_par,pattern)

    return solution

# Returns a string out of the current pattern
def str_calcul(pattern):
    # Adding every number and operator in the right order
    str_calcul = str(pattern["num1"]) + str(pattern["op1"]) + str(pattern["num2"]) + str(pattern["op2"]) + str(pattern["num3"]) + str(pattern["op3"]) + str(pattern["num4"])
    # If there are parenthesis, add them in the correct place, depending on the current parenthesis pattern
    if(pattern["par_ou1"] == 1):
        str_calcul = "(" + str_calcul
        if(pattern["par_fe1"] == 1):
            str_calcul = str_calcul[:4] + ")" + str_calcul[4:]
        else:
            str_calcul = str_calcul[:6] + ")" + str_calcul[6:]
    elif(pattern["par_ou2"] == 1):
        str_calcul = str_calcul[:2] + "(" + str_calcul[2:]
        if(pattern["par_fe2"] == 1):
            str_calcul = str_calcul[:6] + ")" + str_calcul[6:]
        else:
            str_calcul = str_calcul + ")"
    elif(pattern["par_ou3"] == 1):
        str_calcul = str_calcul[:4] + "(" + str_calcul[4:] + ")"
    
    # Return the string
    return str_calcul

# Reset every parenthesis
def clean_par(pattern):
    pattern["par_ou1"] = 0
    pattern["par_ou2"] = 0
    pattern["par_ou3"] = 0
    pattern["par_fe1"] = 0
    pattern["par_fe2"] = 0
    pattern["par_fe3"] = 0
    
    return pattern

# For every number of the iteration in the research function, change the parenthesis
def par_pattern(x,pattern):
    pattern = clean_par(pattern)
    if(x == 1):
        pattern["par_ou1"] = 1 
        pattern["par_fe1"] = 1 
    elif(x == 2):
        pattern["par_ou1"] = 1 
        pattern["par_fe2"] = 1 
    elif(x == 3):
        pattern["par_ou2"] = 1 
        pattern["par_fe2"] = 1 
    elif(x == 4):
        pattern["par_ou2"] = 1 
        pattern["par_fe3"] = 1 
    elif(x == 5):
        pattern["par_ou3"] = 1 
        pattern["par_ou3"] = 1 

    return pattern