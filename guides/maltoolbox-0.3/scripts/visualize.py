from maltoolbox.attackgraph import create_attack_graph
from maltoolbox.ingestors import neo4j

lang_file = "../resources/org.mal-lang.coreLang-1.0.0.mar" 
model_file = "../resources/model.json"

# Generate attack graph from language + model
attack_graph = create_attack_graph(lang_file, model_file)

# Send model to neo4j
neo4j.ingest_model(
    attack_graph.model,
    uri=None,
    username=None,
    password=None,
    dbname=None
)

# Send attack graph to neo4j
neo4j.ingest_attack_graph(
    attack_graph,
    uri=None,
    username=None,
    password=None,
    dbname=None
)
