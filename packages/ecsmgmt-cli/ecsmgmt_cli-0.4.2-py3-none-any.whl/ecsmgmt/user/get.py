import click

from .._util.format import pretty_info


@click.command()
@click.argument('user-id', type=click.STRING)
@click.option('-n', '--namespace', type=click.STRING, show_default=True)
@click.pass_obj
def cli(obj, user_id, namespace):
    """Get user details
    """
    client = obj['client']

    res = client.object_user.get(user_id=user_id, namespace=namespace)

    click.secho(f'User "{user_id}" info:', bold=True)
    click.echo(pretty_info(res))
