# Mini Game Hub

A Tkinter menu that lets students play multiple small games in one window.

## What this app does
- Choose between three games: Guess the Number, Dice Roll, and Quiz Game.
- Track attempts, roll history, and quiz score.
- Reset any game to play again.

## How to run
From the project root:

```bash
python "Mini Game Hub/main.py"
```

## Files
- `main.py`: The full game hub app and all game logic.

## Games included
### Guess the Number
- The computer picks a number from 1 to 20.
- The player keeps guessing until they get it right.
- Attempts and guess history are tracked.

### Dice Roll
- Rolls a virtual six-sided die.
- Tracks roll history and total rolls.

### Quiz Game
- Asks three short questions.
- Tracks score and shows results at the end.

## How it works
- Each game is a class (`GuessTheNumberGame`, `DiceRollGame`, `QuizGame`).
- The `GameHubApp` switches between game screens.
- Lists store guesses, rolls, and quiz answers.
- Input is validated to prevent crashes.

## Notes for students
- This project demonstrates classes, lists, loops, functions, and user input handling.
- Try adding difficulty levels or more quiz questions.
