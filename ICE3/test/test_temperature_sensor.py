###################################################################
# Program:              Tests for temperature_sensor
# Author:               Jayce Baxter
# Date:                 February 16th, 2025
# Description           Testing boundary values, robustness
#                       and special cases for temperature_sensor
###################################################################


import unittest

from ICE3.src import temperature_sensor
from ICE3.src.temperature_sensor import *

class TestTemperatureSensor(unittest.TestCase):

    def test_clear_list(self):
        clear_list()


    # Tests for temp input
    def test_valid_temps(self):
        self.assertEqual(add_temp("-50"), "Added to list.")
        self.assertEqual(add_temp("150"), "Added to list.")
        self.assertEqual(add_temp("20"), "Added to list.")

    def test_alpha_temps(self):
        self.assertEqual(add_temp("Test string"), "Please enter a valid number.")

    def test_temp_too_low(self):
        self.assertEqual(add_temp("-51"), "Temperature must be between -50 and 150 degrees Celsius.")
        self.assertEqual(add_temp("-500000"), "Temperature must be between -50 and 150 degrees Celsius.")

    def test_temp_too_high(self):
        self.assertEqual(add_temp("151"), "Temperature must be between -50 and 150 degrees Celsius.")
        self.assertEqual(add_temp("500000"), "Temperature must be between -50 and 150 degrees Celsius.")

    def test_null_temp(self):
        self.assertEqual(add_temp(""), "Input cannot be blank.")


    # Tests for calculations
    def calculate_empty_list(self):
        self.assertEqual(calculate(), "List is blank. Unable to calculate.")

    def calculate_valid_temps(self):
        add_temp("150")
        add_temp("-50")
        add_temp("50")

        self.assertEqual(calculate(), "The average temperature is 50.0°C.\n"
                                            "The minimum temperature is -50.0°C.\n"
                                            "The maximum temperature is 150.0°C.")