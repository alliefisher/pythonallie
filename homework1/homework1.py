# File: homework1.py
# --- Variables and Data Types ---
a = 10 
print(a)
print(type(a)) # integer, a whole number

b = 1.5
print(b)
print(type(b)) # float, a decimal

c = 3j
print(c)
print(type(c)) # complex, has both a real and imaginary part

d = "hello"
print(d)
print(type(d)) # string, words or text

e = [1, 2, 3]
print(e)
print(type(e)) # list, an array of any type of item inside

f = {"name": "Ellen", "favorite fruit": "strawberry"} 
print(f)
print(type(f)) # dictionary, similar to list but it stores values in key:value pairs

g = (1, 2)
print(g)
print(type(g)) # tuple, method of storing multiple items in a single variable and can't be changed after creation

h = ["apple", "banana", "strawberry"]
print(h)
print(type(h)) # list

i = True
print(i)
print(type(i)) # boolean

j = None
print(j)
print(type(j)) # none type, represents the absence of a value/null value

k = [True, "blue", 12]
print(k)
print(type(k)) # list, an array of any type of item inside

l = str(14)
print(l)
print(type(l)) # string, words or text

m = 1e4
print(m)
print(type(m)) # float, fraction/decimal/exponent

# 1) I found 9 different types!
# 2) The data types I found were integer, float, complex, string, list, dictionary, tuple, boolean, and none type.
# 3) m & b are both floats, l and d are both strings, and e, h, and k are all lists.
# 4) The data type of l was a string because it had the command str() around 14. str() converts any value into a string.
# 5) The data type I choose is range!

z = range(7)
print(z)
print(type(z)) # range, creates a sequence of numbers that starts at 0 and goes up by 1, then stops before the specified number

# --- Booleans ---
print(10 > 9) # True, 10 is greather than 9
print(10 == 9) #False, 10 is not equal to 9
print(10<=9) #False, 10 is not less than or equal to 9
bool("abc") # True, not an empty string so it's true
bool(123) # True, not 0 so it's true
bool(["apple", "cherry'", "banana"]) # True, not an empty list so it's true
bool(True) # True because it is true
bool(False) # False because it just says false
bool(0) # False because 0 in a boolean is considered false
bool("") # False because an empty string returns a false boolean value
bool(" ") # True because it's no longer an empty string
bool(()) # False because it's an empty tuple
bool([]) # False because it's an empty list
bool({}) # False because it's an empty dictionary
bool(True and False) # False because one of the values say false
bool(True and True) # True because both values are true
bool(False and False) # False, both values are false
bool(True or False) # True, one of the values is true
bool(True or True) # True, both values are true
bool(False or False) # False, both values are false
bool(not(False)) # True, because using the command not() gives the opposite boolean value
bool(not(True)) # False, because using not() gave the opposite of true

# 1) I noticed the pattern that majority of the boolean values depend on if it's an empty string or if an integer is 0. Otherwise, it was logical operations that determined the boolean value.
# 2) I was surprised that empty lists/strings return false.
bool(2*9==18) # True, because 2*9 = 18 which is what the expression says 
bool(2<1 and 6<7) # False, although 6 is less than 7, 2 is not less than 1

# --- Operators ---
10 + 5 # 15, adds numbers together
10 - 5 # 5, subtracts numbers
2 * 4 # 8, multiplies numbers
6 / 3 # 2.0, divides numbers
5 % 2 # 1, called a modulus & gives the remainder from division
3 ** 2 # 9, exponentiation
15 // 2 # 7, floor division that divides and always returns an integer
5 == 2 # False, checked if 5 & 2 are equal to each other
10 != 10 # False, checked if 10 is not equal to 10
2 < 5 # True, < does less than comparison
12 > 5 # True, > does greater than comparison
5 <=6 # True, <= does less than or equal to comparison
1 >= 10 # False, >= does greater than or equal to comparison

