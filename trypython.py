
# name = input("Enter name:")
# print("Hello " + name)

# first = int(input('Enter first number: '))
# second = int(input('Enter second number: '))
# sum = first+second
# # plus = 'plus'
# # equal = '='

# result = '{0} plus {1} = {2}'.format(first,second,sum)

# # print(first,plus,second,equal,sum)
# print(result)

# name = input("Enter name:")
# print("Howdy " + name.upper())

# address = input("Enter address:")
# print("I live at " + address.lower())

# birthmonth = input("Enter birth month:")
# birthmonth = birthmonth.title()
# print("My birth month is "+ birthmonth)


# name = input("Enter name:")
# name = name[::-1]
# print(name)

# number = int(input("Enter a number: "))
# if number < 10:
#     print("Small")
# else:
#     print("Big")

# numberone = int(input("Enter a number: "))
# numbertwo = int(input("Enter a number: "))

# if numberone ==numbertwo:
#     print("Same")
# else:
#     print("Different")
    
# number = int(input("Enter number: "))

# if number == 1:
#     yourname = input("What is your name: ")
#     print("Your name is: "+yourname)
# if number == 2:
#     age = input("Enter your age: ")
#     print("Your age is: " + age)

# i = 0

# while i < 100:
#     i+=2
    
#     print(i)


# l = [1, 3,[1, 2, 3], 5, 7, 9, 100]

# for i in l:
#     print(i)

# ages =[23, 25, 61, 32]

# ages.sort()

# for age in ages:
#     print(age)

#--------------------------------------------------
# for i in range(10):
#     number = int(input("Enter a number:"))
#     total +=number
    
# print(total)
#-------------------------------------------------
#Write a script that contains a function called add, which accepts two arguments a, and b.

#The function should return the result of adding a and b. In the script, call the function passing it 3 and 5, and print the result.
# total = 0


#-------------------------------------------------
# def add (a,b):
    
#     return a+b

# print(add(3,5))


#----------------------------------------

#Modify the script above to allow the user to enter two numbers. Pass those numbers to the add function, print the result.

# a = int(input("Enter a number:"))
# b = int(input("Enter a number:"))


# def add(a,b):
#     return (a + b)
    

# print(add(a,b))

#------------------------------------------

# Write a function that accepts one argument n. You can assume that n is an integer. The function should return #True if n is even, False if it's odd.

# def num(n):
#     return n % 2 == 0
    
        
# print(num(19))

#---------------------------------------------
#Write a function called message that accepts no arguments, it returns "This is the message". Try the following two print
#statements to test the function, compare the results.

#print(message())
#print(message)

# def message():
#     print("This is the message")

# print(message())
# print(message)

#---------------------------------------------

#Create a List containing all of the numbers from 1 to 6. Use the sum function to calculate the sum of the contents of the list.
# numbers = [1, 2, 3, 4, 5, 6]

# numbersSum = sum(numbers)

# print(numbersSum)

#--------------------------------------------------
#Use the range function to create a range from 0 to 99, use the list function to convert the range into a list. Print the list.

# l = list(range(0,99))

# print(l)

#-------------------------------------------------

# Use the range and list functions to create a list of all of the even numbers from 10 to 50 (including 50). Print out the length of that list.

# mylist = list(range(10,52,2))

# print (len(mylist))

#---------------------------------------------------
    
# Create the following list of lists.
# [[0], [0, 1], [0, 1, 2] ... [0, 1, 2, 3, 4, 5, 6]]
# print the 3rd item of the fifth list.

# outerList = []
# for i in range(1,8):
#     v = list(range(i))
#     outerList.append(v)
    
# print(outerList)

# mylist = [[0], [0,1], [0, 1, 2], [0, 1, 2, 3], [0, 1, 2, 3, 4],[0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5, 6]]

# print(mylist[4][2])

#----------------------------------------------------

# Create an empty list called evens. Write a for loop that loops through all the numbers from 0 to 10. Append the even numbers to the evens list. Print out the evens list.

# evens = []

# for x in range (0,11,2):

#   evens.append(x)
   
# print(evens)

#----------------------------------------------------

# Create any list with at least 10 items. 
# Use python's list slicing syntax to print

# The first item
# The last item
# All but the first item
# All but the last item

# list = [1, 3, 'hello', 'goodbye', 5, 25, 65, 6, 9 ,12]

# print(list[0])
# print(list[-1])
# print(list[1:])
# print(list[:-1])
#------------------------------------------
# Create a dictionary that represents a student. Each student has a name, an age, a nationality, and a list of subjects.

studa = {'name':'John', 'Age':'20', 'Nationality':'Irish', 'Subjects':['maths', 'science', 'english']}
studb = {'name':'Sarah', 'Age':'25', 'Nationality':'French', 'Subjects':['irish', 'history', 'english']}
studc = {'name':'Jack', 'Age':'32', 'Nationality':'German', 'Subjects':['maths', 'accounting', 'english']}
studd = {'name':'Mary', 'Age':'64', 'Nationality':'Scottish', 'Subjects':['french', 'biology', 'english']}


# Create a list containing at least 4 of the students described in challenge 63
# Convert the list into a dictionary, use the the students names as the key for the dictionary.


# studentlist = [{'name':'John', 'Age':'20', 'Nationality':'Irish', 'Subjects':['maths', 'science', 'english']},
# {'name':'Sarah', 'Age':'25', 'Nationality':'French', 'Subjects':['irish', 'history', 'english']},
# {'name':'Jack', 'Age':'32', 'Nationality':'German', 'Subjects':['maths', 'accounting', 'english']},
# {'name':'Mary', 'Age':'64', 'Nationality':'Scottish', 'Subjects':['french', 'biology', 'english']}]

# studentlist = {
# 'John':{'name':'John', 'Age':'20', 'Nationality':'Irish', 'Subjects':['maths', 'science', 'english']},
# 'Sarah':{'name':'Sarah', 'Age':'25', 'Nationality':'French', 'Subjects':['irish', 'history', 'english']},
# 'Jack':{'name':'Jack', 'Age':'32', 'Nationality':'German', 'Subjects':['maths', 'accounting', 'english']},
# 'Mary':{'name':'Mary', 'Age':'64', 'Nationality':'Scottish', 'Subjects':['french', 'biology', 'english']}]

words = ["apple", "car","fruit","phone"]

d = {}
for word in words:
    d[word] = len(word)
    
print({word : len(word) for word in words})
    
# print(d)

