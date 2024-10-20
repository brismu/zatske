import json

import click
from click_repl import register_repl

from jsonschema import validate

# Provided by Nix during the build step.
SCHEMA_PATH = "@SCHEMA@"

@click.group()
@click.pass_context
def cli(ctx):
    with open(SCHEMA_PATH, "rb") as handle:
        ctx.obj["SCHEMA"] = json.load(handle)

@cli.command()
@click.argument("olog", type=click.File("rb"))
@click.pass_context
def summarize(ctx, olog):
    validate(ctx.obj["SCHEMA"], json.load(olog))
    print("Yep, it's an olog!")

register_repl(cli)
cli(obj={})
