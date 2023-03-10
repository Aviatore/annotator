from argparse import ArgumentParser
import os
import sys
import json
from lib.Blast import Blast
from lib.Circos import Circos


def get_config():
    parser = ArgumentParser()
    parser.add_argument('-c', '--config', dest='config', required=True)
    args = parser.parse_args()

    if not os.path.exists(args.config):
        print(f'The provided config file "{args.config}" does not exist')
        exit()

    with open(args.config, 'r') as file:
        config_json = file.read()

        config = json.loads(config_json)

        return config


def main():
    config = get_config()
    circos = Circos(config)
    circos.run()



if __name__ == '__main__':
    main()
