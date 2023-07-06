# OtherWorld
A simple text game.

## Introduction
Inspired by countless questions on Reddit / learnpython, I decided to write my own
text game. The game doesn't contain a hard-coded world - it's just an engine
which loads the world from YAML files in `./resources/`.

## Internals
There are two type of resources at the moment:
- maps which define the world
- items which define items the player can interact with

YAML format has been chosen as it's readable, self-documenting.

## Next steps
I'm considering some kind of *effects* on the player, I mean on the avatar.
Two main effects are comming to my mind:
- healing effects (increase HP)
- harming effects like poisons, deaths, injuries (decrease HP)
These effects would update the player's HP over time, i.e. moves.

Another effects like hunger are currently not "on the table" - the game mechanics
doesn't work with hunger at all.