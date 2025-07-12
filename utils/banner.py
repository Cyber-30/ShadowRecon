from pyfiglet import Figlet
from rich.align import Align
from rich.panel import Panel
from rich.console import Console
from utils.typing import type_writer
from shadowrecon.version import __version__

console = Console()


def show_banner():
    figlet = Figlet(font="doom")
    ascii_art_lines = figlet.renderText("ShadowRecon").rstrip().splitlines()

    # Center ASCII art lines manually
    max_line_length = max(len(line) for line in ascii_art_lines)
    centered_ascii = "\n".join(
        f"[blue]{line.center(max_line_length)}[/blue]" for line in ascii_art_lines
    )

    # Center subtitle and meta line
    subtitle = "[bold cyan]" + "Passive Recon Toolkit".center(max_line_length) + "[/bold cyan]"
    meta_line = "[bold red]" + f"ShadowRecon v{__version__}".center(max_line_length) + "[/bold red]"

    # Combine content
    content = f"{centered_ascii}\n\n{subtitle}\n{meta_line}"

    # Create tight panel and center everything inside
    panel = Panel.fit(Align.center(content), border_style="cyan", padding=(1, 4))

    # Capture and animate
    with console.capture() as capture:
        console.print(panel)
    type_writer(capture.get())
