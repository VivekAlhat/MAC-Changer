import re
import netifaces
import subprocess

print(netifaces.interfaces())
_interface = input('Which interface? > ')
print('Current MAC address for {} is {}'.format(_interface, netifaces.ifaddresses(_interface)[netifaces.AF_LINK][0].get('addr')))
print('[+] Changing MAC address for {}'.format(_interface))
_newMac = input('New MAC address > ')

if re.match('^[a-zA-Z0-9]{2}:[a-zA-Z0-9]{2}:[a-zA-Z0-9]{2}:[a-zA-Z0-9]{2}:[a-zA-Z0-9]{2}:[a-zA-Z0-9]{2}$', _newMac):
    # subprocess.call("ifconfig "+ _interface + " down",shell=True)
    # subprocess.call("ifconfig "+ _interface + " hw ether "+ _newMac, shell=True)
    # subprocess.call("ifconfig "+ _interface + " up",shell=True)
    
    # The above way is less secure because in end user can execute multiple commands by manipulating variables
    # To restrict user from executing unnecessary commands, following way is more preferable

    subprocess.call(["ifconfig", _interface, "down"])
    subprocess.call(["ifconfig", _interface, "hw", "ether", _newMac])
    subprocess.call(["ifconfig", _interface, "up"])
    print('[+] Changed MAC address of {} from {} to {}'.format(_interface, netifaces.ifaddresses(_interface)[netifaces.AF_LINK][0].get('addr'), _newMac))
else:
    print('Please enter MAC in the following format (00:11:22:33:44:55)')