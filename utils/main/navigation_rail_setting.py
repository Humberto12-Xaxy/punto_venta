import flet as ft

LIST_DESTINATIONS = [
    ft.NavigationRailDestination(
        label_content=ft.Text('Vender'),
        icon=ft.icons.POINT_OF_SALE,
        selected_icon=ft.icons.POINT_OF_SALE,
    ),
    ft.NavigationRailDestination(
        label_content=ft.Text('Inventario'),
        icon=ft.icons.INVENTORY,
        selected_icon=ft.icons.INVENTORY,
    ),
    ft.NavigationRailDestination(
        label_content=ft.Text('Ventas'),
        icon=ft.icons.ATTACH_MONEY,
        selected_icon=ft.icons.ATTACH_MONEY,
    ),
]

LEADING = ft.FloatingActionButton(
    icon=ft.icons.SHOP_2, text="Vender", tooltip="Vender")

NAVIGATION_RAIL_SETTINGS = {
    'leading': LEADING,
    'label_type': ft.NavigationRailLabelType.ALL,
    'selected_index': 0,
    'destinations': LIST_DESTINATIONS,
}
