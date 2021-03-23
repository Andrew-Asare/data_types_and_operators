# Introduction to Python Data Types and Operators

- Strings
- Numbers Integers, floats, longs
- Boolean (True or False)
### Arithmetic Operators
### Comparison Operators

- Arithmetic Operators

```python
+, -, *, /
```

- Modulus
```python
%
```
It gives the remainder of the 2 numbers

- Comparison Operators 
-`>` greater than
 - `<` less than
 - `>=` greater than equal to 
   -`<=` less than equal to 
   -`==` equals
   -`!=` not equal to
   
##indexing in Python starts from 0
-  H e l l o   w o r l d !
-  0 1 2 3 4 5 6 7 8 9 10 11


## Reverse Indexing
-  H   E   L  L  0  W  O  R L   D  !
- -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1

### Let's have a look at some string methods
```python
greetings = "Hello World!"
print(greetings[0:5])
print(greetings[6:11])
print(greetings[-6:])

```
### Concatination

- Here is an example of concatination adding both variables together
```python
first_name = "Ben"
last_name = "Jerry"
print(first_name + " "  + last_name)
```

### A Useful formating tool!

- Using f{} we can format and concat variables
```python
print(f"Your first name is {first_name} and your last name is {last_name} is {age} old")

```
- If first name was Ben, last name was Jerry and age was 99 the output would be
`Your first name is Ben and your last name is Jerry and your age is 99
`
