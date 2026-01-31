# Smart Habit Tracker

A simple Tkinter app that lets students create habits, mark daily progress, and view a weekly summary. Habits can also be saved to a local JSON file.

## What this app does
- Add habits with a name and weekly goal.
- Mark habits complete for a specific day.
- Show progress counts and percentages.
- Display a readable summary for all habits.
- Optionally reset all progress for a new week.
- Save and load habits between runs.

## How to run
From the project root:

```bash
python "Smart Habit Tracker/main.py"
```

## Files
- `main.py`: The full Tkinter app.
- `habits.json`: Auto-created when you click "Save Habits".

## How it works
- `Habit` class stores a habit name, weekly goal, and a list of completed days.
- `HabitTrackerApp` builds the UI and connects buttons to logic.
- The app uses lists to store all habits and their completion days.
- Each update runs through the habits list and refreshes the display.
- Input validation prevents empty names, duplicates, and invalid goals.

## User flow
1. Enter a habit name and weekly goal, then click **Add Habit**.
2. Select the habit in the list.
3. Pick a day and click **Mark Complete**.
4. View progress in the list and in the summary area.
5. Use **Weekly Reset** to clear all completions for a new week.
6. Use **Save Habits** to store progress to `habits.json`.

## Notes for students
- This project demonstrates classes, lists, loops, functions, and error handling.
- Try adding new features like streaks or daily reminders.
