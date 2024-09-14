from flet import (
    Page,
    TextField,
    IconButton,
    Row,
    icons,
    colors,
    FloatingActionButton
)


class SeachWidget(Row):

    def __init__(self, page: Page):
        super().__init__()

        self.page = page
        
        self.width = page.window.width - 300
        self.alignment = 'end'

        self.controls = [
            TextField(
                width=500,
                height=40,
                color="white",
                border_color=colors.GREY_100,
                bgcolor="grey",
            ),
            FloatingActionButton(
                icon=icons.SEARCH,
                width=40,
                height=40,
                bgcolor="grey",
                on_click=lambda _: print(_)
            )
        ]
        self.page.update()
        