import flet as ft


def main(page: ft.Page):
    page.add(ft.SafeArea(ft.Text("Hello, 中国!")))


ft.app(target=main, view=ft.AppView.WEB_BROWSER)
