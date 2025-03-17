# MyPokedex

MyPokedex is an application written with python which allows user to browse 152 Pokemon that are available in Pokemon Red, and view the flavor text of the selected Pokemon including it's sprite.

This project includes a custom database with two tables holding information for available Pokemon.

## Features
- View the list of available Pokemon
- Observe sprite and flavor text of selected Pokemon

## Database
Consists of two tables `pokemon` and `pokemon_info`.

`pokemon` includes an id, which is the same number as in the PokeDex, and name of the Pokemon.

`pokemon_info` includes sprite link, flavor text of selected Pokemon and id referenced from `pokemon` table.