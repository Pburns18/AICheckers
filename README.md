## AI Checkers Using Minimax

This project was created by me, Peyton Burns, in an effort to continue to practice object oriented programming with SOLID principles, robust testing, and MVC architecture.

The goal of this project was to create a playable GUI based version of Checkers that has the option to play vs. an AI agent. This was achieved using the Model View Controller architecture to build out an object oriented version of the game. The Minimax algorithm was then implemented to the game along with performance improvements such as alpha beta pruning.

With the Minimax optimizations, the AI is able to explore a search depth of 5 in just a couple of seconds. I found the middle ground for performance and speed to be a search depth of 3. This was simulated in 1000 games where the AI agent played against a simulated player making random moves in which the AI agent won all 1000 games in under an hour.

The game is playable in three modes, Simulation (AI vs. Random Moves), AI vs. Player, and Player vs. Player.

![alt text](https://github.com/Pburns18/)

### Built With

* [Python](https://www.python.org/)
* [Pygame](https://www.pygame.org/)

### Getting Started & Usage
For ease of use I have created a [Jupyter Notebook](https://github.com/Pburns18/NHLAdDetection/blob/main/NHLAdDetectionInterface.ipynb) to easily interfacte with the created model. The easiest way to run this notebook would be to use Google Colab, and simply run all of the code within the notebook. The notebook will set up the environment, download 
the trained model, display some examples and training results, and run an example test detection session.

### Contact
Peyton Burns - peyton.burns.j@gmail.com

AI Checkers - [https://github.com/Pburns18/AICheckers](https://github.com/Pburns18/AICheckers)
