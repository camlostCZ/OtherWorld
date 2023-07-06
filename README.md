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

The player has their own inventory to keep items they are collecting during
their journey through the world.

Some items are collectable, some are consumable. They have, however, no effect
on the player or the world at the moment.

## Next steps

### Effects
I'm considering some kind of *effects* on the player, I mean on the character.
Two main effects are comming to my mind:
- healing effects (increase HP)
- harming effects like poisons, deaths, injuries (decrease HP)
These effects would update the player's HP over time, i.e. moves.

*Effects* could be cause both by items (like poisons) and by maps (death in lava
for example, teleport to another map).

### Shops
Shops are another possible extension to the current state of the game.
Shops should be pretty easy to implement as the current implementation of inventory
is quite flexible.

### NPCs and Monsters
All of the above doesn't make much sense without any kind of life or randomness
in the game.
Unfortunately, this feature is not on top of the next steps. But stay tuned for
updates. :-)

# Final Words
This is just a first implementation. If I will be able to implement all the 
planned features, I will run the game as a Discord bot so that we can enjoy 
the game from any place on any device.