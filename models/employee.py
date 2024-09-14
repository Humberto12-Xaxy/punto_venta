class Employee:

    def __init__(self, name:str, username:str, password:str, rol:str):
        self._name = name
        self._username = username
        self._password = password
        self._rol = rol

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
        return f"Name: {self._name}, Username: {self._username}, Password: {self._password}, Rol: {self._rol}"