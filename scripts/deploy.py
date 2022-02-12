from scripts.heplfulScripts import get_account, deploy_MockV3Aggregator
from brownie import accounts, fundMe, config, network, MockV3Aggregator
from web3 import Web3





def deploy_fund_me():
   account =  get_account()
   if network.show_active() != 'development':
      price_feed_address = config['networks'][network.show_active()]['eth_usd_price_feed']
   else:
      deploy_MockV3Aggregator()

      




   fund_me = fundMe.deploy(
      price_feed_address,
      {'from': account},
      publish_source = config['networks'][network.show_active()].get('verify'),
   )
   print(f'Contract deployed at: {fund_me.address}')


def main():
    deploy_fund_me()