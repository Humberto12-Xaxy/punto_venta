import flet as ft

def create_navigation_rail(page: ft.Page) -> list[ft.NavigationRailDestination]:
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
    ) if page.client_storage.get('privileges') == 'admin' else ft.NavigationRailDestination(
        
    ),
    ft.NavigationRailDestination(
        label_content=ft.Text('Empleados'),
        icon=ft.icons.PERSON,
        selected_icon=ft.icons.PERSON,
    ) if page.client_storage.get('privileges') == 'admin' else ft.NavigationRailDestination(
        
    ),
]
    return LIST_DESTINATIONS

LEADING = ft.FloatingActionButton(
    icon=ft.icons.SHOP_2, text="Vender", tooltip="Vender")

NAVIGATION_RAIL_SETTINGS = {
    'leading': LEADING,
    'label_type': ft.NavigationRailLabelType.ALL,
    'selected_index': 0,
}
