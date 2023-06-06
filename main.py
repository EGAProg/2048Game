from tkinter import *
from creational.Game import Game
from creational.Board import Board

panel = Board()
root = Game(panel)
root.start()