###################################################################
# Program:              Tests for temperature_sensor
# Author:               Jayce Baxter
# Date:                 February 16th, 2025
# Description           Testing boundary values, robustness
#                       and special cases for temperature_sensor
###################################################################


import unittest

from ICE3.src import temperature_sensor
from ICE3.src.temperature_sensor import menu_options

class TestTemperatureSensor(unittest.TestCase):

    def test_menu_low(self):
        self.assertEqual()