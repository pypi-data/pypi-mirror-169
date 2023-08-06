import click
from ecsclient.common.exceptions import ECSClientException

from .._util.exceptions import EcsmgmtClickException
from .._util.echo import success


@click.command()
@click.argument('bucket-name', type=click.STRING)
@click.argument('user-id', type=click.STRING)
@click.option('-n', '--namespace', type=click.STRING, show_default=True)
@click.pass_obj
def cli(obj, bucket_name, user_id, namespace):
    """Create bucket in namespace
    """
    client = obj['client']

    try:
        client.bucket.set_owner(bucket_name=bucket_name, new_owner=user_id, namespace=namespace)
        success(f'created bucket "{bucket_name}" in namespace "{namespace}"')
    except ECSClientException as e:
        raise EcsmgmtClickException(e.message)
