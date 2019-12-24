import re
import optparse
import netifaces
import subprocess

def macChanger(_interface,_newMac):
    # subprocess.call("ifconfig "+ _interface + " down",shell=True)
    # subprocess.call("ifconfig "+ _interface + " hw ether "+ _newMac, shell=True)
    # subprocess.call("ifconfig "+ _interface + " up",shell=True)
    # The above way is less secure because end user can execute multiple commands by manipulating variables

    # To restrict user from executing unnecessary commands, following way is more preferable
    if(_interface in netifaces.interfaces()):
        if re.match('^[a-zA-Z0-9]{2}:[a-zA-Z0-9]{2}:[a-zA-Z0-9]{2}:[a-zA-Z0-9]{2}:[a-zA-Z0-9]{2}:[a-zA-Z0-9]{2}$', _newMac):
            subprocess.call(["ifconfig", _interface, "down"])
            subprocess.call(["ifconfig", _interface, "hw", "ether", _newMac])
            subprocess.call(["ifconfig", _interface, "up"])
            print('Current MAC address for {} is {}'.format(_interface, netifaces.ifaddresses(_interface)[netifaces.AF_LINK][0].get('addr')))
            # print('[+] Changing MAC address for {}'.format(_interface))
            print('[+] Changed MAC address of {} from {} to {}'.format(_interface, netifaces.ifaddresses(_interface)[netifaces.AF_LINK][0].get('addr'), _newMac))
        else:
            print('Please enter MAC in the following format (00:11:22:33:44:55)')
    else:
        print('Your machine only have following interfaces {}'.format(netifaces.interfaces()))

# Command Line Arguments
parser = optparse.OptionParser()
parser.add_option("-i", "--interface", dest="interface", help="Your Network Interface (Run ifconfig to see available interfaces)")
parser.add_option("-m", "--mac", dest="new_MACaddr", help="New MAC address (e.g = 00:11:22:33:44:55)")
(opt, args) = parser.parse_args()

_interface = opt.interface
_newMac = opt.new_MACaddr
macChanger(_interface,_newMac)
ifcRes = subprocess.check_output(["ifconfig", _interface])
print(ifcRes)