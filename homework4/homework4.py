# -- Lists --
# 3.1 List Operations
fav_foods = ['ice cream', 'goldfish', 'malatang', 'pickles', 'ramen']
print(fav_foods[0])
print(fav_foods[-1])
fav_foods.append('rice')
fav_foods.insert(0, 'apple')
print(fav_foods)

del fav_foods[2]
len(fav_foods)
print(fav_foods)

for food in fav_foods:
    str_foods = str(fav_foods)
    food = str_foods.upper() # didn't make fav_foods a string, so the for loop wouldn't run
    print(food)
# I encountered this error: AttributeError: 'list' object has no attribute 'upper'
# I solved it by making my list, fav_foods, into a string, which allows the command .upper() to work.

real_fav_foods = [fav_foods[1], fav_foods[-1]]
print(real_fav_foods)

# I encountered this error, TypeError: 'list' object is not callable.
# I realized that it meant I was supposed to use [] instead of () when indexing from a list.

if "potato" in real_fav_foods:
    print("A potato!")
else:
    print("No potato!")

# 3.2 Slicing and Striding
numbers = list(range(0, 21, 1))
n = 15
for get_first_15 in numbers:
    get_first_15 = numbers[:n]
    for get_every_5th in get_first_15:
        get_every_5th = get_first_15[0:15:5]
        for reverse_and_stride in get_every_5th:
            reverse_and_stride = get_every_5th[::-1], get_every_5th[0:4:3]
print(get_first_15)
print(get_every_5th)
print(reverse_and_stride)

# 3.3 Nested Lists
num = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# 3.3.1 Nested List Operations
print(num[1])
print(num[1],[1])
num.append([10, 11, 12])
print(num)
def sum_nested(nested_list):
    total = 0
    for row in nested_list:
        for num in row: 
            total += num
    return total
print(sum_nested(num))

# 3.4 Create a 5x5 List
def create_grid():
    grid = []
    num = 1
    for i in range(5):
        row = []
        for j in range(5):
            row.append(num)
            num += 1
        grid.append(row)
    return grid

grid = create_grid()
print(grid)

def replace_multiples(grid):
    new_grid = []
    for row in grid:
        new_row = []
        for num in row:
            new_row.append("?" if num % 3 == 0 else num)
        new_grid.append(new_row)
    return new_grid

updated_grid = replace_multiples(grid)
print(updated_grid)

def sum_numbers(grid):
    total = 0
    for row in grid:
        for num in row:
            if num != "?":
                total += num
    return total

result = sum_numbers(updated_grid)
print(result)

# -- Dictionaries --
# 4.1 Dictionary Operations
ages = {
"Katie": 30,
"Mariam": 42,
"Safia": 25,
"Mira": 48
}
print(ages["Katie"])

ages["Mira"] = 100
print(ages["Mira"])

ages.update({"Milana": 52}) 
# I got the error, "AttributeError: 'dict' object has no attribute 'append'", when trying to append the dict. like you do lists.
# I fixed it by changing the .append() to .update(), which is how you actually add new keys to dictionaries.
print(ages["Milana"])

del ages["Mariam"]
print(ages)

for people, age in ages.items():
    print(f"Their name is {people} and they are {age} years old.")
