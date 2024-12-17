from app import app
from constants import factors, hidden_style, visible_style
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import dash
from dash import dcc, html

# app = dash.Dash(
#     __name__,
#     external_stylesheets=[
#         dbc.themes.BOOTSTRAP,
#         'https://use.fontawesome.com/releases/v6.6.0/css/all.css',
#         'assets/styles.css'
#     ],
#     assets_folder='assets',
#     suppress_callback_exceptions=True
# )

# app.title = "PsySys"

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
        'bottom': '70px',
        'right': '48px',
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
# nav_col = dbc.Col(
#     [
#         html.Br(),
#         html.A(
#             html.Img(
#                 src="/assets/new-logo.png",
#                 style={"marginLeft": "1px", "width": "175px", "height": "auto", "marginTop": "20px", "marginBottom": '10px'}
#             ), href="/",  # Redirect to landing page
#         ),
#         html.Br(),
#         html.Br(),
#         html.Br(),
#         dbc.Nav(
#             [
#                 dbc.NavLink(
#                     "about us",
#                     href="#",
#                     id="about-us",
#                     active="exact",
#                     style={"fontSize": "20px", "color": "#8793c9", "alignItems": "center"},
#                 ),
#                 dbc.NavLink(
#                     "psysys demo",
#                     href="/psysys-demo",
#                     id="psysys-demo",
#                     active="exact",
#                     style={"fontSize": "20px", "margin": "0px 0", "color": "#8793c9"}, 
#                 ),
#                 dbc.Nav(
#                     [
#                         dbc.NavLink(
#                             "psychoeducation",
#                             href="/psychoeducation",
#                             id="psychoeducation",
#                             active="exact",
#                             style={"fontSize": "16px", "marginLeft": "0px", "color": "#8793c9"}, # "marginLeft": "30px", 
#                         ),
#                         dbc.NavLink(
#                             "map editor",
#                             href="/my-mental-health-map",
#                             id="edit-my-map",
#                             active="exact",
#                             style={"fontSize": "16px", "color": "#8793c9"}, # "marginLeft": "30px", 
#                         ),
#                         dbc.NavLink(
#                             "map tracker",
#                             href="/track-my-mental-health-map",
#                             id="compare-my-map",
#                             active="exact",
#                             style={"fontSize": "16px", "marginLeft": "0px", "color": "#8793c9"}, # "marginLeft": "30px", 
#                         ),
#                     ],
#                     vertical=True,
#                     pills=True,
#                     className="sub-nav",
#                     style={"alignItems": "center"}
#                 ),
#                 dbc.NavLink(
#                     "output",
#                     href="/output",
#                     id="output",
#                     active="exact",
#                     style={"fontSize": "20px",  "margin": "0px 0", "color": "#8793c9"},
#                 ),
#                 dbc.NavLink(
#                     "team",
#                     href="/about",
#                     id="about",
#                     active="exact",
#                     style={"fontSize": "20px",  "margin": "0px 0px", "color": "#8793c9"},
#                 ),
#             ],
#             vertical=True,
#             pills=True,
#             className="main-nav",
#             id="nav-links",
#             style={
#                 "display": "flex",
#                 "flexDirection": "column",
#                 "alignItems": "center",  # Center horizontally
#             },
#         ),
#         html.Br(),
#         html.Br(),
#         dcc.Loading(
#             id="loading-1",
#             type="circle",
#             color="#8793c9",
#             children=html.Div(id="tab-content")
#         ),
#         dcc.Store(id="loading-state", data=False),  # False means not loading
#     ],
#     md=1,
#     #className="nav-yellow",  # Custom class for yellow background
#     className = "nav-primary",
#     style={
#         "position": "fixed",
#         "top": "0",
#         "left": "0",
#         "height": "100vh",
#         "overflowY": "auto",
#         "zIndex": "5000",
#         "width": "190px"
#     },
# )

