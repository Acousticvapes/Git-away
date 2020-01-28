 #this is my practice
header = "Practice"
date = "1/21/20"
title = date + ' ' + header
print(title) #1/11/20 Practice
repeattitle = (title + ' ') * 4
print(repeattitle) #1/21/20 Practice 1/21/20 Practice 1/21/20 Practice 1/21/20 Practice
#use [] to pick specific characters
#first character is always 0
print(repeattitle[12]) #t
#using [-#] starts from the last character
print(header[-3]) #i
#use [#:#]to pick a range of characters not including the second number
print(date[0:3]) #1/1
print(date[3:-1]) #1/2
# "" is not required for intigers(whole number) or floats(decimal)
integer = 9
float1 = 3.2
print(integer) #9
print(float1) #3.2
#can use +(add), -(subtract), *(multiply), /(divide), %(modulo/remainder)
add = integer + float1
subtract = integer - float1
multiply = integer * float1
divide = integer / float1
modulo = integer % float1
power = integer ** float1
print(add) #12.2
print(subtract) #5.8
print(multiply) #28.8
print(divide) #2.8125
print(modulo) #2.6
print(power) #1131.29542338
def new_function():
    print("inside a function")
new_function() #prints "inside a function"
#booleans can only answer True or False
#booleans must be capitalized
bool1 = False
print(bool1) #False
bool2 = True
print(bool2) #True
#list group things together
list1 = [1,2,3]
print(list1) #[1, 2, 3]
list2 = ["Hello", True]
print(list2) #['Hello', True]
list1plus2 = list1 + list2 + ["End"]
print(list1plus2) #[1, 2, 3, 'Hello', True, 'End']
  #list count starting from 0
  #use print([]) to pick out variables from list
print(list1plus2[0]) #1
print(list1plus2[3]) #Hello
  #use - to start from end of list
print(list1plus2[-1]) #End
   #use [ : ] to splice a range from a list up to but not including the second #
print(list1plus2[2:4]) #[3, 'Hello']
 #can change variables ofthe list by reassaigning it below
list1plus2[2] = "three"
print(list1plus2) #[1, 2, 'three', 'Hello', True, 'End']
  #use .append() to add variables to list without making a new list
list1plus2.append(10)
print(list1plus2) #[1, 2, 'three', 'Hello', True, 'End', 10]
 #create a dictionary using {"key":"value"}
dict1 = {"key":"value","key2":"value2"}
print(dict1) #{'key2': 'value2', 'key': 'value'}
 #access info in dictionary using ([])
print(dict1["key2"]) #value2
 #to add keys and values use Dict1["newkeyname"] = "new value"
dict1["newkey"] = 0.1
print(dict1) #{'key2': 'value2', 'key': 'value', 'newkey': 0.1}
 #create Tuple with = (), must always use commas
testTuple = (2,)
secondTuple = ("Hello","World")
print(testTuple) #(2,)
print(secondTuple) #('Hello', 'World')
print(testTuple+secondTuple) #(2, 'Hello', 'World')
print(testTuple[0]) #2
print(secondTuple[0:]) #('Hello', 'World')
 #cant reassaign values in tuples
 #must change to same type to add together
int1 = 1
string1 = "3"
 #can only convert to "int" if integers are present in string
 #int("3") = 3
testSum = int(string1)+int1
print(testSum) #4
 #float("4.7") = 4.7
floatstring = "4.7"
secondsum = float(floatstring) + int1
print(secondsum) #5.7
 #int(5.7) = 5
float2 = 5.7
thirdsum = int(float2) + int1
print(thirdsum) #6
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
factorial(5) #120

 #global variables. add global before to access global variables when not available otherwise
 #functions define code we want to repeat
 # use def to define functions foloowed by a name
 #def name(variables)
    #code
    #more code
#no longer in function
def addOne(x):
    y = x+1
    return y
    #use return to return variables
startNumber = 1
nextNumber = addOne(startNumber)
print(nextNumber) #2
globalx = 5
def addOne(x):
    global globalx
    y = globalx+1
    return y
lastNumber = addOne(startNumber)
print(lastNumber) #6
 #Boolean expressions return True or False
greaterthan = 7 > 6
print(greaterthan) #True
lessthan = 7 < 6
print(lessthan) #False
equalto = 7 == 6
print(equalto) #False
notequalto = 7 != 6
print(notequalto) #True
 #  > is greater than
 #  < is less than
 #  == is Equal to
 #  != is not equal to
 #  >= is greater than or equal to
 #  <= is less than or equal to

 # control flow
#if Boolean:
    #code
    #more code
#elif Boolean:
    #code
    #more code
#else:
    #code
    #more code
#no longer in statement
testflow = 10
if testflow < 10:
    print("Less than ten")
    print("Still in if")
elif testflow == 10:
    print("Equal to ten")
#else must follow the if
else:
    print("Not less than ten")
print("No longer in if")
 #Loops
#for loopingvariable in whatweloopover:
    #code
    #more code

testlist = [1,5,7]

for element in testlist:
    print(element)
teststring = "hello"
for character in teststring:
    print(character)
start = 0
stop = 30
stepsize = 2
for number in range(start, stop, stepsize):
    print(number)

 #While Loops
#while Boolean:
    #code
    #more code
