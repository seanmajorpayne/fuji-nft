from brownie import FujiCollectible, accounts, network, config
from scripts.helpful_scripts import fund_advanced_collectible


def main():
    dev = accounts.add(config['wallets']['from_key'])
    print(network.show_active())
    publish_source = False
    fuji_collectible = FujiCollectible.deploy(
        config['networks'][network.show_active()]['vrf_coordinator'],
        config['networks'][network.show_active()]['link_token'],
        config['networks'][network.show_active()]['keyhash'],
        {"from": dev},
        publish_source=publish_source,
    )
    fund_advanced_collectible(fuji_collectible)
    return fuji_collectible