# MAL-toolbox-tutorial
A tutorial on how to use mal-toolbox and associated tools.
Examples in this repository is written to work for mal-toolbox and mal-simulator 2.\*.\*.
This repository contains tutorials and guides on how to do things with the toolbox and simulator, as well as other tools in the MAL ecosystem.


## What is MAL?
A language to create cyber threat modeling systems for specific domains.

Read more about MAL at: https://mal-lang.org

For mal-toolbox api docs, visit: https://github.com/mal-lang/mal-toolbox/wiki

## Tutorials

Tutorials are step by step instructions that you can follow along with.

- [Tutorial 1 - Create a MAL-Language, crate a model and run simulations](tutorials/tutorial1/language-model-tutorial.md)
- [Tutorial 2 - Load a MAL-Language, create a model and run simulations](tutorials/tutorial2/model-tutorial.md)

## Guides

Guides work as documentation for separate parts of the mal ecosystem.

### Create a MAL Language

A MAL language defines a domain to work within.

Each MAL language consists of assets with defense steps, attack steps and associations.

- A very simple example of a MAL language: https://github.com/mal-lang/exampleLang 
- A more complex MAL language: https://github.com/mal-lang/coreLang
- VSCode plugin for syntax highlighting and search by reference: https://github.com/mal-lang/mal-vscode-extension

More documentation on MAL syntax: https://github.com/mal-lang/mal-documentation/wiki/MAL-Code-Examples.

### Compiling a MAL-language (LEGACY)

Compilation of MAL-languages is now deprecated and no longer supported. However, if desired, information about this process might be found in the following link 

[Guide on how to compile a MAL language](guides/compile_language.md).

### Create a MAL model using your language

A model is a description of a specific infrastructure in your MAL languages terminology.
A model contains assets and relations between assets.

[Guide on how to create a MAL model for the MAL toolbox](guides/create_model.md).

#### Visualizing a model

[Guide on how to visualize a model](guides/visualize.md).

### Generate an attack graph from your model

An attack graph is a granular representation of the infrastructure defined in the model from an 'action' perspective.
All the attacks and defenses will be generated for each asset according to how they were defined in the MAL language.
The MAL Toolbox can be used to generate an attack graph from a model and language.

[Guide on how to generate an attack graph](guides/generate_attack_graph.md).

#### Visualizing an attack graph
[Guide on how to visualize an attack graph](guides/visualize.md).

### Run simulations / traverse the attack graph

You now have a language, a model and an attack graph. A probable next step is to run analysis, traversal or simulations.
If you want to run simulations or traverse the graph using different types of agents, use the MAL simulator (https://github.com/mal-lang/mal-simulator/).

[Guide on how to run simulations with your attack graph](guides/run_simulation.md).
