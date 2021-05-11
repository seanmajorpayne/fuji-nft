from brownie import FujiCollectible, accounts, config
from scripts.helpful_scripts import get_breed
import time

STATIC_SEED = 123

def main():
    dev = accounts.add(config['wallets']['from_key'])
    fuji_collectible = FujiCollectible[len(FujiCollectible) - 1]
    transaction = fuji_collectible.createCollectible(
        STATIC_SEED, "None", {"from": dev}
    )
    transaction.wait(1)
    requestId = transaction.events['requestedCollectible']['requestId']
    token_id = fuji_collectible.requestIdToTokenId(requestId)
    time.sleep(45)
    breed = get_breed(fuji_collectible.tokenIdToBreed(token_id))
    print('Dog breed of tokenId {} is {}'.format(token_id, breed))
