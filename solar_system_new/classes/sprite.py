"""Base game sprite"""
from turtle import Turtle
from abc import ABCMeta, abstractmethod


class Sprite(Turtle, metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        Turtle.__init__(self, shape='circle')
