import os
from maltoolbox.model import Model
from maltoolbox.language import LanguageGraph
from maltoolbox.attackgraph import AttackGraph
from malsim import MalSimulator, run_simulation
from malsim.policies import RandomAgent
from malsim import MalSimulator, run_simulation, AttackerSettings


def create_model(lang_graph: LanguageGraph) -> Model:
    model = Model("my-model", lang_graph)

    # Two computers
    comp_a = model.add_asset("Computer", "ComputerA")
    comp_b = model.add_asset("Computer", "ComputerB")

    # Connection between computers
    comp_a.add_associated_assets("toComputer", {comp_b})

    # Two folders
    folder1 = model.add_asset("Folder", "FolderA")
    folder2 = model.add_asset("Folder", "FolderB")

    # Connect the folders to the computers
    comp_b.add_associated_assets("folder", {folder2})
    comp_a.add_associated_assets("folder", {folder1})

    return model


def main():
    lang_file = "my-language.mal"
    current_dir = os.path.dirname(os.path.abspath(__file__))
    lang_file_path = os.path.join(current_dir, lang_file)
    my_language = LanguageGraph.load_from_file(lang_file_path)

    # Create our example model and generate the attack graph
    model = create_model(my_language)
    graph = AttackGraph(my_language, model)

    # Register the agent
    agent_settings = AttackerSettings(
        "MyAttacker",
        entry_points={"ComputerA:access"},
        goals={"FolderB:stealSecrets"},
        policy=RandomAgent
    )

    simulator = MalSimulator(graph)
    simulator.register_attacker_settings(agent_settings)
    path = run_simulation(simulator, {'MyAttacker': agent_settings})


if __name__ == "__main__":
    main()
