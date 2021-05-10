from brownie import FujiCollectible, accounts, config, interface, network

def fund_advanced_collectible(nft_contract):
    dev = accounts.add(config['wallets']['from_key'])
