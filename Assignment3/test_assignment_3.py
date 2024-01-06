import pytest
import sys
sys.path.insert(0, 'Assignment 2')
from assignment_2 import BankingSystem


@pytest.fixture
def banking_system():
    return BankingSystem()


def test_create_account_success(banking_system):
    res = banking_system.create_account("001", "Casper", 100)
    assert res == "Account created successfully"


def test_create_account_negative_balance(banking_system):
    res = banking_system.create_account("002", "Casper", -100)
    assert res == "Initial balance must be non-negative"


def test_create_duplicate_account(banking_system):
    banking_system.create_account("003", "Casper", 50)
    res = banking_system.create_account("003", "Casper", 50)
    assert res == "Account already exists"


def test_deposit_success(banking_system):
    banking_system.create_account("004", "Casper", 100)
    res = banking_system.deposit("004", 50)
    assert res == "Deposit successful"


def test_deposit_non_existing_account(banking_system):
    res = banking_system.deposit("999", 50)
    assert res == "Account not found"


def test_deposit_negative_amount(banking_system):
    banking_system.create_account("005", "Casper", 100)
    res = banking_system.deposit("005", -50)
    assert res == "Deposit amount must be positive"


def test_withdraw_success(banking_system):
    banking_system.create_account("006", "Casper", 100)
    res = banking_system.withdraw("006", 50)
    assert res == "Withdrawal successful"


def test_withdraw_non_existing_account(banking_system):
    res = banking_system.withdraw("999", 50)
    assert res == "Account not found"


def test_withdraw_negative_amount(banking_system):
    banking_system.create_account("007", "Casper", 100)
    res = banking_system.withdraw("007", -50)
    assert res == "Withdrawal amount must be positive"


def test_withdraw_insufficient_funds(banking_system):
    banking_system.create_account("008", "Casper", 50)
    res = banking_system.withdraw("008", 100)
    assert res == "Insufficient funds"


def test_get_balance_existing_account(banking_system):
    banking_system.create_account("009", "Casper", 100)
    res = banking_system.get_balance("009")
    assert res == 100


def test_get_balance_non_existing_account(banking_system):
    res = banking_system.get_balance("999")
    assert res == "Account not found"


def test_get_balance_after_deposit(banking_system):
    banking_system.create_account("010", "Casper", 100)
    banking_system.deposit("010", 50)
    res = banking_system.get_balance("010")
    assert res == 150


def test_get_balance_after_withdrawal(banking_system):
    banking_system.create_account("011", "Casper", 100)
    banking_system.withdraw("011", 50)
    res = banking_system.get_balance("011")
    assert res == 50
