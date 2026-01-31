# Student Task & Grade Manager

A Tkinter app that lets students add classmates, record tasks and grades, and view averages.

## What this app does
- Add students by name.
- Assign tasks with numeric grades.
- Calculate averages and letter grades.
- Show a summary of all students and their work.

## How to run
From the project root:

```bash
python "Student Task & Grade Manager/main.py"
```

## Files
- `main.py`: The full student manager app.

## How it works
- `Student` class stores a name and a list of `(task, grade)` pairs.
- `StudentManagerApp` builds the UI and handles all actions.
- Lists hold students, tasks, and grades.
- Loops calculate averages and build the summary view.
- Input validation prevents empty names, missing tasks, and invalid grades.

## User flow
1. Add a student name and click **Add Student**.
2. Select the student from the list.
3. Enter a task name and grade, then click **Add Task**.
4. View averages and letter grades in the summary panel.

## Notes for students
- This project demonstrates classes, lists, loops, functions, and error handling.
- Try adding sorting or letter-grade customization.
