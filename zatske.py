import json

import click
from click_repl import register_repl

from jsonschema import validate

# Provided by Nix during the build step.
SCHEMA_PATH = "@SCHEMA@"

@click.group()
@click.pass_context
def cli(ctx):
    print("Loading schema:", SCHEMA_PATH)
    with open(SCHEMA_PATH, "rb") as handle:
        ctx.obj["SCHEMA"] = json.load(handle)

@cli.command()
@click.argument("olog", type=click.File("rb"))
@click.pass_context
def summarize(ctx, olog):
    olog = json.load(olog)
    validate(ctx.obj["SCHEMA"], olog)
    print("Yep, it's an olog!")
    print("Types:", len(olog["types"]))
    print("Aspects:", *list(olog["aspects"].keys()))
    print("Facts:", len(olog["facts"]))

register_repl(cli)
cli(obj={})
