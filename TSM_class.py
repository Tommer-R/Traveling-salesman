#  Copyright (c) 2021. | by: Tommer Rissin | github: github.com/Tommer-R

import random
from math import dist, cos, sin, pi

import matplotlib.pyplot as plt


class TSM:
    def __init__(self, locations: int = 10, circle: bool = False) -> None:
        """
        generates n 2D locations on matrix of 1000*1000 in circle shape or random scatter.
        :param locations: the number of locations to generate
        :param circle: generate locations in circle shape or randomly
        """
        self.__circle = circle  # if locations should be arranged in a circle
        # dict with location ID as key and location in tuple {1:(10,42)}
        self.locations = self.__gen_locations(locations)
        self.__initial_route = list(self.locations.keys())  # optimal state in circle form, first state in general
        self.__initial_cost = self.cost(self.__initial_route)  # cost of op_route

    # generate a list of random cities
    def __gen_locations(self, locations):  # generate dict of locations
        result = {}
        if self.__circle:  # arrange locations in a circle
            dr = (2 * pi) / locations
            for i in range(locations):  # create n locations
                radians = dr * i
                result[i] = (cos(radians) * 1000, sin(radians) * 1000)

            return result

        elif not self.__circle:  # arrange locations randomly
            for i in range(locations):  # create n locations
                result[i] = (random.randint(1, 1000), random.randint(1, 1000))
            return result

    # add one new location with input coordinates
    def add_location(self, x: int, y: int, name: any = None) -> None:
        for i in {x, y}:
            if not 1 <= i <= 1000 or type(i) not in {int, float}:
                raise ValueError(f'x and y must be numbers in range [1, 1000]')

        if name is not None:
            new_key = name
        else:
            new_key = 1
            while True:
                if new_key not in self.locations.keys():
                    break
                else:
                    new_key += 1

        self.locations[new_key] = (x, y)
        self.__initial_route.append(new_key)
        self.__initial_cost = self.cost(self.__initial_route)  # cost of op_route

    # calculate the cost (sum distance) of a route
    def cost(self, route: list = None) -> float:  # calculate the cost of a state
        """
        calculates the total distance of the input state.
        :param route: list of ID keys of the locations.
        :return: float of sum state distance.
        """
        result = 0.0
        if route:  # check if state is empty
            for i in range(len(route) - 1):  # iterate locations and sum distances
                a = self.locations[route[i]]  # first location
                b = self.locations[route[i + 1]]  # second location
                distance = dist(a, b)  # distance between the 2 locations
                result += distance  # add distance to sum
            return result
        else:  # raise Error if empty
            raise ValueError('temp_route is empty')

    # show a plot of the locations and a route if there is one
    def plot(self, route: list = None, labels: bool = False) -> None:
        """
        plots the locations in a scatter plot and route if provided or the first route
        :param route: list of location ID's in as the route
        :param labels: show ID's on top of scatter plot.
        """
        if route is None:  # if state is empty use start_route
            x = [self.locations[key][0] for key in self.__initial_route]
            y = [self.locations[key][1] for key in self.__initial_route]
            plt.title(f'Distance: {round(self.cost(route=self.__initial_route), 1)}')
        else:  # use input state
            x = [self.locations[key][0] for key in route]
            y = [self.locations[key][1] for key in route]
            plt.title(f'Distance: {round(self.cost(route=route), 1)}')
        plt.plot(x, y, zorder=1)  # plot the state
        plt.scatter(x, y, s=50, c='red', zorder=2)  # scatter the locations
        for i in self.locations.keys():  # create labels
            x = self.locations[i][0]
            y = self.locations[i][1]
            label = str(i)
            if labels:  # add labels to plot
                plt.annotate(label, (x, y), xytext=(0, 10), textcoords="offset points", ha='center')
        plt.show()

    def random_route(self, seed: any = None) -> list:
        """
        :param seed: the seed for random functions
        :return: a list representing a randomized route
        """
        result = self.__initial_route.copy()  # random state
        if seed is not None:
            random.seed(seed)
        random.shuffle(result)  # shuffle the random state

        return result

    @property
    def circle(self):
        return self.__circle

    @property
    def initial_route(self):
        return self.__initial_route
