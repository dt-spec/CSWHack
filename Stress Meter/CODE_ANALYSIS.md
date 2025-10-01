# 🔍 Stress Meter - Line-by-Line Code Analysis

## 📋 Program Overview
This program simulates stress levels over time for project planning. It demonstrates date handling, loops, mathematical calculations, and conditional logic.

## 🧩 Code Structure Breakdown

### **Lines 1-5: File Header and Comments**
```python
# ==========================================
# STRESS METER - TEACHING SKELETON (PYTHON)
# Concepts: variables, input, for-loop, while-loop, if/elif/else, lists
# Optional: basic plotting (matplotlib)
# ==========================================
```

**What this means:** These are comments that explain what the program teaches and what concepts it demonstrates.

### **Lines 7-9: Import Statements**
```python
# ---- 0) Imports (ONLY if you use dates/plotting later) ----
import datetime as dt
# import matplotlib.pyplot as plt  # <- OPTIONAL (uncomment when ready)
```

**Line-by-line breakdown:**
- **Line 7:** Comment explaining the import section
- **Line 8:** `import datetime as dt` - Import datetime module with alias 'dt'
- **Line 9:** Commented matplotlib import for optional graphing

**Key concepts:**
- **Import:** Bringing in external functionality
- **Alias:** Short name for long module names (`dt` instead of `datetime`)
- **Commenting:** Using `#` to disable code temporarily

### **Lines 11-16: Input Variables**
```python
# ---- 1) Inputs (students can EDIT these numbers) ----
# TODO: Change these and re-run to see how the output changes
due_date_str     = "2025-10-05"   # YYYY-MM-DD
start_date_str   = "2025-09-28"   # YYYY-MM-DD
work_hours_needed = 10            # total hours needed to finish the task
daily_capacity    = 2             # how many hours you can realistically do each day
```

**Line-by-line breakdown:**
- **Line 11:** Comment explaining this section
- **Line 12:** TODO comment encouraging experimentation
- **Line 13:** `due_date_str = "2025-10-05"` - Project deadline as string
- **Line 14:** `start_date_str = "2025-09-28"` - Project start date as string
- **Line 15:** `work_hours_needed = 10` - Total work required (integer)
- **Line 16:** `daily_capacity = 2` - Daily work capacity (integer)

**Key concepts:**
- **Variables:** Named storage for data
- **String literals:** Text in quotes
- **Integer literals:** Whole numbers
- **Comments:** Explaining what each variable represents

### **Lines 18-21: Date Parsing**
```python
# ---- 2) Parse dates + compute how many days we have ----
due   = dt.datetime.fromisoformat(due_date_str)
start = dt.datetime.fromisoformat(start_date_str)
total_days = (due - start).days
```

**Line-by-line breakdown:**
- **Line 18:** Comment explaining date processing
- **Line 19:** `due = dt.datetime.fromisoformat(due_date_str)` - Convert string to datetime object
- **Line 20:** `start = dt.datetime.fromisoformat(start_date_str)` - Convert string to datetime object
- **Line 21:** `total_days = (due - start).days` - Calculate difference in days

**Key concepts:**
- **Method calls:** `dt.datetime.fromisoformat()` - Calling functions on objects
- **Date arithmetic:** Subtracting dates to get time difference
- **Attribute access:** `.days` - Getting a property from an object

### **Lines 23-26: Input Validation**
```python
# Guard rail: make sure we have at least 1 day
if total_days <= 0:
    print("⚠️ Start date is not before the due date. Adjusting to 1 day.")
    total_days = 1
```

**Line-by-line breakdown:**
- **Line 23:** Comment explaining the validation
- **Line 24:** `if total_days <= 0:` - Check if dates are invalid
- **Line 25:** `print("⚠️ Start date is not before the due date. Adjusting to 1 day.")` - Error message
- **Line 26:** `total_days = 1` - Fix the invalid input

**Key concepts:**
- **Conditional statements:** `if` for decision making
- **Comparison operators:** `<=` (less than or equal)
- **Error handling:** Checking for invalid inputs
- **String formatting:** Using emoji in output

