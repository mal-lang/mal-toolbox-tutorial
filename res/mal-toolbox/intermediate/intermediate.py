import logging

import maltoolbox
from maltoolbox.language import classes_factory
from maltoolbox.language import specification
from maltoolbox import attackgraph
from maltoolbox import model as malmodel
from maltoolbox.ingestors import neo4j

logger = logging.getLogger(__name__)

lang_file = '../common/org.mal-lang.coreLang-1.0.0.mar'
lang_spec = specification.load_language_specification_from_mar(lang_file)
specification.save_language_specification_to_json(lang_spec, 'lang_spec.json')
lang_classes_factory = classes_factory.LanguageClassesFactory(lang_spec)
lang_classes_factory.create_classes()

model = malmodel.Model('Example Model', lang_spec, lang_classes_factory)
model.load_from_file('example_model.json')

model.save_to_file('processed_model.json')

if maltoolbox.neo4j_configs['uri'] != "":
    neo4j.ingest_model(model,
        maltoolbox.neo4j_configs['uri'],
        maltoolbox.neo4j_configs['username'],
        maltoolbox.neo4j_configs['password'],
        maltoolbox.neo4j_configs['dbname'],
        delete=True)
