# MAC-Changer

- MAC stands for Media Access Control. It is a permanent, unique and physical address associated with any device. 
- It is assigned by the manufacturer. MAC address mostly operates at the layer 1 of TCP/IP reference model i.e a network interface layer.
- MAC address is used to uniquely identify each device across a computer network. A network filters different devices using their MAC addresses. A MAC address can be changed to increase anonymity and bypass filters.
- Example : 00:11:22:33:44:55

# How to use ?
* Execute - pip install -r requirements.txt to install the requirements
* python main.py --interface <interface_name> --mac <new_MAC> or
* python main.py -i <interface_name> -m <new_MAC>

I use [pipreqs](https://pypi.org/project/pipreqs/) to generate dependencies.
