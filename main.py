import sqlite3
import doubles

import Dubs
import datab
import sum


# sqlite3 database so the database is just a file
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print("Hi, {0}".format(name))  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    sum.summing()
    datab.databasing()
    datab.customerss(22, 'vida', 6)
    datab.orderss(23, 5)
    datab.retrieve()

    Dubs.test_mocking_setup()
    Dubs.test_mocking_customer()
    Dubs.test_mocking_orders()
    Dubs.test_stub_retrieve()
    Dubs.test_stub_databasing()
    print("done")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
