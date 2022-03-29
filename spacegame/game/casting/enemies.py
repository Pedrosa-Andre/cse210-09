from game.casting.actor import Actor
import pygame
from game.shared.gameconstants import *
import random
from game.services.keyboard_service import KeyboardService
import time
from game.shared.gameconstants import *


class Enemies(Actor):


    def __init__(self, pos, num=0):
        """
        """
        super().__init__()
        self.set_position(pos)

        #self._keyboard_service = KeyboardService()
        self._dead = False
        self._previous_position = pos
        self._t = time.perf_counter()
        self._enemy_image = ENEMY_IMAGE

    def get_image(self):
        return self._image

    def get_direction(self):
        """
        """
        velocity = self._keyboard_service.get_direction()
        return velocity

    def die(self):
        """
        """
        self._dead = True

    def is_shooting(self):
        """
        """


        return self._keyboard_service.is_shooting()

    def is_recharged(self):
        t_now = time.perf_counter()
        diff = t_now - self._t
        return diff > 1

    def uncharge(self):
        self._t = time.perf_counter()
