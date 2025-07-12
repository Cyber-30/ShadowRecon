import click
from rich.console import Console
from utils.banner import show_banner
from modules.crtsh import fetch_crtsh_data
from modules.whois import fetch_whois_info


console = Console()

@click.command()
@click.argument('target')
@click.option('--crt', is_flag=True, help='Gather SSL certificate data from crt.sh')
@click.option('--whois', is_flag=True, help='Gather WHOIS information')
def cli(target, crt, whois):
    if crt:
        console.print(f"[bold green][*] Fetching info from crt.sh: {target}[/bold green]")
        fetch_crtsh_data(target)
    elif whois:
        console.print(f"[bold green][*] Fetching WHOIS info for {target}[/bold green]")
        fetch_whois_info(target)
    else:
        console.print("[red][!] No option specified. Use --crt or --whois.[/red]")

if __name__ == "__main__":
    show_banner()
    cli()
