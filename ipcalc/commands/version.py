import click
from ipcalc.cli import pass_context


@click.command()
@pass_context
def command(ctx):
    """Show the ipCalc version information"""
    from ipcalc import __version__
    ctx.log('ipcalc:')
    ctx.log(' Version:      %s' % __version__)
