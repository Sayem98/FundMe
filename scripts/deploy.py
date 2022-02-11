from scripts.heplfulScripts import get_account
from brownie import fundMe
def deploy_fund_me():
   account =  get_account()
   fund_me = fundMe.deploy({'from': account})
   print(f'Contract deployed at: {fund_me.address}')


def main():
    deploy_fund_me()