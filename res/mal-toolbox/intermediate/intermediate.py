import logging

import maltoolbox
from maltoolbox.language import LanguageGraph, LanguageClassesFactory
from maltoolbox.model import Model
from maltoolbox.attackgraph import AttackGraph, query
from maltoolbox.attackgraph.analyzers import apriori
from maltoolbox.ingestors import neo4j

logger = logging.getLogger(__name__)

lang_file = '../common/org.mal-lang.coreLang-1.0.0.mar'
lang_graph = LanguageGraph.from_mar_archive(lang_file)
lang_classes_factory = LanguageClassesFactory(lang_graph)

model = Model.load_from_file('../common/simple_example_model.yml', lang_classes_factory)

graph = AttackGraph(lang_graph, model)
graph.attach_attackers()
os_app_local_access = graph.get_node_by_id('OS App:localAccess')
os_app_np = graph.get_node_by_full_name('OS App:notPresent')
os_app_np.defense_status = 1.0

graph.save_to_file('ag.yml')

apriori.calculate_viability_and_necessity(graph)

graph.save_to_file('post_ag.yml')

attacker = graph.attackers[0]
attacker.compromise(graph.get_node_by_full_name('OS App:networkConnect'))
attacker.compromise(graph.get_node_by_full_name('OS App:authenticate'))

print('Reached attack steps:')
for step in graph.attackers[0].reached_attack_steps:
    print(step.id)

print('Attack Surface:')
for step in query.get_attack_surface(graph.attackers[0]):
    print(step.id)

model.save_to_file('processed_model.yml')

if maltoolbox.neo4j_configs['uri'] != "":
    neo4j.ingest_model(model,
        maltoolbox.neo4j_configs['uri'],
        maltoolbox.neo4j_configs['username'],
        maltoolbox.neo4j_configs['password'],
        maltoolbox.neo4j_configs['dbname'],
        delete=True)

if maltoolbox.neo4j_configs['uri'] != "":
    neo4j.ingest_attack_graph(graph,
        maltoolbox.neo4j_configs['uri'],
        maltoolbox.neo4j_configs['username'],
        maltoolbox.neo4j_configs['password'],
        maltoolbox.neo4j_configs['dbname'],
        delete=True)
