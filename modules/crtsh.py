import requests
from rich.table import Table
from rich.console import Console

def fetch_crtsh_data(target):
    url=f"https://crt.sh/?q=%25.{target}&output=json"
    console=Console()

    try:
        response = requests.get(url, timeout=50)
        if response.status_code != 200:
            console.print("[red][-] Failed to fetch data from crt.sh [/red]")
            return
        
        data = response.json()
        seen = set()
        certs = []

        for entry in data:
            name_value = entry.get("name_value", "").replace("\n", ", ")
            issuer_name = entry.get("issuer_name", "N/A")
            not_before = entry.get("not_before", "N/A")
            not_after = entry.get("not_after", "N/A")
            logged_at = entry.get("entry_timestamp", "N/A")
            fingerprint = (name_value, not_before)
            if fingerprint not in seen:
                seen.add(fingerprint)
                certs.append((logged_at, name_value, issuer_name, not_before, not_after))

        certs = sorted(certs, key=lambda x: x[0], reverse=True)
        table = Table(title=f"Latest SSL Certificates for {target}")

        table.add_column("Logged At", style="cyan")
        table.add_column("Common Name(s)", style="magenta")
        table.add_column("Issuer", style="green")
        table.add_column("Valid From", style="yellow")
        table.add_column("Valid To", style="red")

        for cert in certs[:20]: 
            table.add_row(*cert)

        console.print(table)

    except Exception as e:
        console.print(f"[red][-] Error fetching data from crt.sh: {e}[/red]")