# nav_col = dbc.Col(
#     [
#         html.Br(),
#         html.A(
#             html.Img(
#                 src="/assets/new-logo.png",
#                 style={"marginLeft": "1px", "width": "175px", "height": "auto", "marginTop": "20px", "marginBottom": '10px'}
#             ),
#             href="/",  # Redirect to landing page
#         ),
#         html.Br(),
#         html.Br(),
#         html.Br(),
#         dbc.Nav(
#             [
#                 dbc.NavLink(
#                     "About",
#                     href="/project-info",
#                     id="about-us",
#                     active="exact",
#                     style={"fontSize": "20px", "color": "#8793c9", "alignItems": "center"},
#                 ),
#                 # Collapsible NavLink
#                 html.Div(
#                     [
#                         dbc.NavLink(
#                             "Demo",
#                             id="psysys-demo-link",
#                             active="exact",
#                             style={"fontSize": "20px", "margin": "0px 0", "color": "#8793c9", "textAlign": "center"},
#                             href="/psysys-demo",  # No link since it's a parent
#                             n_clicks=0,  # Needed for toggling
#                         ),
#                         dbc.Collapse(
#                             id="psysys-demo-collapse",
#                             is_open=False,  # Initially closed
#                             style={"textAlign": "center"},
#                             children=dbc.Nav(
#                                 [
#                                     dbc.NavLink(
#                                         "psychoeducation",
#                                         href="/psychoeducation",
#                                         id="psychoeducation",
#                                         active="exact",
#                                         style={"fontSize": "16px", "color": "#8793c9", "textAlign": "center"},
#                                     ),
#                                     dbc.NavLink(
#                                         "map editor",
#                                         href="/my-mental-health-map",
#                                         id="edit-my-map",
#                                         active="exact",
#                                         style={"fontSize": "16px", "color": "#8793c9", "textAlign": "center"},
#                                     ),
#                                     dbc.NavLink(
#                                         "map tracker",
#                                         href="/track-my-mental-health-map",
#                                         id="compare-my-map",
#                                         active="exact",
#                                         style={"fontSize": "16px", "color": "#8793c9", "textAlign": "center"},
#                                     ),
#                                 ],
#                                 vertical=True,
#                                 pills=True,
#                                 className="sub-nav",
#                             ),
#                         ),
#                     ]
#                 ),
#                 dbc.NavLink(
#                     "Output",
#                     href="/output",
#                     id="output",
#                     active="exact",
#                     style={"fontSize": "20px", "margin": "0px 0", "color": "#8793c9"},
#                 ),
#                 dbc.NavLink(
#                     "Team",
#                     href="/about",
#                     id="about",
#                     active="exact",
#                     style={"fontSize": "20px", "margin": "0px 0px", "color": "#8793c9"},
#                 ),
#             ],
#             vertical=True,
#             pills=True,
#             className="main-nav",
#             id="nav-links",
#             style={
#                 "display": "flex",
#                 "flexDirection": "column",
#                 "alignItems": "center",  # Center horizontally
#             },
#         ),
#         html.Br(),
#         html.Br(),
#         dcc.Loading(
#             id="loading-1",
#             type="circle",
#             color="#8793c9",
#             children=html.Div(id="tab-content"),
#         ),
#         dcc.Store(id="loading-state", data=False),  # False means not loading
#     ],
#     md=1,
#     className="nav-primary",
#     style={
#         "position": "fixed",
#         "top": "0",
#         "left": "0",
#         "height": "100vh",
#         "overflowY": "auto",
#         "zIndex": "5000",
#         "width": "190px",
#     },
# )

# Nav Bar on top 
# nav_col = html.Div(
#     style={
#         "position": "fixed",  # Ensure navbar stays fixed
#         "top": "25px",  # Lowered slightly from the top
#         "left": "18%",  # Centered horizontally
#         "width": "65%",  # Restrict width to 65% of the screen
#         "background": "rgba(255, 255, 255, 0.85)",  # Semi-transparent white
#         "boxShadow": "0px 4px 10px rgba(0, 0, 0, 0.1)",  # Subtle shadow
#         "borderRadius": "15px",  # Rounded edges
#         "backdropFilter": "blur(8px)",  # Smooth blur effect
#         "padding": "10px 10px",  # Reduced padding for tighter layout
#         "zIndex": 1000,  # Ensure it's on top of content
#         "display": "flex",  # Flexbox for alignment
#         "alignItems": "center",  # Vertically center items
#     },
#     children=[
#         # Logo Section (Very Left)
#         html.A(
#             html.Img(
#                 src="/assets/logo-clean.png",  # Path to your logo
#                 className="glowing-button",
#                 style={
#                     "height": "50px",  # Control the logo size
#                     "width": "50px",  # Make it a square
#                     "borderRadius": "50%",  # Crop into a perfect circle
#                     "objectFit": "cover",  # Tight crop to exclude text
#                     "marginLeft": "10px",  # Align to the very left
#                     "marginRight": "200px",  # Spacing to the nav links
#                 },
#             ),
#             href="/",  # Redirect to landing page
#             style={"textDecoration": "none"},  # Remove underline
#         ),
#         # Nav Links Section (Centered)
#         dbc.Nav(
#             [
#                 dbc.NavItem(
#                     dbc.NavLink(
#                         "About",
#                         href="/project-info",
#                         className="nav-link-custom",
#                         style={
#                             #"color": "#4A4A8D",
#                             "fontSize": "18px",
#                             "fontWeight": "300",
#                             "marginRight": "20px",
#                         },
#                     )
#                 ),
#                 dbc.NavItem(
#                     dbc.NavLink(
#                         "Demo",
#                         href="/psysys-demo",
#                         className="nav-link-custom",
#                         style={
#                             #"color": "#4A4A8D",
#                             "fontSize": "18px",
#                             "fontWeight": "300",
#                             "marginRight": "20px",
#                         },
#                     )
#                 ),
#                 dbc.NavItem(
#                     dbc.NavLink(
#                         "Output",
#                         href="/output",
#                         className="nav-link-custom",
#                         style={
#                             #"color": "#4A4A8D",
#                             "fontSize": "18px",
#                             "fontWeight": "300",
#                             "marginRight": "20px",
#                         },
#                     )
#                 ),
#                 dbc.NavItem(
#                     dbc.NavLink(
#                         "Team",
#                         href="/about",
#                         className="nav-link-custom",
#                         style={
#                             #"color": "#4A4A8D",
#                             "fontSize": "18px",
#                             "fontWeight": "300",
#                         },
#                     )
#                 ),
#             ],
#             className="justify-content-center",  # Center nav links within navbar
#         ),
#     ],
# )

