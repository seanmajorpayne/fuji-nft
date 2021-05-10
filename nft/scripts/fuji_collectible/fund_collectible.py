from brownie import FujiCollectible
from scripts.helpful_scripts import fund_advanced_collectible

def main():
    fuji_collectible = FujiCollectible[len(FujiCollectible) - 1]
    fund_advanced_collectible[fuji_collectible]