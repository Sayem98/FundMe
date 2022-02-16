from brownie import accounts
from scripts.heplfulScripts import get_account
from scripts.deploy import deploy_fund_me


def test_can_fund_and_withdraw():
    account = get_account()
    fund_me = deploy_fund_me()
    enter_fee = fund_me.getEntranceFee()
    tx1 = fund_me.fund({"from": account, "value": enter_fee})
    tx1.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == enter_fee

    tx2 = fund_me.withdraw({"from": account})
    tx2.wait(1)
    assert fund_me.contractBalance() == 0
