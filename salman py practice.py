#Print a simple message
print("hello, world")

#Print multiple item in one statement
print("Name:SALMAN, Age:20, City:Nowshera")

#print multiple line using escape sequence
print("Welcome to python! \nLet's learn coding to code")

#Print quotes inside a code string
print("He said:, \"Python is amazing!\"")

#Print star pattern
for i in range(1,6):
   for j in range(i):
      print("*",end=" ")
   print()

#Formatted string output using f-format
name="SALMAN"
Age=20
print(f"My name is {name} And {Age} years old.")

#Print a  5x5 multiplication table
for num in range(1,6):
    print(num,"*",num,"=",num*num)
    num+=1

#Align text with padding
name1="Apple"
name2="Banana"
name3="Cherry"
print(name1.ljust(10),name2.ljust(10),name3.ljust(10))
#OR
print(f"{name1:<10} {name2:<10} {name3:<10}")

#Output the result od simple calculation
print(7+5)

#Print a formatted receipt
Item_name,Quantity,Price="kiwi",5,50
Total=Quantity*Price
print(f"Item_name:{Item_name} \nQuantity:{Quantity} \nPrice:{Price} \nTotal:{Total}") 

#Print a list of some common Python Keywords(manually type)
list=["if","else","elif","for","while","in","is","and","or","continue"]
print(list)

#Print three keywords used for conditional statement
list=["if","else","elif"]
print(list)

#Print three keywords use in loop
list=["loop","while","break"]
print(list)

#Print the boolean keywords in python
list=["true","false","and","or","not","is"]
print(list)

#Print five keyword and sortthem alphabetically
list=["elif","else","for","if","is","while"]
print(list)

#Print the keyword that represent the constant values
list=["true","false","none"]
print(list)

#Print keywordsused for flow control
list=["break","continue","pass"]
print(list)

#Create a print statement that used the word 'if'as the part of the text
print("The keyword 'if' is used to check the condition")

#Print all the capital letter version of 5 keywords
keywords="if,while,for,def,else"
print(keywords.upper())

#Make a list(manually) of 10 python keywords and print it
list=["if","else","elif","for","while","in","is","and","or","continue"]
print(list)

#print 5 keywords that cannot be used as variable name
list=["if","else","elif","for","while",]
print(list)

#Print a sentence that uses3 keywords
print("Python uses if,else and for to control the flow of code")

#Group and print keywords into 3 category
print("Conditional:if,else,elif\nlooping:for,while\nboolean:true,false,and,or,not,is")

#write a short explanation (using print) of why we can't use keywords as variable names
print("We can't use python keywords as variable names because it create conflict for compile either it is variable or keyword")

#Take the user name as input and print a welcome message
name=input("Enter your name:")
print("Hello,",name)

#Take two number as input and ptint their sum
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
sum=num1+num2
print("The sum is:",sum)

#Ask the user for the favourite color and print it
Favourite_color=input("Enter your favourite color:")
print(f"Your favourite color is {Favourite_color}")

#Take the user age and print
Age=int(input("What is your age:"))
print("Your Age is",Age)

#Ask the user for their city and countrythen print it
City=input("Enter your city name:")
Country=input("Enter your country name:")
print(f"You live in {City}, {Country}")

#Take two number as input and print their difference
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
difference=num1-num2
print("The differnece is:",difference)

#Take a word as input and print it in upper case
name=input("Enter your name:")
print("Your name is:",name.upper())

#Take a sentence from user and print how many character it has
advice=input("Give an advice:")
character=len(advice)
print(f"It has {character} character.")

#Take your school name as input and print a message
school_name=input("Enetr your school name:")
print("I study at",school_name)

#Take the user's first name and last name nd print the full name
first_name=input("Enter your first name:")
second_name=input("Enter your second name:")
Full_name=first_name+second_name
print("Your full name:",Full_name)

#Take the user age and print how old they will be five years
Age=int(input("Enter your age:"))
print("Your age after 5 years:",Age+5)

#Ask the user for two number and print their product
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
product=num1*num2
print("The product is:",product)

#Take a hobby and name from the user and print a sentence
name=input("Enter your name:")
hobby=input("Enter your hobby:")
print(f"{name} likes {hobby}.")

#Convert a string "10" into int and add five to it
str="10"
int=int(str)
int+=5
print(int)
#OR
Result=int("10")+5
print(Result)

#Take a float as string and convert it into float
str_name="7.5"
float=float(str_name)
print(float)

#Convert an integer 5 into string and print the sentence using 5 and cocatenation
num=5
str=str(num)
print("The number is "+str)

#Convert the float 3.14 into string and print the result
float=3.14
str_name=str(float)
print(str_name)

#Convert an integer 1 to boolean and print the result
int=1
bool=bool(int)
print(bool)

#Convert string "false" to boolean.What happen! 
str="false"
name=bool(str)
print(name)  #it return true because bool() return true for all non empty string

#Take a number from user as string and convert to integer and multiply by 2
str=input("Enter the number:")
int=int(str)
int*=2
print(int)

#Take a floating point number from user, convert it into integer,and print both
num=float(input("Enter the number:"))
int=int(num)
print("Float:",num,"int:",int) 

#Convert a number into string and check the type using type().
num=5
str=str(num)
print(type(str))

#Take two number from the user and add them as integer not string
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
sum=num1+num2
print("The sum is:",sum)

#Take a string input like 3.2 and convert into float and int and print both
string="3.2"
float=float(string)
int=int(string)
print("Float:",float) #string can't be converted into int

#Convert a string like "123abc" into string and what error do you get
string="123abc"
int=int(string)
print(int) #string can't be converted into int

#Take a string input and check is it numeric if yes convert to int
string=input("Enter a string:")
check=string.isnumeric()
print("The string is numeric ",check)
num=int(string)
print(num)
print(type(num)) #numeric string can be converted

#convert a float into int and then string and print each step
float=9.99
print(float)
print(type(float))
int=int(float)
print(int)
print(type(int))
str=str(int)
print(str)
print(type(str))

#Print string literal that say's "learning python is fun!"
string="Learning python is fun!"
print(string)

#Create and print an integer literal and float literal
integer=5
float=4.5
print("Integer:",integer," float:",float ,sep="")

#Create a string using single quote and double quote and print both
string1='shah'
string2="rukh"
print(string1+string2)

#Create boolean literal and print it
condition1=True
condition2=False
print(condition1)
print(condition2)

#Create a variable with the value none and print it
a=None
print(a)

#Print the type of some literal
print(type("hello"))
print(type(10))
print(type(10.5))
print(type(True))
print(type(None))

#Use a string literal to print a simple sentence
print("Python's simplicity is powerful")

#Use string concatenation to join two string literal and print the result
string1='SALMAN '
string2="AHMAD"
print(string1+string2)

#Create a list of mixed literal and print it
list=["SALMAN",22,True]
print(list)

#Print a multi line string using triple quote
print("""Hey 
I am SALMAN 
20 years old""")

#What is the output
print(None==0) and print|(None==False) #None represent the absence of value therefore it's not equal to either 0 or false
