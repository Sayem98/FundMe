from multiprocessing.sharedctypes import Value
from brownie import accounts, fundMe
from scripts.heplfulScripts import get_account


def balance():
    fund_me = fundMe[-1]  # Gets the latest state of the smart contract.
    print(fund_me.contractBalance())


def fund():
    fund_me = fundMe[-1]
    enter_fee = fund_me.getEntranceFee()
    account = get_account()
    print(enter_fee)
    fund_me.fund({"from": account, "value": enter_fee})

def withdraw():
    fund_me = fundMe[-1]
    account = get_account()
    fund_me.withdraw({'from': account})


def main():
    balance()
    fund()
