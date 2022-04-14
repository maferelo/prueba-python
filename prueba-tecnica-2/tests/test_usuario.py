import random
import string
import unittest

from context import usuario

import main


# Create test users
DUMMY_USER = [
    "Manuel Felipe",
    "Restrepo Londoño",
    "29",
    "maferelo@outlook.com"
]

letters = string.digits
rando = ' ' + ''.join(random.choice(letters) for i in range(3))
DUMMY_USER = [d + rando for d in DUMMY_USER]

class TestUser(unittest.TestCase):

    def test_usuario_dict(self):
        users_class = usuario.Usuario()
        self.assertEqual(type(users_class.users), dict)

    def test_usuario_load_users(self):
        users_class = usuario.Usuario()
        self.assertEqual(type(users_class.users), dict)

    def test_usuario_delete_user(self):
        users_class = usuario.Usuario()
        new_id = users_class.create_user(*DUMMY_USER)
        users_class.delete_user(new_id)
        self.assertEqual(users_class.user_exists(new_id), False)

    def test_usuario_create_user(self):
        users_class = usuario.Usuario()
        old_user_count = users_class.get_user_count()
        new_id = users_class.create_user(*DUMMY_USER)
        new_user_count = users_class.get_user_count()
        users_class.delete_user(new_id)
        self.assertEqual(old_user_count + 1, new_user_count)

    def test_usuario_update_user(self):
        field, new_value = ["nombres", "updated"]
        users_class = usuario.Usuario()
        new_id = users_class.create_user(*DUMMY_USER)
        updated_user = users_class.update_user(new_id, field, new_value)
        self.assertEqual(updated_user[field], new_value)

    def test_main_create_parser(self):
        my_parser = main.create_parser()
        args = my_parser.parse_args(['-l'])
        main.parse_args(args, my_parser)

if __name__ == '__main__':
    unittest.main()