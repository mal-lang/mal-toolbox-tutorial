# Tutorial 2 - Create a language and a model
In this tutorial, you will learn how to build a simple MAL language and create a model from it.

## Step by step
Create a directory for the tutorial and set it as your working directory: `mkdir mal-tutorial2 && cd mal-tutorial2`
Create a Python virtual environment and activate it.
- On Linux-based operating systems:
```
python -m venv .venv
source .venv/bin/activate
```
- On Windows:
```
python -m venv .venv
.\.venv\Scripts\activate
```
Install the requirements: `pip install mal-toolbox`.

Create a MAL file in the same directory called `my-language.mal`.

Copy this code into `my-language.mal`:

```
#id: "org.mal-lang.my-language"
#version: "1.0.0"

category System {
    asset Computer {
        | connect
            -> access
        | crackPassword
            -> access
        & access
            -> compromise
	    | compromise
            ->  folder.accessFolder
    }
    asset Folder {
        | accessFolder
            -> stealSecrets
        | stealSecrets
    }
}

associations {
    Computer [computer1] * <-- ComputerConnectionRule --> * [computer2] Computer
    Computer [computer] * <-- ComputerFolderConnectionRule --> * [folder] Folder
}
```

This piece of code defines a simple MALLang. We define a category called System that holds two assets:
- Computer
    - If steps `connect` and `crackPassword` happen, then `access` would be triggered, which at the same time would trigger `compromise`.
    - If `compromise` is activated, we would move to the step `accessFolder` in asset `Folder`.
- Folder
    - If `accessFolder` is given, it would trigger `stealSecrets`.

In the `associations` section we define the relationship assets have. In this case, `Computer` and `Folder` have an N to M relationship, represented by the `*`.

Once we have the MALLang file, we can create a python file to create models from this language.

Create a .py file in the same directory called `my-model.py`.

Copy this code into `my-model.py`:

```python
import os
from maltoolbox.model import Model, ModelAsset
from maltoolbox.language import LanguageGraph


def connect_computer_to_computer(model: Model, comp1: ModelAsset, comp2: ModelAsset):
    """
    Create a connection rule between comp1 and comp2 and return it.
    """
    cr_asset_name = f"ConnectionRule {comp1.name} {comp2.name}"
    cr_asset = model.add_asset("ComputerConnectionRule", cr_asset_name)
    comp1.add_associated_assets("computer1", [cr_asset])
    comp2.add_associated_assets("computer2", [cr_asset])
    return cr_asset


def connect_computer_to_folder(model: Model, comp: ModelAsset, folder: ModelAsset):
    """
    Create a connection rule between comp and folder and return it.
    """
    cr_asset_name = f"ConnectionRule {comp.name} {folder.name}"
    cr_asset = model.add_asset("ComputerFolderConnectionRule", cr_asset_name)
    comp.add_associated_assets("computer", [cr_asset])
    folder.add_associated_assets("folder", [cr_asset])
    return cr_asset
```
These helper functions are made to work with the our `my-language.mal` language. Here we defined how the assets will connect with each other. Each function creates assets in a model and connects the assets to other assets using associations.

Now we can create a model and use the helper methods. Add this to the end of the file:

```python
def create_model(lang_graph: LanguageGraph) -> Model:
    """Create a model with 2 computers"""
    model = Model("my-model", lang_graph)

    # Two computers
    comp_a = model.add_asset("Computer", "ComputerA")
    comp_b = model.add_asset("Computer", "ComputerB")

    # Connection between computers
    connect_computer_to_computer(model, comp_a, comp_b)

    # two folders with connection to the computers
    folder1 = model.add_asset("Folder", "ComputerA")
    connect_computer_to_folder(model, comp_a, folder1)
    folder2 = model.add_asset("Folder", "ComputerB")
    connect_computer_to_folder(model, comp_b, folder2)

    return model


def main():
    lang_file = "my-language.mal"
    current_dir = os.path.dirname(os.path.abspath(__file__))
    lang_file_path = os.path.join(current_dir, lang_file)
    my_language = LanguageGraph.load_from_file(lang_file_path)

    # Create our example model
    model = create_model(my_language)


if __name__ == "__main__":
    main()
```

To compile this, run the script with `python my-model.py`.