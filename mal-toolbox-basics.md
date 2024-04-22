# MAL Toolbox - The Basics

## 1) Download the model and language specification
https://github.com/mal-lang/mal-toolbox-tutorial/tree/main/res/mal-toolbox/basics

## 2) Run the command line client
```sh
python -m maltoolbox gen_ag simple_example_model.json org.mal-lang.coreLang-1.0.0.mal
```

## 3) Restart Neo4j
```sh
service neo4j restart
```

## 4) Change the neo4j password
```sh
ALTER USER neo4j SET PASSWORD '<new-password>'
```

## 5) Update Neo4j configuration
Update the neo4j section of the default.conf file.

You can find the file location by running the following command:

```sh
pip show mal-toolbox
```

The neo4j section should look something like this:
```
[neo4j]
uri=bolt://localhost:7687
username=neo4j
password=mgg12345!
dbname=neo4j
```

## 6) Run the command line client with the neo4j parameter
```sh
python -m maltoolbox gen_ag --neo4j simple_example_model.json org.mal-lang.coreLang-1.0.0.mal
```
