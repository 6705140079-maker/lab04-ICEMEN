import pytest
from bank import BankAccount

@pytest.fixture
def temp_account():
    print("\n[setup]")
    acc = BankAccount(200)
    yield acc
    print("\n[teardown]")

def test_teardown_deposit(temp_account):
    temp_account.deposit(50)
    assert temp_account.balance == 250

def test_teardown_withdraw(temp_account):
    temp_account.withdraw(100)
    assert temp_account.balance == 100