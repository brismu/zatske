# zatske

**la zatske** is an implementation of
[ologs](https://en.wikipedia.org/wiki/Olog):

* a JSON schema for declaring ologs,
* a Python script for manipulating ologs, and
* rules for sharing ologs.

It supports three formalisms of ologs:

* double ologs [Lambert & Patterson 2024](https://arxiv.org/abs/2403.19884),
  which have relations and functions;
* relational ologs [Patterson 2017](https://arxiv.org/abs/1706.00526), which
  have relations and also can designate functions with effort; and
* functional ologs [Spivak & Kent 2012](https://arxiv.org/abs/1102.1889),
  which have functions.

## Design

la zatske is intended to provide the next generation of ontological diagrams
for [la brismu](https://github.com/MostAwesomeDude/brismu). It is the third
tool created for the purpose, succeeding [la
klesi](https://github.com/MostAwesomeDude/klesi) and [la
zaha](https://github.com/MostAwesomeDude/zaha).

Diagrams in la brismu are compiled to Metamath databases. In la zaha, each
arrow of a poset is compiled to a Metamath axiom representing subrelation
inclusion; there is no way to define a function or relation. Additionally,
while there are basic tools for combining posets, la zaha struggles beneath
the weight of an overly-clever schema.

In contrast, la zatske directly represents functions, relations, and
inclusions; each of which are compiled to Metamath axioms representing
themselves in Lojban syntax for la brismu.

## Schema

Abstractly, an olog is:

* a set of *types*,
* a set of *aspects* relating types, and
* a set of *facts* indicating inclusion between aspects.

Of course, using the standard language of category theory, an olog is:

* a set of *objects*,
* a set of *arrows* relating types, and
* a set of *transformations* indicating implication between arrows.

Every practical olog system additionally includes some sort of color/flavor
system which annotates arrows. For double ologs, a good system might have:

* relations,
* functions,
* partial functions,
* bijections,
* injections,
* surjections, and
* constant elements.

The schema supports a fragment of categorical logic, expressed as the
following primitive expressions:

* id

And the following compound expressions:

* (comp X0 X1 X2 ...)
* (dagger X)
* (delete I0 I1 I2 ...)

Expressions may also include any relation defined in the associated olog.
