# 🏷️ Python Data Types and Variables - Complete Guide for Kids

## 🤔 What are Data Types?

Think of data types like different kinds of containers in your kitchen:
- **String** = A label on a jar (text)
- **Integer** = A counting number (1, 2, 3...)
- **Float** = A measuring cup (1.5, 2.7, 3.14...)
- **Boolean** = A light switch (True or False)
- **List** = A shopping basket (holds multiple items)

## 📦 Variables: Your Storage Boxes

Variables are like labeled boxes where you store information. The label is the variable name, and the box contains your data!

```python
name = "Alex"        # String in a box labeled "name"
age = 10            # Integer in a box labeled "age"
height = 5.2         # Float in a box labeled "height"
is_student = True    # Boolean in a box labeled "is_student"
```

## 🔤 String Data Type (Text)

**What it is:** Strings are for storing text - letters, words, sentences!

### **Creating Strings:**
```python
# Single quotes
name = 'Alex'

# Double quotes
greeting = "Hello, world!"

# Triple quotes for multiple lines
story = """Once upon a time,
there was a brave programmer
who loved to code!"""
```

### **String Operations:**
```python
first_name = "Alex"
last_name = "Smith"

# Concatenation (joining strings)
full_name = first_name + " " + last_name
print(full_name)  # "Alex Smith"

# String formatting
age = 10
message = f"Hi, I'm {first_name} and I'm {age} years old!"
print(message)  # "Hi, I'm Alex and I'm 10 years old!"

# String methods
text = "Hello World"
print(text.lower())      # "hello world"
print(text.upper())      # "HELLO WORLD"
print(text.replace("World", "Python"))  # "Hello Python"
```

### **In Your Code:**
```python
# From Buddy System
name = "Alice"                    # String
print(f"{student.name} (Grade {student.grade})")  # String formatting

# From Stress Meter
due_date_str = "2025-10-05"       # String
print(f"Start: {start.date()}")   # String formatting
```

## 🔢 Integer Data Type (Whole Numbers)

**What it is:** Integers are whole numbers - no decimals!

### **Creating Integers:**
```python
age = 10
count = 0
temperature = -5
big_number = 1000000
```

### **Integer Operations:**
```python
a = 10
b = 3

print(a + b)    # Addition: 13
print(a - b)    # Subtraction: 7
print(a * b)    # Multiplication: 30
print(a / b)    # Division: 3.333... (becomes float!)
print(a // b)   # Floor division: 3 (whole number part)
print(a % b)    # Modulo (remainder): 1
print(a ** b)   # Power: 1000
```

### **In Your Code:**
```python
# From Buddy System
grade = 10                       # Integer
for i in range(0, len(self.students)-1, 2):  # Integer in range

# From Stress Meter
work_hours_needed = 10           # Integer
daily_capacity = 2               # Integer
total_days = (due - start).days  # Integer
```

## 🎯 Float Data Type (Decimal Numbers)

**What it is:** Floats are numbers with decimal points!

### **Creating Floats:**
```python
pi = 3.14159
temperature = 98.6
percentage = 85.5
```

### **Float Operations:**
```python
a = 10.5
b = 3.2

print(a + b)    # 13.7
print(a - b)    # 7.3
print(a * b)    # 33.6
print(a / b)    # 3.28125
```

### **In Your Code:**
```python
# From Stress Meter
today_stress = 10 * urgency * backlog_ratio  # Float result
print(f"stress ≈ {level:.1f}")  # Formatting float to 1 decimal
```

## ✅ Boolean Data Type (True/False)

**What it is:** Booleans are like light switches - only two states: True or False!

### **Creating Booleans:**
```python
is_sunny = True
is_raining = False
is_weekend = True
```

### **Boolean Operations:**
```python
a = True
b = False

print(a and b)   # False (both must be True)
print(a or b)    # True (at least one is True)
print(not a)     # False (opposite)
```

### **In Your Code:**
```python
# From Buddy System
if student.buddy and student.name not in paired:  # Boolean conditions
    print(f"{student.name} ↔ {student.buddy.name}")

# From Stress Meter
if total_days <= 0:  # Boolean condition
    print("⚠️ Start date is not before the due date.")
```

## 📝 List Data Type (Multiple Items)

**What it is:** Lists are like shopping baskets - they can hold multiple items!

### **Creating Lists:**
```python
# Empty list
shopping_list = []

# List with items
fruits = ["apple", "banana", "orange"]
numbers = [1, 2, 3, 4, 5]
mixed = ["hello", 42, True, 3.14]
```

### **List Operations:**
```python
fruits = ["apple", "banana"]

# Add items
fruits.append("orange")        # Add to end
fruits.insert(0, "grape")     # Add at specific position

# Access items
first_fruit = fruits[0]       # "grape"
last_fruit = fruits[-1]       # "orange"

# Remove items
fruits.remove("banana")       # Remove specific item
popped = fruits.pop()         # Remove and return last item

# List length
count = len(fruits)          # Number of items
```

### **In Your Code:**
```python
# From Buddy System
self.students = []                    # Empty list
self.students.append(student)         # Add student to list
for student in self.students:         # Loop through list

# From Stress Meter
dates = []                            # Empty list
stress = []                           # Empty list
dates.append(today.date())            # Add to list
stress.append(today_stress)           # Add to list
```

## 🎯 Type Checking and Conversion

### **Check Data Type:**
```python
name = "Alex"
age = 10
height = 5.2

print(type(name))    # <class 'str'>
print(type(age))     # <class 'int'>
print(type(height))  # <class 'float'>
```

