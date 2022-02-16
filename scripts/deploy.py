from scripts.heplfulScripts import get_account, deploy_MockV3Aggregator, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from brownie import accounts, fundMe, config, network, MockV3Aggregator






def deploy_fund_me():
   account =  get_account()
   if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
      price_feed_address = config['networks'][network.show_active()]['eth_usd_price_feed']
   else:
      deploy_MockV3Aggregator()
      price_feed_address = MockV3Aggregator[-1].address

   fund_me = fundMe.deploy(
      price_feed_address,
      {'from': account},
      publish_source = config['networks'][network.show_active()].get('verify'),
   )
   print(f'Contract deployed at: {fund_me.address}')

   return fund_me


def main():
    deploy_fund_me()