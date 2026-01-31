import random
import tkinter as tk
from tkinter import messagebox, ttk


# Game logic for guessing a hidden number.
class GuessTheNumberGame:
    def __init__(self) -> None:
        # Initialize game state.
        self.reset()

    def reset(self) -> None:
        # Pick a new secret and clear attempts/guesses.
        self.secret = random.randint(1, 20)
        self.attempts = 0
        self.guesses: list[int] = []

    def make_guess(self, guess: int) -> str:
        # Record the guess and return a hint.
        self.attempts += 1
        self.guesses.append(guess)
        if guess < self.secret:
            return "Too low!"
        if guess > self.secret:
            return "Too high!"
        return "Correct!"


# Game logic for rolling a die.
class DiceRollGame:
    def __init__(self) -> None:
        # Track roll history.
        self.rolls: list[int] = []

    def roll(self) -> int:
        # Roll a six-sided die and store the result.
        value = random.randint(1, 6)
        self.rolls.append(value)
        return value


# Game logic for a short quiz.
class QuizGame:
    def __init__(self) -> None:
        # Store question/answer pairs and progress.
        self.questions = [
            ("What is the capital of France?", "Paris"),
            ("How many continents are there?", "7"),
            ("What planet is known as the Red Planet?", "Mars"),
        ]
        self.index = 0
        self.score = 0
        self.answers: list[str] = []

    def current_question(self) -> str:
        # Return the current question prompt.
        return self.questions[self.index][0]

    def answer(self, response: str) -> bool:
        # Check the response and update score/progress.
        correct = self.questions[self.index][1].lower()
        is_correct = response.strip().lower() == correct
        self.answers.append(response)
        if is_correct:
            self.score += 1
        self.index += 1
        return is_correct

    def has_more(self) -> bool:
        # True if there are unanswered questions.
        return self.index < len(self.questions)

    def reset(self) -> None:
        # Restart the quiz.
        self.index = 0
        self.score = 0
        self.answers.clear()


