from eosiopy.eosioparams import EosioParams
from eosiopy.nodenetwork import NodeNetwork
from eosiopy.rawinputparams import RawinputParams
from eosiopy import eosio_config
eosio_config.url="http://192.168.199.110"
eosio_config.port=8888
raw = RawinputParams("newaccount", {"creator":"eosio","name":"aeztcnjmhegg","owner":{"threshold":1,"keys":[{"key":"EOS7EZgfh13yVxaXuzH12cC2Yru7Wv1JNNNbxnSdZQXNX2hWAyBTm","weight":1}],"accounts":[],"waits":[]},"active":{"threshold":1,"keys":[{"key":"EOS7EZgfh13yVxaXuzH12cC2Yru7Wv1JNNNbxnSdZQXNX2hWAyBTm","weight":1}],"accounts":[],"waits":[]}}, "eosio", "eosio@active")
eosiop_arams=EosioParams(raw.params_actions_list,"5KQwrPbwdL6PhXujxW37FSSQZ1JiwsST4cqQzDeyXtP79zkvFD3")
net=NodeNetwork.push_transaction(eosiop_arams.trx_json)
print(net)