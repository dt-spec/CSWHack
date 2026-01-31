import json
import os
import tkinter as tk
from tkinter import messagebox, ttk


# File used to persist habits between runs.
DATA_FILE = "habits.json"


# Data model for one habit and its weekly progress.
class Habit:
    def __init__(self, name: str, weekly_goal: int) -> None:
        # Store the habit name and target goal for the week.
        self.name = name
        self.weekly_goal = weekly_goal
        # Track completed days (strings like "Monday").
        self.completions: list[str] = []

    def mark_complete(self, day: str) -> None:
        # Add a completion day only once.
        if day not in self.completions:
            self.completions.append(day)

    def progress_text(self) -> str:
        # Build a short progress summary with percentage.
        count = len(self.completions)
        percent = (count / self.weekly_goal) * 100 if self.weekly_goal else 0
        return f"{count}/{self.weekly_goal} ({percent:.0f}%)"

    def to_dict(self) -> dict:
        # Convert the habit to a JSON-friendly dictionary.
        return {
            "name": self.name,
            "weekly_goal": self.weekly_goal,
            "completions": self.completions,
        }

    @staticmethod
    def from_dict(data: dict) -> "Habit":
        # Rebuild a Habit object from saved data.
        habit = Habit(data["name"], int(data["weekly_goal"]))
        habit.completions = list(data.get("completions", []))
        return habit


