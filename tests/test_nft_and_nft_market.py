from brownie import NFT, NFTMarket, network, exceptions
from scripts.helpful_scripts import (
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
    get_account,
)
import pytest
from scripts.deploy import deploy_nft_and_nft_market


def test_nft_and_nft_market_place():
    # test will only execute on local enviorments
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("Only for local testing!")

    account = get_account()  # get account for testing
    non_owner = get_account(index=1)  # declaring user account

    nft_market = NFTMarket.deploy({"from": account})
    nft = NFT.deploy(
        nft_market.address,
        {"from": account}
    )

    listing_price = nft_market.getListingPrice()

    assert nft_market.getListingPrice == listing_price