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


def main():
    lang_file = "my-language.mal"
    current_dir = os.path.dirname(os.path.abspath(__file__))
    lang_file_path = os.path.join(current_dir, lang_file)
    my_language = LanguageGraph.load_from_file(lang_file_path)

    # Create our example model
    model = create_model(my_language)


if __name__ == "__main__":
    main()
