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

Some items are collectable, some are consumable. 

Items and even maps can have some effect on the player's character like poison.
So not only the player can influence the game world but the world can influence
the player's character as well.

## Next steps
_Note_: Some of the *Next steps* have already been implemented. This section has
been updated accordingly.

### Shops
Shops are a possible extension to the current state of the game.
Shops should be pretty easy to implement as the current implementation of inventory
is quite flexible.

### NPCs and Monsters
All of the above doesn't make much sense without any kind of life or randomness
in the game.
Unfortunately, this feature is not on top of the next steps. But stay tuned for
updates. :-)

## Final Words
I must admit it's quite fun to develop a game - it takes only several hours but
the fun when friends are dying while testing it is worthing every minute. Highly
recommended.