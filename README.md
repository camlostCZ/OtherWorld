# OtherWorld
A simple text game.

## Introduction
Inspired by countless questions on Reddit / learnpython, I decided to write my own
text game. The game doesn't contain a hard-coded world - it's just an engine
which loads the world from YAML files in `./resources/`.

## Game features

### The World
There are two type of resources int the game world at the moment:
- maps which define the world
- items which define items the player can interact with

Both allow for interaction meaning the player can change the world
by taking items from one map a dropping them elsewhere.

Items and maps can cause effects on the player's character like poison.

Items also have some flags which define how they can be used. Examples:
- consumable (can be consumed using the `consume` command), 
- collectable (can be collected from the map using the `take` command)

YAML format has been chosen as the rouserce file format as it's readable, 
self-documenting.

### The player's character
The character has some stats which affect the game play. A special attention
should be paid to hit points (HP) - when HP get to 0, the character dies.

The player has their own inventory to keep items they are collecting during
their journey through the world.

## Next steps
_Note_: Some of the *Next steps* have already been implemented. This section has
been updated accordingly.

### NPCs and monsters
All of the above doesn't make much sense without any kind of life or randomness
in the game.

_Update_: After the last changes, this feature is getting on top of the list. It's quite
a lot of work but we will have moving NPC with stats and items.

### Containers like chests, bags

Currently, the game doesn't support container items. This could be a nice feature
and it should be quite easy to implement.

### Shops
Shops are a possible extension to the current state of the game.
Shops should be pretty easy to implement as the current implementation of inventory
is quite flexible. However, we don't have support for money so it will still require
some effort.

## Final words
I must admit it's quite fun to develop a game - it took only several hours so far but
the fun when friends are dying while testing it worths every minute. Highly
recommended.