import copy
from CheckersModel.checkersModel import CheckersModel
from CheckersModel.gameConstants import WHITE
from CheckersView.guiView import GuiView
from CheckersView.textView import TextView
from CheckersController.checkersController import CheckersController
import argparse

""" What is next to Build Out:
1. Tighten up logic of turns - Currently we switch turns if a normal move is made
but not if a capture move is made - that is because you keep moving after a capture move
if you can continue to capture. We need to check to see if there is another capture possible
if so - do not change turns - make another move w the same piece. (Need to check if it is just double
jumps or jump then move (rule))

3. Implement win condition checking. Probably when either pieces are = 0.
"""


def main(play_type, model, view, games=100):
    if model == 'checkers':
        model = CheckersModel()
    else:
        raise NotImplementedError('This model is not implemented')

    if view == 'gui':
        view = GuiView()
    elif view == 'text':
        view = TextView()
    else:
        raise NotImplementedError('This view is not implemented')

    controller = CheckersController(model=model, view=view)

    if play_type == 'play':
        controller.run_game()
    elif play_type == 'play_ai':
        controller.play_ai()
    elif play_type == 'play_ai_vs_random':
        controller.play_ai_vs_random()
    elif play_type == 'simulation':
        run_simulation(model, view, games)

    else:
        raise NotImplementedError('This play type is not valid. Chose from: play, play_ai, '
                                  'play_ai_vs_random, and simulation')


def run_simulation(model, view, games=100):
    white = 0
    black = 0
    while games > 0:
        m = copy.deepcopy(model)
        controller = CheckersController(model=m, view=view)
        if games % 10 == 0:
            print(f'White won: {white}')
            print(f'Black won: {black}')
        winner = controller.play_ai_vs_random()
        if winner == WHITE:
            white += 1
        else:
            black += 1

        games -= 1

    print(f'White won: {white}')
    print(f'Black won: {black}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Checkers Details')
    parser.add_argument('--play_type', dest='play_type', type=str, help='Type of mode to run Checkers')
    parser.add_argument('--model', dest='model', type=str, help='Model of Checkers game')
    parser.add_argument('--view', dest='view', type=str, help='View type of Checkers game')
    parser.add_argument('--games', dest='games', type=int, help='Number of games to run in simulation option')

    args = parser.parse_args()
    main(args.play_type, args.model, args.view, args.games)
