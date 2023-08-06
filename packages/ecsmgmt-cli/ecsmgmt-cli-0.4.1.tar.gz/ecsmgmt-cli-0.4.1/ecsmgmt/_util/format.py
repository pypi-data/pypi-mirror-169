from tabulate import tabulate
import yaml


class IndentedListDumper(yaml.SafeDumper):
    def increase_indent(self, flow=False, indentless=False):
        return super(IndentedListDumper, self).increase_indent(flow, False)


def pretty_table(data: list, headers: list = None, tablefmt: str = 'github') -> str:
    """Tabulate wrapper function with predefined format"""
    if headers is None:
        table = tabulate(data, tablefmt=tablefmt)
    else:
        table = tabulate(data, headers=headers, tablefmt=tablefmt)
    return table


def pretty_info(data: dict) -> str:
    """Print data in a nice form"""
    return yaml.safe_dump(data)
