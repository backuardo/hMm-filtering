from random import *
# RoboMaze.py
# Eisner Nov 2017
#
# This class is responsible for generating a 4 x 4 maze with n randomly
# placed walls, and randomly coloring the maze positions red, green, blue, or
# yellow. It also generates a random sequence of steps a robot took, and can
# display the maze.


class RoboMaze:
    def __init__(self, num_walls, num_steps):
        """
        :param num_walls: number of walls in the maze
        :param num_steps: number of steps in the sequence
        """
        self.num_walls = num_walls
        self.num_steps = num_steps
        self.w = set()  # Wall locations
        self.b = [      # Boarder locations
            {0, 1, 2, 3},
            {12, 13, 14, 15},
            {3, 7, 11, 15},
            {0, 4, 8, 12},
        ]
        self.maze = self.generate_maze()  # Maze representation in a list
        self.sequence = self.generate_sequence()  # Random robot sequence

    def generate_maze(self):
        """
        Builds a randomly colored 4 x 4 maze with randomly placed walls.

        :return: a maze in list form
        """
        colors = ['r', 'g', 'b', 'y']
        maze = [colors[randint(0, 3)] for i in range(16)]

        i = self.num_walls
        while i > 0:
            wall_loc = randint(0, 15)
            if maze[wall_loc] is not 'X':
                maze[wall_loc] = 'X'
                self.w.add(wall_loc)
                i -= 1

        return maze

    def display_maze(self):
        """
        Displays a maze
        """
        print(self.maze[0:4])
        print(self.maze[4:8])
        print(self.maze[8:12])
        print(self.maze[12:16])

    def generate_sequence(self):
        """
        Randomly generates a robot movement sequence

        :return: a sequence in list form
        """
        # move maps a direction to it's effect on position
        move = {0: -4,
                1: 4,
                2: 1,
                3: -1}

        # s is a sequence of indices in maze, initialized with start position
        s = [choice([i for i in range(16) if i not in self.w])]

        for i in range(self.num_steps - 1):
            pos = s[-1]        # Current position
            d = randint(0, 3)  # 0: north, 1: south, 2: east, 3: west

            if (pos not in self.b[d]) and ((pos + move[d]) not in self.w):
                s.append(pos + move[d])
                continue

            s.append(pos)

        return s



