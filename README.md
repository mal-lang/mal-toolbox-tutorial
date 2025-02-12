# mal-toolbox-tutorial
A tutorial on how to use mal-toolbox and associated tools

# What is MAL?
A language to create cyber threat modeling systems for specific domains.

# Steps towards your MAL journey

## 1. Create a MAL Language

A MAL language defines a domain to work within.

Each MAL language consists of assets with defense steps, attack steps and associations.

- A very simple example of a MAL language: https://github.com/mal-lang/exampleLang 
- A more complex MAL language: https://github.com/mal-lang/coreLang

More documentation on MAL syntax: https://github.com/mal-lang/mal-documentation/wiki/MAL-Code-Examples

## 2. Compile the language into a .mar

Download malc: https://github.com/mal-lang/malc/releases

Compile your language with malc: https://github.com/mal-lang/malc?tab=readme-ov-file#usage

This should result in a .mar-archive of your language that can be used within the MAL toolbox.

## 3. Create a MAL model using your language

A model is a description of a specific infrastructure in your MAL languages terminology.
A model contains assets and relations between assets.

Here you have two options:
i. Create a model using the MAL GUI (https://github.com/mal-lang/mal-gui/)
ii. Create a model programmatically using the MAL toolbox (see guide)

## 4. Generate an attack graph from your model

An attack graph is a granular representation of the infrastructure defined in the model with all the attacks and defenses defined in the MAL language.

The MAL Toolbox can be used to generate an attack graph from a model and language.

You have two options:
i. Use the MAL Toolbox cli (https://github.com/mal-lang/mal-gui/)
ii. Generate the model programatically using MAL Toolbox (see guide)

## 5. Run simulations

Use MAL Simulator to run simulations (https://github.com/mal-lang/mal-simulator/)


## 6. Attack Graph Traversal

Use MAL Simulator to run traversal of the attack graph (https://github.com/mal-lang/mal-simulator/)


## Run analysis

Programatically.