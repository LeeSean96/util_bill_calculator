from datetime import date
from typing import List

class Absent_Day:
    def __init__(self, begin_date: date, end_date: date, pays_first_day: bool):
        self.begin_date = begin_date
        self.end_date = end_date
        self.pays_first_day = pays_first_day

    def calc_num_of_days(self) -> int:
        return (self.end_date - self.begin_date).days + int(not self.pays_first_day)

class Payee:
    def __init__(self, name: str, absent_days: List[Absent_Day]):
        self.name = name
        self.absent_days = absent_days
        self.billable_amount = 0

    def calc_total_absent_days(self) -> int:
        total_day = 0
        for absent_day in self.absent_days:
            total_day += absent_day.calc_num_of_days()
        return total_day


def calc_share_of_costs(begin_date: date, end_date: date, is_inclusive: bool, cost: float, payees: List[Payee]):
    duration = (end_date - begin_date).days + int(not is_inclusive)
    number_of_payees = len(payees)

    billable_days = 0
    for payee in payees:
        billable_days += duration - payee.calc_total_absent_days()

    for payee in payees:
        payee.billable_amount = (duration - payee.calc_total_absent_days()) / billable_days * cost

    return payees

def main():
    begin_date = date(2019, 3, 1)
    end_date = date(2019, 5, 31)

    # Brian's share
    brian_begin_date = date(2019, 3, 1)
    brian_end_date = date(2019, 5, 12)

    # Raymond's share
    raymond_0_begin_date = date(2019, 3, 9)
    raymond_0_end_date = date(2019, 5, 12)
    raymond_1_begin_date = date(2019, 5, 28)
    raymond_1_end_date = date(2019, 5, 31)
    
    payees = [
            Payee('Sean', []), 
             Payee('Chris', []),
             Payee('Brian', [ 
                 Absent_Day(date(2019, 5, 12), date(2019, 5, 31), False)
                 ]),
             Payee('Raymond', [ 
                 Absent_Day(date(2019, 5, 9), date(2019, 5, 18), False),
                 Absent_Day(date(2019, 5, 28), date(2019, 5, 31), False),
                 ]),
            ]

    transformed_payees = calc_share_of_costs(begin_date, end_date, True, 340.53, payees)

    for payee in transformed_payees:
        print(f'{payee.name} : {payee.billable_amount}')

main()
