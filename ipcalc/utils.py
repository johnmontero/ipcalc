def get_address_min(address):
    address_min = int(address.split(".")[::-1][0]) + 1
    pos = address.rfind(".")
    return (address[:pos+1] + str(address_min))

def get_address_max(address):
    address_min = int(address.split(".")[::-1][0]) - 1
    pos = address.rfind(".")
    return (address[:pos+1] + str(address_min))

def get_networkToBin(network):
    address = get_address(network)
    netmask = get_netmask(network)
    addressToBin = get_addressToBin(address).replace(".","")
    networkToBin = "{}{}".format(addressToBin[:int(netmask)], '0' * (32 - int(netmask)))
    return ".".join([ networkToBin[(i*8)-8:i*8] for i in range(1, 5)])

def get_broadcastToBin(network):
    address = get_address(network)
    netmask = get_netmask(network)
    addressToBin = get_addressToBin(address).replace(".","")
    broadcastToBin = "{}{}".format(addressToBin[:int(netmask)], '1' * (32 - int(netmask)))
    return ".".join([ broadcastToBin[(i*8)-8:i*8] for i in range(1, 5)])

def get_netmaskToBin(netmask):
    netmaskToBin = "{}{}".format('1' * int(netmask), '0' * (32 - int(netmask)))
    return ".".join([ netmaskToBin[(i*8)-8:i*8] for i in range(1, 5)])

def get_netmask(network):
    address, netmask = network.split("/")
    return netmask

def get_address(network):
    address, netmask = network.split("/")
    return address

def get_wildcardToBin(netmask):
    netmaskToBin = "{}{}".format('0' * int(netmask), '1' * (32 - int(netmask)))
    return ".".join([ netmaskToBin[(i*8)-8:i*8] for i in range(1, 5)])

def get_binToAddress(address_binary):
    return ".".join([ str(int(i,2)) for i in address_binary.split(".")])

def get_addressToBin(address):
    return ".".join([ "{0:08b}".format(int(i))  for i in address.split(".")])

def valid_format_address(address):
    a, l = address.split("/")
    return ".".join([ "{0:08b}".format(int(i))  for i in a.split(".")])

def valid_format_network(network):
    a, l = address.split("/")
    return ".".join([ "{0:08b}".format(int(i))  for i in a.split(".")])
