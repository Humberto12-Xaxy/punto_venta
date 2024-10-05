from flet import (
    Container,
    DataTable,
    Text,
    FontWeight,
    colors,
    Column,
    Row,
    icons,
    DataColumn,
    DataRow,
    IconButton,
    MainAxisAlignment,
    Page,
    ControlEvent
)


class DataTablePagination(Container):

    DEFAULT_ROW_PER_PAGE = 10

    def __init__(self, page: Page, data_table: DataTable, rows_per_page: int = DEFAULT_ROW_PER_PAGE):
        super().__init__()
    
        self.width = page.window.width * 0.8

        self.data_table = data_table
        self.rows_per_page = rows_per_page

        self.num_rows = len(self.data_table.rows)
        self.current_page = 1

        p_int, p_add = divmod(self.num_rows, self.rows_per_page)
        self.num_pages = p_int + (1 if p_add else 0)

        self.v_current_page = Text(
            str(self.current_page),
            weight=FontWeight.BOLD,
            color=colors.GREY_500
        )

        self.v_count = Text(
            color='black'
        )

        self.pdt = DataTable(
            width=page.window.width * 0.8,
            columns=self.data_table.columns,
            rows=self.build_rows()
        )

        self.content = Column(
            horizontal_alignment='center',
            controls=[
                self.pdt,
                Row(
                    controls=[
                        Row(
                            controls=[
                                IconButton(
                                    icon=icons.KEYBOARD_DOUBLE_ARROW_LEFT,
                                    icon_color='#495B6B' if self.num_pages == 1 and self.current_page == 1 else colors.GREY_500,
                                    on_click=self.goto_first_page,
                                    tooltip='First page',
                                    disabled= False if self.num_pages == 1 and self.current_page == 1 else True
                                ),
                                IconButton(
                                    icon=icons.ARROW_LEFT,
                                    on_click=self.previous_page,
                                    icon_color='#495B6B'if self.num_pages == 1 and self.current_page == 1 else colors.GREY_500,
                                    tooltip='Previous page',
                                    disabled= False if self.num_pages == 1 and self.current_page == 1 else True
                                ),
                                self.v_current_page,
                                IconButton(
                                    icon=icons.ARROW_RIGHT,
                                    on_click=self.next_page,
                                    icon_color='#495B6B',
                                    tooltip='Next page',
                                    disabled=self.num_pages == 1
                                ),
                                IconButton(
                                    icon=icons.KEYBOARD_DOUBLE_ARROW_RIGHT,
                                    on_click=self.goto_last_page,
                                    icon_color='#495B6B',
                                    tooltip='Last page',
                                    disabled= self.num_pages == 1
                                ),
                            ]
                        ),
                        self.v_count
                    ],
                    alignment=MainAxisAlignment.SPACE_BETWEEN
                )
            ]
        )

    @property
    def datatable(self) -> DataTable:
        return self.pdt

    @property
    def data_columns(self) -> list[DataColumn]:
        return self.pdt.columns

    @property
    def data_rows(self) -> list[DataRow]:
        return self.pdt.rows
    
    @data_rows.setter
    def data_rows(self, rows: list[DataRow]):
        self.pdt.rows = rows
        self.num_rows = len(self.pdt.rows)
        p_int, p_add = divmod(self.num_rows, self.rows_per_page)
        self.num_pages = p_int + (1 if p_add else 0)
        self.v_count.value = f'Total rows: {self.num_rows}'
        self.v_current_page.value = f'{self.current_page}/{self.num_pages}'
        if self.num_pages == 1:
            self.content.controls[1].controls[0].controls[0].disabled = True
            self.content.controls[1].controls[0].controls[0].icon_color = colors.GREY_500
            self.content.controls[1].controls[0].controls[1].disabled = True
            self.content.controls[1].controls[0].controls[1].icon_color = colors.GREY_500
            self.content.controls[1].controls[0].controls[3].disabled = True
            self.content.controls[1].controls[0].controls[3].icon_color = colors.GREY_500
            self.content.controls[1].controls[0].controls[4].disabled = True
            self.content.controls[1].controls[0].controls[4].icon_color = colors.GREY_500
        else:
            self.content.controls[1].controls[0].controls[0].disabled = False
            self.content.controls[1].controls[0].controls[0].icon_color = '#495B6B'
            self.content.controls[1].controls[0].controls[1].disabled = False
            self.content.controls[1].controls[0].controls[1].icon_color = '#495B6B'
            self.content.controls[1].controls[0].controls[3].disabled = False
            self.content.controls[1].controls[0].controls[3].icon_color = '#495B6B'
            self.content.controls[1].controls[0].controls[4].disabled = False
            self.content.controls[1].controls[0].controls[4].icon_color = '#495B6B'
        
        self.refresh_data()
        self.build_rows()

    def set_page(self, page: [str, int, None] = None, delta: int = 0):
        if page is not None:
            try:
                self.current_page = int(page) if 1 <= int(
                    page) <= self.num_pages else 1
            except ValueError:
                self.current_page = 1
        elif delta:
            self.current_page += delta
        else:
            return

        self.refresh_data()

    def next_page(self, e: ControlEvent):
        if self.current_page < self.num_pages:
            self.set_page(delta=1)
        
            if self.current_page == self.num_pages:
                self.content.controls[1].controls[0].controls[0].disabled = False
                self.content.controls[1].controls[0].controls[0].icon_color = '#495B6B'
                self.content.controls[1].controls[0].controls[1].disabled = False
                self.content.controls[1].controls[0].controls[1].icon_color = '#495B6B'
                self.content.controls[1].controls[0].controls[3].disabled = True
                self.content.controls[1].controls[0].controls[3].icon_color = colors.GREY_500
                self.content.controls[1].controls[0].controls[4].disabled = True
                self.content.controls[1].controls[0].controls[4].icon_color = colors.GREY_500
            self.update()
    def previous_page(self, e: ControlEvent):
        if self.current_page > 1:
            self.set_page(delta=-1)
            if self.current_page == 1:
                self.content.controls[1].controls[0].controls[0].disabled = True
                self.content.controls[1].controls[0].controls[0].icon_color = colors.GREY_500
                self.content.controls[1].controls[0].controls[1].disabled = True
                self.content.controls[1].controls[0].controls[1].icon_color = colors.GREY_500
                self.content.controls[1].controls[0].controls[3].disabled = False
                self.content.controls[1].controls[0].controls[3].icon_color = '#495B6B'
                self.content.controls[1].controls[0].controls[4].disabled = False
                self.content.controls[1].controls[0].controls[4].icon_color = '#495B6B'
            self.update()

    def goto_first_page(self, e: ControlEvent):
        self.set_page(page=1)

    def goto_last_page(self, e: ControlEvent):
        self.set_page(page=self.num_pages)

    def build_rows(self) -> list:
        start, end = self.paginate()
        return self.data_table.rows[slice(start, end)]

    def paginate(self) -> tuple[int, int]:

        i1_multiplier = 0 if self.current_page == 1 else self.current_page - 1
        i1 = i1_multiplier * self.rows_per_page
        i2 = self.current_page * self.rows_per_page

        return i1, i2

    def refresh_data(self):
        self.pdt.rows = self.build_rows()
        self.v_count.value = f'Total rows: {self.num_rows}'
        self.v_current_page.value = f'{self.current_page}/{self.num_pages}'

        self.v_current_page.visible = True
        self.page.update()
        self.update()

    def did_mount(self):
        self.refresh_data()


    