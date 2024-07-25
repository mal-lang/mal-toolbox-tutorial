# MAL Toolbox API Examples

## Preparations

- Install maltoolbox

- Download the [model](https://github.com/mal-lang/mal-toolbox-tutorial/blob/main/res/mal-toolbox/basics/simple_example_model.yml) and [language specification](https://github.com/mal-lang/mal-toolbox-tutorial/blob/main/res/mal-toolbox/common/org.mal-lang.coreLang-1.0.0.mar)

### Load / Create Model

```python
from maltoolbox.language import LanguageGraph, LanguageClassesFactory
from maltoolbox.model import Model

# First load the language either from .mal or .mar
# lang_graph = LanguageGraph.from_mal_spec(lang_file_path)
lang_graph = LanguageGraph.from_mar_archive(lang_file_path)

# Then create the lang_classes_factory
lang_classes_factory = LanguageClassesFactory(lang_graph)

# Load existing model (i.e. simple_example_model.yml, can also be json)
instance_model = Model.load_from_file(model_file_path, lang_classes_factory)

# Or create an empty model
instance_model = Model("Example Model", lang_classes_factory)
```

### Load / Create AttackGraph

```python
from maltoolbox.wrappers import create_attack_graph
from maltoolbox.attackgraph import AttackGraph

# Either use the wrapper with files
attack_graph = create_attack_graph(lang_file, model_file)

# Or use already generated lang_graph and model
attack_graph = AttackGraph(lang_graph, instance_model)

# Or load an existing AttackGraph
loaded_attack_graph = AttackGraph.load_from_file(example_graph_path)
```

### Querying the attack graph 

In res/mal-toolbox/intermediate/intermediate.py you can see an example of how to query the attack graph for attack steps.