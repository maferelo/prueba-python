import argparse

import os
import json
import sys

from usuario import usuario

def create_parser():
    # Create the parser
    my_parser = argparse.ArgumentParser(prog='usuarios',
                                        description='CRUD usuarios')

    # Add the arguments
    my_parser.add_argument('user_id',
                            nargs='?',
                            type=str,
                            help='Id of the user')

    my_parser.add_argument('-l',
                            '--list',
                            action='store_true',
                            help='List all users')

    my_parser.add_argument('-u',
                            '--update',
                            action='store',
                            nargs='?',
                            default='nombres',
                            choices=['nombres', 'apellidos', 'edad', 'email'],
                            help='Choose field to update e.j. -u nombres')

    my_parser.add_argument('-v',
                            '--value',
                            action='store',
                            nargs='*',
                            help='New field value e.j. -v new value')

    my_parser.add_argument('-c',
                            '--create',
                            action='store',
                            nargs='*',
                            help='Get id for new user')
    
    return my_parser


def parse_args(args, my_parser):
    users_class = usuario.Usuario()
    if args.list:
        print(users_class)
    elif args.user_id and args.update and args.value:
        users_class.update_user(args.user_id, args.update, ' '.join(args.value))
    elif args.user_id and not (args.update or args.value):
        users_class.get_user(args.user_id)
    elif args.create:
        users_class.create_user()
    else:
        my_parser.print_help()
    

if __name__ == '__main__':
    my_parser = create_parser()
    args = my_parser.parse_args()
    parse_args(args, my_parser)