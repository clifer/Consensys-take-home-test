import sys
import web3
from web3 import Web3, HTTPProvider
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('contractAddress')
parser.add_argument("--host", dest="host", help="API Host", metavar="HOST")

args = parser.parse_args()

apihost = args.host

w3 = Web3(HTTPProvider(apihost))

if not w3.isAddress(args.contractAddress):
    sys.exit('\n' + args.contractAddress + ' is not a valid eth address\n')

contractAddress = w3.toChecksumAddress(args.contractAddress)
upper = w3.eth.blockNumber
lower = 0
searching = True

code = w3.eth.getCode(contractAddress, block_identifier=upper)
if not code:
    sys.exit('\nErr: it appears that ' + contractAddress + ' is not a contract address\n')

while searching:
    midling = (lower + upper) // 2

    if lower == midling:
        searching = False
        contractBlockNumber = upper
        contractBlock = w3.eth.getBlock(contractBlockNumber)
        contractBlockHash = contractBlock['hash'].hex()
        for tx in contractBlock['transactions']:
            txReceipt = w3.eth.getTransactionReceipt(tx)
            if txReceipt['contractAddress'] == contractAddress:
                contractTx = tx.hex()

        print( '\nBlock: ' + str(contractBlockHash))
        print( 'Transaction: ' + str(contractTx) + '\n')

        break

    code = w3.eth.getCode(contractAddress, block_identifier=midling)

    if code:
        upper = midling
    elif not code :
        lower = midling

