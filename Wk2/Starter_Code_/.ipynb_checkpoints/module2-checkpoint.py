# Import the Web3 library
from web3 import Web3

# Import the RPC Provider
from web3 import EthereumTesterProvider

# Create an instance of Web3
w3 = Web3()

print("***********************************************")
print(f"*{w3}*")
print("***********************************************")


provider = EthereumTesterProvider()

#print(provider)

w3 = Web3(provider)


# Access information for the most recent block
