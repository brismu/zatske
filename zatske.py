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

def formatAspect(ty): return " × ".join(ty[1:]) if ty[0] == "prod" else ty
CLASS_ARROWS = {
    "relation": "↛", "partial": "⇀", "injection": "↣", "surjection": "↠",
    "bijection": "↔",
}

def formatExpression(expr):
    if expr[0] == "comp": return "; ".join(map(formatExpression, expr[1:]))
    elif expr[0] == "dagger": return "(" + formatExpression(expr[1]) + ")†"
    elif expr[0] == "select": return "select(" + str(expr[1:]) + ")"
    else: return expr

@cli.command()
@click.argument("ologs", nargs=-1, type=click.File("rb"))
@click.pass_context
def summarize(ctx, ologs):
    for olog in ologs:
        title = click.format_filename(olog.name)
        olog = json.load(olog)
        validate(ctx.obj["SCHEMA"], olog)
        print(title + ":", "Olog with", len(olog["types"]), "types,",
              len(olog["aspects"]), "aspects, and",
              len(olog["facts"]), "facts")
        print("Aspects:")
        for k, aspect in olog["aspects"].items():
            print(" ", k, ":", formatAspect(aspect[1]),
                  CLASS_ARROWS.get(aspect[0], "→"), formatAspect(aspect[2]))
        facts = olog.get("facts", ())
        if facts: print("Facts:")
        for fact in facts:
            print(" ", formatExpression(fact[0]), "⇒", formatExpression(fact[1]))

register_repl(cli)
cli(obj={})
