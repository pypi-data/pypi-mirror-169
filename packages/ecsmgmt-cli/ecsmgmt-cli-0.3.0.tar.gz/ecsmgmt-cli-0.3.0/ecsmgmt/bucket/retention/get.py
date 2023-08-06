import click

from ..._util.format import pretty_info


@click.command()
@click.argument('bucket-name', type=click.STRING)
@click.option('-n', '--namespace', type=click.STRING, show_default=True)
@click.pass_obj
def cli(obj, bucket_name, namespace):
    """Get bucket retention
    """
    client = obj['client']

    res = client.bucket.get_retention(bucket_name=bucket_name, namespace=namespace)

    click.secho(f'Bucket "{bucket_name}" retention info:', bold=True)
    click.echo(pretty_info(res))
