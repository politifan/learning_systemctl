from web3 import Web3, HTTPProvider
from os import getenv
from dotenv import load_dotenv

load_dotenv()

NODE_URL = getenv("NODE_URL")

web = Web3(HTTPProvider(NODE_URL))
last_block = web.eth.block_number

while True:
  if last_block != web.eth.block_number:
    last_block = web.eth.block_number
    print(f"Номер последненго блока: {last_block}")
