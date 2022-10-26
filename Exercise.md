# TicTacToe with NamedTuples
Implement the game of Tic Tac Toe in python, where a human can play against the computer.

## Part 1 -- Model
Implement your model code in `tic_tac_toe_model.py`.
In this file, you should:
* Define a namedtuple to represent the tic tac toe game state.
* Define methods that are useful in interpreting the state, and making moves to manipulate the state (if it is mutable), or create new states if it is immutable.
* Validate that moves made are valid, and throw an invalid move exception (see part 2) if they are not

Hints
* All functions in your model file should be pure (no i/o or global variables) -- the model is not concerned about how the game is played
* Consider which data structures are best suited to model each part of the game
* Try to make an elegant function to determine if the game is over
* Think carefully about function and variable naming
* Use list comprehensions where possible


## Part 2 -- Exception
Define your own invalid move exception in the file `tic_tac_toe_move_exception.py`

## Part 3 -- Tests
Define tests in `tic_tac_toe_model_test.py` to cover every function in `tic_tac_toe_model.py`

## Part 4 -- Game
Define the logic to play the game through a terminal in `tic_tac_toe_game.py`

The computer player logic and rendering code can be placed in this file or another if you wish.

It is not required to make the computer player intelligent, but it should always make a valid move.


# Optional Parts
## Persistence
Make it possible to store the state of a game to a file, and resume it later. Ensure that this logic resides in a separate module and is appropriately integration tested.

## Master A.I.
Write an A.I. that plays the [perfect game](https://en.wikipedia.org/wiki/Solved_game#Perfect_play)

## UI
Using the framework of your choice, make it possible to click on a cell to make a move there.

# Exercise etiquette
Please populate the files indicated for each part (in the `exercise` folder of your branch). 