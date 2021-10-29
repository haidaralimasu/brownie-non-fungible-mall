from scripts.helpful_scripts import get_account
from brownie import NFTMarket, NFT, network, config

def deploy_nft_and_nft_market():
	account = get_account() # get account according to network
	print(f'account used for deploying is {account}')

	publish_source = config["networks"][network.show_active()]["verify"]
	
	print('deploying contracts .....')
	nft_market = NFTMarket.deploy(
		{"from": account},
		publish_source=publish_source
	) # NOTE: deploying nft contract first is neccessary
	nft = NFT.deploy(
		nft_market.address, 
		{"from": account},
		publish_source=publish_source
	) # NOTE: {"from": account} must be a last argument

	print('contracts deployed !')
	print(f'NFT is deployed at {nft.address} in {network.show_active()}')
	print(f'Marketplace is deployed at {nft_market.address} in {network.show_active()}')

def main():
	deploy_nft_and_nft_market()