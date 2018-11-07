##################################################################
# FILE : car.py
# WRITER : Lior Paz, lioraryepaz, 206240996
# EXERCISE : intro2cs ex8 2017-2018
# DESCRIPTION : contains helper class Direction and class Car
##################################################################

############################################################
# Helper class
############################################################


class Direction:
    """ Class representing a direction in 2D world. """
    UP = 12
    DOWN = 6
    LEFT = 9
    RIGHT = 3

    NOT_MOVING = ...  # Choose your own value

    VERTICAL = 0
    HORIZONTAL = 1

    ALL_DIRECTIONS = (UP, DOWN, LEFT, RIGHT)


############################################################
# Class definition
############################################################

class Car:
    """ A class representing a car in rush hour game.
    A car is 1-dimensional object that could be laid in either horizontal or
    vertical alignment. A car drives on its vertical\horizontal axis back and
    forth until reaching the board's boarders. A car can only drive to an empty
    slot (it can't override another car). """

    RED = 'R'

    def __init__(self, color, length, location, orientation):
        """
        A constructor for a Car object
        :param color: A string representing the car's color
        :param length: An int in the range of (2,4) representing the car's
        length.
        :param location: A tuple representing the car's head (x, y) location
        :param orientation: An int representing the car's orientation
        """
        self.__color = color
        self.__length = length
        self.__location = location
        self.__orientation = orientation

    def get_coordinates(self):
        """
        A method for Car object
        :return: Car's list of coordinates
        """
        coordinates_list = []
        for i in range(self.__length):
            if self.__orientation == Direction.VERTICAL:
                temp = (self.__location[0] + i, self.__location[1])
            if self.__orientation == Direction.HORIZONTAL:
                temp = (self.__location[0], self.__location[1] + i)
            coordinates_list.append(temp)
        return coordinates_list

    def get_orientation(self):
        """
        A method for Car object
        :return: Car's orientation
        """
        return self.__orientation

    def get_end_plus_coordinate(self):
        """
        A method for Car object
        :return: the proximal coordinate of the car final location
        """
        if self.__orientation == Direction.VERTICAL:
            end_plus_coordinate = (self.__location[0] + self.__length,
                                   self.__location[1])
        if self.__orientation == Direction.HORIZONTAL:
            end_plus_coordinate = (
                self.__location[0], self.__location[1] + self.__length)
        return end_plus_coordinate

    def get_pre_start_coordinate(self):
        """
        A method for Car object
        :return: the previous coordinate of the car start location
        """
        if self.__orientation == Direction.VERTICAL:
            pre_start_coordinate = (self.__location[0] - 1,
                                    self.__location[1])
        if self.__orientation == Direction.HORIZONTAL:
            pre_start_coordinate = (self.__location[0],
                                    self.__location[1] - 1)
        return pre_start_coordinate

    def get_start_plus_coordinate(self):
        """
        A method for Car object
        :return: the proximal coordinate of the car start location
        """
        if self.__orientation == Direction.VERTICAL:
            start_plus_coordinate = (self.__location[0] + 1,
                                     self.__location[1])
        if self.__orientation == Direction.HORIZONTAL:
            start_plus_coordinate = (self.__location[0],
                                     self.__location[1] + 1)
        return start_plus_coordinate

    def set_location(self, location):
        """
        A method for Car object
        :param location: new start location for the car
        :return:
        """
        self.__location = location

    def get_color(self):
        """
        A method for Car object
        :return: Car color
        """
        return self.__color

    def get_location(self):
        """
        A method for Car object
        :return: Car start location
        """
        return self.__location

    def __repr__(self):
        """
        Car representation
        :return: Car's color
        """
        return self.__color
