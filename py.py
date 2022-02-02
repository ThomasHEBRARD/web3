import requests
import pprint

API_KEY="QCXYQAWT76S2WED57P5T19XC7KN84E7N55"
address = "0x8a9a5B3719783D5b530CC72dFCda081F7A3c0528"  # nano X / Metamask
usdc_address = "0xDFd5293D8e347dFe59E90eFd55b2956a1343963d"
from_1 = "0x55fdf3e89970c26470bb6732105df810cb93c6a5"  # nano S
from_2 = "0x708396f17127c42383e3b9014072679b2f60b82f"  # binance
from_3 = "0x6163a7bb6908a401ffab0550cf8ece50e11f44ed"  # binance eth
wei = 1 / (10 ** 18)

tx_url = f"https://api.etherscan.io/api?module=account&action=txlist&address={usdc_address}&startblock=0&endblock=99999999&sort=asc&apikey={API_KEY}"
bal_url = f"https://api.etherscan.io/api?module=account&action=balance&address={from_3}&tag=latest&apikey={API_KEY}"
res = requests.get(url=tx_url).json()
pprint.pprint(res)
