'''Question 1 :
Write a simple calculator program using match to perform addition, subtraction, multiplication, and division.
operation = "add"
a, b = 10, 5
# Expected Output: 15'''

def calculator(a,b,operation):
    match operation:
        case "add":
            print (a + b)
        case "subtract":
            print (a - b)
        case "multiply":
            print (a * b)
        case "divide":
            print (a / b)
        case _: 
            print("unknown operation")
        
#calling the function
calculator(10,5,"add")

'''
Question 2 :
Write a program to filter out even numbers from a list and count how many are left.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Expected Output: [1, 3, 5, 7, 9], Count = 5
# '''

def filter_even_numbers(numbers):
    filtered_numbers = [number for number in numbers if number %2 != 0]
    left_count = len(numbers) - len(filtered_numbers) 
    print("numbers after ",filtered_numbers , "Count =",left_count)
    
        
myNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

filter_even_numbers(myNumbers)

'''
Question 3 :
Write a program to check if a password meets the following criteria:
- At least 8 characters long.
- Contains at least one uppercase letter.
- Contains at least one digit.
password = "Pass1234"
# Expected Output: "Valid Password"
'''

def is_valid_password(password):
    if len(password) < 8:
        print("Invalid Password")
        return
    if password == password.lower(): 
        print("Invalid Password")
        return
    if not any(char.isdigit() for char in password):
        print("Invalid Password")
        return
    
    print("Valid Password")


password = "Pass1234"
is_valid_password(password)  

'''
Question 4: 
Write a Python script to concatenate the following dictionaries to create a new one.
Sample Dictionary :
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
'''

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
result = {**dic1, **dic2, **dic3} #unpacking
print(result)


'''
Question 5: 
takes a string and prints the longest
alphabetical ordered substring occured.
For example, if the string is 'abdulrahman' then the output is:
Longest substring in alphabetical order is: abdu
'''
def longest_alphabetical_order(word):
    myvar = word[0]
    for i in range(1,len(word)):
        if word[i] > myvar[i-1]:
            myvar+= word[i]
        else:
            print(myvar)
            return 

longest_alphabetical_order("abdulrahman")

'''
Question 6:
Write a program to check if a Email meets the following criteria:
- Ensures the email follows a standard format (e.g., local@domain.com).
- Does not check if the email actually exists or is deliverable.
'''
import re
def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    
    if re.match(pattern, email):
        print("Valid Email")
    else:
        print("Invalid Email")

is_valid_email("test@example.com")  
