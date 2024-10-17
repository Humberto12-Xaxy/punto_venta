class Employee:

    def __init__(self, id:int, name:str, username:str, password:str, rol:str):
        self._id = id
        self._name = name
        self._username = username
        self._password = password
        self._rol = rol

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id:int):
        self._id = id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name:str):
        self._name = name

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username:str):
        self._username = username
    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password:str):
        self._password = password

    @property
    def rol(self):
        return self._rol

    @rol.setter
    def rol(self, rol:str):
        self._rol = rol
    
    def __str__(self):
        return f"Id: {self._id}, Name: {self._name}, Username: {self._username}, Password: {self._password}, Rol: {self._rol}"