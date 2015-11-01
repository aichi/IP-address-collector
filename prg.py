import socket
import uuid
from azure.storage.table import TableService, Entity

# http://stackoverflow.com/questions/166506/finding-local-ip-addresses-using-pythons-stdlib
ip = socket.gethostbyname(socket.getfqdn())
# http://stackoverflow.com/questions/799767/getting-name-of-windows-computer-running-python-script
name = socket.gethostname()

# https://azure.microsoft.com/en-us/documentation/articles/storage-python-how-to-use-table-storage/
account_name='xxx'
account_key='xxx'
table_service = TableService(account_name, account_key)
table_service.create_table('deviceip')
task = {'PartitionKey': 'localIp', 'RowKey': str(uuid.uuid4()), 'ip' : '' + ip, 'hostName' : '' + name}
table_service.insert_entity('deviceip', task)