

# to make a variable
# name = value

# Examples:

score = 0
# creates a score variable and sets it to 0

answer = "apples"
# creates a answer variable and sets it to the string "apples"
# remember that variables can store any value
# but if you make a variable a string
# you shouldn't make it a number later or vice versa

score += 2
score = score + 2
# you can change variables too, these are both ways to change score by 1 (they work the exact same way most of the time)
score -= 2
# this lowers score by 2
score = score * 2
# this multiplies score by 2
score = 0
# lets set score back to 0 for now

# to print a string to the user
# print(string)
# keep in mind that strings need quotation marks around them

# examples:

print("Hello User!")
# tells the user hello

print("The answer is "+answer)
# the above code prints "The answer is apples"
# you can put strings together
# the variable answer is currently set to "apples"

print(score)
# prints the value of score
# even though score is a number it can figure out to print "0"



# how to make an array
# name = [item1, item2, item3, ...]
# arrays are variables that hold lists of values rather than just 1
# you can make an array of numbers, strings, or other things

# examples:

choices = ["apples","oranges","lemons","limes"]
# creats a list of fruit
# I can use this as a list of choices for our quiz question

primes = [1,2,3,5,7,11,13,17,19,23,29]
# creats a list of numbers, I put in the prime numbers under 30
print(primes[5])
# prints the 6th item in primes
# why 6th and not 5th? because computers start counting at 0
# so the first item is actually item number 0



# how to get user input
# varname = input(prompt)
# to get user input you actually have to make a variable
# you can also use an existing variable
# but instead of setting the variable to a value
# you use the input() command to let the use choose the value

# examples:

userAns = input("which of the following is not like the rest: "+ choices[0]+", "+choices[1]+", "+choices[2]+", or "+choices[3]+"?")
# this asks the user "which of the following is not like the rest: apples, oranges, lemons, or limes?"
# the user's response is then put into a variable called userAns
# remember that users can input ANYTHING
# so you have to make sure their answer is valid



# how to make a while loop
# while condition:
#       code to repeat as long as condition is true
#       it is important that this code is tabbed correctly
#       this is how python knows what code should be repeated
# and what code should be run after the while loop finishes

# examples

while score < 10:
    score += 1
    print(score)
score = 0
# this checks if score is less than 10, it is right now (we set it to 0 when we made it)
# it then increases score by one and prints the value of score
# then it goes to the beginning and checks if score is still less than 10
# once it repeats enough for the condition (score < 10) to no longer be true
# it sets score to 0

while score < 10:
    score += 1
print(score)
score = 0
# to show how indentation works, this is the same program except the print() function is no longer tabbed
# now the print function no longer happens inside the loop, it happens after the loop
# instead of printing the numbers 1-10 this program only prints 10

#while score == 0:
#    print(score)
# there is a reason I commented this code out
# this while loop never ends
# score is equal to 0 at the start
# and that never changes inside the loop
# this will crash the program
# don't do this


# how to make an if statement
# if condition:
#     code to execute if condition is true
# indentation is still important
# there is another useful addon to if statements
# else statements allow you to have code that executes if the condition is not true
# that would look like this:
# if condition:
#     code to execute if condition is true
#  else:
#     code to execute if condition is not true

# examples:

if str.lower(userAns) in choices:
    print("you answered "+str.lower(userAns))
else:
    print("your answer is invalid.")
# this checks if the users answer to our previous question was one of the choices that we gave them
# if it is, we tell them what they aswered
# if it isn't we tell them that they failed
# rather than telling them that they failed, it would be better to let them try again
# I'll let you figure out how to do that yourself (hint: whiles loops and variables are handy)
# wait
# I didn't explain str.lower()
# all that does is make whatever string you put in all lowercase
# for example str.lower("I fEeL gReAt") is equivalent to "i feel great"
# a lot less cryptic
# also very useful for making sure your user can use any capitalization they want

boolean = 1<2

if boolean:
    print("A boolean is a type of data! it is just true or false, but you can even assign booleans to variables like I did above!")
# neat
# everything with a true of false value is a boolean
# so it makes sense that since if statements and while loops use booleans on their own
# if you assign a boolean to a variable
# you can just put that variable into the if statement directly!
# no == needed!
# this is never necessary but can save you several key presses occasionally
# also you can do this:
boolean = False
# yup the computer understands that
# you are assigning it the boolean value of False
# so if you put that into an if statement
# the if statement wouldn't activate
# because the condition you put in (the boolean) is false

if not boolean:
    print("boolean is currently false. not false is true!")
# not is useful when you want the else part of the statement without the if
# in some situations you can write this neater than just putting not in front of it
# for example
# not 1 = 2
# and
# 1 != 2
# do the same thing
# neat



# now I will get into things that might not be necessary for this project, but that will make your program better

# the first thing is importing libraries
# importing libraries just adds more commands that you can use in your code
# and is as simple as
# import nameOfLibrary
# here is a neat one I found online:
import time
# this library lets me use time commands
# the only one I know right now is
# time.sleep()
# you put in a number, and your program pauses for that many seconds

print("your test results are in!")
time.sleep(1)
print("dramatic pause")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)
if userAns == answer:
    print("WHAT A GENIUS")
else:
    print("I literally told you what the answer is. Seriously?")

# the last thing I should mention is one that is almost never necessary, but is INCREDIBLY helpful and should be used often

# FUNCTIONS!!!
# you can create your own commands
# it looks like this:
# def funcName():
#     code here

#lets give it a whirl

def pause():
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)

# simple as that!
# keep in mind that this doesn't actually do anything on its own
# but now whenever I want a dramatic pause in my program
# I can just
pause()
# incredible right?
# you can put ANYTHING into a function
# and whenever you want
# you can just call your function and not have to write the code again


# but there is another important thing about functions
# you can add parameters
# it looks like this
# def funcName(para1,para2,para3...)
#     code that interacts with parameters

# check this out:

def pauseV2(length,dots):
    i = dots
    while i > 0:
        i -= 1
        time.sleep(length)
        print(".")

# now I can customize my dramatic pauses

pauseV2(3,3)
# this does a long ominous .        .         .

pauseV2(0.2,10)
# this does a quickfire ..........

# parameters don't just have to be numbers though, strings, lists, booleans and any other type of data works too
# any code that you repeate multiple times should probably be a function
# even if you have to make 6 parameters it is still often worth it to make your code more readable and easily expandable