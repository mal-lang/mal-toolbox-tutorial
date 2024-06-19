# MAL Toolbox - The Basics

## Preparations
- Install maltoolbox
- Download the [model](https://github.com/mal-lang/mal-toolbox-tutorial/blob/main/res/mal-toolbox/basics/simple_example_model.json) and [language specification](https://github.com/mal-lang/mal-toolbox-tutorial/blob/main/res/mal-toolbox/common/org.mal-lang.coreLang-1.0.0.mar)

## Command line interface - Generate and display Attack Graph in neo4j

### 1) Run the command line client
```sh
python3 -m maltoolbox attack-graph generate simple_example_model.json org.mal-lang.coreLang-1.0.0.mar
```

### 2) Have a look at the attack graph file generated
It is located in the tmp folder: `tmp/attackgraph.json`

### 3) Restart Neo4j
```sh
service neo4j restart
```

### 4) Change the neo4j password
```sh
ALTER USER neo4j SET PASSWORD '<new-password>'
```

### 5) Update Neo4j configuration
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

### 6) Run the command line client with the neo4j parameter
```sh
python3 -m maltoolbox attack-graph generate --neo4j simple_example_model.json org.mal-lang.coreLang-1.0.0.mar
```

### 7) Modify the debug level of the mal-toolbox python package
Update the logging section of the default.conf file.

You can find the file location by running the following command:

```sh
pip show mal-toolbox
```

Set the log_level configuration variable to DEBUG

```
log_level = DEBUG
```

### 9) Have a look at the log file generated
Re-run the coomand line client 
```sh
python3 -m maltoolbox attack-graph generate --neo4j simple_example_model.json org.mal-lang.coreLang-1.0.0.mar
```

The log file should be present in the tmp folder: `tmp/log.txt`