### **Lines 28-33: Data Storage Setup**
```python
# ---- 3) Prepare storage for results ----
dates  = []       # list of each date in the plan
stress = []       # list of stress values for each day

# Remaining work at the beginning
remaining_work = work_hours_needed
```

**Line-by-line breakdown:**
- **Line 28:** Comment explaining data preparation
- **Line 29:** `dates = []` - Empty list for storing dates
- **Line 30:** `stress = []` - Empty list for storing stress values
- **Line 32:** Comment explaining remaining work
- **Line 33:** `remaining_work = work_hours_needed` - Initialize work counter

**Key concepts:**
- **Lists:** `[]` - Empty collections for storing multiple values
- **Variable assignment:** Copying values between variables
- **Data structure planning:** Setting up storage before processing

### **Lines 35-41: Main Simulation Loop**
```python
# ==========================================
# FOR LOOP: simulate day-by-day progression
# ==========================================
for i in range(total_days + 1):
    # current day = start date + i days
    today = start + dt.timedelta(days=i)
    days_left = (due - today).days
```

**Line-by-line breakdown:**
- **Lines 35-37:** Comments explaining the main loop
- **Line 38:** `for i in range(total_days + 1):` - Loop through each day
- **Line 39:** Comment explaining the calculation
- **Line 40:** `today = start + dt.timedelta(days=i)` - Calculate current date
- **Line 41:** `days_left = (due - today).days` - Calculate days remaining

**Key concepts:**
- **For loops:** Repeating code for each day
- **Range function:** `range(total_days + 1)` creates sequence 0, 1, 2, ...
- **Date arithmetic:** Adding days to dates
- **Timedelta:** `dt.timedelta(days=i)` - Represents a time duration

### **Lines 43-52: Urgency Calculation**
```python
# -------------------------------
# IF / ELIF / ELSE:
# define an "urgency multiplier" based on days_left
# -------------------------------
if days_left >= 5:
    urgency = 1.0            # plenty of time
elif days_left >= 2:
    urgency = 1.5            # getting closer
else:
    urgency = 2.5            # last-minute panic
```

**Line-by-line breakdown:**
- **Lines 43-46:** Comments explaining the urgency logic
- **Line 47:** `if days_left >= 5:` - Check if plenty of time left
- **Line 48:** `urgency = 1.0` - Low urgency multiplier
- **Line 49:** `elif days_left >= 2:` - Check if moderate time left
- **Line 50:** `urgency = 1.5` - Medium urgency multiplier
- **Line 51:** `else:` - Handle last-minute situations
- **Line 52:** `urgency = 2.5` - High urgency multiplier

**Key concepts:**
- **Conditional chains:** `if/elif/else` for multiple conditions
- **Comparison operators:** `>=` (greater than or equal)
- **Floating point numbers:** `1.0`, `1.5`, `2.5` - Decimal values
- **Logic flow:** Different paths based on conditions

### **Lines 54-58: Backlog Ratio Calculation**
```python
# A simple "how behind am I?" ratio:
# (work left) / (how much I can do before the deadline)
# Add +1 to days_left so we never divide by zero on the due day
capacity_left = (days_left + 1) * max(1, daily_capacity)
backlog_ratio = remaining_work / capacity_left
```

**Line-by-line breakdown:**
- **Lines 54-56:** Comments explaining the calculation
- **Line 57:** `capacity_left = (days_left + 1) * max(1, daily_capacity)` - Calculate remaining capacity
- **Line 58:** `backlog_ratio = remaining_work / capacity_left` - Calculate how behind we are

**Key concepts:**
- **Mathematical operations:** Addition, multiplication, division
- **Function calls:** `max(1, daily_capacity)` - Returns the larger value
- **Division:** Calculating ratios and proportions
- **Safety measures:** Adding 1 to prevent division by zero

### **Lines 60-66: Stress Calculation and Storage**
```python
# Compute today's stress score
# Scale 0..something; students can tweak the 10x
today_stress = 10 * urgency * backlog_ratio

# Save results
dates.append(today.date())   # store as date only
stress.append(today_stress)
```

