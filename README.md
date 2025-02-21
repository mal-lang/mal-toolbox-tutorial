# mal-toolbox-tutorial
A tutorial on how to use mal-toolbox and associated tools

## What is MAL?
A language to create cyber threat modeling systems for specific domains.

Read more about MAL at: https://mal-lang.org

For maltoolbox api docs, visit: https://mal-lang.org/mal-toolbox/

## 1. Create a MAL Language

A MAL language defines a domain to work within.

Each MAL language consists of assets with defense steps, attack steps and associations.

- A very simple example of a MAL language: https://github.com/mal-lang/exampleLang 
- A more complex MAL language: https://github.com/mal-lang/coreLang

More documentation on MAL syntax: https://github.com/mal-lang/mal-documentation/wiki/MAL-Code-Examples.

## 2. Compile the language

[Guide on how to compile a MAL language](guides/maltoolbox-0.3/compile_language.md).


## 3. Create a MAL model using your language

A model is a description of a specific infrastructure in your MAL languages terminology.
A model contains assets and relations between assets.

[Guide on how to create a MAL model for the MAL toolbox](guides/maltoolbox-0.3/create_model.md).

### Visualizing a model

[Guide on how to visualize a model](guides/maltoolbox-0.3/visualize.md).

## 4. Generate an attack graph from your model

An attack graph is a granular representation of the infrastructure defined in the model from an 'action' perspective.
All the attacks and defenses will be generated for each asset according to how they were defined in the MAL language.
The MAL Toolbox can be used to generate an attack graph from a model and language.

[Guide on how to generate an attack graph](guides/maltoolbox-0.3/generate_attack_graph.md).

### Visualizing an attack graph
[Guide on how to visualize an attack graph](guides/maltoolbox-0.3/visualize.md).

## 5. Run simulations / traverse the attack graph

You now have a language, a model and an attack graph. A probable next step is to run analysis, traversal or simulations.
If you want to run simulations or traverse the graph using different types of agents, use the MAL simulator (https://github.com/mal-lang/mal-simulator/).

TODO: provide guide on how to run simulations in MAL Simulator. For now we refer to the MAL-simulator README on github.
