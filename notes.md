# Lecture 1 and 2 Hello World

## Objects
1. Integar: 3
2. Float: 3.0
3. Boolean: True/False, 1/0
4. String: "Apple"

## Functions
1. Operators: + - * / ** _(power)_ // _(only integar)_ % _(reminder)_
2. Coveret betweeen data types
3. String functions

## Indexing
```
" H e l l o   W o r l d "
  0 1 2 3 4 5 6 7 8 9 10
"Hello World"[0]
H
"Hello World"[7]
o
"Hello World"[1:5]
ello #Stop at [4]
```

## np.exp() / np.log function
```
import numpy as np #import the package numpy
np.exp(1)
np.float(2.718)
np.log(2.718) #inverse of expotential
np.float(0.999)
```
Use to find the expotential function and inverse expotential function

## Comparison operators
1. #> : bigger than
2. < : smaller than
3. #>= : bigger than and equal
4. <= : smaller than and equal
5. == : equal or not
6. != : not equal or not

## Logical operators
1. and : both side must be true
2. or : only one side must be true
3. not : reverser for the operators

## Print function
```
print("Hello")
Hello
```
Used to print Hello on the output

## \n / \t functions
```
print("Hello World\nHow are you?")
Hello World
How are you?
```
Use to line break and tab spaces

## Operators with strings
```
print("Hello" + "World")
HelloWorld
print("Hello World "*4)
Hello World Hello World Hello World Hello World 
```
Arithemetic operators + and * works in print function _also work without print()_

## type() function
```
type(3)
int
```
Use to ask for the type of the function

## int() / float() / str() function
```
float(5)
5.0
```
Use to change the type of the function

## abs() / round() function
```
abs(-1)
1
round(5.02, 1)
5.0
```
Absolute the number and round down for the specfic decimal places _-1: round to the nearest tenth_

## len() function
```
len("Hello")
5
```
Use to count how many item

## .replace() functioin
```
hello = "Hello World"
hello.replace("H", "h")
"hello World"
```
Use to replace a specific term or characters

## .upper() / .lower() function
```
hello = "Hello World"
hello.upper()
HELLO WORLD
```
Use to capitalize or lower all the character

## Writing function
```
def hello(#could add arguments inside): #Define function name
    #Used to print hello #Usage of the function
    print("hello") #Action of the function
hello()
hello
```
Function can do something whenever it's called

## return in fuction
```
def area2(length = 5, width = 10):
    #This function takes a length and width of a rectangle and returns the area.
    answer = length * width
    return answer #Return the variable
area2
50
```
Return can return back any function or variable

# Recitation 1

## Data types
Common confusion: digit and number
- Digit: 0, 1, 2, 3, ...
- Number: written with one or more digit
- e.g.: 3 + 2 = 5, "3" + "2" = "32"

## Variables
- Variable is a pointer point to that memory

## Assigning values to variables
- Not require specifiy data type
- Data type is inferred by the value and can be overwritten

## Program flow
1. Unique: pass one by one
2. Divergent: make a judgement and decide the way
3. Loops: repetitions with known or unknown numbers

## range() function
```
range(start, stop, step)
```
- range(1, 3): cycle 2 times
- range(3): cycle 3 times

## for function
```
count = 0
for _ in range(3):
  count = count + 1
```
For loop used to repitation for known number of times

## while function
```
count = 0
while count > 4:
  count = count + 1
```
While loop used to repitation for unknown number of times until specific requirement meet

## read / write function
```
file = open("amount.txt", "r") #used to read the file
file = open("amount.txt", "w") #used to write the file from start
file = open("amount.txt", "a") # used to add data after the end of the file
```
# Lecture 3 Lists, Loops, Ifs, Dictionaries and Files

## Lists
```
list = [1, "2", 3.0, [4]]
```
- Collection of objects kept in a strict order
- Order matters
- List can contain mixed data type
- Nested list: list within a list

## Array
```
import array as arr
arr.array(type, [item])
```
- Array need to be the same data type
- Elements are contiguous memeory location allowing easy modification