nav_col = html.Div(
    style={
        "position": "fixed",
        "top": "25px",
        "left": "18%",
        "width": "65%",
        "background": "rgba(255, 255, 255, 0.85)",
        "boxShadow": "0px 4px 10px rgba(0, 0, 0, 0.1)",
        "borderRadius": "15px",
        "backdropFilter": "blur(8px)",
        "padding": "10px 10px",
        "zIndex": 1000,
        "display": "flex",
        "alignItems": "center",
    },
    children=[
        # Logo Section
        html.A(
            html.Img(
                src="/assets/logo-clean.png",
                className="glowing-button",
                style={
                    "height": "50px",
                    "width": "50px",
                    "borderRadius": "50%",
                    "objectFit": "cover",
                    "marginLeft": "10px",
                    "marginRight": "200px",
                },
            ),
            href="/",
            style={"textDecoration": "none"},
        ),
        # Nav Links
        dbc.Nav(
            [
                dbc.NavItem(dbc.NavLink("About", href="/project-info", className="nav-link-custom")),
                html.Div(
                    className="dropdown-container",
                    children=[
                        dbc.NavLink(
                            ["Demo", html.Span(" ▼", style={"fontSize": "12px"})],
                            href="/psysys-demo",
                            className="nav-link-custom dropdown-hover",
                        ),
                        html.Div(
                            className="dropdown-content",
                            children=[
                                html.Div(
                                    className="dropdown-item",
                                    children=[
                                        dbc.NavLink("Psychoeducation", href="/psychoeducation", className="dropdown-link"),
                                        dbc.NavLink("Map Editor", href="/my-mental-health-map", className="dropdown-link"),
                                        dbc.NavLink("Map Tracker", href="/track-my-mental-health-map", className="dropdown-link"),
                                    ],
                                )
                            ],
                        ),
                    ],
                ),
                dbc.NavItem(dbc.NavLink("Output", href="/output", className="nav-link-custom")),
                dbc.NavItem(dbc.NavLink("Team", href="/about", className="nav-link-custom")),
            ],
            className="justify-content-center",
        ),
    ],
)



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
    md=2, 
    style={'position': 'absolute', 
           'top': '10px', 
           'right': '50px',
           'textAlign': 'left', 
           'padding': '10px', 
           'zIndex': '3000',
           'width': '300px'})

# Email toggle
# email_toggle = dbc.Col([
#     html.A(
#         html.I(className="fas fa-envelope", style={'fontSize': '30px', 'color': '#9AA6D6'}),
#         href="mailto:campos.sindermann@gmail.com?subject=Inquiry%20for%20PsySys%20App&",
#         id="email-button", 
#         style={
#             'position': 'absolute',
#             'top': '22px',
#             'right': '15px',
#             'textDecoration': 'none',
#             'zIndex': '5000'
#             }
#         ),

#     dbc.Tooltip(
#         "e-mail",  # Tooltip text
#         target="email-button",  # ID of the element to show the tooltip for
#         placement="top",
#         autohide=True, 
#         delay={"show": 500, "hide": 100}
#     )
#     ], md = 1)

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
                         'font-family': 'Outfit',
                         'text-max-width': '5px'}},
              {'selector': 'edge',
               'style': {'curve-style': 'bezier', 
                         'target-arrow-shape': 'triangle', 
                         'control-point-step-size': '40px' }}
    ]

# Define app layout
app.layout = dbc.Container([
    dbc.Row([nav_col,translation_toggle, content_col]),
    dcc.Store(id='dropdown-store', storage_type='memory'),
    dcc.Store(id='history-store', data=[]),
    dcc.Store(id="now-step", data=1, storage_type="session"),
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