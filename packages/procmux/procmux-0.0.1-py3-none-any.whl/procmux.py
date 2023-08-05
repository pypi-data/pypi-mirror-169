from app.__main__ import run_app
from app.config import parse_config
from app.args import cli_args, close_open_arg_resources


def start_cli():
    config = parse_config(cli_args.config)
    close_open_arg_resources()
    run_app(config)


if __name__ == '__main__':
    start_cli()
