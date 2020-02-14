# Coding with Latin!

Today you will be coding an interactive adventure in Latin.  Your code will be in English, but the input prompts will be composed in Latin.  If you are confused already, that's ok!  These instructions and this guide will help.

Here are some common Python commands you will be able to use and identify in the code:

\#
When a # is used in Python, it indicates that there is a comment in the code.  A comment can be any words or instructions.  When a computer runs code, it ignores the comments.  They are usually input by the programmer to help explain their code.

### def
"def" introduces or "defines" a function.  A function is a command that contains special instructions.  The instructions for each function is indented under the "def" line and always follow a ":" character.

The function doesnʻt do anything until you call it.  The function is called by writing its name followed by the "()" - without "def" or anything else written before it.

```#defining a function
def hello():
	print("salve!")

#calling a function - which will actually print "salve!"
hello()
```

### variable
adventure =...
"adventure" is a variable.  It is set equal to an input command.  Variables can be set equal to numbers, or strings (letters or numbers contained by quotation marks), or Boolean values (the words True or False).  Here adventure is set equal to the response to the Input command.

```#different variables
#number
a=0

#string
b="uxor"

#boolean value
c=True
```

### input
So, you are probably wondering what an input command does!  It prints a statement that returns whatever is typed as the response back to the code.

For example:
```
#set the variable a equal to what someone types as their name
a = input("type your name:")

#now print a message followed by the value of the variable, a.
print("Salve, " + a)
```

### if, elif, else
These are examples of conditional statements.  They follow the logic you would expect in any language.  If something is true, do this, or if this is true, do this, otherwise, do this.

If statements, like functions are followed by the ":" character.  This lets the computer know that instructions or coding is following.  It too must be indented.

The "==" we would express in English as "equals;" instead of assigning a value to a variable, which uses the single "=," however, it tests for whether a statement is True or False, its Boolean value.

```
#put forth our condition
if(a=="Magister B"):

#indent and type our instructions 
	print("O, tu es senex!")

#now put forth a second condition
elif(a=="Clara"):
	print("tu es discipula bona!")

#now the response if the first two fail the condition test
else:
	print("ego sum laetus, quod tu ades!")

```

### In the code you will be editing, 
1. The functions are defined in a list beginning at the top of the file.
2. The last line of code calls the first function and "runs" the program.
3. Within each function, conditions test for responses.  
4. If the test succeeds, it calls a new function.  
5. If it fails, it calls a different function.

### Your own code:
1. Edit the existing strings (words withing quotation marks) by changing the English sentences into Latin. 
2. Add or delete functions, edit and add more if, elif, and else statements, etc. 
3. Extend the code and make it more flexible by adding:

-- variable.lower()  
```
adventure = input("Do you want...").lower()
```
  -- is in
```
if "y" is in adventure:
```
4. Ask if you need help!
