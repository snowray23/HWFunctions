#1
def add(x, y):
    return x + y

def subtract (x, y):
    return x - y

def multiply (x, y):
    return x * y

def divide (x, y):
    if y == 0:
        return "error"
    else:
        return x / y


num1 = int(input("enter number "))
num2 = int(input("enter number2 "))
operation = input ("what is your operation? add,subtract,multiply, divide ")

if operation == "add":
    print("answer:", add(num1, num2))
elif operation == "subtract":
    print("answer:", subtract(num1, num2))
elif operation == "multiply":
    print("answer:", multiply (num1, num2))
elif operation == "divide":
    print("answer", divide(num1, num2))
else:
    print("invalid input")


          

#2
def add_item(shopping_list, item):
    shopping_list.append(item)
    print(f"{item} has been added to your list")

def remove_item(shopping_list, item):
    shopping_list.remove(item)
    print(f"{item} has been removed from your list")

def print_list(shopping_list):
    print("shopping list")


#3
def avg_grade(grades_list):
    return sum(grades_list) / len(grades_list)

def highest_grade(grades_list):
 return max(grades_list)

def lowest_grade(grades_list):
    return min(grades_list)
    
def sorted_list(grades_list):
    return sorted(grades_list)
