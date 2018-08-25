# Install a python 3.6 virtual environemnt

virtualenv -p python3.6 ~/virtualenvs/consensys

# Activate the virtual environment
. ~/virtualenvs/consensys/bin/activate

# Install this repository

git clone https://github.com/clifer/Consensys-take-home-test.git

# Install requirements (web3)

pip install -r requirements.txt

# How to Execute

python contractinfo.py <contract address> --host <API URL>

# Example execution using Infura and Omisego (OMG) Token Contract

python contractinfo.py 0xd26114cd6EE289AccF82350c8d8487fedB8A0C07 --host https://mainnet.infura.io/v3/< your API key>
