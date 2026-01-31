import tkinter as tk
from tkinter import messagebox, ttk
from statistics import mean


# Data model for a student and their work.
class Student:
    def __init__(self, name: str) -> None:
        # Store the student's name and task list.
        self.name = name
        self.tasks: list[tuple[str, float]] = []

    def add_task(self, task: str, grade: float) -> None:
        # Add a (task, grade) pair to the student record.
        self.tasks.append((task, grade))

    def average(self) -> float | None:
        # Return the average grade or None if no tasks exist.
        if not self.tasks:
            return None
        return mean(grade for _, grade in self.tasks)


def letter_grade(avg: float) -> str:
    # Convert a numeric average to a letter grade.
    if avg >= 90:
        return "A"
    if avg >= 80:
        return "B"
    if avg >= 70:
        return "C"
    if avg >= 60:
        return "D"
    return "F"


# Main GUI application for managing students and grades.
class StudentManagerApp:
    def __init__(self, root: tk.Tk) -> None:
        # Store root window and initialize state.
        self.root = root
        self.root.title("Student Task & Grade Manager")
        self.students: list[Student] = []

        # Build UI and show initial summary.
        self._build_ui()
        self._refresh_views()

    def _build_ui(self) -> None:
        # Build the full GUI layout.
        main = ttk.Frame(self.root, padding=12)
        main.grid(row=0, column=0, sticky="nsew")

        # Allow the window to resize smoothly.
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        # Student input
        student_frame = ttk.LabelFrame(main, text="Add Student", padding=10)
        student_frame.grid(row=0, column=0, sticky="ew", padx=4, pady=4)
        student_frame.columnconfigure(1, weight=1)

        ttk.Label(student_frame, text="Student Name:").grid(
            row=0, column=0, sticky="w"
        )
        self.student_name_entry = ttk.Entry(student_frame)
        self.student_name_entry.grid(row=0, column=1, sticky="ew", padx=6)
        ttk.Button(
            student_frame, text="Add Student", command=self.add_student
        ).grid(row=0, column=2, sticky="e")

        # Task input
        task_frame = ttk.LabelFrame(main, text="Add Task & Grade", padding=10)
        task_frame.grid(row=1, column=0, sticky="ew", padx=4, pady=4)
        task_frame.columnconfigure(1, weight=1)
        task_frame.columnconfigure(3, weight=0)

        ttk.Label(task_frame, text="Task Name:").grid(row=0, column=0, sticky="w")
        self.task_name_entry = ttk.Entry(task_frame)
        self.task_name_entry.grid(row=0, column=1, sticky="ew", padx=6)

        ttk.Label(task_frame, text="Grade (0-100):").grid(row=0, column=2, sticky="w")
        self.grade_entry = ttk.Entry(task_frame, width=10)
        self.grade_entry.grid(row=0, column=3, sticky="w", padx=6)

        ttk.Button(
            task_frame, text="Add Task", command=self.add_task
        ).grid(row=0, column=4, sticky="e")

        # Students list
        list_frame = ttk.LabelFrame(main, text="Students", padding=10)
        list_frame.grid(row=2, column=0, sticky="nsew", padx=4, pady=4)
        list_frame.columnconfigure(0, weight=1)
        list_frame.rowconfigure(0, weight=1)

        self.student_listbox = tk.Listbox(list_frame, height=6)
        self.student_listbox.grid(row=0, column=0, sticky="nsew")
        self.student_listbox.bind("<<ListboxSelect>>", self._refresh_views)

        # Summary display
        summary_frame = ttk.LabelFrame(main, text="Summary", padding=10)
        summary_frame.grid(row=3, column=0, sticky="nsew", padx=4, pady=4)
        summary_frame.columnconfigure(0, weight=1)
        summary_frame.rowconfigure(0, weight=1)

        self.summary_text = tk.Text(summary_frame, height=12, wrap="word")
        self.summary_text.grid(row=0, column=0, sticky="nsew")
        self.summary_text.configure(state="disabled")

        # Bottom buttons
        button_frame = ttk.Frame(main)
        button_frame.grid(row=4, column=0, sticky="ew", pady=6)
        button_frame.columnconfigure(0, weight=1)
        ttk.Button(button_frame, text="Refresh Summary", command=self._refresh_views).grid(
            row=0, column=0, sticky="w"
        )
        ttk.Button(button_frame, text="Clear Inputs", command=self._clear_inputs).grid(
            row=0, column=1, sticky="e"
        )

    def _clear_inputs(self) -> None:
        # Clear all input fields.
        self.student_name_entry.delete(0, tk.END)
        self.task_name_entry.delete(0, tk.END)
        self.grade_entry.delete(0, tk.END)

    def add_student(self) -> None:
        # Validate and add a new student.
        name = self.student_name_entry.get().strip()
        if not name:
            messagebox.showerror("Invalid Name", "Please enter a student name.")
            return

        if any(s.name.lower() == name.lower() for s in self.students):
            messagebox.showerror("Duplicate Student", "That student already exists.")
            return

        self.students.append(Student(name))
        self.student_name_entry.delete(0, tk.END)
        self._refresh_views()

    def _get_selected_student(self) -> Student | None:
        # Return the selected student, if any.
        selection = self.student_listbox.curselection()
        if not selection:
            return None
        return self.students[selection[0]]

    def add_task(self) -> None:
        # Validate input and add a task to the selected student.
        student = self._get_selected_student()
        if not student:
            messagebox.showerror("No Student Selected", "Select a student first.")
            return

        task = self.task_name_entry.get().strip()
        if not task:
            messagebox.showerror("Invalid Task", "Please enter a task name.")
            return

        try:
            grade = float(self.grade_entry.get().strip())
        except ValueError:
            messagebox.showerror("Invalid Grade", "Grade must be a number.")
            return

        if grade < 0 or grade > 100:
            messagebox.showerror("Invalid Grade", "Grade must be between 0 and 100.")
            return

        student.add_task(task, grade)
        self.task_name_entry.delete(0, tk.END)
        self.grade_entry.delete(0, tk.END)
        self._refresh_views()

    def _refresh_views(self, _event: object | None = None) -> None:
        # Refresh the listbox and summary display.
        # Update listbox
        self.student_listbox.delete(0, tk.END)
        for student in self.students:
            avg = student.average()
            if avg is None:
                label = f"{student.name} — No grades yet"
            else:
                label = f"{student.name} — Avg: {avg:.1f} ({letter_grade(avg)})"
            self.student_listbox.insert(tk.END, label)

        # Update summary text
        self.summary_text.configure(state="normal")
        self.summary_text.delete("1.0", tk.END)

        if not self.students:
            self.summary_text.insert(
                tk.END, "No students yet. Add a student to get started."
            )
        else:
            for student in self.students:
                self.summary_text.insert(tk.END, f"Student: {student.name}\n")
                if not student.tasks:
                    self.summary_text.insert(tk.END, "  - No tasks yet\n\n")
                else:
                    for task, grade in student.tasks:
                        self.summary_text.insert(
                            tk.END, f"  - {task}: {grade:.1f}\n"
                        )
                    avg = student.average()
                    if avg is not None:
                        self.summary_text.insert(
                            tk.END,
                            f"  Average: {avg:.1f} ({letter_grade(avg)})\n\n",
                        )

        self.summary_text.configure(state="disabled")


def main() -> None:
    # Create the window and start the app.
    root = tk.Tk()
    app = StudentManagerApp(root)
    root.minsize(560, 520)
    root.mainloop()


if __name__ == "__main__":
    # Run the app only when executed directly.
    main()
