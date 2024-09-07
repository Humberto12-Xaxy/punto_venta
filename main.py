import flet 
from flet import *

from database.create_table import create_table
from views.main_view import MainView

create_table()

def main(page: Page):
    MainView(page)


flet.app(target=main)