## Different between List and Array
![alt text](https://github.com/21104988d/AF3214/blob/main/Lecture%203/list%20vs%20array.png)

## .sort()
```
list = [3, 2, 1, 4]
list.sort()
[1, 2, 3, 4]
list.sort(reverse = True)
[4, 3, 2, 1]
```
- Sort the order for a list
- Setting resverse equal to True can sort for descending order

## .append()
```
list = ["a", "b", "c", "d"]
list.append("e")
["a", "b", "c", "d", "e"]
```
- Add a new item to the end of the list

## sum()
```
list = [1, 2, 3]
sum(list)
6
```
- Sum up all the item in the list
- Cannot sum up a list of strings

## Operators with list
- Comparison operators: == !=
- Arithmetic operators: + *
- #- and / not work in list

## min() / max() function
- Used to find the minimum and the maximum item in the list

## .mean() / .median() function
```
import statistics as s

list = [1, 2, 3]
mean = s.mean(list)
2
```
- Used to find the mean and the median of the list

## .join() function
```
list = ["a", "b", "c"]
",".join(list)
'a,b,c'
```
- Connect all the items in the list

## .split() function
```
line = "a,b,c,d,e"
list = line.split(",")
["a", "b", "c", "d", "e"]
```
- Seperate the item for the list

## Loops
- Loops can execute a block of code repeatedly

## for loops
```
list = [1, 2, 3, 4, 5]
for _ in list:
  print(_)
1
2
3
4
5
```
- Used to repeat for known multiple
- Temp variable should not use the name of the list

## if statements
```
a = 5
if a < 0:
  print("a is smaller than 0")
elif a > 5:
  print("a is bigger than 5")
else:
  print("a is between 0 and 5")
```
- Used to perform different action with different requirements

## try / except
```
test_scores = [90, 95, "absent", 100, 76]
bonus_scores = []
for score in test_scores:
    try:
        bonus_scores.append(score + 2)
    except:
        bonus_scores.append(score)
```
- Use when not sure whether all the item can run correctly

## in / not in 
```
"pie" in "pizza pie"
True
```
- Use to test specfic statement contain or not

## Dictionary
```
dict = {
  "a" #key: [1, 3] #value, 
  "b": [2, 4]
}
```
- Collection of {key: value} pairs
- Indexed by keys
- Compound data types

## Dicitionary Methods
![alt text](https://github.com/21104988d/AF3214/blob/main/Lecture%203/dictionary_method.png)

## Looping through a dictionary
```
dict = {
  "a": [1, 3], 
  "b": [2, 4]
}
for key in dict.keys():
  print(key)
a
b
for value in dict.values():
  print(value)
[1, 3]
[2, 4]
for key, value in dict.items():
  print(key)
  print(value)
a
[1, 3]
b
[2, 4]
```
- Can explicit to loop through keys and values

## Opening files
```
with open("file.txt", "r" #mode) as f #temp variable:
  save file as something else
  or save part of file
```
- File automatically closes when exit the indentation
- "r": read
- "w": write _(wipes the file clean and rewrite from zero)_
- "a": append _(add to the end of the file)_

## .read() / .readlines() function
```
with open(alice_filename, "r") as f:
    alice_text = f.read()
```
- .read(): Use to change the file object into a string
- .readlines(): Use to change the file object into a list by seperate each item by each line

## .write() function
```
with open(new_alice, "w") as f:
    for line in alice_list:
        if line != "\n":
            f.write(line)
```
- Use to write item into the file object

## .rstrip() function
```
with open(dog_file, "r") as f:
    for line in f.readlines():
        dog_list.append(line.rstrip("\n")) # .rstrip() returns a copy of the string with trailing characters removed
print(dog_list)
```
- Use to delete the specific charcter in the last of the string

# Recitation 2 Branching, Iterations, Strings, Functions, Lists, Dictionaries, Debugging, Testing, Exceptions

## Strings
- Letters, special characters, spaces, digits
- Enclose in quotation marks or signle quotes
- Concatenate strings
```
hi = "hello"
name = "me"
greet = hi + name
"hellome"
```

## INPUT/OUTPUT
- print()
- input()

## Comparison operators
- i > j
- i >= j
- i < j
- i <= j 
- i == j 
- i != j 

## Logic operators
- not abs
- a and back
- a or b

## Control flow
1. if statement
```
if <condition>:
  <expression>
elif <conditon>:
  <expression>
else:
  <expression>
```
2. while loop
```
while <condition>:
  <expression>
```
3. for loop
```
for <variable> in range (<num>):
  <expression>
```

## break statement
- Immediate exit whatever loop it is in
- Skip remaining expression
- Exits only innermost loop

## String
- Senquence of characters
- Can compare with ==, >, <
- len() is used to retrieve the length
- Square brackets _[]_ used to perform indexing
- Can slice using [start: stop: step] _(Step = 1 by default)_
- Immutable _(Cannot be modified)_

## Functions
- Resusable pieces / chunks of code
- Not run until "called"
- Function structure:
	1. Name
	2. Parameters
	3. Docstring
	4. Body
	5. Returns _(Return None, if no return given)_

## Scope
- Inside a function, can access a variable defined outside
- Inside a function, cannot modify a variable defined outside

## Lists
- Ordered sequence, can accessible by index
- Denoted by []
- List elements can contain mixed types
- Mutable _(list elements can be changed)_
- .append() to add elements
- .extend() to mutate list
- .remove() remove a specific element _(only once)_
- del() remove a specific index
- .pop() remove the end of the list and return the removed element
- list() covert string to a list by every character as an element
- .split() splist a string on a specfic character _(Split on spaces default)_
- "".join() turn a list of character into a string
- __sorted() sort the list but not modify the list and can store for a new value__
- __.sort() sort the list and modify and return None__
- .reverse() sort the list in descending order and modify
- __Aliases effect: change the list will let the object that refer to the list will also change__
- __Need to copy the list by lisy[:] will not change the list of object__
- __Change the object of the inner list will also change the outer list__

## Dictionary
1. Values
	- Any type
	- Can be deplicates
	- Values can be list
2. Keys
	- Must be unique
	- Immutable _Careful with float type as key_
3. No order to keys or values

## Testing approaches
1. Black box testing
	- Explore paths through specification
2. Glass box testing
	- Explore path through code

## Error messages
1. IndexError: access beyond the limit
2. TypeError: convert an inappropriate type
3. NameError: reference a non-existent variable
4. TypeError: mixing data types without appropriate coercion
5. SyntaxError: forget to close quotation


# Lecture 4 Pandas dataframes

## Series object
```
import pandas as pd
import numpy as np
pd.Series([1, 2, 3, 4], index = ['a', 'b', 'c', 'd'])
a		1
b		2
c		3
d		4
```
- One-dimensional labeled array of indexed data
- Can set the index number _(default start by 0)_
- Need to use double brackets for selecting two or more columns

## pd.DataFrame() function
```
dict = {'a': 1,
			'b': 2,
			'c': 3}
series1 = pd.Series(dict) #turn the dicitionary into a series
df = pd.DataFrame({'series1': series1}) #turn the series into a dataframe
a		1
b		2
c		3
dtype: int64
```
- Index of the series will turn into the index of dataframe
- Index will start from 0 when turning a list into dataframe
- .index: return the index of the dataframe
- .values: return the values of the dataframe
- .columns: return the column name of the dataframe
- .shape: return the structure of the dataframe _e.g. (3,1) for the example_
- .size: return the number of element in the dataframe
- .set_index('column', inplace = True): set the specific column into index and replace it
- .index.name = None: set the index name into none
- .reset_index(replace = True): reset the index start from 0 and keep the original index as column


## .iloc[] / .loc[] function
```
data = pd.Series([100, 200, 300, 400], index = [4, 3, 2, 1])
data.iloc[1]
np.int64(200) #result in the position
data.loc[1]
np.int64(400) #result in the index name
```
- .iloc[]: used to output the position
- .loc[]: used to output the index name _(Error if no setting index name)_
- df[['column1', 'column2']]['row1', 'row2']: index on specific row and column for the dataframe
- .loc[['row1', 'row2'], ['column1', 'column2']]: indicate the row first then the column
- __Indexing in iloc do not include the last variable, loc does include the last variable__

## .describe() function
![alt text}(https://github.com/21104988d/AF3214/blob/main/Lecture%204/IMG_0141.jpeg)
- Use to have a brief statistical numeric
	1. count
	2. mean
	3. std
	4. min
	5. 25%
	6. 50%
	7. 75%
	8. max

## .max() function
- Use to find the largest values of the specific column

## .nlargest() function
```
column_name.nlargest(num)
df.nlargest(num, column_name)
```
- Use to find the largest n item for the specific column

## Combining DataFrames
```
df_combine = pd.concat([df1, df2])
```
- pd.concat([df1, df2]): combine on the row
- pd.concat([df1, df2], axis = 1): combine on the column
```
pd.merge(df1, df2) #inner merge
pd.merge(df1, df2, how = 'outer') #outer merge
```
- Inner join: merge values contain in both dataframe
- Outer join: merge all the value and state NaN for null in columns

## pd.read_csv() function
- Load csv file into a dataframe

## .head() / .tail() / .sample function
- .head(num): first n row in dataframe _(default is 5)_
- .tail(num): last n row in dataframe _(default is 5)_
- .sample(num): random n row in dataframe _(default is 1)_

## .info() function
![alt text](https://github.com/21104988d/AF3214/blob/main/Lecture%204/info%20function.png)
- Use to result the column, number of column, null value and the column data

## Boolean return of a Dataframe
```
df[df[column] == 'num']
```
- Return the column which is equal to the 'num' values

## .rename() function
```
df.rename(columns = {'new_name': 'old_name'})
```

##.drop() function
```
df.drop(num)
df.drop(['column1'], axis = 1)
```
- Use the drop the specific row index or column name of the dataframe

## Data aggregation
- .count(): number of row
- .sum()
- .mean()
- .median()
- .min()
- .max()
- .unique()
- .std()
- .var()

## .groupby() function
```
df.groupby('column1')
```
- Use to group the values in a column to look at summary measures

## .sort_index() / .sort_values() function
```
df.sort_index() #sort the row ascending
df.sort_index(ascending = False) # sort the row descending
df.sort_index(axis = 1) # sort the column ascending
df.sort_index(axis = 1, ascending = False) # sort the column descending
df.sort_values(by = 'column1') # sort the specific column in row ascending
```

## .to_csv() function
```
df.to_csv(file) # save the dataframe to csv file
```

## .plot() function
```
df.plot(kind = graph, x = x_variable, y = y_variable)
```
- Use the plot the scatter, bar, line plt, etc

## Seasborn
```
import seaborn as sns
sns.lineplot(x = x_variable, y = y_variable, data = df, hue = column)
sns.scatterplot()
sns.barplot()
```
- Use to plot different graph by different column as x and y variable on the dataframe
- Seperate through different variable by hue parameter

## dt.month function
```
df[column1].dt.month # use to turns into month variable where January = 1
```

# Lecture 5 Introduction to Database Systems

## Data Models
- Data model is data in a database
- Schema is a particular collection of data

## Relational model
- Avoid cost of having to maintain the overhead
	- Store database in simple data structure
	- Physical storage left up to the DBMS implementation
	- Access data through high-level language
- Three components
	1. Structure: database's table and independent of their physical representation
	2. Integrity: ensure database's contents satisfy constraints
	3. Manipulation: programming interface for accessing and modifying a database
- DBMS can auto-generate unique primary key via identity column
- Foreign key specifies attribute one relation maps to another relation

## Relational Algebra
1. \sigma (SELECT)
	- Choose a subset from a table
	- e.g. \sigma<sub>a_id = 'a2'</sub> (R)
	- From Table R, select a_id column, where value equal to a2
2. \Pi (PROJECTION)
	- Define the output should look like
	- e.g. \Phi<sub>b_id - 100, a_id</sub>(\sigma<sub>a_id = 'a'</sub>(R))




