x = 5
x += 5 # += adds the value on the right to the variable on the left
x -= 4 # -= subtractes the value on the right from the variable on the left
x *= 3 # *= multiplies the variable on the left by the value on the right

# - Logical Operators -
# 1) The operator and is used to combine two boolean expression and returns true only if both expressions are true, otherwise it only returns false.
    # Results in true: True and True
    # Results in false: True and False
# 2) The operator or is used to combine two boolean expressions and returns true if at least one of the expressions is true, only returning false if both expressions are false.
    # Results in true: True or False
    # Results in false: False or False
# 3) The operator not reverses the boolean expression it surrounds.
    # Results in true: not(False)
    # Results in false: not(True)

# -- More Questions -
# 1) The difference between / and // is that / is pure division, while // returns the a rounded integer value from division.
# 2) The difference between % and // is that % returns the remainder from division, while // returns the rounded integer value from division.
# 3) I would use % to calculate the remainder. For example, 6 % 4 would return 2.
# 4) Assignment operators assign a value from the right side of an expression to the variable on the left side.

# --- Strings ---
my_string = "hello"
print(my_string) # prints: hello
print(my_string[0]) # prints: h
print(my_string[1]) # prints: e
print(my_string[2]) # prints: l
print(my_string[3]) # prints: l
print(my_string[4]) # prints: o
print(my_string[-1]) # prints: o
print(my_string[1:3]) # prints: el
print(my_string[0:5:2]) # prints: hlo
print(len(my_string)) # prints: 5
print(my_string+"goodbye") # prints: hellogoodbye
print(my_string*7) # prints: hellohellohellohellohellohellohello

# - 3.4.1 Questions -
# 1) Slicing is a way to extract specific parts of a string with the notation of [start:stop:step].
# 2)
name = "Oski"
print("Hello my name is", name) # prints: Hello my name is Oski
# 3)
name = "Oski"
print(f"Hello my name is {name}") # prints: Hello my name is Oski
# 4) The second method using f-strings is an easier way to insert variables into strings, due to it being very legible.

# -- Terminal Commands --
# 1) cd
# changes directories, used to move from one folder to another
# example: cd Documents

# 2) ls
# lists files and folders in the current directory
# example: ls

# 3) ls -a
# lists all files, including hidden ones
# example: ls -a

# 4) mkdir
# used to make new direcotories/folders
# example: mkdir New_Folder

# 5) cat
# prints out the contents of a file
# example: cat datatypes.py

# 6) pwd
# prints the current folder you're working in
# example: pwd

# 7) cd ..
# allows you to move up one directory level
# example: cd ..

# 8) cd .
# keeps you in the same directory
# cxample: cd .

# 9) cd ~
# moves you to your home directory
# example: cd ~

# 10) cp
# copies files or folders from one location to another
# example: cp chem.txt physics.txt

# 11) mv
# moves/renames files or folders
# example: mv old_name.txt new_name.txt

# 12) rm
# removes files/directories/folders PERMANENTLY
# example: rm old_name.txt

# 13) clear
# clears the terminal screen
# example: clear

# 14) grep
# searches for specific text inside files
# example: grep "hello" old_name.txt

# - Questions -
# 1) 3 commands not present in the list are: tac, comm, and useradd.
#       tac is the opposite of cat, displaying file content in reverse order.
#       comm compares two files, showing three columns: lines unique to the first file, lines unique to the second file, and lines common to both files.
#       useradd is used to add a new user to the Linux system
# 2) The difference between ls and ls -a is that ls lists the files in the current directory while ls -a lists all files, including hidden ones.
# 3) A hidden file is a file that starts with a period (.) and is not normally visible when listing files in a directory.
# 4) 3 other flags are -l, -r, and -f. 
#     -l is used with ls to displace files in a long format.
#     -r can be used to copy a director with cp. -r can also remove a directory if you use it with rm. 
#     -f (when used with fail filename.txt) prints the last lines of a file whenever it changes.