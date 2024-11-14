from flet import (
    Page,
    TextField,
    Text,
    Column,
    Row,
    Container,
    ElevatedButton,
    MainAxisAlignment,
    CrossAxisAlignment,
    TextStyle
)

from bcrypt import checkpw

from controllers.employee_controller import EmployeeController

from models.employee import Employee


class Login(Row):
    def __init__(self, page: Page):
        super().__init__()
        self.page = page

        self.bgcolor = 'white'
        self.employee_controller = EmployeeController()

        self.expand = True

        self.controls = [
            Container(
                bgcolor='white',
                expand=True,
                content=Column(
                    [
                        Text(
                            'Login',
                            color='black',
                            size=30
                        ),
                        TextField(
                            width=300,
                            label='Username',
                            label_style=TextStyle(color='gray'),
                            autofocus=True,
                            color='black'
                        ),
                        TextField(
                            width=300,
                            label='Password',
                            label_style=TextStyle(color='gray'),   
                            password=True,
                            color='black',
                            can_reveal_password=True
                        ),
                        ElevatedButton(
                            'Iniciar sesión',
                            width=200,
                            height=50,
                            on_click=self.login
                        )
                    ],
                    alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    width=page.window.width,
                    height=page.window.height
                )

            )

        ]

    def login(self, e):

        username = self.controls[0].content.controls[1].value
        user_password = self.controls[0].content.controls[2].value

        user = self.employee_controller.get_employee_by_username(username)

        if user:
            password = user[3]
            user_password = bytes(user_password, 'utf-8')
            if checkpw(user_password, password):
                self.page.client_storage.set('privileges', user[4])
                print(self.page.client_storage.get('privileges'))
                self.page.go('/main')
            else:
                print('Username o password incorrectos')
        else:
            print('Username o password incorrectos')