# Python Projects for Beginners - freeCodeCamp
This repository documents my attempts at building the beginner level Python projects listed on [this](https://www.freecodecamp.org/news/python-projects-for-beginners/) article on [freeCodeCamp](https://www.freecodecamp.org/news).

## Table of Contents:
- [Mad Libs](#mad-libs)
    - [madLibs01.py](https://github.com/nadupoy/Python-Projects-for-Beginners---freeCodeCamp/blob/main/madLibs01.py)
    - [madLibs02.py](https://github.com/nadupoy/Python-Projects-for-Beginners---freeCodeCamp/blob/main/madLibs02.py)
- [Guess the Number Game - computer](#guess-the-number-game---computer)

### Mad Libs:
---
#### [madLibs01.py](https://github.com/nadupoy/Python-Projects-for-Beginners---freeCodeCamp/blob/main/madLibs01.py)
I encountered the following error in the terminal when running the code in the VS Code editor:

`activate.ps1 cannot be loaded because running scripts is disabled ...`

I managed to find a solution [here](https://support.enthought.com/hc/en-us/articles/360058403072-Windows-error-activate-ps1-cannot-be-loaded-because-running-scripts-is-disabled-UnauthorizedAccess-). I opted for  *'Option 1 - Select Command Prompt as the default terminal shell in VS Code'*  as it is a quick and straightforward solution.

#### [madLibs02.py](https://github.com/nadupoy/Python-Projects-for-Beginners---freeCodeCamp/blob/main/madLibs02.py)
When using **Git** to push the code to **GitHub**, I encountered the following error in both instances:

`The following paths are ignored by one of your .gitignore files`

Using the following **Git** command resolved the issue:

`git add -f <file_name.py>`

In this project, I applied the [choice( )](https://www.w3schools.com/python/module_random.asp) method in Python's [random module](https://www.w3schools.com/python/module_random.asp):

`noun_subjects = ["i", "you", "he", "she", "it", "they"]`

`...`

`noun_subject = random.choice(noun_subjects)`

### [Guess the Number Game - computer:](https://github.com/nadupoy/Python-Projects-for-Beginners---freeCodeCamp/blob/main/numberGame-computer.py)
---
I gained a better understanding of `while` loops with this exercise and applied the [randint( )](https://www.w3schools.com/python/ref_random_randint.asp) method in Python's [random module](https://www.w3schools.com/python/module_random.asp).

Initially, the clause used in the `while` loop was only:

`print(number_01, number_02)`

`print("The numbers are not a match. 😔\n")`

This resulted in an infinite output of the `print` statement as follows:

`48 59`

`The numbers are not a match. 😔`

`The numbers are not a match. 😔`

`The numbers are not a match. 😔`

`The numbers are not a match. 😔`

`The numbers are not a match. 😔`

`. . .`

New random numbers were not being generated after the starting values defined outside the `while` loop. Thus, the values being compared to the `while` condition remained constant, producing the same output over and over again.

For more random numbers to be generated so as to be compared with the condition in the `while` loop, the values contained in `number_01` and `number_02` had to change from the starting values.

This was solved by adding the following statements in the clause:

`number_01 = random.randint(1, 100)`

`number_02 = random.randint(1, 100)`

**N/B:** Increasing the range in the `randint()` method made for a longer and more interesting program.