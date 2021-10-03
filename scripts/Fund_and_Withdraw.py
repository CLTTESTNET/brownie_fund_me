from brownie import FundMe
from scripts.helpful_scripts import get_account


def fundme():
    fund_me = FundMe[-1]
    account = get_account()
    entrance_fee = fund_me.getEntranceFee()
    print(entrance_fee)
    print(f"the current entrace fee is {entrance_fee}")
    print("funding")
    fund_me.fund({"from": account, "value": entrance_fee})


def withdraw():
    fundme = FundMe[-1]
    account = get_account()
    fund_me.withdraw({"from": account})


def main():
    fund()
    withdraw()