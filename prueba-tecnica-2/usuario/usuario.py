import csv
import json
import uuid
import os 

dir_name = os.path.dirname(os.path.realpath(__file__))

class Usuario:
    def __init__(self):
        self.uri = 'ws://209.126.82.146:8080/'
        self.json_file_path = os.path.join(dir_name, 'users.json')
        self.users = {}
        self.load_users()

    def __str__(self):
        return str(self.users)

    def load_users(self):
        users = {}
        if not os.stat(self.get_path()).st_size == 0 or  not os.path.isfile(self.get_path()):
            with open(self.get_path(), 'r') as openfile:
                users = json.load(openfile)
        self.users = users

    def save_users_json(self):
        json_object = json.dumps(self.get_users(), indent=2)
        with open(self.get_path(), "w") as outfile:
            outfile.write(json_object)

    def create_user(self):
        new_id = str(uuid.uuid4())
        while self.user_exists(new_id):
            new_id = str(uuid.uuid4())

        self.users[new_id] = {
            "nombres": '',
            "apellidos": '',
            "edad": '',
            "email": ''
        }
        self.save_users_json()
        print("Created id {}".format(new_id))
        return new_id

    def update_user(self, id_, field, new_value):
        if self.user_exists(id_):
            self.users[id_][field] = new_value 
            self.save_users_json()
            print("Updated.")
            print(self.users[id_])
            return self.users[id_]
        else:
            print("User does not exists.")

    def delete_user(self, id_):
        if self.user_exists(id_):
            del self.users[id_]
            self.save_users_json()
            print("Deleted.")
        else:
            print("User does not exists.")

    def get_path(self):
        return self.json_file_path

    def get_user(self, id_):
        if self.user_exists(id_):
            user = self.users[id_]
            print(user)
            return user
        else:
            print("User does not exists.")

    def get_users(self):
        return self.users

    def get_user_count(self):
        return len(self.users)

    def user_exists(self, id_):
        return id_ in self.users


if __name__ == '__main__':
    fetcher = Fetcher()
    fetcher.start()