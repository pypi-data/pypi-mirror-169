# ecash-python-rpc
eCash JSON-RPC Python module.

Serves as a tiny layer between an application and an eCash node daemon, its primary usage
is querying the current state of the eCash blockchain, network stats, transactions...

Compatible with **Avalanche Post-Consensus** (0.26.x and later).


## Installation

#### 1. Install from pip3
```bash
$ pip3 install ecashrpc
```

#### 2. Node configuration
Configure your eCash Avalanche Node for remote RPC calls based on your node's security needs. This includes:
- adding `server=1`, `rpcallowip=`, `rpcbind=` and `rpcauth/rpcuser/rpcpassword=` parameters to your node configuration in bitcoin.conf. (refer to the **Server Configuration section** of [this Blockchain Dev guide](https://www.buildblockchain.tech/blog/btc-node-developers-guide))
- a reverse proxy server such as [nginx](http://nginx.org/) to serve RPC data to external web apps subject to your eCash node's rpcallowip whitelist
- install a digital certificate (e.g. [Let's Encrypt](https://letsencrypt.org)) on your node to enable HTTPS if desired


## Usage

Create a sample `ecashrpctest.py` script as follows:
```
import asyncio
from ecashrpc import ECashRPC

async def main():
    async with ECashRPC('HOST:PORT','RPCUSER','RPCPASSWORD') as xecNode:
        print(await xecNode.getavalancheinfo())

if __name__ == "__main__":
    asyncio.run(main())
```

Running this script (with some additional formatting) yields:
```
$ python3 ecashrpctest.py

{
  "ready_to_poll":true,
  "local":{
     "verified":true,
     "proofid":"...",
     "limited_proofid":"...",
     "master":"...",
     "payout_address":"ecash:qqmd..........",
     "stake_amount":1560000000
  },
  "network":{
     "proof_count":18,
     "connected_proof_count":18,
     "dangling_proof_count":0,
     "finalized_proof_count":18,
     "conflicting_proof_count":0,
     "immature_proof_count":4,
     "total_stake_amount":83681202831.85,
     "connected_stake_amount":83681202831.85,
     "dangling_stake_amount":0,
     "node_count":37,
     "connected_node_count":33,
     "pending_node_count":4
  }
 }
```

## Supported methods
Here is a list of supported methods. Please submit a PR if you'd like to have a specific RPC method added.

### Avalanche

|   Method   |   Supported?     |
|------------|:----------------:|
| `addavalanchenode` | ✔ |
| `buildavalancheproof` | ✔ |
| `decodeavalanchedelegation` | ✔ |
| `decodeavalancheproof` | ✔ |
| `delegateavalancheproof` | ✔ |
| `getavalancheinfo` | ✔ |
| `getavalanchekey` | ✔ |
| `getavalanchepeerinfo` | ✔ |
| `getrawavalancheproof` | ✔ |
| `isfinalblock` | ✔ |
| `isfinaltransaction` | ✔ |
| `sendavalancheproof` | ✔ |
| `verifyavalanchedelegation` | ✔ |
| `verifyavalancheproof` | ✔ |

### Blockchain

|   Method   |   Supported?     |
|------------|:----------------:|
| `getbestblockhash` | ✔ |
| `getblock` | ✔ |
| `getblockchaininfo` | ✔ |
| `getblockcount` | ✔ |
| `getblockhash` | ✔ |
| `getblockheader` | ✔ |
| `getblockstats` | ✔ |
| `getchaintips` | ✔ |
| `getdifficulty` | ✔ |
| `getmempoolinfo` | ✔ |
| `getrawmempool` | ✔ |
| `getnetworkhashps` | ✔ |

### Mining

|   Method   |   Supported?     |
|------------|:----------------:|
| `getmininginfo` | ✔ |

### Network

|   Method   |   Supported?     |
|------------|:----------------:|
| `getconnectioncount` | ✔ |
| `getnetworkinfo` | ✔ |

### Raw transactions

|   Method   |   Supported?     |
|------------|:----------------:|
| `getrawtransaction` | ✔ |



## License
MIT
