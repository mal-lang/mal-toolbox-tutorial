# Visualize a MAL Model or Attack Graph

## Prerequisites:
- Create / find a MAL model file (.yml / .json)
- Compile / download a MAL langage (.mar)


## Option 1: Visualize Model in Mal GUI

Install and use [mal gui](https://github.com/mal-lang/mal-gui) to load your model file (.yml or .json).


## Option 2: Visualize Model + Attack Graph with maltoolbox CLI

### Prerequisites:
- Install and launch [neo4j](https://neo4j.com/docs/operations-manual/current/installation/).
- [Configure maltoolbox](configure_maltoolbox.md) to use your neo4j user and password.


The MAL-toolbox cli supports visualizing an attack graph in `neo4j` when it is generated through the CLI.

`maltoolbox attack-graph generate <model_file> <lang_file> --neo4j`

You will now be able to view the models and attack graphs in neo4j in your browser (http://localhost:7474).


## Option 3: Visualize Model + Attack Graph programatically

See [example script](scripts/visualize.py).
