from asyncio import exceptions
from brownie import accounts, network
from scripts.heplfulScripts import get_account, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from scripts.deploy import deploy_fund_me
import pytest


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


def only_owner_can_withdraw():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("Only for local testing...!")
    else:
        fund_me = deploy_fund_me()
        new_char = accounts.add()
        with pytest.raises(exceptions.VirtualMachineError):
            fund_me.withdraw({"from": new_char})
