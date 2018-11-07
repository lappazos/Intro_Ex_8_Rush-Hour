##################################################################
# FILE : board.py
# WRITER : Lior Paz, lioraryepaz, 206240996
# EXERCISE : intro2cs ex8 2017-2018
# DESCRIPTION : contains class Board
##################################################################

############################################################
# Imports
############################################################
import game_helper as gh
from car import Car, Direction


############################################################
# Class definition
############################################################


class Board:
    """
    A class representing a rush hour board.
    """

    UN_FIT_ERROR = "Direction is un-fit to car's Orientation"
    OCCUPIED_ERROR = "There is already a car in that position"
    COLOR_ERROR = "There is already a car in that color"
    OUT_OF_RANGE_ERROR = "The car location is out of range"
    ADD_OK = "The car was added successfully!"
    EXIT = 'E'
    DEFAULT_EXIT = (0,0)

    def __init__(self, cars, size=6):
        """
        Initialize a new Board object.
        :param cars: A list (or dictionary) of cars.
        :param size: Size of board (Default size is 6).
        """
        self.__size = size
        self.__exit_board = Board.DEFAULT_EXIT
        self.__cars = cars

    def add_car(self, car):
        """
        Add a single car to the board.
        :param car: A car object
        :return: True if a car was succesfuly added, or False otherwise.
        """
        coor_list = car.get_coordinates()
        for coordinate in coor_list:
            # empty spot check
            if not self.is_empty(coordinate):
                print(Board.OCCUPIED_ERROR)
                return False
            # out of range check
            if self.is_out_of_range(coordinate):
                print(Board.OUT_OF_RANGE_ERROR)
                return False
            for check_car in self.__cars:
                # exist car check
                if check_car.get_color() == car.get_color():
                    print(Board.COLOR_ERROR)
                    return False
        # in case all test came back clear - car add
        self.__cars.append(car)
        # prevent printing a message in the init of the game
        if car.get_color() != Car.RED:
            print(Board.ADD_OK)
        return True

    def is_empty(self, location):
        """
        Check if a given location on the board is free.
        :param location: x and y coordinations of location to be check
        :return: True if location is free, False otherwise
        """
        for exist_car in self.__cars:
            # go over every car
            for exist_coordinate in exist_car.get_coordinates():
                # go over every coordination in a given car
                if exist_coordinate == location:
                    return False
        return True

    def move(self, car, direction):
        """
        Move a car in the given direction.
        :param car: A Car object to be moved.
        :param direction: A Direction object representing desired direction
            to move car.
        :return: True if movement was possible and car was moved, False
        otherwise."""
        # direction fit check
        if car.get_orientation() == Direction.HORIZONTAL:
            if (direction != Direction.RIGHT) and (
                    direction != Direction.LEFT):
                print(Board.UN_FIT_ERROR)
                return False
        elif car.get_orientation() == Direction.VERTICAL:
            if (direction != Direction.UP) and (direction != Direction.DOWN):
                print(Board.UN_FIT_ERROR)
                return False
        # empty space check & out of range check
        if (direction == Direction.RIGHT) or (direction == Direction.DOWN):
            if not self.is_empty(car.get_end_plus_coordinate()):
                print(Board.OCCUPIED_ERROR)
                return False
            if self.is_out_of_range(car.get_end_plus_coordinate()):
                print(Board.OUT_OF_RANGE_ERROR)
                return False
            # in case all test came back clear - car move
            car.set_location(car.get_start_plus_coordinate())
            return True
        if (direction == Direction.LEFT) or (direction == Direction.UP):
            if not self.is_empty(car.get_pre_start_coordinate()):
                print(Board.OCCUPIED_ERROR)
                return False
            if self.is_out_of_range(car.get_pre_start_coordinate()):
                print(Board.OUT_OF_RANGE_ERROR)
                return False
            # in case all test came back clear - car move
            car.set_location(car.get_pre_start_coordinate())
            return True

    def is_out_of_range(self, location):
        """
        check if a given location is out of the board
        :param location: a given location for check
        :return: True if out of range, False if ok
        """
        for i in location:
            if i == -1:
                return True
            if i >= self.__size:
                return True
        return False

    def __repr__(self):
        """
        :return: Return a string representation of the board.
        """
        # boards init
        rep = []
        # blanks fill
        for i in range(self.__size):
            temp = []
            for j in range(self.__size + 1):
                temp.append('_')
            rep.append(temp)
        # index fill
        temp = ['_']
        for j in range(self.__size):
            temp.append(str(j))
            rep[j][0] = str(j)
        rep.append(temp)
        # exit fill
        x, y = self.__exit_board
        rep[x][y] = Board.EXIT
        # Cars fill
        for car in self.__cars:
            for coordinate in car.get_coordinates():
                x, y = coordinate
                y += 1
                rep[x][y] = str(car)
        # lines adjustments
        result = str()
        for line in rep:
            result += str(line) + '\n'
        return result

    def get_cars(self):
        """
        A Board class method
        :return: list of board Cars
        """
        return self.__cars

    def get_size(self):
        """
        A Board class method
        :return: size of board
        """
        return self.__size

    def set_exit(self, exit):
        """
        A Board class method
        :param exit: a given exit from  board location
        :return:
        """
        self.__exit_board = exit
