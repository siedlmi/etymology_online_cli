#!/usr/bin/env python3

import requests
import argparse
from bs4 import BeautifulSoup
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel

console = Console()
BASE_URL = "https://www.etymonline.com/word/"

def fetch_etymology(word):
    """Fetch the etymology of a word from Etymonline."""
    url = f"{BASE_URL}{word}"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        console.print(f"[red]Error fetching data: {e}[/red]")
        return None, url

    soup = BeautifulSoup(response.text, "html.parser")
    definition_section = soup.find("section", class_="word__defination--2q7ZH")
    etymology = definition_section.get_text(separator="\n").strip() if definition_section else None

    return etymology, url

def fetch_related_words(word):
    """Fetch related words from Etymonline's /related page."""
    related_url = f"{BASE_URL}{word}/related"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(related_url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        console.print(f"[yellow]Warning: Could not fetch related words. ({e})[/yellow]")
        return None

    soup = BeautifulSoup(response.text, "html.parser")
    
    # Extract related words from the "word__name--TTbAA word_thumbnail__name--1khEg" class
    related_words = [
        word_tag.get_text(strip=True) 
        for word_tag in soup.find_all("a", class_="word__name--TTbAA word_thumbnail__name--1khEg")
    ]

    return related_words if related_words else None

def display_results(word, etymology, related_words, url):
    """Format and display the results with better readability and a clickable link."""
    
    # Display clickable link to main word page
    console.print(Panel(f"[bold cyan]🔗 [link={url}]{url}[/link][/bold cyan]", expand=False))

    # Display etymology section
    console.print(Panel(f"[bold cyan]Etymology of '{word}'[/bold cyan]", expand=False))
    
    if etymology:
        console.print(Markdown(etymology))
    else:
        console.print("[red]No etymology found.[/red]")

    # Display related words section
    related_url = f"{BASE_URL}{word}/related"
    if related_words:
        console.print(Panel(f"[bold cyan] [link={related_url}]Related Words (View More)[/link][/bold cyan]", expand=False))
        console.print(", ".join(f"[blue]{w}[/blue]" for w in related_words))
    else:
        console.print("[yellow]No related words found.[/yellow]")

def main():
    """CLI entry point."""
    parser = argparse.ArgumentParser(description="Fetch etymology and related words from Etymonline.")
    parser.add_argument("word", type=str, help="Word to look up")
    args = parser.parse_args()

    etymology, url = fetch_etymology(args.word)
    related_words = fetch_related_words(args.word)

    if etymology or related_words:
        display_results(args.word, etymology, related_words, url)
    else:
        console.print(f"[red]No information found for '{args.word}'.[/red]")

if __name__ == "__main__":
    main()