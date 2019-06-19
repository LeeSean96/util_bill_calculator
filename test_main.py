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

class TestPayee(unittest.TestCase):

    def test_total_days(self):
        payee = main.Payee('name', [
             main.Relevant_Day(date(2019, 5, 1), date(2019, 5, 10), True),
             main.Relevant_Day(date(2019, 5, 11), date(2019, 5, 20), True),
            ])
        self.assertEqual(payee.calc_total_absent_days(), 20)

def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(TestRelevantDay('test_inclusive_day_sum'))
    suite.addTest(TestRelevantDay('test_exclusive_day_sum'))
    suite.addTest(TestPayee('test_total_days'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(test_suite())
