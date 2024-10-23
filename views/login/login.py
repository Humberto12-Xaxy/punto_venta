from flet import (
    Page,
    TextField,
    Text,
    Column,
    Container,
    ElevatedButton,
    MainAxisAlignment,
    CrossAxisAlignment
)

from bcrypt import checkpw

from controllers.employee_controller import EmployeeController

from models.employee import Employee


class Login(Container):
    def __init__(self, page: Page):
        super().__init__()
        self.page = page

        self.expand = True
        self.width = page.window.width
        self.height = page.window.height

        self.bgcolor = 'white'
        self.employee_controller = EmployeeController()

        self.content = Column(
            [
                Text(
                    'Login',
                    color='black',
                    size=30
                ),
                TextField(
                    width=300,
                    label='Username',
                    autofocus=True,
                    color='black'
                ),
                TextField(
                    width=300,
                    label='Password',
                    password=True,
                    color='black'
                ),
                ElevatedButton(
                    'Iniciar sesión',
                    on_click=self.login
                )
            ],
            alignment=MainAxisAlignment.CENTER,
            horizontal_alignment= CrossAxisAlignment.CENTER
        )

    def login(self, e):

        username = self.content.controls[1].value
        user_password = self.content.controls[2].value

        password = self.employee_controller.get_employee_by_username(username)

        if password:
            password = password[0]
            user_password = bytes(user_password, 'utf-8')
            if checkpw(password, password):
                print('Login correcto')

