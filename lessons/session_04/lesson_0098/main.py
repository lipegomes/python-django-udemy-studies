# 98. Encapsulamento - Python Orientado a Objetos

"""
_ protected (public _)
__private (_CLASSNAME__atrybut)

"""


class DataBase:
    def __init__(self):
        self.__data = {}

    @property
    def data(self):
        return self.__data

    def insert_client(self, id, name):
        if "clients" not in self.__data:
            self.__data["clients"] = {id: name}
        else:
            self.__data["clients"].update({id: name})

    def clients_list(self):
        for id, name in self.__data["clients"].items():
            print(id, name)

    def delete_client(self, id):
        del self.__data["clients"][id]


db = DataBase()
db.insert_client(1, "Luffy")
db.insert_client(2, "Zoro")
db.insert_client(3, "Goku")
db.insert_client(4, "Urek Mazino")

# print(db._data)
print(db._DataBase__data)

# db.delete_client(4)
# db.clients_list()

db.__data = "Another value"
print(db.__data)

print(db.data)
