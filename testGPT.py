# 1️⃣ Variables and Data Types
name = "Alice"  # String
age = 25        # Integer
height = 5.6    # Float
is_student = True  # Boolean

# 2️⃣ Functions in Python
def greet_user(username):
    """Function to greet the user"""
    print(f"Hello, {username}! Welcome to Python.")

greet_user(name)  # Function call

# 3️⃣ Conditional Statements
def check_age(age):
    """Check if the person is an adult or minor"""
    if age >= 18:
        print("You are an adult.")
    elif age > 12:
        print("You are a teenager.")
    else:
        print("You are a child.")

check_age(age)

# 4️⃣ Loops (For and While)
print("\nCounting using for loop:")
for i in range(1, 6):  # Loop from 1 to 5
    print(i, end=" ")

print("\nCounting using while loop:")
x = 1
while x <= 5:
    print(x, end=" ")
    x += 1  # Increment x

# 5️⃣ Lists (Arrays in Python)
fruits = ["Apple", "Banana", "Cherry"]
print("\n\nFruits List:", fruits)

# Adding an item to the list
fruits.append("Mango")
print("Updated List:", fruits)

# Looping through the list
print("Printing each fruit:")
for fruit in fruits:
    print(fruit)

# 6️⃣ Dictionaries (Key-Value Pairs)
person = {"name": "Bob", "age": 30, "city": "New York"}
print("\nPerson Dictionary:", person)

# Accessing dictionary values
print("Person's Name:", person["name"])

# 7️⃣ Classes and Objects (OOP Basics)
class Car:
    """A simple Car class"""
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        """Displays car details"""
        print(f"{self.year} {self.brand} {self.model}")

# Creating an object of Car class
my_car = Car("Tesla", "Model S", 2023)
my_car.display_info()

# 8⃣ Exception Handling (Error Handling)
try:
    num = int(input("\nEnter a number: "))
    print(f"You entered: {num}")
except ValueError:
    print("Invalid input! Please enter a valid number.")

print("\n🚀 End of Python Crash Course!")