# DayZ Custom Loot Configuration

This repository contains custom loot configuration files for DayZ servers. These configuration files are designed to modify the spawn rates, restock timers, and lifetimes of various in-game items such as weapons, armor, food, drink, medical supplies, and utility items. The goal of this configuration is to create a more balanced and enjoyable gameplay experience for players on the server.

## How to use

To use these custom loot configuration files, follow these steps:

1. Clone or download this repository to your local machine.
2. Open the `types.xml` file from your DayZ server's `Missions` folder (e.g., `DayZServer\mpmissions\dayzOffline.chernarusplus\db\types.xml`) in a text editor.
3. Make a backup of the original `types.xml` file before making any changes.
4. Install the required Python libraries (xmltodict, pyyaml, and ipywidgets) if you haven't already.
5. Open the provided Jupyter Notebook `apply_config.ipynb` in Jupyter.
6. Run the cells in the notebook and follow the instructions to select and apply the YAML configuration files to your `types.xml` file.
7. Save your modified `types.xml` file and upload it back to your DayZ server.
8. Restart your DayZ server to apply the changes.

## Customization

You can customize the YAML configuration files to better suit your preferences or the needs of your server. Each YAML file contains a list of items with the following properties:

- `name`: The name of the item as it appears in the `types.xml` file.
- `factor`: The factor by which the spawn rate (nominal value) should be multiplied.
- `restock`: The time in seconds after which the item should restock.
- `lifetime`: The time in seconds before the item despawns.
- `tier`: (Optional) The tier of the item, if applicable.

To change the configuration for a specific item, simply update its properties in the corresponding YAML file.

## License

This project is licensed under the [MIT License](LICENSE).

## Contributing

Feel free to submit pull requests or open issues if you find any problems or have suggestions for improvements.
