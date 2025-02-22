'''
Question 1 & Question 2
a = [10, 20, 30, 20, 40, 50]
'''
a = [10, 20, 30, 20, 40, 50]
#Remove the first occurance of 20
a.remove(20)
#Remove element at index 1 and return its value in val
val = a.pop(1)
print(val)

'''

Question 3 and Question 4
a = [10, 20, 30, 40, 50, 60, 70]
Removes elements from index 1 to index 3 (which are 20, 30, 40)
'''
a = [10, 20, 30, 40, 50, 60, 70]
a[1:4] = []

#Remove all elements
a[:] = []



#Write a program that prints the number of times the substring 'iti' occurs in a string
my_string = "iti is iti an iti string"
count = my_string.count('iti')
print(count)


#application to take a number in binary form from the user, and print it as a decimal
binary = input("Enter a binary number: ")
if not binary.count("0") + binary.count("1") == len(binary):
    print("Invalid input. Please enter a valid binary number.")
    exit()
decimal = int(binary, 2)
print("The decimal equivalent is:", decimal)


#write a code take a number as an argument and if the number divisible by 3 return "Fizz" and if it is divisible by 5 return "buzz" and if is is divisible by both return "FizzBuzz"
def fizzbuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return str(number)


#Ask the user to enter the radius of a circle print its calculated area and circumference
radius = float(input("Enter the radius of a circle: "))
area = 3.14 * radius ** 2
circumference = 2 * 3.14 * radius
print("The area of the circle is:", area)
print("The circumference of the circle is:", circumference)


#Ask the user for his name then confirm that he has entered his name (not an empty string/integers).then proceed to ask him for his email and print all this data

name = input("Enter your name: ")
email = input("Enter your email: ")
#check if name is not empty
if not name:
    print("Please enter your name.")
    name = input("Enter your name: ")
#check if email is not empty
if not email:
    print("Please enter your email.")
    email = input("Enter your email: ")
#check email format
if "@" not in email or "." not in email:
    print("Please enter a valid email.")
    email = input("Enter your email: ")
print("Name:", name)
print("Email:", email)