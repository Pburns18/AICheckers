## AI Checkers Using Minimax

This project was created by me, Peyton Burns, in an effort to continue to practice object oriented programming with SOLID principles, robust testing, and MVC architecture.

The goal of this project was to create a playable GUI based version of Checkers that has the option to play vs. an AI agent. This was achieved using the Model View Controller architecture to build out an object oriented version of the game. The Minimax algorithm was then implemented to the game along with performance improvements such as alpha beta pruning.

With the Minimax optimizations, the AI is able to explore a search depth of 5 in just a couple of seconds. I found the middle ground for performance and speed to be a search depth of 3. This was simulated in 1000 games where the AI agent played against a simulated player making random moves in which the AI agent won all 1000 games in under an hour.

The game is playable in three modes, Simulation (AI vs. Random Moves), AI vs. Player, and Player vs. Player.

![alt text](https://github.com/Pburns18/AICheckers/blob/main/CheckersGUIExample.png)

### Built With

* [Python](https://www.python.org/)
* [Pygame](https://www.pygame.org/)

### Getting Started & Usage
To get this game of checkers running locally you must have python3 installed and also install the Pygame package as well.

Installing Pygame:
```
python3 -m pip install -U pygame --user
```
Playing Checkers:
1. Clone the repo:
 ```
 git clone https://github.com/Pburns18/AICheckers.git 
 ```
2. Run the main.py found in the repository with the following arguments:
```
--play_type --model --view --games
```
* --play_type arguments: play, play_ai, play_ai_vs_random, simulation
* --model arguments: checkers
* --view arguments: gui, text
* --games arguments: (any integer - for determining number of games to run in a simulation)
3. An example running of the game would be:
```
python main.py --play_type simulation --model checkers --view gui --games 100
```
This would run a simulation of AI vs. player making random moves for 100 games.


### Contact
Peyton Burns - peyton.burns.j@gmail.com

AI Checkers - [https://github.com/Pburns18/AICheckers](https://github.com/Pburns18/AICheckers)
