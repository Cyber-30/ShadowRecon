import click
from modules.crtsh import fetch_crtsh_data

@click.command()
@click.argument('target')
@click.option('--crt', is_flag=True, help='Gather SSL certificate data from crt.sh')
def cli(target,crt):
    if crt:
        click.echo(f"[*] Fetching info from crt.sh: {target}")
        fetch_crtsh_data(target)

if __name__ == "__main__":
    cli()