from flet import (
    AlertDialog,
    Text,
    Page,
    Dropdown,
    dropdown,
    TextButton,
    Column,
    MainAxisAlignment,
    CrossAxisAlignment,
    ControlEvent,
    ButtonStyle,
    TextField,
    SnackBar
)

import bcrypt

from models.employee import Employee

from controllers.employee_controller import EmployeeController

from widgets.dt_pagination import DataTablePagination

class ModalWidget(AlertDialog):
    def __init__(self, page: Page, table, table_pagination: DataTablePagination = None, employee:Employee= None):
        super().__init__()

        self.page = page
        self.modal = True

        self.employee_controller = EmployeeController()

        self.table_pagination = table_pagination
        self.table = table

        self.title = Text('Registrar usuario', color='black')

        self.bgcolor = 'white'

        self.employee = employee

        self.content = Column(
            height= self.page.height * 0.35,
            width= self.page.width * 0.3,
            horizontal_alignment= CrossAxisAlignment.CENTER,
            alignment= MainAxisAlignment.SPACE_EVENLY,
            controls=[
                TextField(
                    width= self.page.width * 0.2,
                    label= 'Nombre',
                    color= 'black',
                    value= employee.name if employee else '',
                ),
                TextField(
                    width= self.page.width * 0.2,
                    label= 'Nombre de usuario',
                    color= 'black',
                    value= employee.username if employee else '',
                ),
                TextField(
                    width= self.page.width * 0.2,
                    label= 'Contraseña',
                    color= 'black',
                    password= True,
                    can_reveal_password= True,
                    value= employee.password.decode() if employee else '',
                ),
                Dropdown(
                    width= self.page.width * 0.2,
                    label= 'Rol',
                    bgcolor = 'white',
                    color= 'black',
                    options=[
                        dropdown.Option(text='admin'),
                        dropdown.Option(text='cajero'),
                    ],
                    value= employee.rol if employee else '',
                ),  
            ]
        )

        self.actions = [
            TextButton(
                'Registrar' if not employee else 'Actualizar',
                style= ButtonStyle(color='green'),
                on_click= self.register_user if not employee else self.update_user
            ),
            TextButton(
                'Cancelar',
                on_click= self.close
            )
        ]

    
    def close(self, e:ControlEvent):
        self.page.close(self)
    
    def register_user(self, e: ControlEvent):

        name = self.content.controls[0].value
        username = self.content.controls[1].value
        password:str = self.content.controls[2].value
        role = self.content.controls[3].value

        if name != '' and password != '' and username != '' and role != '':
            
            pwd = password.encode('utf-8')
            salt = bcrypt.gensalt()
            hashed = bcrypt.hashpw(pwd, salt)

            employee = {
                'name': name,
                'username': username,
                'password': hashed,
                'rol': role
            }
            

            if self.employee_controller.add_employee(employee['name'], employee['username'], employee['password'], employee['rol']):
                self.page.close(self)
                self.table.load_rows()
                self.table_pagination.data_rows = self.table.rows
                self.table_pagination.build_rows()
                self.page.snack_bar = SnackBar(
                    Text('Usuario registrado exitosamente', color='white'),
                    bgcolor= 'green'
                )
                self.page.snack_bar.open = True
                self.page.update()
            
            else:
                self.page.snack_bar = SnackBar(
                    Text('Hubo un error al registrar el usuario', color='white'),
                    bgcolor= 'red'
                )
                self.page.snack_bar.open = True
                self.page.update()

    def update_user(self, e: ControlEvent):

        name = self.content.controls[0].value
        username = self.content.controls[1].value
        password:str = self.content.controls[2].value
        role = self.content.controls[3].value

        if name != '' and password != '' and username != '' and role != '':

            pwd = password.encode('utf-8')
            salt = bcrypt.gensalt()
            hashed = bcrypt.hashpw(pwd, salt)

            employee = {
                'id_employee': self.employee.id,
                'name': name,
                'username': username,
                'password': hashed,
                'rol': role
            }

            if self.employee_controller.update_employee(employee['id_employee'], employee['name'], employee['username'], employee['password'], employee['rol']):
                self.page.close(self)
                self.page.snack_bar = SnackBar(
                    Text('Usuario actualizado exitosamente', color='white'),
                    bgcolor= 'green'
                )
                self.page.snack_bar.open = True
                self.page.update()
            
            else:
                self.page.snack_bar = SnackBar(
                    Text('Hubo un error al actualizar el usuario', color='white'),
                    bgcolor= 'red'
                )
                self.page.snack_bar.open = True
                self.page.update()