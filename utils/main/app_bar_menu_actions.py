from flet import (
    PopupMenuItem,
    icons,
    Page,
    ControlEvent
    )

def GET_LIST_MENU_ACTIONS(page: Page) -> list[PopupMenuItem]:
    LIST_MENU_ACTIONS = [
        PopupMenuItem(
            text='Logout', 
            icon=icons.LOGOUT,
            on_click=lambda e: on_click_logout(page),),
    ]

    return LIST_MENU_ACTIONS


def on_click_logout(page: Page):
    page.client_storage.clear()
    page.go('/')