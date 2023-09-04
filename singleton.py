class DataBase:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            return cls.__instance
        else:
            return 'already created'

    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port
 
    def connect(self):
        print(f"соединение с БД: {self.user}, {self.psw}, {self.port}")
 
    def close(self):
        print("закрытие соединения с БД")
 
    def read(self):
        return "данные из БД"
 
    def write(self, data):
        print(f"запись в БД {data}")

    def __del__(self):
        print('del' + str(self.connect()))
        cls = self.__class__
        cls.__instance = None

db = DataBase('root', '1234', 80)
db.connect()
print(id(db))
db.__del__()
db2 = DataBase('root2', '5678', 40)
db2.connect()
print(id(db2))