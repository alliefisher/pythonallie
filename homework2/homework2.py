# File: homework2.py

# Your file path should look like:
# python_decal_fa25/yourname/homework2/homework2.py

# Questions (Answer these in the homework2.py file as comments):

# 1) What’s the difference between Git, GitHub, and Git Bash?
# Git is the core coding program installed on your computer, GitHub is an online platform that stores all of the information saved through Git repositories, and Git Bash is an interface for Windows that allows you to use Git commands in a similar terminal environment to Mac.

# 2) What’s the difference between the terminal and the command line?
# The terminal is the interface you use to interact with your computer and the command line is just the text interface you use to type in the terminal.

# 3) How does Windows PowerShell differ from Git Bash?
# Windows Powershell is a specific terminal for Windows while Git Bash is an application on terminal that can be used to mimic the terminal on Mac. Git Bash is used to run Git commands while Windows Powershell is used for a variety of different commands and functions on Windows.

# 4) What’s the difference between Anaconda, conda, and Python?
# Python is a core programming language, conda is a package manager that allows you to install different libraries for Python, and Anaconda is a set of packages that includes many other packages and libraries that are useful for coding.

# 5) What is VS Code? 
# VS Code is coding platform that you can write and run code in. It's also an easier platform due to its user-friendly interface (autofill and error highlighting).

# 6) What is a Jupyter Notebook? How is it different from Jupyter Lab?
# Jupyter Notebook is a interface that you can run and write code in, with a notebook-like format. Jupyter lab is a more advanced version of Jupyter Notebook. 

# 7) What does ~/ mean?
# ~/ is a shortcut for the home directory of your computer. (Allows for shortcuts in writing your path names when trying to cd into a directory off of your home directory).

# 8) What’s the difference between an absolute path and a relative path?
# Absolute paths provide a full, explicit address to a file or directory from the root directory, while relative paths are more flexible and you can use shortcuts like ./ and ../ to navigate to files or directories based on current location.

# 9) Imagine you're in your "yourname" repo. Write the absolute and relative paths to "course_assignments/homework2".
# Absolute path: /Users/alliefisher/python_decal_sp26/course_assignments/homework2
# Relative path: course_assignments/homework2

# 10) What command lets you move from "course_assignments/homework2/" to "course_assignments/"?
# The command to move from course_assignments/homework2/ to course_assignments/ is cd .. (which moves you up one directory).

# 11) What would rm ./ do in your current directory? (Don’t try it!)
# Running rm ./ would delete the current directory and all of its contents, which is why you should never try it! It would be a very destructive command.

# 12) What do the following commands do?
# git add: This command adds changes from your working directory to the staging area. This sets the stage for the next command, commit.
# git commit: This command takes the changes from the staging area to the repository, creating a new commit with a message describing the changes.
# git push: This command uploads your local commits to a remote repository, such as in GitHub, 

# 13) What's the difference between "git add ." and "git add <file>"?
# Git add . adds all changes in the current directory, but git add <file> adds one specific file to the staging area.

# 14) What do "git status" and "git log -1" do?
# Git status tells you the current status of your repository, including if any changes to the repository have been staged or not. Git log -1 shows you the most recent commit in your repository, including the commit message and the changes that were made in that commit.

# 15) What’s the difference between cloning a repository and pulling from it?
# Cloning a repository creates a complete copy of the repository from a remote source. Git pull can be used later to update and existing copy with new changes from the remote repository.

# 16) What has been your most frustrating bug or error in this class so far? How did you troubleshoot or fix it?
# My most frustrating bug happened when I forgot the passkey to my terminal. I had to go to office hours and get help, which meant having to delete my old passkey and entirely re-install my SSH key.

# 17) What’s a question you still have? What’s something you’re confused about?
# A question I still have is how to directly move from one file to another in a shorter path because sometimes I get confused. Something I'm confused about is the git add and pushing process, but I think it's something I need to repeat more to become used to it.

# 18) Tell me a fun fact!
# A fun fact is that I have been stung by a stingray before!

# 19) Print your favorite math expression you've learned in Python so far. 
# (Hint: Use print() and add a comment explaining what it does.)
print(20%6) # This is the modulus operator, which returns the remainder of a division problem. This should return 2, since 20 divided by 6 is 3 with a remainder of 2.