### **Convert Between Types:**
```python
# String to Integer
age_str = "10"
age = int(age_str)    # 10

# Integer to String
age = 10
age_str = str(age)     # "10"

# Float to Integer
price = 9.99
whole_price = int(price)  # 9 (truncates decimal)

# String to Float
pi_str = "3.14159"
pi = float(pi_str)    # 3.14159
```

### **In Your Code:**
```python
# From Stress Meter
due = dt.datetime.fromisoformat(due_date_str)  # String to datetime
remaining_work = work_hours_needed             # Integer
today_stress = 10 * urgency * backlog_ratio    # Float
```

## 🧪 Advanced Data Types in Your Code:

### **Datetime Objects:**
```python
import datetime as dt

# Create datetime objects
due = dt.datetime(2025, 10, 5)        # Year, month, day
start = dt.datetime(2025, 9, 28)      # Year, month, day

# Calculate differences
time_diff = due - start               # timedelta object
days = time_diff.days                # Integer: number of days
```

### **Sets (Unique Items):**
```python
# From Buddy System
paired = set()                       # Empty set
paired.add(student.name)             # Add to set
if student.name not in paired:      # Check if in set
```

## 🎮 Fun Data Type Projects:

### **Project 1: Student Grade Calculator**
```python
def grade_calculator():
    # Get student information
    name = input("Student name: ")           # String
    math_grade = float(input("Math grade: ")) # Float
    science_grade = float(input("Science grade: ")) # Float
    english_grade = float(input("English grade: ")) # Float
    
    # Calculate average
    grades = [math_grade, science_grade, english_grade]  # List
    average = sum(grades) / len(grades)      # Float
    
    # Determine letter grade
    if average >= 90:                        # Boolean condition
        letter_grade = "A"                   # String
    elif average >= 80:
        letter_grade = "B"
    elif average >= 70:
        letter_grade = "C"
    else:
        letter_grade = "F"
    
    # Display results
    print(f"{name}'s average: {average:.1f} ({letter_grade})")

grade_calculator()
```

### **Project 2: Shopping List Manager**
```python
def shopping_manager():
    shopping_list = []                       # List
    
    while True:                               # Boolean loop
        print("\n1. Add item")
        print("2. Remove item")
        print("3. View list")
        print("4. Exit")
        
        choice = input("Choose (1-4): ")     # String
        
        if choice == "1":                    # String comparison
            item = input("Item name: ")      # String
            shopping_list.append(item)       # Add to list
            print(f"Added {item} to list!")
            
        elif choice == "2":
            if len(shopping_list) > 0:       # Boolean condition
                print("Current items:")
                for i, item in enumerate(shopping_list):  # Loop through list
                    print(f"{i+1}. {item}")
                
                try:
                    index = int(input("Item number to remove: ")) - 1  # String to int
                    removed = shopping_list.pop(index)                # Remove from list
                    print(f"Removed {removed}")
                except (ValueError, IndexError):
                    print("Invalid choice!")
            else:
                print("List is empty!")
                
        elif choice == "3":
            if shopping_list:                # Boolean check (empty list = False)
                print("\nShopping List:")
                for i, item in enumerate(shopping_list):
                    print(f"{i+1}. {item}")
            else:
                print("List is empty!")
                
        elif choice == "4":
            print("Goodbye!")
            break                           # Exit loop
        else:
            print("Invalid choice!")

shopping_manager()
```

## 🎯 Best Practices:

### **1. Use Descriptive Variable Names:**
```python
# Good ✅
student_name = "Alex"
student_age = 10
is_passing = True

# Bad ❌
n = "Alex"
a = 10
p = True
```

### **2. Choose the Right Data Type:**
```python
# Good ✅
age = 10                    # Integer for whole numbers
price = 9.99                # Float for money
name = "Alex"               # String for text
is_student = True           # Boolean for yes/no

# Bad ❌
age = "10"                  # Don't use string for numbers
price = 9                   # Don't use integer for money
```

### **3. Handle Type Conversion Safely:**
```python
# Good ✅
try:
    age = int(input("Enter age: "))
except ValueError:
    print("Please enter a valid number!")
    age = 0
```

## 🚨 Common Mistakes:

### **Mistake 1: String vs Integer Math**
```python
# This won't work!
age = "10"                   # String
next_year = age + 1          # Error! Can't add string and integer

# Fix it:
age = int("10")              # Convert to integer
next_year = age + 1          # Now it works!
```

### **Mistake 2: Forgetting Quotes for Strings**
```python
# This won't work!
name = Alex                  # Error! Alex is not defined

# Fix it:
name = "Alex"                # Use quotes for strings
```

### **Mistake 3: Case Sensitivity**
```python
# These are different variables!
Name = "Alex"
name = "Bob"
print(Name)  # "Alex"
print(name)  # "Bob"
```

## 🎉 Summary:

**Data Types are like different containers:**
- **String** = Text labels 📝
- **Integer** = Counting numbers 🔢
- **Float** = Measuring numbers 📏
- **Boolean** = Yes/No switches 🔘
- **List** = Shopping baskets 🛒

**Remember:**
- Choose the right type for your data
- Use descriptive variable names
- Convert types when needed
- Practice with different data types

**Next Steps:**
1. Experiment with different data types
2. Try the fun projects above
3. Look at how data types are used in your programs
4. Create your own programs using different data types!

Happy coding with data types! 🏷️✨
