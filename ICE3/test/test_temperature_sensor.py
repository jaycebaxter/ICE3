###################################################################
# Program:              Tests for temperature_sensor
# Author:               Jayce Baxter
# Date:                 February 16th, 2025
# Description           Testing boundary values, robustness
#                       and special cases for temperature_sensor
###################################################################


import unittest

from ICE3.src import temperature_sensor

class TestTemperatureSensor(unittest.TestCase):
    def test_menu_option_low(self):