**Line-by-line breakdown:**
- **Line 60:** Comment explaining stress calculation
- **Line 61:** Comment about the scaling factor
- **Line 62:** `today_stress = 10 * urgency * backlog_ratio` - Calculate stress score
- **Line 64:** Comment explaining data storage
- **Line 65:** `dates.append(today.date())` - Add current date to list
- **Line 66:** `stress.append(today_stress)` - Add stress value to list

**Key concepts:**
- **Mathematical formulas:** Combining multiple factors
- **List methods:** `.append()` - Adding items to lists
- **Date methods:** `.date()` - Getting just the date part
- **Variable assignment:** Storing calculated values

### **Lines 68-84: Work Simulation Loop**
```python
# -------------------------------
# WHILE LOOP:
# simulate "work sessions" DONE TODAY until
#  - you hit your daily capacity, OR
#  - you finish the remaining work
# (This is exaggerated for teaching purposes.)
# -------------------------------
sessions_done = 0
while sessions_done < daily_capacity and remaining_work > 0:
    # Do 1 hour of work (you can change "1" to 0.5 etc.)
    remaining_work -= 1
    sessions_done += 1
    # (We don't print to avoid spam. Add prints if you want to see it.)

# Optional: Clamp remaining_work to zero (no negative hours)
if remaining_work < 0:
    remaining_work = 0
```

**Line-by-line breakdown:**
- **Lines 68-74:** Comments explaining the work simulation
- **Line 75:** `sessions_done = 0` - Initialize work counter
- **Line 76:** `while sessions_done < daily_capacity and remaining_work > 0:` - Work loop condition
- **Line 77:** Comment about work amount
- **Line 78:** `remaining_work -= 1` - Reduce remaining work
- **Line 79:** `sessions_done += 1` - Increment work counter
- **Line 80:** Comment about printing
- **Lines 82-84:** Safety check to prevent negative work

**Key concepts:**
- **While loops:** Repeating until conditions are met
- **Compound conditions:** `and` - Both conditions must be true
- **Increment operators:** `+=` and `-=` - Short ways to add/subtract
- **Boundary conditions:** Preventing impossible values

### **Lines 86-106: Output Generation**
```python
# ---- 4) Text Output (beginner-friendly) ----
print("---- STRESS METER REPORT ----")
print(f"Start: {start.date()}  |  Due: {due.date()}")
print(f"Total days: {total_days}  |  Hours needed: {work_hours_needed}  |  Daily capacity: {daily_capacity}")
print()

# Show the first few days to avoid long output
show_n = min(7, len(dates))
for i in range(show_n):
    level = stress[i]
    # Another IF/ELSE to convert number -> label
    if level < 5:
        label = "😌 low"
    elif level < 12:
        label = "😬 medium"
    else:
        label = "😭 high"
    print(f"{dates[i]}  |  stress ≈ {level:.1f}  ({label})")

if len(dates) > show_n:
    print(f"... and {len(dates)-show_n} more days")
```

**Line-by-line breakdown:**
- **Line 86:** Comment explaining output section
- **Line 87:** `print("---- STRESS METER REPORT ----")` - Header
- **Line 88:** `print(f"Start: {start.date()}  |  Due: {due.date()}")` - Project timeline
- **Line 89:** `print(f"Total days: {total_days}  |  Hours needed: {work_hours_needed}  |  Daily capacity: {daily_capacity}")` - Summary
- **Line 90:** `print()` - Empty line
- **Line 92:** Comment about limiting output
- **Line 93:** `show_n = min(7, len(dates))` - Limit to 7 days or all days
- **Line 94:** `for i in range(show_n):` - Loop through days to show
- **Line 95:** `level = stress[i]` - Get stress level for this day
- **Line 96:** Comment about label conversion
- **Lines 97-101:** Convert numeric stress to descriptive labels
- **Line 102:** `print(f"{dates[i]}  |  stress ≈ {level:.1f}  ({label})")` - Display day info
- **Lines 104-105:** Show count of remaining days if there are more

