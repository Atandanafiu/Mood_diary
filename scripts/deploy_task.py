from scripts.helpful_scripts import get_account
from brownie import MoodDiary, network, config


def main():
    account = get_account()
    print(f"Deploying to {network.show_active()}")
    mood = MoodDiary.deploy(
        {"from": account, "gas_limit": 1000000},
        publish_source=config["networks"][network.show_active()]["verify"],
    )
