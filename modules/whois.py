import whois
from rich.console import Console
from rich.panel import Panel

console = Console()

def fetch_whois_info(target):
    try:
        info = whois.whois(target)
        data = {
            "Domain": target,
            "Registrar": info.registrar,
            "Creation Date": info.creation_date,
            "Expiration Date": info.expiration_date,
            "Name Server": info.name_server,
            "Emails": info.emails,
            "Updated Date": info.updated_date,
        }

        output = "\n".join(f"[bold cyan]{k}:[/bold cyan] {v}" for k, v in data.items() if v)
        console.print(Panel(output, title=f"[bold green] WHOIS Info For {target}"))

    except Exception as e:
        console.print(f"[red]Error fetching WHOIS Info: {e}[/red]")