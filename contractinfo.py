import web3
from web3 import Web3, HTTPProvider
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('contractAddress')
parser.add_argument("--host", dest="host", help="API Host", metavar="HOST")

args = parser.parse_args()

apihost = args.host

w3 = Web3(HTTPProvider(apihost))

contractAddress = w3.toChecksumAddress(args.contractAddress)

blockNumber = w3.eth.blockNumber
blockNumber = 3978300
code = w3.eth.getCode(contractAddress, block_identifier=blockNumber)

if code:
    while code:
        code = w3.eth.getCode(contractAddress, block_identifier=blockNumber)
        blockNumber -= 1
    contractBlockNumber = blockNumber + 2
    contractBlock = w3.eth.getBlock(contractBlockNumber)
    contractBlockHash = contractBlock['hash'].hex()
    for tx in contractBlock['transactions']:
        txReceipt = w3.eth.getTransactionReceipt(tx)
        if txReceipt['contractAddress'] == contractAddress:
            contractTx = tx.hex()
            break

    print( '\nBlock: ' + str(contractBlockHash))
    print( 'Transaction: ' + str(contractTx) + '\n')
else:
    print('Err: it appears that ' + contractAddress + ' is not a contract address')

