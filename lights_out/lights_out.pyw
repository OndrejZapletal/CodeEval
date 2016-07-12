# -*- coding: utf-8 -*-
# Author: Ondrej Zapletal
# Date: 27/06/2016
# Description:
""" lights_out application. """
# import ipdb
import re
from tkinter import ttk, Tk, N, W, E, S, StringVar
import tkinter
from functools import partial


class grid(object):
    """Documentation for grid """
    def __init__(self, x, y, alive_points):
        super(grid, self).__init__()
        self._x = x
        self._y = y
        if x and y:
            self.grid = [None] * x
            for i in range(x):
                self.grid[i] = [False] * y
                for n in range(y):
                    for point in alive_points:
                        if i == point[0] and n == point[1]:
                            self.grid[i][n] = True
        else:
            self.grid = None

    def data(self):
        result = []
        for i in range(len(self.grid)):
            line = ""
            for n in range(len(self.grid[i])):
                if self.grid[i][n]:
                    line += "0"
                else:
                    line += "."
            result.append(line)
        return result

    def getitem(self, x, y):
        if self.grid[x][y]:
            return "O"
        else:
            return "."

    def toggle(self, x, y):
        if self._valid_index(x, y):
            self.grid[x][y] = not self.grid[x][y]
            if self._valid_index(x-1, y):
                self.grid[x-1][y] = not self.grid[x-1][y]

            if self._valid_index(x+1, y):
                self.grid[x+1][y] = not self.grid[x+1][y]

            if self._valid_index(x, y-1):
                self.grid[x][y-1] = not self.grid[x][y-1]

            if self._valid_index(x, y+1):
                self.grid[x][y+1] = not self.grid[x][y+1]

    def _valid_index(self, y, x):
        return (y > -1 and y < len(self.grid)) and (x > -1 and x < len(self.grid[0]))


def print_grid(grid_data):
    if isinstance(grid_data, grid):
        grid_data = grid_data.data()
    result = " |" + "".join(map(str, range(1, len(grid_data[0])+1))) + "\n"
    result = result + "-" * len(result[:-1]) + "\n"
    for i, line in enumerate(grid_data):
        result = result + str(i+1) + "|" + line + "\n"
    print(result)
    return result


def parse_line(line):
    regex = re.compile("(\d+)\s(\d+)\s(.+)")
    result = [None]*3
    result[0] = int(regex.match(line).group(1))
    result[1] = int(regex.match(line).group(2))
    alive_points = []
    for i, line in enumerate(regex.match(line).group(3).split('|')):
        for n, c in enumerate(line):
            if c == "O":
                alive_points.append([i, n])
    result[2] = alive_points
    return result


def press_button(r, c, button_reference, grid_reference):
    grid_reference.toggle(r, c)
    for i in range(grid_reference._x):
        for n in range(grid_reference._y):
            button_reference[i][n].set(grid_reference.getitem(i, n))


def main():
    """ TODO: main function description."""
    root = Tk()
    # title of window
    root.title("Light Bulbs")
    # padding - size of padding on frame
    mainframe = ttk.Frame(root, padding="5 5 5 5")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)

    [x1, y1, args1] = parse_line("4 10 ...OOOOOOO|.OO.O.O...|.OO..OO.OO|...O....O.")
    # [x1, y1, args1] = parse_line("3 3 ..O|OOO|OOO")
    # [x1, y1, args1] = parse_line("5 7 .O.O...|..O.O..|.O.O..O|.O..OOO|OO.OOOO")
    grid1 = grid(x1, y1, args1)

    button_references = [None] * x1

    for r in range(x1):
        button_references[r] = [None] * y1
        for c in range(y1):
            button_references[r][c] = StringVar()
            tkinter.Button(
                mainframe, textvariable=button_references[r][c], command=partial(
                    press_button, r, c, button_references, grid1), height=3, width=5).grid(
                        column=c, row=r, sticky=(W, E))
            button_references[r][c].set(grid1.getitem(r, c))

    # starts loop that is facilitating control of form
    root.mainloop()

if __name__ == "__main__":
    main()
