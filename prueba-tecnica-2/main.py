import argparse

import os
import sys

# Create the parser
my_parser = argparse.ArgumentParser(prog='main',
                                    description='Funcionalidades básicas modelo Usuario')

my_parser = argparse.ArgumentParser(description='Funcionalidades básicas modelo Usuario',
                                    epilog='Crea, modifica y lista el modelo Usuarios')

# Add the arguments
my_parser.add_argument('Path',
                       metavar='path',
                       type=str,
                       help='the path to list')

# Execute the parse_args() method
args = my_parser.parse_args()

input_path = args.Path

if not os.path.isdir(input_path):
    print('The path specified does not exist')
    sys.exit()

print('\n'.join(os.listdir(input_path)))