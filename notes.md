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
# Lecture 3 Lists, Loops, and Ifs

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

## Loops
- Loops can execute a block of code repeatedly