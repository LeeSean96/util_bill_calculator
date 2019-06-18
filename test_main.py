import main
from datetime import date
import unittest

class TestRelevantDay(unittest.TestCase):
    
    def test_inclusive_day_sum(self):
        day = main.Relevant_Day(date(2019, 5, 1), date(2019, 5, 10), True)
        self.assertEqual(day.calc_num_of_days(), 10)

    def test_exclusive_day_sum(self):
        day = main.Relevant_Day(date(2019, 5, 1), date(2019, 5, 10), False)
        self.assertEqual(day.calc_num_of_days(), 9)
