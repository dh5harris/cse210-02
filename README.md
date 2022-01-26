#cse210-02
#Team project file for CSE 210

# Team contributors - Weylin Douglas, Daniel Harris, Kirsten Jackson, Christi Johnson, Christian Mijangos

```
Team contributors -
  Weylin Douglas Weylin76@msn.com,
  Daniel Harris har21072@byui.edu,
  Kirsten Jackson jac19019@byui.edu,
  Christi Johnson joh21088@byui.edu,
  Christian Mijangos mij17001@byui.edu
```

# Hilo

Hilo is a game in which the player guesses if the next card drawn by the dealer will be higher or lower than
the previous one. Points are won or lost based on whether or not the player guessed correctly.

# Rules

The player starts the game with 300 points.
Individual cards are represented as a number from 1 to 13.
The current card is displayed.
The player guesses if the next one will be higher or lower.
Then the next card is displayed.

# Points

The player earns 100 points if they guessed correctly.
The player loses 75 points if they guessed incorrectly.
If a player reaches 0 points the game is over.
If a player has more than 0 points they decide if they want to keep playing.
If a player decides not to play again the game is over.

# Getting Started

---

Use Python 3.8.x or newer installed and running on your machine. Open a terminal and browse to the project's
root folder. Start the program by running the following command

```
python.exe hilo
```

## Project Structure

The project files and folders are organized as follows:

```

root                    (project root folder)
+-- hilo                (source code for game)
  +-- director          (specific classes)
  +-- __main__.py       (program entry point)
+-- README.md           (general info)

```
