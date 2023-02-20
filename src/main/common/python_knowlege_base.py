import random
#Important info: in python you start counting from 0

#1. Data types (variables)
#Strings
String = "Hello world" #Strings (str) store letters and words
Integer = 1.999999999 #Integers (int) store numbers which can also be used for mathematical operations
Boolean = True #Booleans (bool) store a value that has to be "True" or "False"
Array = ["String", 3, True] #An array stores different datataypes

#2. The basics
#printing Strings
print("Hello World") #Prints "Hello World to the console"
print(String) #Prints "Hello World" which has been defined in the String called "String"

#You can also add two Strings together
String2 = "My name is funny"
print(String + String2)
print(String2 + "Right?") #We can also combine a string and a regular text

#Printing Integers (int)
print(1.999999999) #Prints 1.999999999 to the console
print(Integer) #Prints the value that has been assigned to the integer called "Integer" to the console

#maths
print(3+1) #This will output the result of this addition
print(Integer + 1) #It works with Integers as well!
print(Integer - 1) #subtraction
print(Integer * 1) #multiplication
print(Integer % 1) #division

math = 4 - 1 #you can also use integers to solve math problems
print(math)

#Printing Booleans
print(True) #This will output the value "True"
print(Boolean) #This will output the value assigned to it (in this case "True" this makes it more dynamic than simply printing a certain value)
print(5 < Integer) #You can also output a boolean when comparing different values with "<", ">" or "=". Here the program checks if 5 is smaller than "Integer" (1.999999999) and outputs the result (in this case "False")

#Printing Arrays
print(Array[0]) #This will print the first array entry
print(Array[1]) #This will print the second array entry
print(Array[2]) #This will print the third array entry

#3. if statements (logical operators)
a = 1
b = 2 #Declaring some variables

if a < b: #This will only print a message to the terminal if the conditions are fullfilled. In this case the program will only execute successfully if int "a" is smaller than int "b"
    print("a is smaller than b") #prints if the condition is met

if a < b and b > a: #now both conditions connected with "and" need to be fullfilled for this to execute
    print("a indeed is smaller than b")

if a < b or a > b:  #now one of the conditions needs to be fullfilled for this to execute (due to the "or")
    print("a is smaller than b OR a is bigger than b")


if a < b:   #If the conditions are not fullfilled this statement will now prints something ELSE to the terminal
    print("a is smaller than b")
else:       #In this case the else will never print because the conditions of the first if statement are always fullfilled
    print("a is bigger than b") #Remember that you can only use one "else" per if statement

if a < b:   #If the conditions are not fullfilled the program will check if the second conditions mentioned in the elif (short for else if) statement are fullfilled. If these arent fullfilled either the project will output the something ELSE
    print("a is smaller than b")
elif a > b: #Cannot be fullfilled because a is always smaller than b (not dynamic)
    print("a is bigger than b")
else:       #Cannot be fullfilled because a is always smaller than b (not dynamic)
    print("something else is true")

c = 3
d = 4

if a < b: #Instead of using "and" you can also put two if statements inside of each other. But remember it is a very unelegant way of utilizing multiple conditions
    if c < d: 
        print("Both conditions are met") 

#4. Input
#After looking at how to output code, we will take a look at a simple way to read user input
question1 = input("What is your name?") #This will print a string and wait for user input (the input is a string by default so booleans and ints will be ignored). As soon as the user has typed his answer into the terminal and has pressed "Enter", the information will be stored and printed out in the next line
print("Hello " + question1) #This will output the stored input

#3. negative and positive if statements
#if the input is "t" prints out "Your name is t"
if question1 is "t": #the "is" can be replaced with "==" as well
    print("Your name is t")
else:
    print("Your name is not t")
    
#Weird way to check for integers
#if the input is "0" prints out "Your name is 0"
if question1 == "0": #the "==" can be replaced with "is" as well
    print("Your name is 0")
else:
    print("Your name is not 0")

#Inputs that accept different values
question2 = input("How old are you? ") #Prints out "How old are you?" and waits for user input
question2 = int(question2) #Converts the input into an integer (allows for better mathematical interaction)

question2 = input("How old are you? ") #Prints out "How old are you?" and waits for user input
question2 = bool(question2) #Converts the input into an integer (allows for better mathematical interaction)

question2 = input("How old are you? ") #Prints out "How old are you?" and waits for user input
question2 = (question2) #Converts the input into an integer (allows for better mathematical interaction)

#While loops
#while(True):    #This will infinetly print because the value always is "True"
#    print("it never stops...")

#while(a < b):   #This wont stop either because a always is smaller than b. That means the output boolean is always "True"
#    print("it does not stop either")

#5. for loops (me is too dumb to figure this out...)
for i in Array: #prints an entire array. I dont understand this pls help
    print(i)

