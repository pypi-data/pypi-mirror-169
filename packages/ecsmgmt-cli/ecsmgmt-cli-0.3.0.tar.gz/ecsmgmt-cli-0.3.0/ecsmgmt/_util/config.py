import os.path

import click
import yaml


def build_namespace_options(parent_command, ctx, namespace):
    command_tree = {}
    for command in parent_command.list_commands(ctx):
        cmd = parent_command.get_command(ctx, command)
        if isinstance(cmd, click.MultiCommand):
            command_tree[command] = build_namespace_options(cmd, ctx, namespace)
        else:
            if 'namespace' in [param.name for param in cmd.params if isinstance(param, click.Option)]:
                command_tree[command] = {'namespace': namespace}
    return command_tree


def load_config(ctx, param, config_path):
    configpath = os.path.abspath(os.path.expanduser(config_path))

    try:
        with open(configpath, 'r') as infile:
            config = yaml.safe_load(infile.read())
    except FileNotFoundError:
        return

    options = dict(config.pop('defaults', {}))

    try:
        namespace_options = build_namespace_options(ctx.command, ctx, options['namespace'])
        options.update(namespace_options)
    except KeyError:
        pass

    ctx.default_map = options
    ctx.obj = {
        'config': config,
    }
