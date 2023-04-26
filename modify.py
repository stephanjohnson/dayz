import xml.etree.ElementTree as ET
import yaml
import argparse

# Set up command-line argument parser
parser = argparse.ArgumentParser(description='Modify types.xml based on a YAML configuration file.')
parser.add_argument('config_file', type=str, help='Path to the YAML configuration file')
args = parser.parse_args()

# Read the YAML configuration file
with open(args.config_file, 'r') as file:
    config = yaml.safe_load(file)

# Read the original types.xml file
tree = ET.parse('types.xml')
root = tree.getroot()

# Function to update the nominal value for specific items
def update_item(item_config):
    item_name = item_config['name']
    factor = item_config.get('factor', 1)
    restock = item_config.get('restock')
    lifetime = item_config.get('lifetime')
    tier_changes = item_config.get('tier', [])

    item_found = False

    for item in root.iter('type'):
        if item.get('name') == item_name:
            item_found = True

            # Update nominal value
            nominal = int(item.get('nominal'))
            new_nominal = int(nominal * factor)
            item.set('nominal', str(new_nominal))

            # Update restock and lifetime values if provided
            if restock is not None:
                item.set('restock', str(restock))
            if lifetime is not None:
                item.set('lifetime', str(lifetime))

            # Update tier values
            if not isinstance(tier_changes, list):
                tier_changes = [tier_changes]
            for i in range(1, 5):
                if i in tier_changes:
                    item.set(f'tier{i}', '1')
                else:
                    item.set(f'tier{i}', '0')

    if not item_found:
        print(f"Warning: Item '{item_name}' not found in types.xml")

# Update the nominal values for items in the config
for item in config['items']:
    update_item(item)

# Save the updated XML to a new file
tree.write('types.updated.xml', encoding='utf-8', xml_declaration=True)
