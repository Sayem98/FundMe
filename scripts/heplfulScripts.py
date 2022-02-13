from re import L
from brownie import accounts, config, network, MockV3Aggregator
from web3 import Web3

LOCAL_BLOCKCHAIN_ENVIRONMENTS = ['development', 'ganache-local']

def get_account():
    # print(f'netwotk.show_active() = {network.show_active()}')
    if(network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS):
        return accounts[0]
    else:
        return accounts.add(config['wallets']['from_key'])

def deploy_MockV3Aggregator():
    print('Mock deploying...')
    if len(MockV3Aggregator) <=0:
        MockV3Aggregator.deploy(18, Web3.toWei(200, 'ether'), {'from': get_account()})
    
    # print(price_feed_address)
    print('Deployed...')