# Main GUI application class for the habit tracker.
class HabitTrackerApp:
    def __init__(self, root: tk.Tk) -> None:
        # Store root window and initialize state.
        self.root = root
        self.root.title("Smart Habit Tracker")
        self.habits: list[Habit] = []

        # Build UI, load saved data, and show current state.
        self._build_ui()
        self._load_habits()
        self._refresh_views()

    def _build_ui(self) -> None:
        # Build the full GUI layout.
        main = ttk.Frame(self.root, padding=12)
        main.grid(row=0, column=0, sticky="nsew")

        # Allow the window to resize smoothly.
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        # Section: add a new habit.
        add_frame = ttk.LabelFrame(main, text="Add Habit", padding=10)
        add_frame.grid(row=0, column=0, sticky="ew", padx=4, pady=4)
        add_frame.columnconfigure(1, weight=1)

        ttk.Label(add_frame, text="Habit Name:").grid(row=0, column=0, sticky="w")
        self.habit_entry = ttk.Entry(add_frame)
        self.habit_entry.grid(row=0, column=1, sticky="ew", padx=6)

        ttk.Label(add_frame, text="Weekly Goal:").grid(row=0, column=2, sticky="w")
        self.goal_entry = ttk.Entry(add_frame, width=10)
        self.goal_entry.grid(row=0, column=3, sticky="w", padx=6)

        ttk.Button(add_frame, text="Add Habit", command=self.add_habit).grid(
            row=0, column=4, sticky="e"
        )

        # Section: list existing habits.
        list_frame = ttk.LabelFrame(main, text="Habits", padding=10)
        list_frame.grid(row=1, column=0, sticky="nsew", padx=4, pady=4)
        list_frame.columnconfigure(0, weight=1)
        list_frame.rowconfigure(1, weight=1)

        self.habit_listbox = tk.Listbox(list_frame, height=6)
        self.habit_listbox.grid(row=1, column=0, sticky="nsew")

        # Section: mark completion for a selected habit.
        complete_frame = ttk.LabelFrame(main, text="Mark Complete", padding=10)
        complete_frame.grid(row=2, column=0, sticky="ew", padx=4, pady=4)
        complete_frame.columnconfigure(1, weight=1)

        ttk.Label(complete_frame, text="Day:").grid(row=0, column=0, sticky="w")
        self.day_var = tk.StringVar(value="Monday")
        self.day_combo = ttk.Combobox(
            complete_frame,
            textvariable=self.day_var,
            values=[
                "Monday",
                "Tuesday",
                "Wednesday",
                "Thursday",
                "Friday",
                "Saturday",
                "Sunday",
            ],
            state="readonly",
            width=14,
        )
        self.day_combo.grid(row=0, column=1, sticky="w", padx=6)

        ttk.Button(
            complete_frame, text="Mark Complete", command=self.mark_complete
        ).grid(row=0, column=2, sticky="e")

        ttk.Button(
            complete_frame, text="Weekly Reset", command=self.reset_week
        ).grid(row=0, column=3, sticky="e", padx=6)

        # Section: summary of all habits.
        summary_frame = ttk.LabelFrame(main, text="Summary", padding=10)
        summary_frame.grid(row=3, column=0, sticky="nsew", padx=4, pady=4)
        summary_frame.columnconfigure(0, weight=1)
        summary_frame.rowconfigure(0, weight=1)

        self.summary_text = tk.Text(summary_frame, height=10, wrap="word")
        self.summary_text.grid(row=0, column=0, sticky="nsew")
        self.summary_text.configure(state="disabled")

        # Bottom action buttons.
        button_frame = ttk.Frame(main)
        button_frame.grid(row=4, column=0, sticky="ew", pady=6)
        button_frame.columnconfigure(0, weight=1)
        ttk.Button(
            button_frame, text="Save Habits", command=self._save_habits
        ).grid(row=0, column=0, sticky="w")
        ttk.Button(
            button_frame, text="Clear Inputs", command=self._clear_inputs
        ).grid(row=0, column=1, sticky="e")

    def _clear_inputs(self) -> None:
        # Clear the habit name and goal fields.
        self.habit_entry.delete(0, tk.END)
        self.goal_entry.delete(0, tk.END)

    def add_habit(self) -> None:
        # Validate inputs and add a new habit.
        name = self.habit_entry.get().strip()
        if not name:
            messagebox.showerror("Invalid Name", "Please enter a habit name.")
            return

        if any(habit.name.lower() == name.lower() for habit in self.habits):
            messagebox.showerror("Duplicate Habit", "That habit already exists.")
            return

        try:
            goal = int(self.goal_entry.get().strip())
        except ValueError:
            messagebox.showerror("Invalid Goal", "Weekly goal must be a number.")
            return

        if goal <= 0:
            messagebox.showerror("Invalid Goal", "Weekly goal must be at least 1.")
            return

        self.habits.append(Habit(name, goal))
        self._clear_inputs()
        self._refresh_views()

    def _get_selected_habit(self) -> Habit | None:
        # Get the habit selected in the listbox, if any.
        selection = self.habit_listbox.curselection()
        if not selection:
            return None
        return self.habits[selection[0]]

    def mark_complete(self) -> None:
        # Mark the selected habit complete for the chosen day.
        habit = self._get_selected_habit()
        if not habit:
            messagebox.showerror("No Habit Selected", "Select a habit first.")
            return

        day = self.day_var.get()
        habit.mark_complete(day)
        self._refresh_views()

    def reset_week(self) -> None:
        # Clear all completion data for every habit.
        if not self.habits:
            messagebox.showinfo("Nothing to Reset", "Add a habit first.")
            return

        if not messagebox.askyesno(
            "Reset Week", "Clear all weekly completions?"
        ):
            return

        for habit in self.habits:
            habit.completions.clear()
        self._refresh_views()

    def _refresh_views(self) -> None:
        # Rebuild the listbox and summary area from current data.
        self.habit_listbox.delete(0, tk.END)
        for habit in self.habits:
            label = f"{habit.name} — {habit.progress_text()}"
            self.habit_listbox.insert(tk.END, label)

        # Update the read-only summary text.
        self.summary_text.configure(state="normal")
        self.summary_text.delete("1.0", tk.END)
        if not self.habits:
            self.summary_text.insert(
                tk.END, "No habits yet. Add one to get started."
            )
        else:
            for habit in self.habits:
                self.summary_text.insert(tk.END, f"Habit: {habit.name}\n")
                self.summary_text.insert(
                    tk.END, f"  Goal: {habit.weekly_goal} times/week\n"
                )
                if habit.completions:
                    days = ", ".join(habit.completions)
                    self.summary_text.insert(tk.END, f"  Done: {days}\n")
                else:
                    self.summary_text.insert(tk.END, "  Done: none yet\n")
                self.summary_text.insert(
                    tk.END, f"  Progress: {habit.progress_text()}\n\n"
                )
        self.summary_text.configure(state="disabled")

    def _save_habits(self) -> None:
        # Save all habits to a local JSON file.
        data = [habit.to_dict() for habit in self.habits]
        try:
            with open(DATA_FILE, "w", encoding="utf-8") as handle:
                json.dump(data, handle, indent=2)
            messagebox.showinfo("Saved", "Habits saved successfully.")
        except OSError:
            messagebox.showerror("Save Failed", "Could not save habits.")

    def _load_habits(self) -> None:
        # Load habits from disk if a save file exists.
        if not os.path.exists(DATA_FILE):
            return
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as handle:
                data = json.load(handle)
            self.habits = [Habit.from_dict(item) for item in data]
        except (OSError, json.JSONDecodeError, KeyError, TypeError):
            messagebox.showerror("Load Failed", "Could not load saved habits.")


def main() -> None:
    # Create the window and start the app.
    root = tk.Tk()
    app = HabitTrackerApp(root)
    root.minsize(560, 540)
    root.mainloop()


if __name__ == "__main__":
    # Run the app only when executed directly.
    main()
