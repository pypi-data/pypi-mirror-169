import click
from .init import initialize_project
from .generate import generate_artifacts
from .migrate import migrate_db
import os
import pathlib

@click.group()
def cli():
    pass


@cli.command()
@click.argument('project_path', type=click.Path())
def init(project_path):
    path = pathlib.Path(project_path)
    if not path.is_absolute():
        path = pathlib.Path(os.getcwd()).joinpath(project_path)
    initialize_project(path)


@cli.command()
@click.argument('object_type')
@click.argument('generated_file')
def create(object_type: str, generated_file):
    generate_artifacts(object_type, generated_file)


@cli.command()
def migrate():
    migrate_db()


def main():
    cli()
