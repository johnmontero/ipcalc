import click
from tabulate import tabulate
from ipcalc.cli import pass_context
from ipcalc.utils import get_netmaskToBin, get_binToAddress, get_wildcardToBin
from ipcalc.utils import get_netmask, get_address, get_addressToBin
from ipcalc.utils import get_address_min, get_address_max, get_broadcastToBin
from ipcalc.utils import get_networkToBin

@click.command()
@click.argument('network', default=None)
@pass_context
def command(ctx, network):
    """Network calc"""
    address = get_address(network)
    netmask = get_netmask(network)

    # Netmask
    network_bin = get_networkToBin(network)
    network_add = get_binToAddress(network_bin)

    # Netmask
    netmask_bin  = get_netmaskToBin(netmask)
    netmask_add = get_binToAddress(netmask_bin)

    # Wildcard
    wildcard_bin = get_wildcardToBin(netmask)
    wildcard_add = get_binToAddress(wildcard_bin)

    # Broadcast
    broadcast_bin = get_broadcastToBin(network)
    broadcast_add = get_binToAddress(broadcast_bin)

    # Host Minimo
    host_min_add = get_address_min(network_add)
    host_min_bin = get_addressToBin(host_min_add)

    # Host Maximo
    host_max_add = get_address_max(broadcast_add)
    host_max_bin = get_addressToBin(host_max_add)

    headers = ["Description", "Address", "Binary"]
    table =[
        ['Address',address,  get_addressToBin(address)],
        ['Netmask','{} = {}'.format(netmask_add, netmask),  netmask_bin],
        ['Wildcard',wildcard_add,  wildcard_bin],
        ['','',''],
        ['Network','{}/{}'.format(network_add, netmask), network_bin],
        ['Broadcast',broadcast_add,  broadcast_bin],
        ['HostMin',host_min_add,  host_min_bin],
        ['HostMax',host_max_add,  host_max_bin]

    ]

    ctx.log(tabulate(table, headers))
