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
