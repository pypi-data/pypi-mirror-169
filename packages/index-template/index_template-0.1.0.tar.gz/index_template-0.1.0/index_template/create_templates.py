from index_template.index_configs import index_config_lists
from index_template.utils import create_index, build_template_json
from loguru import logger
import json

def main():
    for config in index_config_lists:
        # Uncomment to pretty print the template
        # print(json.dumps(build_template_json(config), indent=2))

        logger.info(f'Creating index {config.index_name} in {config.uri}')
        response = create_index(config)
        logger.info(f'Creating Index Response: {response}')

if __name__ == "__main__":
    main()