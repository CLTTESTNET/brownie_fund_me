from brownie import FundMe, network, config, MockV3Aggregator
from scripts.helpful_scripts import (
    LOCAL_BLOCKCHAIN_ENVIRONMENT,
    deploy_mocks,
    get_account,
    deploy_mocks,
)


def deploy_fund_me():
    # Forking / Mocking

    account = get_account()
    # pass the price feed address to the FundMe contract - Forking / Mocking
    # if we are persistently on rinkeby then use the address of the rinkeby ether price address
    # else use Mock
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENT:
        price_Feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    # Mocking for else
    else:
        deploy_mocks()
        price_Feed_address = MockV3Aggregator[-1].address

    fund_me = FundMe.deploy(
        price_Feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(f"Contract deployed to {fund_me.address}")
    return fund_me


def main():
    deploy_fund_me()
