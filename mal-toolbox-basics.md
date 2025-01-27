# MAL Toolbox - The Basics

## Preparations
- Install maltoolbox (`pip install mal-toolbox`)
- Install [neo4j](https://neo4j.com/docs/operations-manual/current/installation/)
- Download the [model](https://github.com/mal-lang/mal-toolbox-tutorial/blob/main/res/mal-toolbox/common/simple_example_model.yml) and the [coreLang language specification](https://github.com/mal-lang/mal-toolbox-tutorial/blob/main/res/mal-toolbox/common/org.mal-lang.coreLang-1.0.0.mar)

## Command line interface - Generate and display Attack Graph in neo4j

### 1) Run the command line client
```sh
python3 -m maltoolbox attack-graph generate simple_example_model.yml org.mal-lang.coreLang-1.0.0.mar
```

### 2) Have a look at the attack graph file generated
It is located in the tmp folder: `tmp/attackgraph.yml`

### 3) Restart Neo4j
```sh
service neo4j restart
```

or

```sh
sudo systemctl restart neo4j
```

You can now access the neo4j GUI through your browser (http://localhost:7474/).
Default login is neo4j:neo4j.

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
password=<new-password>
dbname=neo4j
```

### 6) Run the command line client with the neo4j parameter
```sh
python3 -m maltoolbox attack-graph generate --neo4j simple_example_model.yml org.mal-lang.coreLang-1.0.0.mar
```

### 7) Modify the debug level of the mal-toolbox python package
Update the logging section of the default.conf file.

You can find the file location by running the following command:

```sh
pip show mal-toolbox
```

Set the log_level configuration variable to DEBUG (case sensitive)

```
log_level = DEBUG
```

### 9) Have a look at the log file generated
Re-run the command line client 
```sh
python3 -m maltoolbox attack-graph generate --neo4j simple_example_model.yml org.mal-lang.coreLang-1.0.0.mar
```

The log file should be present in the tmp folder: `tmp/log.txt`
