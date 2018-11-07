##################################################################
# FILE : game.py
# WRITER : Lior Paz, lioraryepaz, 206240996
# EXERCISE : intro2cs ex8 2017-2018
# DESCRIPTION : main File - contains class Game
##################################################################

############################################################
# Imports
############################################################
import game_helper as gh
from random import randint
from car import Car, Direction
from board import Board


############################################################
# Class definition
############################################################


class Game:
    """
    A class representing a rush hour game.
    A game is composed of cars that are located on a square board and a user
    which tries to move them in a way that will allow the red car to get out
    through the exit
    """

    MOVE_CAR_INPUT = 'What color car would you like to move?'
    NO_CAR = 'There is no such car on board'
    WELCOME = 'Welcome to rush Hour game'

    def __init__(self, board):
        """
        Initialize a new Game object.
        :type board: object
        :param board: An object of type board
        """
        self.__board = board

    def __single_turn(self):
        """
        The function runs one round of the game :
            1. Print board to the screen
            2. Get user's input of: what color car to move, and what direction
            to move it.
            2.a. Check the the input is valid. If not, print an error message
            and return to step 2.
            2. Move car according to user's input. If movement failed (trying
                to move out of board etc.), return to step 2.
            3. Report to the user the result of current round ()
        """
        color = None
        check = False
        # continue to ask as long as the users input is wrong color
        while check is False:
            print(Game.MOVE_CAR_INPUT)
            color = input()
            for car in self.__board.get_cars():
                if color == car.get_color():
                    check = True
                    color = car
            if check is False:
                print(Game.NO_CAR)
        direction = gh.get_direction()
        # the round ends with moving the car
        return self.__board.move(color, direction)

    def play(self):
        """
        The main driver of the Game. Manages the game until completion.
        :return: None
        """
        print(Game.WELCOME)
        # randomize red car size
        if self.__board.get_size() > 7:
            length = randint(2, 4)
        elif self.__board.get_size() > 5:
            length = randint(2, 3)
        else:
            length = 2
        # setting red_car and exit_board
        if randint(0, 1) is 0:
            exit_board = (randint(0, self.__board.get_size() - 1), 0)
            pre_exit_board = exit_board
            red_car = Car(Car.RED, length, (exit_board[0],
                                            self.__board.get_size() -
                                            length), Direction.HORIZONTAL)
        else:
            exit_board = (
                self.__board.get_size(), randint(1, self.__board.get_size()))
            pre_exit_board = (exit_board[0] - 1, exit_board[1] - 1)
            red_car = Car(Car.RED, length, (0, exit_board[1] - 1),
                          Direction.VERTICAL)
        self.__board.add_car(red_car)
        self.__board.set_exit(exit_board)
        # initial board print
        print(self.__board)
        # Cars adding process
        for car in range(gh.get_num_cars()):
            check = False
            # repeat of car adding process as long as it fails
            while not check:
                check = self.new_car_request()
            print(self.__board)
        # the game_over monitor
        while pre_exit_board not in red_car.get_coordinates():
            self.__single_turn()
            print(self.__board)
        gh.report_game_over()

    def new_car_request(self):
        """
        A method for Game object
        :return: True Or False for car adding process success
        """
        # setting Car object according user input parameters
        car_color, car_length, car_location, car_orient = gh.get_car_input(
            self.__board.get_size())
        car = Car(car_color, car_length, (car_location[1], car_location[
            0]), car_orient)
        return self.__board.add_car(car)


############################################################
if __name__ == "__main__":
    # randomize board size
    board = Board([], randint(5, 9))
    game = Game(board)
    game.play()
