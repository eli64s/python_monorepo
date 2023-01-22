"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Python Monorepo."""


if __name__ == "__main__":
    main(prog_name="python_monorepo")  # pragma: no cover
