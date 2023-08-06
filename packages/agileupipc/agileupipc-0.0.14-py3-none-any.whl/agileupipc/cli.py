import click
import pkg_resources

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.group(help='CLI to manage Informatica PowerCenter.')
def cli() -> int:
    pass


@cli.command(help='Display the current version.')
def version() -> None:
    click.echo(f"AgileUp IPC Version: {pkg_resources.get_distribution('agileupipc').version}")


@cli.command(help='Install software.')
def install() -> None:
    click.secho('Install software', fg='green')


@cli.command(help='Configure software.')
def configure() -> None:
    click.secho('Configure software', fg='green')


@cli.command(help='Smoke test application.')
def smoke() -> None:
    click.secho('Smoke test application', fg='green')


@cli.command(help='Start application.')
def start() -> None:
    click.secho('Start application', fg='green')


@cli.command(help='Stop application.')
def stop() -> None:
    click.secho('Stop application', fg='green')


@cli.command(help='Backup application.')
def backup() -> None:
    click.secho('Backup application', fg='green')


@cli.command(help='Restore application.')
def restore() -> None:
    click.secho('Restore application', fg='green')


if __name__ == '__main__':
    exit(cli())
