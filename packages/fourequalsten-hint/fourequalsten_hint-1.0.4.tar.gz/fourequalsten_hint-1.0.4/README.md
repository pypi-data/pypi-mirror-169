# 4=10's Solution Generator

***by Cheewy***

## Version

New v1.0.4 Release :
- Addition of comments :)
- Addition of an ```example.py``` file to test all the functionnalities
- Removal of TONS of useless code (more code deleted than comments added O_O)
- Optimization of the calcul process

## Description : 

This tiny program in Python allows you to quickly and simply calculate every possible solutions to the famous *4=10* game.</br>
I had a lot of fun developping it, I hope you will enjoy it.</br>

*Note : The code has comments, but if you want further explanations, don't hesitate to email me.*

## ❗️ DISCLAIMER BEFORE USING IT ❗️

*Use this program sparingly, or only when you are **REALLY** stuck and you have no more daily solution left.*</br>
*Using this program too much will **RUIN** your entire game experience, and will be **VERY** insulting for the game developper.*</br>
*I am **NOT** responsible for any bad game experience.*</br>

## Installation :

**1. Use pip to install the package**

For Unix/macOS :
```
python3 -m pip install fourequalsten_hint
```
For Windows :
```
py -m pip install fourequalsten_hint
```
**2. Import the package in your program</br>**

Code to write down in your file *before using the commands of the package* :</br>
```
from fourequalsten_hint import feth
```

## Utilisation Guide :

**If you just want the answers :**

1. Create a python file anywhere on your computer (ex: ```test.py```)
2. In this file, write down the following code :
```
from fourequalsten_hint import feth
feth.fancy_solve()
```
3. Execute the program and follow the instructions in the terminal</br></br>

**If you want to use the functions in your program :**

```
feth.solve(input_nb,input_op,all_solutions)
```

*Note : Documentation of the functions are right underneath*

**If you want to test before using it :**

You can download the ```example.py``` file and look at the [examples](https://github.com/CheewyOFF/fourequalsten_hint/tree/main/src/fourequalsten_hint/example.py), or read it directly down here ;)

```
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
```

## Documentation
- ```feth.solve(input_nb,input_op,all_solutions)```</br></br>
  The ```solve()``` function takes 3 parameters :
    - **input_nb** (str) : String made of 4 digits (the ones in the enigma)</br>
      *Ex :* ```"1234"```</br></br>
    - **input_op** (str) : String made of the banned operators</br>
        Working chars :
        - '+' for plus
        - '-' for minus
        - '*' for multiplication
        - '/' for division
        - Empty string for none : ""</br>
      *Ex :* ```"+"```, ```"-+"```, ```""```</br></br>
    - **all_solutions** (int) : 0 or 1 depending of the informations you want in return</br>
        - 0 : Returns one possible solution in the form of a string</br>
          *Ex :* ```"(1+2+3)+4"```</br>
        - 1 : Returns every possible solutions in the form of a list of strings</br>
          *Ex :* ```["(1+2+3)+4", ... , "4+3+2+1"]```
      
  *Note : If there's no result, the function will return an empty list*</br></br>
  
- ```feth.fancy_solve()```</br></br>
  The ```fancy_solve()``` function takes no parameters, and will return nothing.</br>
  It is made of multiple affordable inputs, prints and os.clear to give to the user a casual and simple use of the program.</br></br>
  **Steps :**
    1. Ask for 4 digits
    2. Ask for (potential) banned operators
    3. Display the first solution, the number of possible solution and propose to display every solution
    4. Propose to re-execute the program
  
## License

[MIT License](https://github.com/CheewyOFF/fourequalsten_hint/blob/main/LICENSE)

## Credits :

### Fourequalsten_hint

Developper : Cheewy</br>
Email : cheewy.perso@gmail.com

***Buy Me a Coffee ♥ :*** [Click here](https://www.buymeacoffee.com/CheewyOFF)

### 4=10

Developper : Sveinn Steinarsson</br>
Website : [fourequalsten.app](https://fourequalsten.app)</br>
Email : fourequalsten@fourequalsten.app</br>
Youtube Channel : [svenstone](https://www.youtube.com/user/svenstone)</br>

***Buy Sveinn a Coffee ♥ :*** [Click here](https://www.buymeacoffee.com/steinarsson)

Download game on Google Play Store : [Click here](https://play.google.com/store/apps/details?id=app.fourequalsten.fourequalsten_app&hl=en_US&gl=US")</br>
Download game on Apple Play Store : [Click here](https://apps.apple.com/us/app/4-10/id1609871477)