# Main GUI application for the mini game hub.
class GameHubApp:
    def __init__(self, root: tk.Tk) -> None:
        # Store root window and set up games.
        self.root = root
        self.root.title("Mini Game Hub")

        self.guess_game = GuessTheNumberGame()
        self.dice_game = DiceRollGame()
        self.quiz_game = QuizGame()

        # Build UI and show the default game.
        self._build_ui()
        self._show_guess_game()

    def _build_ui(self) -> None:
        # Build the app layout and top menu.
        main = ttk.Frame(self.root, padding=12)
        main.grid(row=0, column=0, sticky="nsew")

        # Allow the window to resize smoothly.
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        # Menu buttons to switch between games.
        menu_frame = ttk.LabelFrame(main, text="Choose a Game", padding=10)
        menu_frame.grid(row=0, column=0, sticky="ew", padx=4, pady=4)
        ttk.Button(menu_frame, text="Guess the Number", command=self._show_guess_game).grid(
            row=0, column=0, padx=4
        )
        ttk.Button(menu_frame, text="Dice Roll", command=self._show_dice_game).grid(
            row=0, column=1, padx=4
        )
        ttk.Button(menu_frame, text="Quiz Game", command=self._show_quiz_game).grid(
            row=0, column=2, padx=4
        )

        # Container where the active game UI is shown.
        self.game_frame = ttk.Frame(main, padding=10)
        self.game_frame.grid(row=1, column=0, sticky="nsew")
        self.game_frame.columnconfigure(0, weight=1)
        self.game_frame.rowconfigure(0, weight=1)

    def _clear_game_frame(self) -> None:
        # Remove all widgets in the game frame.
        for widget in self.game_frame.winfo_children():
            widget.destroy()

    def _show_guess_game(self) -> None:
        # Build the Guess the Number UI.
        self._clear_game_frame()

        frame = ttk.LabelFrame(self.game_frame, text="Guess the Number", padding=10)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.columnconfigure(1, weight=1)

        ttk.Label(frame, text="Guess a number (1-20):").grid(row=0, column=0, sticky="w")
        guess_entry = ttk.Entry(frame, width=10)
        guess_entry.grid(row=0, column=1, sticky="w", padx=6)

        result_label = ttk.Label(frame, text="Make a guess!")
        result_label.grid(row=1, column=0, columnspan=3, sticky="w", pady=6)

        attempts_label = ttk.Label(frame, text="Attempts: 0")
        attempts_label.grid(row=2, column=0, columnspan=3, sticky="w")

        def submit_guess() -> None:
            # Validate input and submit a guess.
            value = guess_entry.get().strip()
            try:
                guess = int(value)
            except ValueError:
                messagebox.showerror("Invalid Guess", "Enter a whole number.")
                return

            if guess < 1 or guess > 20:
                messagebox.showerror("Invalid Guess", "Pick a number from 1 to 20.")
                return

            message = self.guess_game.make_guess(guess)
            result_label.config(text=message)
            attempts_label.config(text=f"Attempts: {self.guess_game.attempts}")
            if message == "Correct!":
                messagebox.showinfo(
                    "You Win",
                    f"Correct in {self.guess_game.attempts} attempts!",
                )

        def reset_game() -> None:
            # Reset the guessing game UI state.
            self.guess_game.reset()
            result_label.config(text="Make a guess!")
            attempts_label.config(text="Attempts: 0")
            guess_entry.delete(0, tk.END)

        ttk.Button(frame, text="Guess", command=submit_guess).grid(
            row=0, column=2, sticky="e"
        )
        ttk.Button(frame, text="Reset Game", command=reset_game).grid(
            row=3, column=0, pady=6, sticky="w"
        )

        history_text = tk.Text(frame, height=6, wrap="word")
        history_text.grid(row=4, column=0, columnspan=3, sticky="nsew", pady=6)
        history_text.configure(state="disabled")

        def update_history() -> None:
            # Refresh the guess history box.
            history_text.configure(state="normal")
            history_text.delete("1.0", tk.END)
            if self.guess_game.guesses:
                history_text.insert(
                    tk.END,
                    "Guesses: " + ", ".join(str(g) for g in self.guess_game.guesses),
                )
            else:
                history_text.insert(tk.END, "No guesses yet.")
            history_text.configure(state="disabled")

        def submit_and_update() -> None:
            # Combine guess submission with history refresh.
            submit_guess()
            update_history()

        def reset_and_update() -> None:
            # Combine reset with history refresh.
            reset_game()
            update_history()

        ttk.Button(frame, text="Guess + Track", command=submit_and_update).grid(
            row=0, column=3, sticky="e", padx=6
        )
        ttk.Button(frame, text="Reset + Clear", command=reset_and_update).grid(
            row=3, column=1, pady=6, sticky="w"
        )

        # Initialize history display.
        update_history()

    def _show_dice_game(self) -> None:
        # Build the Dice Roll UI.
        self._clear_game_frame()

        frame = ttk.LabelFrame(self.game_frame, text="Dice Roll", padding=10)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.columnconfigure(0, weight=1)

        result_label = ttk.Label(frame, text="Roll the dice!")
        result_label.grid(row=0, column=0, sticky="w")

        roll_count = ttk.Label(frame, text="Rolls: 0")
        roll_count.grid(row=1, column=0, sticky="w", pady=4)

        history_text = tk.Text(frame, height=6, wrap="word")
        history_text.grid(row=2, column=0, sticky="nsew", pady=6)
        history_text.configure(state="disabled")

        def roll_dice() -> None:
            # Roll and update the UI.
            value = self.dice_game.roll()
            result_label.config(text=f"You rolled a {value}!")
            roll_count.config(text=f"Rolls: {len(self.dice_game.rolls)}")
            history_text.configure(state="normal")
            history_text.delete("1.0", tk.END)
            history_text.insert(
                tk.END, "History: " + ", ".join(str(r) for r in self.dice_game.rolls)
            )
            history_text.configure(state="disabled")

        def reset_dice() -> None:
            # Clear history and reset UI.
            self.dice_game.rolls.clear()
            result_label.config(text="Roll the dice!")
            roll_count.config(text="Rolls: 0")
            history_text.configure(state="normal")
            history_text.delete("1.0", tk.END)
            history_text.insert(tk.END, "History: none yet.")
            history_text.configure(state="disabled")

        ttk.Button(frame, text="Roll", command=roll_dice).grid(row=3, column=0, sticky="w")
        ttk.Button(frame, text="Reset", command=reset_dice).grid(
            row=3, column=0, sticky="e"
        )

    def _show_quiz_game(self) -> None:
        # Build the Quiz UI.
        self._clear_game_frame()

        frame = ttk.LabelFrame(self.game_frame, text="Quiz Game", padding=10)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.columnconfigure(0, weight=1)

        question_label = ttk.Label(frame, text=self.quiz_game.current_question())
        question_label.grid(row=0, column=0, sticky="w")

        answer_entry = ttk.Entry(frame)
        answer_entry.grid(row=1, column=0, sticky="ew", pady=6)

        feedback_label = ttk.Label(frame, text="Enter your answer.")
        feedback_label.grid(row=2, column=0, sticky="w")

        score_label = ttk.Label(frame, text="Score: 0")
        score_label.grid(row=3, column=0, sticky="w")

        def submit_answer() -> None:
            # Validate input, check the answer, and update UI.
            if not self.quiz_game.has_more():
                messagebox.showinfo("Quiz Done", "No more questions.")
                return

            response = answer_entry.get().strip()
            if not response:
                messagebox.showerror("Invalid Answer", "Please enter an answer.")
                return

            correct = self.quiz_game.answer(response)
            feedback_label.config(text="Correct!" if correct else "Not quite.")
            score_label.config(
                text=f"Score: {self.quiz_game.score}/{len(self.quiz_game.questions)}"
            )
            answer_entry.delete(0, tk.END)

            if self.quiz_game.has_more():
                question_label.config(text=self.quiz_game.current_question())
            else:
                messagebox.showinfo(
                    "Quiz Complete",
                    f"Final score: {self.quiz_game.score}/{len(self.quiz_game.questions)}",
                )

        def reset_quiz() -> None:
            # Restart the quiz and reset the UI.
            self.quiz_game.reset()
            question_label.config(text=self.quiz_game.current_question())
            feedback_label.config(text="Enter your answer.")
            score_label.config(text="Score: 0")
            answer_entry.delete(0, tk.END)

        ttk.Button(frame, text="Submit", command=submit_answer).grid(
            row=4, column=0, sticky="w"
        )
        ttk.Button(frame, text="Reset Quiz", command=reset_quiz).grid(
            row=4, column=0, sticky="e"
        )


def main() -> None:
    # Create the window and start the app.
    root = tk.Tk()
    app = GameHubApp(root)
    root.minsize(560, 520)
    root.mainloop()


if __name__ == "__main__":
    # Run the app only when executed directly.
    main()