**Key concepts:**
- **String formatting:** f-strings with variables
- **Function calls:** `min()` - Returns smaller value
- **List indexing:** `stress[i]` - Getting item at position i
- **Conditional logic:** Converting numbers to labels
- **String formatting:** `{level:.1f}` - Format to 1 decimal place

### **Lines 108-122: Optional Plotting and Student TODOs**
```python
# ---- 5) OPTIONAL: Plot (uncomment to visualize) ----
# plt.figure(figsize=(8,4))
# plt.plot(dates, stress, marker='o')
# plt.axvline(due.date(), linestyle='--', label='Due Date')
# plt.title("Stress Over Time (start earlier = lower curve)")
# plt.xlabel("Date"); plt.ylabel("Stress (arbitrary units)")
# plt.grid(True); plt.legend(); plt.show()

# ---- 6) STUDENT TODOs ----
# 1) Change work_hours_needed and daily_capacity. What happens to the numbers?
# 2) Edit the IF/ELIF rules for "urgency". Make it harsher or softer.
# 3) In the WHILE loop, try different "work per session" sizes (e.g., 0.5).
# 4) Add a second scenario: start earlier (copy variables with _early suffix) and plot BOTH lines.
# 5) Add a checkpoint: if stress on any day > 15, print "Consider starting earlier!" once.
# 6) BONUS: award "badges" (print a message) when remaining_work hits certain milestones (e.g., 50%, 25%, 0%).
```

**Line-by-line breakdown:**
- **Lines 108-115:** Commented plotting code for visualization
- **Lines 117-122:** TODO list for student experiments

**Key concepts:**
- **Commented code:** Using `#` to disable code
- **Educational scaffolding:** Providing learning exercises
- **Progressive complexity:** From simple changes to advanced features

## 🎯 Key Programming Concepts Demonstrated:

### **1. Date and Time Handling**
- **String to datetime conversion:** `dt.datetime.fromisoformat()`
- **Date arithmetic:** Adding/subtracting days
- **Time differences:** Calculating durations

### **2. Mathematical Modeling**
- **Formula implementation:** Stress = 10 × urgency × backlog_ratio
- **Ratio calculations:** Work remaining vs. capacity
- **Scaling factors:** Adjusting output ranges

### **3. Control Flow**
- **For loops:** Day-by-day simulation
- **While loops:** Work session simulation
- **Conditional statements:** Urgency levels and stress labels

### **4. Data Management**
- **List operations:** Storing and retrieving data
- **List comprehensions:** Processing multiple values
- **Data validation:** Checking for invalid inputs

### **5. User Interface**
- **Formatted output:** Clear, readable results
- **Progressive disclosure:** Showing limited data
- **Visual indicators:** Emojis and labels

## 🧪 How to Experiment with This Code:

### **Experiment 1: Change Project Parameters**
```python
# Try different scenarios:
work_hours_needed = 20    # Bigger project
daily_capacity = 1        # Less time per day
start_date_str = "2025-10-01"  # Start later
```

### **Experiment 2: Modify Urgency Rules**
```python
# Make urgency harsher:
if days_left >= 10:
    urgency = 1.0
elif days_left >= 5:
    urgency = 2.0
else:
    urgency = 4.0
```

### **Experiment 3: Add Weekend Logic**
```python
# Skip weekends in work simulation:
if today.weekday() < 5:  # Monday = 0, Friday = 4
    # Do work only on weekdays
    sessions_done = 0
    while sessions_done < daily_capacity and remaining_work > 0:
        remaining_work -= 1
        sessions_done += 1
```

## 🎉 Summary:

This program demonstrates:
- **Mathematical modeling** - Converting real-world scenarios to code
- **Date handling** - Working with time-based data
- **Simulation** - Modeling complex processes
- **User experience** - Presenting results clearly
- **Educational design** - Encouraging experimentation

The code is well-structured for learning, with clear comments and opportunities for student experimentation!
