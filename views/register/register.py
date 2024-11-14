from flet import (
    View,
    Page,
    Container,
    Column,
    ElevatedButton,
    TextField,
    Dropdown,
    dropdown,
    Text,
    CrossAxisAlignment,
    MainAxisAlignment,
    SnackBar
)


from controllers.employee_controller import EmployeeController
import bcrypt


class RegisterView(View):
    def __init__(self, page: Page):
        super().__init__()
        self.page = page

        self.bgcolor = 'white'

        self.controller = EmployeeController()

        self.controls = [
            Container(
                content=Column(
                    controls=[
                        Text("Registrar usuario", size=30, color="black"),
                        TextField(
                            label="Nombre",
                            color='black',
                            width=300),
                        TextField(
                            label="Nombre de usuario",
                            color='black',
                            width=300),
                        TextField(
                            label="Contraseña",
                            color='black',
                            password=True, 
                            width=300,
                            can_reveal_password=True),
                        ElevatedButton(
                            "Registrar",
                            on_click=self.register, width=200,
                            height=50,)
                    ],
                    width=page.window.width,
                    height=page.window.height,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    alignment=MainAxisAlignment.CENTER
                )
            )
        ]

    def register(self, e):
        
        name = self.controls[0].content.controls[1].value
        username = self.controls[0].content.controls[2].value
        password = self.controls[0].content.controls[3].value
        
        if name != '' and password != '' and username != '':

            pwd = password.encode('utf-8')
            salt = bcrypt.gensalt()
            hashed = bcrypt.hashpw(pwd, salt)

            employee = {
                'name': name,
                'username': username,
                'password': hashed,
                'rol': 'admin'
            }

            if self.controller.add_employee(employee['name'], employee['username'], employee['password'], employee['rol']):
                self.page.go('/')
                self.page.update()
            else:
                self.page.snack_bar = SnackBar(
                    Text('Error al registrar usuario', color='white'),
                    bgcolor= 'red'
                )
                self.page.snack_bar.open = True
                self.page.update()

