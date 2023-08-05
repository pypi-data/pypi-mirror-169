#!/usr/bin/env python3

from pathlib import Path

import typer

from migrate_code import __version__
from migrate_code.cli_utils import load_migration
from migrate_code.types import StageId

app = typer.Typer()

migration_file = typer.Option(
    "migration.py",
    exists=True,
    file_okay=True,
    dir_okay=False,
    readable=True,
    resolve_path=True,
)


@app.command()
def current(file: Path = migration_file):
    """Print the current version of the database"""
    m = load_migration(file)
    latest_applied_stage = m.get_latest_applied_stage()
    typer.echo(f"{latest_applied_stage.id}")


@app.command()
def upgrade(stage: str | None = None, file: Path = migration_file):
    """Upgrade to the given stage"""
    m = load_migration(file)
    if stage is None:
        head = m.get_head_migration_stage()
        if head is None:
            raise RuntimeError("No head migration stage found")
        stage_id = head.id
    else:
        stage_id = StageId.validate(stage)
    m.upgrade_to(stage_id, migration_file=file)


@app.command()
def reset(stage: str | None = None, file: Path = migration_file):
    """Reset to the given former stage"""
    if stage is None:
        stage_id = StageId(())
    else:
        stage_id = StageId.validate(stage)
    m = load_migration(file)
    m.reset_to(stage_id)


@app.command()
def log(file: Path = migration_file):
    """Print the migration log"""
    m = load_migration(file)
    log = m.get_log()
    for entry in log:
        line = ""
        if entry.is_current_sha:
            line += "* "
        else:
            line += "  "
        if entry.sha is not None:
            line += typer.style(
                entry.sha[:7], fg=typer.colors.GREEN if entry.is_current_sha else None
            )
        else:
            line += typer.style("-" * 7, fg=typer.colors.BLACK)
        line += " ("
        line += typer.style(str(entry.stage.id), fg=typer.colors.YELLOW)
        line += ") "
        line += typer.style(
            entry.stage.description, fg=None if entry.applied else typer.colors.BLACK
        )

        typer.echo(line)


def version_callback(value: bool):
    if value:
        typer.echo(__version__)
        raise typer.Exit()


@app.callback()
def main(
    version: bool = typer.Option(
        None,
        "--version",
        callback=version_callback,
        is_eager=True,
        help="Print version number and exit.",
    ),
):
    pass


if __name__ == "__main__":
    app()
