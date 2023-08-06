from pathlib import Path

import click

from .extract import extract_save


@click.group()
def main():
    pass


@main.group()
def extract():
    pass


@extract.command()
@click.argument("pdf_file", required=1)
def on(pdf_file):
    pdf_path = Path(pdf_file)
    pdf_filename = pdf_path.name
    pdf_path = pdf_path.parent
    extract_save(pdf_file, pdf_path)


@extract.command()
@click.option("--folder", help="Tous les fichiers dans folder", default="./")
@click.option("--dest", help="Où mettre les fichiers produits", default="./")
def all(folder, dest):
    p = Path(folder)

    d = Path(dest)
    d.mkdir(exist_ok=True)

    pdf_files = [x for x in p.iterdir() if ".pdf" in str(x)]
    for pdf_file in pdf_files:
        extract_save(pdf_file, d)


@main.command()
def join():
    pass
