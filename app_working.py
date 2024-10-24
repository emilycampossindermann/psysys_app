from app import app
from constants import factors, hidden_style, visible_style
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from dash import dcc, html

# Import callbacks 
from callbacks.layout_callbacks import register_layout_callbacks
from callbacks.editing_callbacks import register_editing_callbacks
from callbacks.comparison_callbacks import register_comparison_callbacks

register_layout_callbacks(app)
register_editing_callbacks(app)
register_comparison_callbacks(app)

############################################################################################################
## LAYOUT
############################################################################################################
# Layout elements: Next & Back button
button_group = html.Div(
    [
        dbc.Button(html.I(className="fas fa-edit nav-icon"), 
                   id='go-to-edit', 
                   n_clicks=0, 
                   style=hidden_style, 
                   color="light"),
        dbc.Button(html.I(className="fas fa-solid fa-angle-right"), 
                   id='next-button', 
                   n_clicks=0, 
                   style=hidden_style, 
                   color="light"),
        dbc.Button(html.I(className="fas fa-solid fa-angle-left"), 
                   id='back-button', 
                   n_clicks=0, 
                   style=hidden_style, 
                   color="light"),
    ],
   style={
        'position': 'fixed',
        'bottom': '80px',
        'right': '35px',
        'display': 'flex',
        'flexDirection': 'row-reverse',  # Align buttons to the right
        'gap': '10px',                   # Adds space between the buttons
        'zIndex': '5000'                 # Ensure it's above other content
    }
)

buttons_map = html.Div(
    [
        dbc.Button("Load from session", id='load', n_clicks=0, style=hidden_style),
        dbc.Button("Upload", id='upload', n_clicks=0, style=hidden_style),
        dbc.Button("Download", id='download', n_clicks=0, style=hidden_style)
    ],
    style={
        'display': 'flex',
        'justifyContent': 'center',  # Centers the buttons horizontally
        'gap': '10px',               # Adds space between the buttons
    }
)

# Layout elements: Navigation sidebar
nav_col = dbc.Col(
    [
        html.Br(),
        html.Img(src="/assets/logo.png", 
                 style={"marginLeft": "-3.5px", 
                        "width": "100px", 
                        "height": "auto", 
                        "marginTop": "20px"}),
        dbc.Nav(
            [
                dbc.NavLink(html.I(className="fas fa-info-circle nav-icon"), 
                            id = "Psychoeducation", 
                            href="/", 
                            active="exact", 
                            style={"fontSize": "25px", 
                                   "marginLeft": "17px", 
                                   "marginTop": "100px", 
                                   "color": "#8793c9"}),
                dbc.NavLink(html.I(className="fas fa-edit nav-icon"),
                            id = "Edit My Map", 
                            href="/my-mental-health-map", 
                            active="exact",
                            style={"fontSize": "25px", 
                                   "marginLeft": "17px",
                                   "marginTop": "5px", 
                                   "color": "#8793c9"}),
                dbc.NavLink(html.I(className="fas fa-chart-bar nav-icon"), 
                            id = "Compare My Map", 
                            href="/track-my-mental-health-map", 
                            active="exact",
                            style={"fontSize": "25px", 
                                   "marginLeft": "17px",
                                   "marginTop": "5px", 
                                   "color": "#8793c9"}),
                dbc.NavLink(html.I(className="fas fa-users nav-icon"), 
                            id = "About Us", 
                            href="/about", 
                            active="exact",
                            style={"fontSize": "25px", 
                                   "marginLeft": "17px", 
                                   "color": "#8793c9"}),
            ],
            vertical=True,
            pills=True,
            className="nav-primary",
            id="nav-links"
        ),
        html.Br(), html.Br(), 

        dcc.Loading(
            id="loading-1",
            type="circle",
            color='#8793c9',
            children=html.Div(id="tab-content")
        ),

        dcc.Store(id="loading-state", data=False)  # False means not loading
    ],
    md=1,
    className="nav-yellow",  # Custom class for yellow background
    style={"position": "fixed", 
           "top": "0", 
           "left": "0", 
           "height": "100vh", 
           "overflowY": "auto", 
           "zIndex": "2000"}
)

# nav_col = dbc.Col(
#     [
#         html.Br(),
#         html.Img(src="/assets/logo.png", 
#                  style={"marginLeft": "-3.5px", 
#                         "width": "100px", 
#                         "height": "auto", 
#                         "marginTop": "20px"}),
#         dbc.Nav(
#             [
#                 dbc.NavLink(
#                     [html.I(className="fas fa-info-circle nav-icon"), " "],
#                     id="Psychoeducation",
#                     href="/",
#                     active="exact",
#                     style={"fontSize": "25px", "marginLeft": "17px", "marginTop": "100px", "color": "#8793c9"}
#                 ),
#                 dbc.NavLink(
#                     [html.I(className="fas fa-edit nav-icon"), " "],
#                     id="go-to-edit",
#                     href="/my-mental-health-map",
#                     active="exact",
#                     style={"fontSize": "25px", "marginLeft": "17px", "marginTop": "5px", "color": "#8793c9"}
#                 ),
#                 dbc.NavLink(
#                     [html.I(className="fas fa-chart-bar nav-icon"), " "],
#                     id="compare-map",
#                     href="/track-my-mental-health-map",
#                     active="exact",
#                     style={"fontSize": "25px", "marginLeft": "17px", "marginTop": "5px", "color": "#8793c9"}
#                 ),
#                 dbc.NavLink(
#                     [html.I(className="fas fa-users nav-icon"), " "],
#                     id="about-us",
#                     href="/about",
#                     active="exact",
#                     style={"fontSize": "25px", "marginLeft": "17px", "color": "#8793c9"}
#                 ),
#             ],
#             vertical=True,
#             pills=True,
#             className="nav-primary"
#         ),
#     ],
#     md=1,
#     className="nav-yellow",
#     style={"position": "fixed", "top": "0", "left": "0", "height": "100vh", "overflowY": "auto", "zIndex": "2000"}
# )

