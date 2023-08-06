import click
from ecsclient.common.exceptions import ECSClientException

from .._util.exceptions import EcsmgmtClickException
from .._util.echo import success


@click.command()
@click.argument('bucket-name', type=click.STRING)
@click.option('-n', '--namespace', type=click.STRING, show_default=True)
@click.pass_obj
def cli(obj, bucket_name, namespace):
    """Create bucket in namespace
    """
    client = obj['client']

    try:
        client.bucket.delete(bucket_name=bucket_name, namespace=namespace)
        success(f'deleted bucket "{bucket_name}" in namespace "{namespace}"')
    except ECSClientException as e:
        raise EcsmgmtClickException(e.message)
