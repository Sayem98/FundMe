from brownie import accounts, config, network, MockV3Aggregator
from web3 import Web3
def get_account():
    if(network.show_active() == 'development'):
        return accounts[0]
    else:
        return accounts.add(config['wallets']['from_key'])

def deploy_MockV3Aggregator():
    print('Mock deploying...')
    if len(MockV3Aggregator) <=0:
        MockV3Aggregator.deploy(18, Web3.toWei(200, 'ether'), {'from': get_account()})
    price_feed_address = MockV3Aggregator[-1].address
    # print(price_feed_address)
    print('Deployed...')