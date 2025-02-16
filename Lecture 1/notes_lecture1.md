# Lecture 1 Hello World

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
