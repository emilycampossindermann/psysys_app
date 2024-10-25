import dash
import dash_bootstrap_components as dbc

app = dash.Dash(
    __name__,
    external_stylesheets=[
        dbc.themes.BOOTSTRAP,
        'https://use.fontawesome.com/releases/v6.6.0/css/all.css',
        'assets/styles.css'
    ],
    assets_folder='assets',
    suppress_callback_exceptions=True
)

server = app.server

app.title = "PsySys"
