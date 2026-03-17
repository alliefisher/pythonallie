# -- 3. Homework 1 + 2 Review --
# - 3.1 Vocabulary Review -
# 1. Git vs. GitHub: Git is a programming language and data storage device used for people to put their code into remote and local repositories. GitHub is the platform on browser apps in which you can see the data that you or others have uploaded to repositories.
# 2. Terminal vs Command line: A terminal is an app where you write your code and a command line is the area on your terminal in which you write your code.
# 3. Local vs. Remote Repository: A local repository is a repository on your own personal device, however a remote repository is in the cloud/a separate server (like GitHub) that is accessible over a network. 
# 4. Version Control: Version control is a system that records and tracks file changes over time so that users can track a file's history.
# 5. Staging Area: The staging area exists in a step of committing your local repository to the remote repository where git allows you to view your changes before committing them to your remote repository.
# 6. git add: This command will add all files in your folder (local repository) to a staging area that notifies you of all the changes you've uploaded.
# 7. git commit: This command will upload the files to your local repository, alongside a message that you add.
# 8. git push: This command now pushes your changes to your remote repository in GitHub.
# 9. git status: This command tells you how many unsaved changes you have in your working directory and what they are.
# 10. git pull: This command allows you to retrieve information from a remote repository that exists in Github.
# 11. pwd: This command tells you your current file path on your terminal.
# 12. ls: This command prints a list of the files in the working directory you're in on terminal.
# 13. cd: This command allows you to move backwards in your folder list on terminal, if you were to say "cd" you'd go back to the very first directory but "cd .." moves back one branch.
# 14. nano: This command opens up a python code option in terminal for the specific file you're working in.
# 15. touch: Touch will create and open a new file in the current branch you're in on your directory tree.
# 16. mv: Mv can move files from one location to another and rename them.
# 17. rm: Rm will delete a file you name.
# 18. cat: Cat can read files of text and print them directly onto your terminal.

# - 3.2 A Directory Tree -
# You have been plopped into Judy’s directory system. What command will tell you what your current working directory is?
# I would call pwd in order to see the directory path she's in.

# The terminal responds by saying you are in ∼/python decal/judy decal. What command will list all the files in your current working directory?
# I would call ls to see the list of files.

# Oh no! Brianna just sent out an announcement saying that there was a typo in homework.py.
# You will need to pull the brianna repo repository to find the updated file. What command(s) will let you move to the correct repository and pull the latest changes?
# I would first change my working directory to Brianna's, by running "cd .." then "cd brianna_repo".
# From here, I could call git pull to pull down the newly changed homework.py from Brianna's remote repository to my local repository. 

# How would you move this new homework.py to the homework/ folder in your personal repository?
# I could use the cp command, calling cp homework.py /Users/directory/path/topersonalrepository.

# How would you move yourself to the same repository as homework.py?
# I can move to it by calling cd .. then cd brianna_repo.

# You want to see the contents of homework.py in your terminal, how would you do this?
# I would call nano homework.py to see the contents of homework.py.

# Great job! You just finished the homework for this week. What command(s) allow you to save the changes and push from your local repository to your remote repository?
# I would first call git add ., to add my changes to my staging area, then git commit -m "my message" to save them to my local repository. After, I can run git push to push all of my files from my local repo to my remote repo.

# Oh no! Git gave you the following error. What commands should you call to resolve this error and push your homework properly? What does the error mean? (i.e. what did “Judy” do wrong when trying to push?)
# I (Judy) likely had commits in my remote branch that my local branch didn't, so I should call git pull to sync up my local and remote repositories, then I could push my new changes.

# What absolute path will allow you to move to Recents/?
# Using the path ~/Recent after calling cd to move back to the main working directory would be the absolute path to run.

# -- Homework 3 Review --
# - 4.1 Data Types -
def checkDataType(x):
    return type(x).__name__
print(checkDataType("hi"))

# 4.2 Conditionals
def evenOrOdd(n):
    if n % 2 == 0:
        return 'Even'
    else:
        return 'Odd' 
print(evenOrOdd(4))

# -- Loops --
numbers = [1, 2, 3, 4, 5]
def sumWithLoop(numbers):
    total = 0
    for i in numbers:
        total += i
    return total
print(sumWithLoop(numbers)) 

# -- Homework 4 Review --
# 6.1 Lists
actual = ['a', 'b', 'c']
def duplicatelist(actual):
    emptyList = []
    for i in actual:
        print(i)
        emptyList.append(i)
        emptyList.append(i)
    return emptyList
print(duplicatelist(actual))

# 6.2 Debugging
def square(num): # The original function didn't add the colon after defining the function, originally giving an error "invalid syntax"
    return num * num
print(square(6))

