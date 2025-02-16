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

    ##### BOUNDARY VALUE ANALYSIS #####

    # Test minimum boundary
    def test_min_boundary(self):
        self.assertEqual(add_temp("-50"), "Added to list.")

    # Test maximum boundary
    def test_max_boundary(self):
        self.assertEqual(add_temp("150"), "Added to list.")

    # Tests near boundary
    def test_near_boundary(self):
        self.assertEqual(add_temp("-49"), "Added to list.")
        self.assertEqual(add_temp("149"), "Added to list.")


    #### ROBUSTNESS TESTING ####

    # Test mixed valid and invalid inputs
    def test_mixed_valid(self):
        self.assertEqual(add_temp("-60"), "Temperature must be between -50 and 150 degrees Celsius.")
        self.assertEqual(add_temp("20"), "Added to list.")
        self.assertEqual(add_temp("160"), "Temperature must be between -50 and 150 degrees Celsius.")

    # Test inputting letters
    def test_alpha_temps(self):
        self.assertEqual(add_temp("Test string"), "Please enter a valid number.")

    # Test special characters
    def test_special_char(self):
        self.assertEqual(add_temp("%"), "Please enter a valid number.")
        self.assertEqual(add_temp("/"), "Please enter a valid number.")


    ##### SPECIAL SCENARIOS #####

    # Test very large negative values
    def test_very_low(self):
        self.assertEqual(add_temp("-100000000000"), "Temperature must be between -50 and 150 degrees Celsius.")
        self.assertEqual(add_temp("-2**31"), "Please enter a valid number.")

    # Test very large positive values
    def test_very_high(self):
        self.assertEqual(add_temp("100000000000"), "Temperature must be between -50 and 150 degrees Celsius.")
        self.assertEqual(add_temp("2**31 - 1"), "Please enter a valid number.")

    def test_null_temp(self):
        self.assertEqual(add_temp(""), "Input cannot be blank.")


    ##### SPECIAL SCENARIOS #####

    # Test calculating an empty list
    def test_calculate_empty_list(self):
        self.assertEqual(calculate(), "List is blank. Unable to calculate.")

    # Test just outside of the boundary
    def test_out_of_bounds(self):
        self.assertEqual(add_temp("-51"), "Temperature must be between -50 and 150 degrees Celsius.")
        self.assertEqual(add_temp("151"), "Temperature must be between -50 and 150 degrees Celsius.")

    # Test valid temperatures to see that math is correct
    def test_calculate_valid_temps(self):
        add_temp("150")
        add_temp("-50")
        add_temp("50")

        self.assertEqual(calculate(), "The average temperature is 50.0°C.\n"
                                            "The minimum temperature is -50.0°C.\n"
                                            "The maximum temperature is 150.0°C.")
