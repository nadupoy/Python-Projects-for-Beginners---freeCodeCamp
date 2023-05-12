# Python Projects for Beginners - freeCodeCamp
This repository documents my attempts at building the beginner level Python projects listed on [this](https://www.freecodecamp.org/news/python-projects-for-beginners/) article on [freeCodeCamp](https://www.freecodecamp.org/news).

## Table of Contents:
- [Mad Libs](#mad-libs)
    - [madLibs01.py](https://github.com/nadupoy/Python-Projects-for-Beginners---freeCodeCamp/blob/main/madLibs01.py)
    - [madLibs02.py](https://github.com/nadupoy/Python-Projects-for-Beginners---freeCodeCamp/blob/main/madLibs02.py)

### Mad Libs:
#### [madLibs01.py](https://github.com/nadupoy/Python-Projects-for-Beginners---freeCodeCamp/blob/main/madLibs01.py)
I encountered the following error in the terminal when running the code in the VS Code editor:

`activate.ps1 cannot be loaded because running scripts is disabled ...`

I managed to find a solution [here](https://support.enthought.com/hc/en-us/articles/360058403072-Windows-error-activate-ps1-cannot-be-loaded-because-running-scripts-is-disabled-UnauthorizedAccess-). I opted for  *'Option 1 - Select Command Prompt as the default terminal shell in VS Code'*  as it is a quick and straightforward solution.

#### [madLibs02.py](https://github.com/nadupoy/Python-Projects-for-Beginners---freeCodeCamp/blob/main/madLibs02.py)
When using **Git** to push the code to **GitHub**, I encountered the following error in both instances:

`The following paths are ignored by one of your .gitignore files`

Using the following **Git** command resolved the issue:

`git add -f <file_name.py>`

With this project, I was introduced to Python's **random module** [choice( )](https://www.w3schools.com/python/module_random.asp) method:

`noun_subjects = ["i", "you", "he", "she", "it", "they"]`

`...`

`noun_subject = random.choice(noun_subjects)`