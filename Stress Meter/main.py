# ==========================================
# STRESS METER - TEACHING SKELETON (PYTHON)
# Concepts: variables, input, for-loop, while-loop, if/elif/else, lists
# Optional: basic plotting (matplotlib)
# ==========================================

# ---- 0) Imports (ONLY if you use dates/plotting later) ----
import datetime as dt
# import matplotlib.pyplot as plt  # <- OPTIONAL (uncomment when ready)

# ---- 1) Inputs (students can EDIT these numbers) ----
# TODO: Change these and re-run to see how the output changes
due_date_str     = "2025-10-05"   # YYYY-MM-DD
start_date_str   = "2025-09-28"   # YYYY-MM-DD
work_hours_needed = 10            # total hours needed to finish the task
daily_capacity    = 2             # how many hours you can realistically do each day

# ---- 2) Parse dates + compute how many days we have ----
due   = dt.datetime.fromisoformat(due_date_str)
start = dt.datetime.fromisoformat(start_date_str)
total_days = (due - start).days

# Guard rail: make sure we have at least 1 day
if total_days <= 0:
    print("⚠️ Start date is not before the due date. Adjusting to 1 day.")
    total_days = 1

# ---- 3) Prepare storage for results ----
dates  = []       # list of each date in the plan
stress = []       # list of stress values for each day

# Remaining work at the beginning
remaining_work = work_hours_needed

# ==========================================
# FOR LOOP: simulate day-by-day progression
# ==========================================
for i in range(total_days + 1):
    # current day = start date + i days
    today = start + dt.timedelta(days=i)
    days_left = (due - today).days

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

    # A simple "how behind am I?" ratio:
    # (work left) / (how much I can do before the deadline)
    # Add +1 to days_left so we never divide by zero on the due day
    capacity_left = (days_left + 1) * max(1, daily_capacity)
    backlog_ratio = remaining_work / capacity_left

    # Compute today's stress score
    # Scale 0..something; students can tweak the 10x
    today_stress = 10 * urgency * backlog_ratio

    # Save results
    dates.append(today.date())   # store as date only
    stress.append(today_stress)

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
