# Python Projects for Beginners - freeCodeCamp
This repository documents my attempts at building the beginner level Python projects listed on [this](https://www.freecodecamp.org/news/python-projects-for-beginners/) article on [freeCodeCamp](https://www.freecodecamp.org/news).

## Table of Contents:
- [Mad Libs](#mad-libs)
    - [madLibs01.py](https://github.com/nadupoy/Python-Projects-for-Beginners---freeCodeCamp/blob/main/madLibs01.py)
    - [madLibs02.py](https://github.com/nadupoy/Python-Projects-for-Beginners---freeCodeCamp/blob/main/madLibs02.py)
- [Guess the Number Game - computer](#guess-the-number-game---computer)
- [Guess the Number Game - user](#guess-the-number-game---user)
- [Rock, paper, scissors](#rock-paper-scissors)

### Mad Libs:
---
#### [madLibs01.py](https://github.com/nadupoy/Python-Projects-for-Beginners---freeCodeCamp/blob/main/madLibs01.py)
I encountered the following error in the terminal when running the code in the VS Code editor:

```
activate.ps1 cannot be loaded because running scripts is disabled ...
```

I managed to find a solution [here](https://support.enthought.com/hc/en-us/articles/360058403072-Windows-error-activate-ps1-cannot-be-loaded-because-running-scripts-is-disabled-UnauthorizedAccess-). I opted for  *'Option 1 - Select Command Prompt as the default terminal shell in VS Code'*  as it is a quick and straightforward solution.

#### [madLibs02.py](https://github.com/nadupoy/Python-Projects-for-Beginners---freeCodeCamp/blob/main/madLibs02.py)
When using **Git** to push the code to **GitHub**, I encountered the following error in both instances:

```
The following paths are ignored by one of your .gitignore files
```

Using the following **Git** command resolved the issue:

```
git add -f <file_name.py>
```

In this project, I applied the [choice( )](https://www.w3schools.com/python/module_random.asp) method in Python's [random module](https://www.w3schools.com/python/module_random.asp):

```python
    noun_subjects = ["i", "you", "he", "she", "it", "they"]`
    ...
    noun_subject = random.choice(noun_subjects)
```

### [Guess the Number Game - computer:](https://github.com/nadupoy/Python-Projects-for-Beginners---freeCodeCamp/blob/main/numberGame-computer.py)
---
I gained a better understanding of `while` loops with this exercise and applied the [randint( )](https://www.w3schools.com/python/ref_random_randint.asp) method in Python's [random module](https://www.w3schools.com/python/module_random.asp).

Initially, the clause used in the `while` loop was only:

```python
    print(number_01, number_02)
    print("The numbers are not a match. 😔\n")
```

This resulted in an infinite output of the `print` statement as follows:

```
    48 59

    The numbers are not a match. 😔

    The numbers are not a match. 😔

    The numbers are not a match. 😔

    The numbers are not a match. 😔

    The numbers are not a match. 😔

    . . .
```

New random numbers were not being generated after the starting values defined outside the `while` loop. Thus, the values being compared to the `while` condition remained constant, producing the same output over and over again.

For more random numbers to be generated so as to be compared with the condition in the `while` loop, the values contained in `number_01` and `number_02` had to change from the starting values.

This was solved by adding the following statements in the clause:

```python
    number_01 = random.randint(1, 100)
    number_02 = random.randint(1, 100)
```

**N/B:** Increasing the range in the `randint()` method made for a longer and more interesting program.

Moreover, I learnt about [fenced code blocks](https://www.markdownguide.org/extended-syntax/#fenced-code-blocks) and [syntax highlighting](https://www.markdownguide.org/extended-syntax/#syntax-highlighting) in Markdown's [extended syntax](https://www.markdownguide.org/extended-syntax).

### [Guess the Number Game - user:](https://github.com/nadupoy/Python-Projects-for-Beginners---freeCodeCamp/blob/main/numberGame-user.py)
---
In the book [Automate the Boring Stuff](https://automatetheboringstuff.com/2e/chapter1/) by [Al Sweigart](https://inventwithpython.com/), the default value type of the `input()` function is a string.

A string value cannot be accurately compared with an integer value. The `int()` function is therefore used to convert the string input value into an integer so as to accurately compare the two values as shown below:

```python
    number_02 = input("Guess a number between 1 and 5. ")
    number_02 = int(number_02)
```

### [Rock, paper, scissors:](https://github.com/nadupoy/Python-Projects-for-Beginners---freeCodeCamp/blob/main/rock_paper_scissors.py)
---
I initially opted to use a `set` sequence for the options available for selection by the computer as it is mainly unchangeable and unordered:

```python
    options = {"rock", "paper", "scissors"}
```

This however resulted in the following error:

```
    TypeError: 'set' object is not subscriptable
```

In addition to being unordered, sets are also unindexed. This resulted in the built-in `random` module's `choice()` method not being able to make a selection.

Using a `tuple` sequence instead resolved the error as they are unchangeable, ordered and indexed.

```python
    options = ("rock", "paper", "scissors")
```

[Borislav Hadzhiev](https://github.com/bobbyhadz) goes into detail about the above error in [this](https://bobbyhadz.com/blog/python-set-object-is-not-subscriptable) blog article.

I also managed to successfully implement nested conditional statements in this project.