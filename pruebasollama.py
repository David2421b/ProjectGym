from nicegui import ui


@ui.page('/redirect')
def redirect():
    ui.label("Redirecting...").style("font-size: 40px; color: green; text-align: center;")


ui.button('REDIRECT', on_click=lambda: ui.open(redirect))
ui.run()