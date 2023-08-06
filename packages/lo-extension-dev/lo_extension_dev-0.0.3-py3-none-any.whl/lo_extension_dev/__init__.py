__version__='0.0.3'

import os
import yaml

config = {}


def load_config(file_str: str='extension.yml') -> None:
    global config
    fp = os.path.join(os.getcwd(), file_str)
    with open(fp) as f:
        config.update(yaml.safe_load(f))
    config.update({
        'output': f"extension/{config['version']}",
        'extension_fn': f"{config['extension_name']}.{config['file_extension']}",
        'user_directory': os.path.expanduser('~'),
    })


load_config()
