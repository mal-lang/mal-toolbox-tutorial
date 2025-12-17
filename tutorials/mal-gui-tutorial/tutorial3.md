# Tutorial 3 - How to use the MAL GUI
The mal-gui is a graphical user interface tool used to create MAL instance models and scenarios (with attacker agents specified). In this tutorial we will learn how to use it.

## Installation
1. In your working directory, clone the mal-gui repository: `git clone https://github.com/mal-lang/mal-gui.git`.
2. Create a virtual environment and activate it.
    - On Linux-based operating systems:
    ```
    python -m venv venv
    source venv/bin/activate
    ```
    - On Windows:
    ```
    python -m venv venv
    .\venv\Scripts\activate
    ```
3. Install the mal-gui package: `pip install mal-gui`.
4. Run the GUI: `malgui`

## Loading a language and creating assets
When we first run the GUI, we get the following Window:

![alt text](image.png)

If you don't know how to create a MAL language, you can follow this [tutorial](https://github.com/mal-lang/mal-toolbox-tutorial/tree/main/tutorials/language-model-tutorial).

To keep things simple, we will download and use the same simple MAL language used in that tutorial (`my-language.mal`).

The next step is to add assets. To do so, Add an asset we can drag and drop new assets from the object explorer on the left. In this case, they are `Computer` and `Folder`.