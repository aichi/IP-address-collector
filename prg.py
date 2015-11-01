import socket
import uuid
from azure.storage.table import TableService, Entity


# http://stackoverflow.com/questions/14050281/how-to-check-if-a-python-module-exists-without-importing-it
import imp
try:
    imp.find_module('fcntl')
    found = True
except ImportError:
    found = False
	
if found == True:
	# http://stackoverflow.com/questions/24196932/how-can-i-get-the-ip-address-of-eth0-in-python/24196955#24196955
	import struct

	def get_ip_address(ifname):
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		return socket.inet_ntoa(fcntl.ioctl(
			s.fileno(),
			0x8915,  # SIOCGIFADDR
			struct.pack('256s', ifname[:15])
		)[20:24])

	ip = get_ip_address('eth0')
else:
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