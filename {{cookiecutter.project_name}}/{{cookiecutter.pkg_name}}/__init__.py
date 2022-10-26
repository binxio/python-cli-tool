import click


@click.group(invoke_without_command=True)
@click.option("--debug/--no-debug")
@click.pass_context
def main(ctx: click.Context, debug: bool) -> None:
    """
    main command
    """
    ctx.obj = {"debug": debug}

    if ctx.invoked_subcommand is None:
        click.echo("Hello World!")


@main.command()
@click.pass_obj
def example(ctx: dict) -> None:
    """
    Example subcommand
    """
    click.echo("Example subcommand")


if __name__ == "__main__":
    main(obj={})
