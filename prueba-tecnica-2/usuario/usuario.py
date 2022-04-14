import csv
import json
import uuid
import os 

from abc import ABC, abstractmethod

dir_name = os.path.dirname(os.path.realpath(__file__))

USER_MODEL = {
    "nombres": '',
    "apellidos": '',
    "edad": '',
    "email": ''
}

class Storage(ABC):
    def __init__(self, file_name):
        self.path = os.path.join(dir_name, file_name)

    @abstractmethod
    def load(self, path):
        pass

    @abstractmethod
    def save(self, data):
        pass

    def get_path(self):
        return self.path

class JsonStorage(Storage):
    def __init__(self, file_name):
        super().__init__(file_name)

    def load(self):
        data = {}
        if not os.stat(self.get_path()).st_size == 0 or not os.path.isfile(self.get_path()):
            with open(self.get_path(), 'r') as openfile:
                data = json.load(openfile)
        return data

    def save(self, data):
        json_object = json.dumps(data, indent=2)
        with open(self.get_path(), "w") as outfile:
            outfile.write(json_object)

# FACADE DESIGN PATTERN
class Usuario:
    def __init__(self, storage: Storage):
        self.users = storage.load()
        self.storage = storage

    def __str__(self):
        return str(self.users)

    def create_user(self):
        new_id = str(uuid.uuid4())
        while self.user_exists(new_id):
            new_id = str(uuid.uuid4())

        self.users[new_id] = USER_MODEL
        self.storage.save(self.users)
        print("Created id {}".format(new_id))
        return new_id

    def update_user(self, id_, field, new_value):
        if self.user_exists(id_):
            self.users[id_][field] = new_value 
            self.storage.save(self.users)
            print("Updated.")
            print(self.users[id_])
            return self.users[id_]
        else:
            print("User does not exists.")

    def delete_user(self, id_):
        if self.user_exists(id_):
            del self.users[id_]
            self.storage.save(self.users)
            print("Deleted.")
        else:
            print("User does not exists.")

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