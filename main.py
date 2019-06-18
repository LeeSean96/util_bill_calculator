from datetime import date
from typing import List

class Relevant_Day:
    def __init__(self, begin_date: date, end_date: date, is_inclusive: bool):
        self.begin_date = begin_date
        self.end_date = end_date
        self.is_inclusive = is_inclusive

    def calc_num_of_days(self) -> int:
        """ Calculate the duration between two dates. """
        return (self.end_date - self.begin_date).days + int(self.is_inclusive)

class Payee:
    """ A shareholder of some duty. """
    def __init__(self, name: str, absent_days: List[Relevant_Day]):
        self.name = name
        self.absent_days = absent_days
        self.billable_amount = 0

    def calc_total_absent_days(self) -> int:
        """ Iterates through the list of days and sum the number of days. """
        total_day = 0
        for absent_day in self.absent_days:
            total_day += absent_day.calc_num_of_days()
        return total_day


def calc_share_of_costs(period: Relevant_Day, cost: float, payees: List[Payee]):
    """ Returns a list of payees with their billable amount property set. """
    duration = period.calc_num_of_days()
    billable_days = 0
    for payee in payees:
        billable_days += duration - payee.calc_total_absent_days()

    for payee in payees:
        payee.billable_amount = (duration - payee.calc_total_absent_days()) / billable_days * cost

    return payees

def main():
    """ Main function."""

    period = Relevant_Day(date(2019, 3, 1), date(2019, 5, 31), True)

    payees = [
        Payee('Sean', []),
        Payee('Chris', []),
        Payee('Brian', [
            Relevant_Day(date(2019, 5, 12), date(2019, 5, 31), True)
        ]),
        Payee('Raymond', [
            Relevant_Day(date(2019, 5, 9), date(2019, 5, 18), True),
            Relevant_Day(date(2019, 5, 28), date(2019, 5, 31), True),
        ]),
    ]

    transformed_payees = calc_share_of_costs(period, 340.53, payees)

    for payee in transformed_payees:
        print(f'{payee.name} for {period.calc_num_of_days() - payee.calc_total_absent_days()} / {period.calc_num_of_days()} days: {payee.billable_amount}')

main()
