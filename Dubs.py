import doubles
from doubles import expect, allow

import datab


# mock
def test_mocking_setup():
    user = datab
    expect(user).databasing()
    user.databasing()
    print("mocked setup")


# mock
def test_mocking_customer():
    user = datab
    expect(user).customerss(1, 'vida', 6)
    user.customerss(1, 'vida', 6)
    print("mocked customer")


# mock
def test_mocking_orders():
    user = datab
    expect(user).orderss(2, 6)
    user.orderss(2, 6)
    print("mocked orders")


# stub
def test_stub_retrieve():
    user = datab
    allow(user).retrieve.and_return("(22, u'vida', 6)")
    assert user.retrieve() == "(22, u'vida', 6)"
    print("tested retrieve")


# stub
def test_stub_databasing():
    user = datab
    assert user.databasing() is None
    print("tested databasing")
