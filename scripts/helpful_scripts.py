from brownie import network, accounts, config


LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["hardhat", "development", "ganache"]


def get_account(mood=None):
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        return accounts[0]
    if mood:
        return accounts[mood]
    if network.show_active() in config["networks"]:
        account = accounts.add(config["wallets"]["from_key"])
        return account
    return None
