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
    Computer [computer1] * <-- ComputerConnection --> * [computer2] Computer
    Computer [computer] * <-- ComputerFolderConnection --> * [folder] Folder
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
from maltoolbox.model import Model
from maltoolbox.language import LanguageGraph


def create_model(lang_graph: LanguageGraph) -> Model:
    """Create a model with 2 computers"""
    model = Model("my-model", lang_graph)

    # Two computers
    comp_a = model.add_asset("Computer", "ComputerA")
    comp_b = model.add_asset("Computer", "ComputerB")

    # Connection between computers
    comp_a.add_associated_assets("computer2", [comp_b])

    # Two folders
    folder1 = model.add_asset("Folder", "FolderA")
    folder2 = model.add_asset("Folder", "FolderB")

    # Connect the folders to the computers
    comp_b.add_associated_assets("folder", [folder2])
    comp_a.add_associated_assets("folder", [folder1])

    return model
```
In this simple function, we create:
- Two instances of our `Computer` asset (`ComputerA` and `ComputerB`) and our `Folder` asset (`FolderA` and `FolderB`).
- A connection between `ComputerA` and `ComputerB`. The string `"computer2"` comes from the `ComputerConnection` association in the MAL language we created. 
- Two connections between the computer and folder instances. The strings `"folder"` come from the `ComputerFolderConnection` association.

Now we can instantiate the model and compile. Add this to the end of the file:

```python
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
Change `lang_file` accordingly. Here we create the model using our own language. To compile it, run the script with `python my-model.py`.