# Layout elements: Translation toggle
translation_toggle = dbc.Col([
    dcc.Dropdown(
        id='language-dropdown',
        className="custom-dropdown",
        options=[
            {'label': 'English', 'value': 'en'},
            {'label': 'Deutsch', 'value': 'de'}
        ],
        value='en',  # Default to English
        clearable=False,
        style={'float': 'right', 
               'width': '100px', 
               'color': '#8793c9'}
    )], 
    md=1, 
    style={'position': 'absolute', 
           'top': '10px', 
           'right': '50px',
           'textAlign': 'left', 
           'padding': '10px', 
           'zIndex': '3000'})

# Email toggle
email_toggle = dbc.Col([
    html.A(
        html.I(className="fas fa-envelope", style={'fontSize': '30px', 'color': '#9AA6D6'}),
        href="mailto:campos.sindermann@gmail.com?subject=Inquiry%20for%20PsySys%20App&",
        id="email-button", 
        style={
            'position': 'absolute',
            'top': '22px',
            'right': '15px',
            'textDecoration': 'none',
            'zIndex': '5000'
            }
        ),

    dbc.Tooltip(
        "e-mail",  # Tooltip text
        target="email-button",  # ID of the element to show the tooltip for
        placement="top",
        autohide=True, 
        delay={"show": 500, "hide": 100}
    )
    ], md = 1)

# Layout elements: Page content
content_col = dbc.Col(
    [
        dcc.Location(id='url', refresh=False),
        html.Div(id='page-content'),
        button_group,
        buttons_map
    ],
    md=9,
)

# Stylesheet for network 
stylesheet = [{'selector': 'node',
               'style': {'background-color': '#9CD3E1', 
                         'label': 'data(label)', 
                         'font-family': 'Arial'}},
              {'selector': 'edge',
               'style': {'curve-style': 'bezier', 
                         'target-arrow-shape': 'triangle', 
                         'control-point-step-size': '40px' }}
    ]

# Define app layout
app.layout = dbc.Container([
    dbc.Row([nav_col,translation_toggle, content_col, email_toggle]),
    dcc.Store(id='history-store', data=[]),
    dcc.Store(id='current-step', data={'step': 0}, storage_type='session'),
    dcc.Store(id='color_scheme', data=None, storage_type='session'),
    dcc.Store(id='edge-type', data=None, storage_type='session'),
    dcc.Store(id='sizing_scheme', data=None, storage_type='session'),
    dcc.Store(id='custom-color', data={}, storage_type='session'),
    html.Div(id='hidden-div', style={'display': 'none'}),
    dcc.Store(id='selected-nodes', data=[]), 
    dcc.Store(id='editing-mode', data=[]),
    dcc.Store(id='plot-mode', data=[]),
    dcc.Store(id='current-filename-store', storage_type='session'),
    dcc.Store(id='session-data', data={
        'dropdowns': {
            'initial-selection': {'options':[{'label': factor, 'value': factor} for factor in factors], 'value': None},
            'chain1': {'options':[], 'value': None},
            'chain2': {'options':[], 'value': None},
            'cycle1': {'options':[], 'value': None},
            'cycle2': {'options':[], 'value': None},
            'target': {'options':[], 'value': None},
            },
        'elements': [], 
        'edges': [],
        'add-nodes': [],
        'add-edges': [],
        'stylesheet': stylesheet,
        'annotations': []
    }, storage_type='session'),
    dcc.Store(id='edit-map-data', data={
        'dropdowns': {
            'initial-selection': {'options':[{'label': factor, 'value': factor} for factor in factors], 'value': None},
            'chain1': {'options':[], 'value': None},
            'chain2': {'options':[], 'value': None},
            'cycle1': {'options':[], 'value': None},
            'cycle2': {'options':[], 'value': None},
            'target': {'options':[], 'value': None},
            },
        'elements': [], 
        'edges': [],
        'add-nodes': [],
        'add-edges': [],
        'stylesheet': stylesheet,
        'annotations': [],
        'severity': {}
    }, storage_type='session'),
    dcc.Store(id='severity-scores', data={}, storage_type='session'),
    dcc.Store(id='severity-scores-edit', data={}, storage_type='session'),
    dcc.Store(id='annotation-data', data={}, storage_type='session'),
    dcc.Store(id='edge-data', data={}, storage_type='session'),
    dcc.Store(id='comparison', data={}, storage_type='session'),
    dcc.Store(id='track-map-data', data={
        'elements': [], 
        'stylesheet': stylesheet,
        'severity': {},
        'timeline-marks': {0: 'PsySys'},
        'timeline-min': 0,
        'timeline-max': 0,
        'timeline-value': 0
        
}, storage_type='session'),
    dcc.Download(id='download-link'),
    html.Div(id='dummy-output', style={'display': 'none'})
], fluid=True)


if __name__ == '__main__':
    app.run_server(debug=True, port=8069)