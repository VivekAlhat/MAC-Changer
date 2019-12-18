import re
import netifaces
import subprocess

print(netifaces.interfaces())
_interface = input('Type the interface: ')
print('Current MAC address for {} is {}'.format(_interface, netifaces.ifaddresses(_interface)[netifaces.AF_LINK][0].get('addr')))
print('[+] Changing MAC address for {}'.format(_interface))
_newMac = input('Enter the new MAC address: ')

if re.match('^[a-zA-Z0-9]{2}:[a-zA-Z0-9]{2}:[a-zA-Z0-9]{2}:[a-zA-Z0-9]{2}:[a-zA-Z0-9]{2}:[a-zA-Z0-9]{2}$', _newMac):
    subprocess.call("ifconfig "+ _interface + " down",shell=True)
    subprocess.call("ifconfig "+ _interface + " hw ether "+ _newMac, shell=True)
    subprocess.call("ifconfig "+ _interface + " up",shell=True)
    print('[+] Changed MAC address of {} to {}'.format(_interface, _newMac))
else:
    print('Please enter MAC in the following format (00:11:22:33:44:55)')