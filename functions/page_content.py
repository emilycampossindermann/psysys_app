import dash, requests, json, base64
import dash_bootstrap_components as dbc
import dash_cytoscape as cyto
from dash import dcc, html
from constants import node_color, node_size

# Function: Embed YouTube video 
def create_iframe(src):
    return html.Iframe(
        width="615",
        height="346",
        src=src,
        allow="accelerometer;autoplay;clipboard-write;encrypted-media;gyroscope;picture-in-picture;fullscreen"
    )

# Function: Create dropdown menu 
def create_dropdown(id, options, value, placeholder, multi=True):
    return dcc.Dropdown(
        id=id,
        options=options,
        value=value,
        placeholder=placeholder,
        multi=multi,
        style={'width': '81.5%'}
    )

# Function: Generate likert scales to indicate factor severity
def create_likert_scale(factor, initial_value=0):
    return html.Div([
        html.Label([
            'Severity of ',
            html.Span(factor, 
                      style={'font-weight': 'bold', 
                             'color': 'black'})
        ]),
        dcc.Slider(
            min=0,
            max=10,
            step=1,
            value=initial_value,
            marks={i: str(i) for i in range(11)},
            id={'type': 'likert-scale', 
                'factor': factor}
        )
    ],style={'width': '50%', 
             'margin': '0 auto'})

# Function: Generate step content based on session data
def generate_step_content(step, session_data):

    common_style = {
        "backgroundColor": "#f0f0f0",
        "position": "fixed",
        "left":"117px",
        "width":"100%",
        "padding": "20px",
        "margin": "0",
    }

    if step == 0:
        return html.Div([
            html.Div(
                [
                    html.Br(), 
                    html.Br(),
                    html.H2("Welcome to PsySys.", 
                            style={"fontFamily":"Gill sans", 
                                   "fontWeight":"normal",
                                   "color":"white", 
                                   "marginLeft": 
                                   "-1100px"}),
                    html.H3("Dive into your mental health!",
                            style={"fontFamily": "Gill sans", 
                                   "fontWeight":"normal",
                                   "color": "white", 
                                   "marginLeft": "-1025px"}),
                    html.Br(), 
                    html.Br(), 
                    html.Br(), 
                    html.Br(), 
                    html.Br(), 
                    html.Br(), 
                    html.Br(),
                ],
                style={
                    "background-image": "linear-gradient(to right, #8793c9, #516395)",
                    "padding": "20px",
                    "textAlign": "center",
                    "margin": "0",
                    "width": "100%",
                    "position": "fixed",
                    "top": "0",
                    "left": "117px",
                    "zIndex": "500", 
                },
            ),
        
        html.Div([
            html.Div([
                html.Div([
                    html.Iframe(
                        src="https://www.youtube.com/embed/d8ZZyuESXcU?si=CYvKNlf17wnzt4iGrel=0&modestbranding=1",
                        style={"width": "55.4%", 
                               "height": "60vh", 
                               "zIndex": "1000", 
                               "position": "relative",
                               "marginLeft": "480px", 
                               "marginTop": "-70px", 
                               "borderRadius": "15px", 
                               "boxShadow": "0px 4px 8px rgba(0, 0, 0, 0.1)"}
                    ),
                    html.Br(), html.Br(),
                ]),
                html.Div([
                        html.Div(
                            style={"height": "6px"}),
                        html.Ol(
                            [
                                html.Li("Everybody struggles from time to time", 
                                        style={"fontFamily": "Arial Black", 
                                               "color": "grey"}), 
                                html.P("Learn about the variability & identify your personal factors", 
                                       style={"font-size":"13px",
                                              "color": "grey"}),
                                html.Li("Seeing the connections", 
                                        style={"fontFamily": "Arial Black",
                                               "color": "grey"}),
                                html.P("Learn how your factors influence each other", 
                                       style={"font-size":"13px",
                                              "color": "grey"}),
                                html.Li("Vicious cycles", 
                                        style={"fontFamily": "Arial Black",
                                               "color": "grey"}),
                                html.P("Understand why you might drift into a downward spiral", 
                                       style={"font-size":"13px",
                                              "color": "grey"}),
                                html.Li("Breaking out of the cycle", 
                                        style={"fontFamily": "Arial Black",
                                               "color": "grey"}),
                                html.P("Detect promising areas for positive change", 
                                       style={"font-size":"13px",
                                              "color": "grey"}),
                            ],
                            style={"maxWidth": "900px", 
                                   "color": "grey", 
                                   "margin": "0 auto", 
                                   "marginLeft": "10px"}
                        ),
                    ], style={"width": "46.5%",
                              "marginLeft": "20px", 
                              "marginTop":"-375px",
                              "flex": "1"})
            ]),
        ], style={
            "position": "fixed",
            "top": "225px",  # Adjust the top position as needed
            "left": "117px",
            "bottom": "0px",
            "zIndex": "1500",  # Ensure this is higher than the top colored bar
            "width": "100%",
            "backgroundColor": "#f0f0f0",  # Ensure all background underneath the top bar is #f0f0f0
        }),
    ], style=common_style)
    
    if step == 1:
        options = session_data['dropdowns']['initial-selection']['options']
        value = session_data['dropdowns']['initial-selection']['value']
        id = {'type': 'dynamic-dropdown', 
              'step': 1}
        text = 'Select factors'
        return html.Div([
            html.Div(
                [
                    html.H2(
                        "", 
                        style={"fontFamily": "Arial Black", 
                                "fontWeight": "bold", 
                                "color": "white", 
                                "marginLeft": "-100px"}),
                    html.Br(),
                    html.P(
                        "",
                        style={"maxWidth": "900px",
                                "color": "white", 
                                "margin": "0 auto", 
                                "marginLeft": "180px"}),
                    html.Br(), 
                    html.Br(), 
                    html.Br(), 
                    html.Br(), 
                    html.Br(), 
                    html.Br(), 
                    html.Br(),
                ],
                style={
                    "background-image": "linear-gradient(to right, #8793c9, #516395)",
                    "padding": "20px",
                    "textAlign": "center",
                    "margin": "0",
                    "width": "100%",
                    "position": "fixed",
                    "top": "0",
                    "left": "117px",
                    "zIndex": "500",  # Ensures it's above other content
                },
            ),

            html.Div([
            html.Div([
                html.Div([
                    html.Iframe(
                        src="https://www.youtube.com/embed/ttLzT4U2F2I?si=xv1ETjdc1uGROZTo",
                        style={"width": "55.4%", 
                               "height": "60vh", 
                               "zIndex": "1000", 
                               "position": "relative", 
                               "marginLeft": "480px", 
                               "marginTop": "-70px", 
                               "borderRadius": "15px", 
                               "boxShadow": "0px 4px 8px rgba(0, 0, 0, 0.1)"}
                    ),
                    html.Br(), html.Br(),
               ]),
               html.Div([
                    create_dropdown(id=id, 
                                    options=options, 
                                    value=value, 
                                    placeholder="Select your personal factors"),
                    html.Br(),
                    html.Div(
                        id='likert-scales-container', 
                        style={'overflowY': 'auto', 
                               'maxHeight': '290px', 
                                "marginLeft": "-210px", 
                                "zIndex": "500"})
                ], style={"width": "46.5%",
                          "marginLeft": "20px", 
                          "marginTop":"-375px",
                          "flex": "1"})
            ]),
        ], style={
            "position": "fixed",
            "top": "225px",  # Adjust the top position as needed
            "left": "117px",
            "bottom": "0px",
            "zIndex": "1500",  # Ensure this is higher than the top colored bar
            "width": "100%",
            "backgroundColor": "#f0f0f0",  # Ensure all background underneath the top bar is #f0f0f0
        }),
        ])

    if step == 2:
        selected_factors = session_data['dropdowns']['initial-selection']['value'] or []
        options = [{'label': factor, 'value': factor} for factor in selected_factors]
        value_chain1 = session_data['dropdowns']['chain1']['value']
        value_chain2 = session_data['dropdowns']['chain2']['value']
        id_chain1 = {'type': 'dynamic-dropdown', 
                     'step': 2}
        id_chain2 = {'type': 'dynamic-dropdown', 
                     'step': 3}
        text = 'Select two factors'
        return html.Div([
            html.Div(
                [
                    html.H2("", 
                            style={"fontFamily": "Arial Black", 
                                   "fontWeight": "bold", 
                                   "color": "white", 
                                   "marginLeft": "-100px"}),
                    html.Br(),
                    html.P("",
                           style={"maxWidth": "900px", 
                                  "color": "white", 
                                  "margin": "0 auto", 
                                  "marginLeft": "180px"}),
                    html.Br(), 
                    html.Br(), 
                    html.Br(), 
                    html.Br(), 
                    html.Br(), 
                    html.Br(), 
                    html.Br(),
                ],
                style={
                    "background-image": "linear-gradient(to right, #8793c9, #516395)",
                    "padding": "20px",
                    "textAlign": "center",
                    "margin": "0",
                    "width": "100%",
                    "position": "fixed",
                    "top": "0",
                    "left": "117px",
                    "zIndex": "500",  # Ensures it's above other content
                },
            ),

            html.Div([
            html.Div([
                html.Div([
                    html.Iframe(
                        src="https://www.youtube.com/embed/stqJRtjIPrI?si=1MI5daW_ldY3aQz3",
                        style={"width": "55.4%", 
                               "height": "60vh", 
                               "zIndex": "1000",
                               "position": "relative", 
                               "marginLeft": "480px", 
                               "marginTop": "-70px", 
                               "borderRadius": "15px", 
                               "boxShadow": "0px 4px 8px rgba(0, 0, 0, 0.1)"}
                    ),
                    html.Br(), html.Br(),
               ]),
               html.Div([
                    create_dropdown(id=id_chain1, 
                                    options=options, 
                                    value=value_chain1, 
                                    placeholder="Select your factors that are causally connected"),
                    html.Br(),
                    create_dropdown(id=id_chain2, 
                                    options=options, 
                                    value=value_chain2, 
                                    placeholder="Select your factors that are causally connected"),
                    html.Br(),
                    html.P("Example: If you feel that normally worrying causes you to become less concentrated, select these factors in this order.", 
                           style={'width': '70%', 
                                  'font-style': 'italic', 
                                  'color': 'grey'}),
                ], style={"width": "46.5%",
                          "marginLeft": "20px", 
                          "marginTop":"-375px",
                          "flex": "1"})
            ]),
        ], style={
            "position": "fixed",
            "top": "225px",  # Adjust the top position as needed
            "left": "117px",
            "bottom": "0px",
            "zIndex": "1500",  # Ensure this is higher than the top colored bar
            "width": "100%",
            "backgroundColor": "#f0f0f0",  # Ensure all background underneath the top bar is #f0f0f0
        }),
        ])
    
    if step == 3:
        selected_factors = session_data['dropdowns']['initial-selection']['value'] or []
        options = [{'label': factor, 'value': factor} for factor in selected_factors]
        value_cycle1 = session_data['dropdowns']['cycle1']['value']
        value_cycle2 = session_data['dropdowns']['cycle2']['value']
        id_cycle1 = {'type': 'dynamic-dropdown', 
                     'step': 4}
        id_cycle2 = {'type': 'dynamic-dropdown', 
                     'step': 5}
        text1 = 'Select two factors that reinforce each other'
        text2 = 'Select three factors that reiforce each other'
        return html.Div([
            html.Div(
                [
                    html.H2("", 
                            style={"fontFamily": "Arial Black", 
                                   "fontWeight": "bold", 
                                   "color": "white", 
                                   "marginLeft": "-100px"}),
                    html.Br(),
                    html.P("",
                           style={"maxWidth": "900px", 
                                  "color": "white", 
                                  "margin": "0 auto", 
                                  "marginLeft": "180px"}),
                    html.Br(), 
                    html.Br(), 
                    html.Br(), 
                    html.Br(), 
                    html.Br(), 
                    html.Br(), 
                    html.Br(),
                ],
                style={
                    "background-image": "linear-gradient(to right, #8793c9, #516395)",
                    "padding": "20px",
                    "textAlign": "center",
                    "margin": "0",
                    "width": "100%",
                    "position": "fixed",
                    "top": "0",
                    "left": "117px",
                    "zIndex": "500",  # Ensures it's above other content
                },
            ),

            html.Div([
            html.Div([
                html.Div([
                    html.Iframe(
                        src="https://www.youtube.com/embed/EdwiSp3BdKk?si=TcqeWxAlGl-_NUfx",
                        style={"width": "55.4%", 
                               "height": "60vh", 
                               "zIndex": "1000", 
                               "position": "relative", 
                               "marginLeft": "480px", 
                               "marginTop": "-70px", 
                               "borderRadius": "15px", 
                               "boxShadow": "0px 4px 8px rgba(0, 0, 0, 0.1)"}
                    ),
                    html.Br(), html.Br(),
               ]),
               html.Div([
                    create_dropdown(id=id_cycle1, 
                                    options=options, 
                                    value=value_cycle1, 
                                    placeholder="Select your factors that reinforce each other"),
                    html.Br(),
                    create_dropdown(id=id_cycle2, 
                                    options=options, 
                                    value=value_cycle2, 
                                    placeholder="Select your factors that reinforce each other"),
                    html.Br(),
                    html.P("Example: If you feel that that ruminating causes you to worry, which only worsens the rumination, select these factors.", 
                           style={'width': '70%', 
                                  'font-style': 'italic', 
                                  'color': 'grey'}),
                ], style={"width": "46.5%",
                          "marginLeft": "20px", 
                          "marginTop":"-375px",
                          "flex": "1"})
            ]),
        ], style={
            "position": "fixed",
            "top": "225px",  # Adjust the top position as needed
            "left": "117px",
            "bottom": "0px",
            "zIndex": "1500",  # Ensure this is higher than the top colored bar
            "width": "100%",
            "backgroundColor": "#f0f0f0",  # Ensure all background underneath the top bar is #f0f0f0
        }),
        ])
    
    if step == 4:
        selected_factors = session_data['dropdowns']['initial-selection']['value'] or []
        options = [{'label': factor, 'value': factor} for factor in selected_factors]
        value_target = session_data['dropdowns']['target']['value']
        id = {'type': 'dynamic-dropdown', 
              'step': 6}
        text = 'Select one factor'
        return html.Div([
            html.Div(
                [
                    html.H2("", 
                            style={"fontFamily": "Arial Black", 
                                   "fontWeight": "bold", 
                                   "color": "white", 
                                   "marginLeft": "-100px"}),
                    html.Br(),
                    html.P("",
                           style={"maxWidth": "900px", 
                                  "color": "white", 
                                  "margin": "0 auto", 
                                  "marginLeft": "180px"}),
                    html.Br(), 
                    html.Br(), 
                    html.Br(), 
                    html.Br(), 
                    html.Br(), 
                    html.Br(), 
                    html.Br(),
                ],
                style={
                    "background-image": "linear-gradient(to right, #8793c9, #516395)",
                    "padding": "20px",
                    "textAlign": "center",
                    "margin": "0",
                    "width": "100%",
                    "position": "fixed",
                    "top": "0",
                    "left": "117px",
                    "zIndex": "500",  # Ensures it's above other content
                },
            ),

            html.Div([
            html.Div([
                html.Div([
                    html.Iframe(
                        src="https://www.youtube.com/embed/hwisVnJ0y88?si=OpCWAMaDwTThocO6",
                        style={"width": "55.4%", 
                               "height": "60vh", 
                               "zIndex": "1000", 
                               "position": "relative", 
                               "marginLeft": "480px", 
                               "marginTop": "-70px", 
                               "borderRadius": "15px", 
                               "boxShadow": "0px 4px 8px rgba(0, 0, 0, 0.1)"}
                    ),
                    html.Br(),
                    html.Br(),
               ]),
               html.Div([
                    create_dropdown(id=id, 
                                    options=options, 
                                    value=value_target, 
                                    placeholder="Select the factor you think is the most influential"),
                ], style={"width": "46.5%",
                          "marginLeft": "20px", 
                          "marginTop":"-375px",
                          "flex": "1"})
            ]),
        ], style={
            "position": "fixed",
            "top": "225px",  # Adjust the top position as needed
            "left": "117px",
            "bottom": "0px",
            "zIndex": "1500",  # Ensure this is higher than the top colored bar
            "width": "100%",
            "backgroundColor": "#f0f0f0",  # Ensure all background underneath the top bar is #f0f0f0
        }),
        ])
    
    if step == 5:
        elements = session_data.get('elements', [])
        selected_factors = session_data['add-nodes'] or []
        options = [{'label': factor, 'value': factor} for factor in selected_factors]
        return html.Div([
            html.Div(
                [
                    html.Br(), html.Br(),
                    html.H2("You've completed PsySys.", 
                            style={"fontFamily": "Gill sans", 
                                   "fontWeight":"normal",
                                   "color": "white", 
                                   "marginLeft": "-1030px"}),
                    html.H3("Explore your Mental-Health-Map!",
                            style={"fontFamily": "Gill sans", 
                                   "fontWeight":"normal",
                                   "color": "white", 
                                   "marginLeft": "-977px"}),
                    html.Br(), 
                    html.Br(), 
                    html.Br(), 
                    html.Br(), 
                    html.Br(), 
                    html.Br(), 
                    html.Br(),
                ],
                style={
                    "background-image": "linear-gradient(to right, #8793c9, #516395)",
                    "padding": "20px",
                    "textAlign": "center",
                    "margin": "0",
                    "width": "100%",
                    "position": "fixed",
                    "top": "0",
                    "left": "117px",
                    "zIndex": "500",  # Ensures it's above other content
                },
            ),
            html.Div([
                html.Div([
                    cyto.Cytoscape(
                        id='graph-output',
                        elements=session_data['elements'],
                        layout={'name': 'cose', 
                                "padding": 10, 
                                "nodeRepulsion": 3500,
                                "idealEdgeLength": 10, 
                                "edgeElasticity": 5000,
                                "nestingFactor": 1.2,
                                "gravity": 1,
                                "numIter": 1000,
                                "initialTemp": 200,
                                "coolingFactor": 0.95,
                                "minTemp": 1.0,
                                'fit': True
                                },
                        zoom=1,
                        pan={'x': 200, 'y': 200},
                        stylesheet = session_data['stylesheet'],
                        style={ 'width': '55.4%',
                               'height': '60vh',
                               'borderRadius': '15px',  # Round the edges of the graph window
                               'zIndex': '1000',        # Bring it to the foreground
                               'backgroundColor': 'white',
                               'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.1)',  # Shadow for  foreground effect
                               "position": "relative", 
                               "marginLeft": "480px",
                               "marginTop": "-70px",
                        }
                    ), 
                    html.Div([
                        html.Br(),
                        html.P("Congratulations! You've completed PsySys and built your personalised mental-health-map. You can now load your map into the Edit tab and further tweak it to create the best representation of your mental health. Ask yourself:", 
                               style={'width': '70%', 
                                      'color': 'grey'}),
                        html.Ul(
                            [
                                html.Li("Are there personal factors or relations missing? ", 
                                        style={"color": "grey", 
                                               'font-style': 'italic'}),
                                html.Li("Are some of the relationships stronger than others?", 
                                        style={"color": "grey", 
                                               'font-style': 'italic'}),
                                html.Li("Is my most influential factor really that central in my map?", 
                                        style={"color": "grey", 
                                               'font-style': 'italic'}),
                                html.Li("Which could be promising treatment targets in my map?", 
                                        style={"color": "grey", 
                                               'font-style': 'italic'}),
                            ],
                            style={'width': '70%', 
                                   'color': 'grey'}
                        ),
                    ], style={"width": "46.5%",
                              "marginLeft": "20px", 
                              "marginTop":"-375px",
                              "flex": "1"})
                ])
                
            ], style={
                "position": "fixed",
                "top": "225px",  # Adjust the top position as needed
                "left": "117px",
                "bottom": "0px",
                "zIndex": "1500",  # Ensure this is higher than the top colored bar
                "width": "100%",
                "backgroundColor": "#f0f0f0",  # Ensure all background underneath the top bar is #f0f0f0
            }),
        ])
    
    else:
        return None

# Function: Create Editing window
def create_editing_window(mode, edit_map_data, color_scheme_data, sizing_scheme_data):
    print(f"Creating editing window with mode: {mode}")
    cytoscape_elements = edit_map_data.get('elements', [])
    options_1 = [{'label': element['data'].get('label', element['data'].get('id')), 
                  'value': element['data'].get('id')} for element in cytoscape_elements if 'data' in element and 'label' in element['data'] and 'id' in element['data']]
    color_schemes = [{'label': color, 'value': color} for color in node_color]
    sizing_schemes = [{'label': size, 'value': size} for size in node_size]
    if mode == "mode-1": # Backup
        return html.Div([
                    html.Div([
                        dbc.Input(id='edit-node', 
                                  type='text', 
                                  placeholder='Enter factor', 
                                  style={'marginRight': '10px', 
                                         'borderRadius': '10px'}),
                        dbc.Button("➕", 
                                   id='btn-plus-node', 
                                   color="primary", 
                                   style={'marginRight': '5px'}),
                        dbc.Button("➖", 
                                   id='btn-minus-node', 
                                   color="danger")
                    ], style={'display': 'flex', 
                              'alignItems': 'right', 
                              'marginBottom': '10px'}),

                    html.Div([
                        dcc.Dropdown(id='edit-edge', 
                                     options=options_1, 
                                     placeholder='Enter connection', 
                                     multi=True, 
                                     style={'width': '96%', 
                                            'borderRadius': '10px'}),
                        dbc.Button("➕", 
                                   id='btn-plus-edge', 
                                   color="primary", 
                                   style={'marginRight': '5px'}),
                        dbc.Button("➖", 
                                   id='btn-minus-edge', 
                                   color="danger"),
                    ], style={'display': 'flex', 
                              'alignItems': 'center', 
                              'marginBottom': '10px'}),
                
                    html.Div([
                        dcc.Dropdown(id='color-scheme', 
                                     options=color_schemes, 
                                     value=color_scheme_data, 
                                     placeholder='Select a color scheme', 
                                     multi=False, 
                                     style={'width': '96%', 
                                            'borderRadius': '10px'}),
                        dbc.Button("❔", 
                                   id='help-color', 
                                   color="light", 
                                   style={'marginRight': '0px'}),
                        dbc.Modal([
                            dbc.ModalHeader(
                                dbc.ModalTitle("Color Scheme Information")),
                                dbc.ModalBody("Content explaining the color scheme will go here...", 
                                              id='modal-color-scheme-body')
                                ], id="modal-color-scheme"),
                    ], 
                    backdrop = 'False',
                    style={'display': 'flex', 
                              'alignItems': 'center', 
                              'marginBottom': '10px'}),

                    html.Div([
                        dcc.Dropdown(id='sizing-scheme', 
                                     options=sizing_schemes, 
                                     value=sizing_scheme_data, 
                                     placeholder='Select a sizing scheme', 
                                     multi=False, 
                                     style={'width': '96%', 
                                            'borderRadius': '10px'}),
                        dbc.Button("❔", 
                                   id='help-size', 
                                   color="light", 
                                   style={'marginRight': '0px'}),
                        dbc.Modal([
                            dbc.ModalHeader(
                                dbc.ModalTitle("Sizing Scheme Information")),
                                dbc.ModalBody("Content explaining the color scheme will go here...", 
                                              id='modal-sizing-scheme-body')
                                ], id="modal-sizing-scheme", 
                                style={"display": "flex",
                                       "gap": "5px"}),
                    ], style={'display': 'flex', 
                              'alignItems': 'center', 
                              'marginBottom': '10px'}),
                    html.Br(),

                    html.Div([
                        dbc.Checklist(options=[{"label": "Inspect", "value": 0}],
                                    value=[1],
                                    id="inspect-switch",
                                    switch=True),
                        dbc.Button("❔", 
                                   id='help-inspect', 
                                   color="light", 
                                   style={'marginLeft': '10px'}),
                        dbc.Modal([
                            dbc.ModalHeader(
                                dbc.ModalTitle("Inspection Mode")),
                                dbc.ModalBody("Within this mode you can further inspect the consequences of a given factor. Just click on a factor to see its direct effects.", 
                                              id='modal-inspect-body')
                                ], id="modal-inspect"),
                                ], style={'display': 'flex', 
                                          'alignItems': 'center', 
                                          'marginBottom': '10px'}),
                    ])
    elif mode == "mode-2":  # Extend
        # Define the layout for "Extend" mode
        return html.Div([
            html.P("mode 2")
        ])

    elif mode == "mode-3":  # Delete
        # Define the layout for "Delete" mode
        return html.Div([
            html.P("mode 3")
        ])

    elif mode == "mode-4":  # Configure
        # Define the layout for "Configure" mode
        return html.Div([
            html.P("mode 4")
        ])

    else:
        return html.Div("Invalid mode selected.")
    
# Function: Create my-mental-health-map editing tab
def create_mental_health_map_tab(edit_map_data, color_scheme_data, sizing_scheme_data, custom_color_data):
    # Assuming 'edit_map_data' contains the Cytoscape elements
    cytoscape_elements = edit_map_data.get('elements', [])
    options_1 = [{'label': element['data'].get('label', element['data'].get('id')), 
                  'value': element['data'].get('id')} for element in cytoscape_elements if 'data' in element and 'label' in element['data'] and 'id' in element['data']]
    # options = [{'label': factor, 'value': factor} for factor in factors]
    color_schemes = [{'label': color, 'value': color} for color in node_color]
    sizing_schemes = [{'label': size, 'value': size} for size in node_size]
    return html.Div(id='edit-wrapper', 
                    className='no-blur', 
                    children=[
                        html.Div(
                                    [
                                        html.Br(), 
                                        html.Br(),
                                        html.Div(
                                            style={"height": "17px"}),
                                        html.Br(), 
                                        html.Br(), 
                                        html.Br(), 
                                        html.Br(), 
                                        html.Br(),
                                    ],
                                    style={
                                        "background-image": "linear-gradient(to right, #8793c9, #516395)",
                                        "padding": "20px",
                                        "textAlign": "center",
                                        "margin": "0",
                                        "width": "100%",
                                        "position": "fixed",
                                        "top": "0",
                                        "left": "117px",
                                        "zIndex": "500",  # Ensures it's above other content
                                    },
                                ), 
                                html.Br(),
                                html.Div(style={"height": "12px"}),
                                html.Div([
                                    html.Div([
                                        # Editing features
                                        dbc.Navbar(
                                            dbc.Container([
                                                dbc.Nav(
                                                    [
                                                        dbc.NavItem(dbc.NavLink("Backup", 
                                                                                id="mode-1", 
                                                                                href="#", 
                                                                                active=True)),
                                                        dbc.NavItem(dbc.NavLink("Extend", 
                                                                                id="mode-2", 
                                                                                href="#")),
                                                        dbc.NavItem(dbc.NavLink("Delete", 
                                                                                id="mode-3", 
                                                                                href="#")),
                                                        dbc.NavItem(dbc.NavLink("Configure", 
                                                                                id="mode-4", 
                                                                                href="#")),
                                                    ],
                                                    className="ml-auto", 
                                                    navbar=True, 
                                                    style={'width': '100%', 
                                                           'justifyContent': 'space-between'}
                                                ),
                                            ]),
                                            color="light", 
                                            className="mb-4", 
                                            style={'width':'30.2%', 
                                                   'marginLeft':'25px', 
                                                   'marginTop':'-105px', 
                                                   'zIndex':'10', 
                                                   'borderRadius': '15px'}
                                                   ),
                                                   html.Br(),
                                                   html.Div([
                                                        html.Div([
                                                        html.Div([
                                                            dbc.Input(id='edit-node', 
                                                                      type='text', 
                                                                      placeholder='Enter factor', 
                                                                      style={'marginRight': '10px', 
                                                                             'borderRadius': '10px'}),
                                                            dbc.Button([
                                                                html.I(className="fas fa-solid fa-plus")], 
                                                                       id='btn-plus-node', 
                                                                       color="primary", 
                                                                       style={'border': 'none',
                                                                              'color': '#8793c9',
                                                                              'backgroundColor': 'lightgray', 
                                                                              'marginLeft':'8px'}),
                                                            dbc.Button([
                                                                html.I(className="fas fa-solid fa-minus")], 
                                                                       id='btn-minus-node', 
                                                                       color="danger", 
                                                                       style={'border': 'none',
                                                                              'color': '#8793c9',
                                                                              'backgroundColor': 'lightgray', 
                                                                              'marginLeft':'8px'})
                                                        ], style={'display': 'flex', 
                                                                  'alignItems': 'right', 
                                                                  'marginBottom': '10px'}),

                        

                                                        html.Div([
                                                            dcc.Dropdown(id='edit-edge', 
                                                                         options=options_1, 
                                                                         placeholder='Enter connection', 
                                                                         multi=True, 
                                                                         style={'width': '96%', 
                                                                                'borderRadius': '10px'}),
                                                            dbc.Button([
                                                                html.I(className="fas fa-solid fa-plus")], 
                                                                       id='btn-plus-edge', 
                                                                       color="primary", 
                                                                       style={'border': 'none',
                                                                              'color': '#8793c9',
                                                                              'backgroundColor': 'lightgray',
                                                                              'marginLeft':'8px'}),
                                                            dbc.Button([
                                                                html.I(className="fas fa-solid fa-minus")], 
                                                                       id='btn-minus-edge', 
                                                                       color="danger", 
                                                                       style={'border': 'none',
                                                                              'color': '#8793c9',
                                                                              'backgroundColor': 'lightgray', 
                                                                              'marginLeft':'8px'}),
                                                        ], style={'display': 'flex', 
                                                                  'alignItems': 'center', 
                                                                  'marginBottom': '10px'}),
                                                    
                                                        html.Div([
                                                            dcc.Dropdown(id='color-scheme', 
                                                                         options=color_schemes, 
                                                                         value=color_scheme_data, 
                                                                         placeholder='Select a color scheme', 
                                                                         multi=False, 
                                                                         style={'width': '96%', 
                                                                                'borderRadius': '10px'}),
                                                            dbc.Button([
                                                                html.I(className="fas fa-solid fa-question")], 
                                                                       id='help-color', 
                                                                       color="light", 
                                                                       style={'border': 'none',
                                                                              'color': 'grey', 
                                                                              'marginLeft':'8px'}),
                                                            dbc.Modal([
                                                                dbc.ModalHeader(
                                                                    dbc.ModalTitle("Color Scheme Information")),
                                                                    dbc.ModalBody("Content explaining the color scheme will go here...", 
                                                                                  id='modal-color-scheme-body')
                                                                    ], 
                                                                    id="modal-color-scheme",
                                                                    backdrop = "False", 
                                                                    style={"display": "flex", 
                                                                           "gap": "5px", 
                                                                           'zIndex':'8000'}),
                                                        ], style={'display': 'flex', 
                                                                  'alignItems': 'center', 
                                                                  'marginBottom': '10px', 
                                                                  'zIndex':'8000'}),

                                                        html.Div([
                                                            dcc.Dropdown(id='sizing-scheme', 
                                                                         options=sizing_schemes, 
                                                                         value=sizing_scheme_data, 
                                                                         placeholder='Select a sizing scheme', 
                                                                         multi=False,
                                                                         style={'width': '96%', 
                                                                                'borderRadius': '10px'}),
                                                            dbc.Button([
                                                                html.I(className="fas fa-solid fa-question")], 
                                                                       id='help-size', 
                                                                       color="light", 
                                                                       style={'border': 'none',
                                                                              'color': 'grey', 
                                                                              'marginLeft':'8px'}),
                                                            dbc.Modal([
                                                                dbc.ModalHeader(
                                                                    dbc.ModalTitle("Sizing Scheme Information")),
                                                                    dbc.ModalBody("Content explaining the color scheme will go here...", 
                                                                                  id='modal-sizing-scheme-body')
                                                                    ], 
                                                                    id="modal-sizing-scheme", 
                                                                    style={"display": "flex", 
                                                                           "gap": "5px", 
                                                                           'zIndex':'8000'}),
                                                        ], style={'display': 'flex', 
                                                                  'alignItems': 'center', 
                                                                  'marginBottom': '10px', 
                                                                  'zIndex':'8000'}),
                                                        html.Br(),

                                                        html.Div([
                                                            dbc.Checklist(
                                                                options=[{"label": "Inspect", "value": 0}],
                                                                value=[1],
                                                                id="inspect-switch",
                                                                switch=True),
                                                            dbc.Button([
                                                                html.I(
                                                                    className="fas fa-solid fa-question")], 
                                                                    id='help-inspect', 
                                                                    color="light", 
                                                                    style={'border': 'none',
                                                                           'color': 'grey', 
                                                                           'marginLeft':'8px'}),
                                                            dbc.Modal([
                                                                dbc.ModalHeader(
                                                                    dbc.ModalTitle("Inspection Mode")),
                                                                    dbc.ModalBody("Within this mode you can further inspect the consequences of a given factor. Just click on a factor to see its direct effects.", 
                                                                                  id='modal-inspect-body')
                                                                    ], 
                                                                    id="modal-inspect", 
                                                                    style={"display": "flex",
                                                                           "gap": "5px", 
                                                                           'zIndex':'8000'}
                                                                           ),
                                                                    ], style={'display': 'flex', 
                                                                              'alignItems': 'center', 
                                                                              'marginBottom': '10px', 
                                                                              'zIndex':'8000'}),
                                                                    
                                                        html.Div([
                                                            dbc.Button([
                                                                html.I(
                                                                    className="fas fa-solid fa-backward")], 
                                                                    id='back-btn', 
                                                                    color="light", 
                                                                    style={'marginRight': '0px'}),
                                                        ], 
                                                        style={'display': 'flex', 
                                                                  'alignItems': 'center', 
                                                                  'marginTop': '55px', 
                                                                  'marginLeft': '365px'}),
                                                        
                                                        ]), 

                                                    ], 
                                                    id = 'editing-window', 
                                                    style={'width': '430px', 
                                                           'height':"360px", 
                                                           'padding': '10px', 
                                                           'marginTop': '-24px', 
                                                           'marginLeft':'25px', 
                                                           'backgroundColor': 'white', 
                                                           'borderRadius': '15px', 
                                                           'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.1)', 
                                                           'zIndex': '2000'}),

                                        cyto.Cytoscape(
                                                id='my-mental-health-map',
                                                elements=edit_map_data['elements'],
                                                layout={'name': 'cose', 
                                                        "padding": 10, 
                                                        "nodeRepulsion": 3500,
                                                        "idealEdgeLength": 10, 
                                                        "edgeElasticity": 5000,
                                                        "nestingFactor": 1.2,
                                                        "gravity": 1,
                                                        "numIter": 1000,
                                                        "initialTemp": 200,
                                                        "coolingFactor": 0.95,
                                                        "minTemp": 1.0,
                                                        'fit': True
                                                        },
                                                zoom=1,
                                                pan={'x': 200, 
                                                     'y': 200},
                                                stylesheet=edit_map_data['stylesheet'],
                                                style={
                                                    'width': '55.4%',
                                                    'height': '60vh',
                                                    'borderRadius': '15px',  # Round the edges of the graph window
                                                    'zIndex': '1000',        # Bring it to the foreground
                                                    'backgroundColor': 'white',
                                                    'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.1)',  # Optional: Add a shadow for better foreground effect
                                                    "position": "fixed", 
                                                    "marginLeft": "480px",
                                                    "marginTop": "-441px",
                                                }
                                            ), 
                                        
                                        html.Br(),
                                        html.Div([
                                            dbc.Button([
                                                html.I(
                                                    className="fas fa-solid fa-upload"), " ","PsySys Map"], 
                                                    id='load-map-btn',
                                                    className="me-2", 
                                                    style={'border': 'none',
                                                           'color': '#8793c9',
                                                           'backgroundColor': 'lightgray'}),
                                            # Style the dcc.Upload component to look like a button
                                            dcc.Upload(
                                                id='upload-data',
                                                children= dbc.Button([
                                                    html.I(
                                                        className="fas fa-solid fa-upload"), " ", ".json"], 
                                                        color="secondary", 
                                                        id='upload-map-btn',
                                                        style={'border': 'none',
                                                               'color': '#8793c9',
                                                               'backgroundColor': 'lightgray', 
                                                               'padding': '7px'}),
                                                style={
                                                    'display': 'inline-block',
                                                },
                                            ),
                                            dbc.Button([
                                                html.I(
                                                    className="fas fa-solid fa-download"), " ",".json"], 
                                                    id='download-file-btn',
                                                    style={'border': 'none',
                                                           'color': '#8793c9',
                                                           'backgroundColor': 'lightgray', 
                                                           'marginLeft':'8px'}), 
                                            dbc.Button([
                                                html.I(
                                                    className="fas fa-solid fa-download"), " ",".jpg"], 
                                                    id='download-image-btn',
                                                    style={'border': 'none',
                                                           'color': '#8793c9',
                                                           'backgroundColor': 'lightgray', 
                                                           'marginLeft':'8px', 
                                                           'marginRight':'8px'}),
                                            dbc.Button([
                                                html.I(
                                                    className="fas fa-solid fa-hand-holding-medical")], 
                                                    id="donate-btn", 
                                                    color="success")
                                        ], style={'marginLeft': '640px', 
                                                  'display': 'flex', 
                                                  'flexWrap': 'wrap', 
                                                  'gap': '10px'}), 
                                        
                                    ], style={'flex': '1'}),

                                    # Modal for node name & severity edit
                                    dbc.Modal([
                                        dbc.ModalHeader(
                                        dbc.ModalTitle("Factor Information")),
                                            dbc.ModalBody([
                                                html.Div("Name:"),
                                                dbc.Input(id='modal-node-name', 
                                                          type='text'),
                                                html.Br(),
                                                html.Div("Severity Score:"),
                                                dcc.Slider(id='modal-severity-score', 
                                                           min=0, 
                                                           max=10, 
                                                           step=1),
                                                html.Br(),
                                                #    html.Div("Color:"),
                                                #    dcc.Dropdown(id='custom-node-color', options=["blue", "purple", "yellow", "green", "red", "orange"], value=None, placeholder='Select a custom color', multi=False, style={'width': '70%', 'borderRadius': '10px'}),
                                                #    html.Br(),
                                                html.Div("Notes:"),
                                                dcc.Textarea(
                                                    id='note-input',
                                                    value='',
                                                    className='custom-textarea',
                                                    style={
                                                        'flex': '1',  # Flex for input to take available space 
                                                        'fontSize': '0.9em',  # Adjust font size to make textbox smaller
                                                        'resize': 'none',
                                                        'width': '32em',
                                                        'height': '10em'
                                                        }
                                                    )
                                                ]),
                                                dbc.ModalFooter(
                                                    dbc.Button("Save Changes", 
                                                               id="modal-save-btn", 
                                                               className="ms-auto", 
                                                               n_clicks=0))    
                                                    ],
                                                    id='node-edit-modal',
                                                    is_open=False,
                                                    style = {'zIndex':'2000'}),

                                    # Modal for edge info
                                    dbc.Modal([
                                        dbc.ModalHeader(
                                            dbc.ModalTitle("Connection Information")),
                                            dbc.ModalBody([
                                                html.Div(id='edge-explanation'),
                                                html.Br(),
                                                html.Div("Strength of the relationship:"),
                                                dcc.Slider(id='edge-strength', 
                                                           min=1, 
                                                           max=5, 
                                                           step=1),
                                                html.Br(),
                                                html.Div("Type:"),
                                                dcc.Dropdown(id='edge-type-dropdown', 
                                                             options=[#{'label': 'Default', 'value': 'default'},
                                                                      {'label': 'Amplifier', 'value': 'amplifier'},
                                                                      {'label': 'Reliever', 'value': 'reliever'}],
                                                             placeholder='Select a custom color', 
                                                             multi=False, 
                                                             style={'width': '70%', 
                                                                    'borderRadius': '10px'}),
                                                html.Br(),
                                                html.Div("Notes:"),
                                                dcc.Textarea(
                                                    id='edge-annotation',
                                                    value='',
                                                    className='custom-textarea',
                                                    style={
                                                        'flex': '1',  # Flex for input to take available space 
                                                        'fontSize': '0.9em',  # Adjust font size to make textbox smaller
                                                        'resize': 'none',
                                                        'width': '32em',
                                                        'height': '10em'
                                                        }
                                                    )
                                                ]),
                                                dbc.ModalFooter(
                                                    dbc.Button(
                                                        "Save Changes", 
                                                        id="edge-save-btn", 
                                                        className="ms-auto", 
                                                        n_clicks=0))    
                                                    ],
                                                    id='edge-edit-modal',
                                                    is_open=False,
                                                    style = {'zIndex':'2000'}),

                                    # Modal for Donation info
                                    dbc.Modal([
                                        dbc.ModalHeader(
                                            dbc.ModalTitle("Data Donation")),
                                            dbc.ModalBody("Here you can anonymously donate your map. Our aim is to continuously improve PsySys to provide scientifically backed content for our users. Therefore, it is imporant to analyze PsySys results to better understand its clinical value and potential use. By choosing to donate your map, you agree that your anonymized data can be used for research purposes.", 
                                                          id = 'donation-info'),
                                            dbc.ModalFooter(
                                                dbc.Button("Yes, I want to donate", 
                                                           id="donation-agree", 
                                                           className="ms-auto", 
                                                           n_clicks=0))    
                                                    ],
                                                    id='donation-modal', 
                                                    is_open=False, 
                                                    style={'zIndex': '5000'}),
                                
                                ], style={'display': 'flex', 
                                          'height': '470px', 
                                          'alignItems': 'flex-start'}),
    ], 
    style={
                "position": "fixed",
                "top": "225px",  # Adjust the top position as needed
                "left": "117px",
                "bottom": "0px",
                "zIndex": "1000",  # Ensure this is higher than the top colored bar
                "width": "100%",
                "backgroundColor": "#f0f0f0",  # Ensure all background underneath the top bar is #f0f0f0
            })

# Function: Create tracking tab
def create_tracking_tab(track_data):

    return html.Div(id='tracking-wrapper', className='no-blur', children=[
        html.Div(
            [
                html.Br(), 
                html.Br(),
                html.Div(style={"height": "17px"}),
                html.Br(), 
                html.Br(), 
                html.Br(), 
                html.Br(), 
                html.Br(),
            ],
            style={
                "background-image": "linear-gradient(to right, #8793c9, #516395)",
                "padding": "20px",
                "textAlign": "center",
                "margin": "0",
                "width": "100%",
                "position": "fixed",
                "top": "0",
                "left": "117px",
                "zIndex": "100",  # Ensures it's above other content
            },
        ),
        html.Br(),
        html.Div(style={"height": "12px"}),
        html.Div([
            html.Div([
                # Left: Navigation for plot modes 
                dbc.Navbar(
                    dbc.Container([
                        dbc.Nav(
                            [
                                dbc.NavItem(
                                    dbc.NavLink(
                                        "Plot 1", 
                                        id="plot-current", 
                                        href="#", 
                                        active='exact')),
                                dbc.NavItem(
                                    dbc.NavLink(
                                        "Plot 2", 
                                        id="plot-overall", 
                                        href="#", 
                                        active='exact')),
                            ],
                            className="modes-plot", 
                            navbar=True, 
                            style={'width': '100%', 
                                   'justifyContent': 'space-between'}
                        ),
                    ]),
                    color="light", 
                    className="mb-2", 
                    style={'width':'30.2%', 
                           'marginLeft':'125px', 
                           'marginTop':'-105px', 
                           'zIndex':'2000', 
                           'borderRadius': '15px'}
                ),
                html.Br(),
                # Left: Box which displays plot (default current network centrality bar plot)
                html.Div([
                    dcc.Store(id='data-ready', 
                              data=False),
                    html.Div([
                        dcc.Graph(
                            id='centrality-plot')
                            ], 
                            id='graph-container', 
                            style={'display':'block',
                                   'height':'10px', 
                                   'width':'400px', 
                                   'marginTop':'-10px'}),
                    html.Div([
                    dbc.Button([
                        html.I(
                            className="fas fa-solid fa-question")], 
                            id='help-plot', 
                            color="light", 
                            style={'border': 'none',
                                   'color': 'grey', 
                                   'marginLeft':'373px', 
                                   'marginTop': '417px',
                                   'zIndex': '0'}),
                    dbc.Modal([
                        dbc.ModalHeader(
                            dbc.ModalTitle("Figure Info")),
                            dbc.ModalBody("Content explaining the color scheme will go here...", 
                                          id='modal-plot-body')
                            ], 
                            id="modal-plot", 
                            is_open=False, 
                            backdrop = True, 
                            style={#"display": "flex", 
                                   #"gap": "5px", 
                                   'zIndex': '50000'}),

                ], style={'display': 'flex', 
                          'alignItems': 'center', 
                          'marginBottom': '10px'}),
                ], style={'width': '430px', 
                          'height':"65vh", 
                          'padding': '10px', 
                          'marginTop': '-8px', 
                          'marginLeft':'25px', 
                          'backgroundColor': 'white', 
                          'borderRadius': '15px', 
                          'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.1)', 
                          'zIndex': '0'}),
                

            ], style={'flex': '1'}),

            # Right: Box which displays networks, timespan under it & upload + delete button
            html.Div([
                cyto.Cytoscape(
                        id='track-graph',
                        elements=track_data['elements'],
                        layout={'name': 'cose', 
                                "padding": 10, 
                                "nodeRepulsion": 3500,
                                "idealEdgeLength": 10, 
                                "edgeElasticity": 5000,
                                "nestingFactor": 1.2,
                                "gravity": 1,
                                "numIter": 1000,
                                "initialTemp": 200,
                                "coolingFactor": 0.95,
                                "minTemp": 1.0,
                                'fit': True
                                },
                        # tapNodeData={'id': 'tapNodeData'},
                        # tapNode={'data': 'tapNode'},
                        # tapEdge={'data': 'tapEdge'},
                        zoom=1,
                        pan={'x': 200, 'y': 200},
                        stylesheet=track_data['stylesheet'],
                        style={
                            'width': '55.4%',
                            'height': '60vh',
                            'borderRadius': '15px',  # Round the edges of the graph window
                            'zIndex': '100',        # Bring it to the foreground
                            'backgroundColor': 'white',
                            'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.1)',  # Optional: Add a shadow for better foreground effect
                            "position": "fixed", 
                            "marginLeft": "-229.5px",
                            #"marginRight": "-450px", 
                            "marginTop": "-106px",
                        }
                    ),

                html.Br(),
                html.Div([
                    dcc.Slider(id='timeline-slider',
                       marks=track_data['timeline-marks'],
                       min=track_data['timeline-min'],
                       max=track_data['timeline-max'],
                       value=track_data['timeline-value'],
                       step=None,
                       className='timeline-slider'),  # Apply CSS class instead of style
                ], style={'position': 'absolute', 
                          'top': '50%', 
                          'width': '55%', 
                          'marginLeft': '-225px', 
                          'marginTop': '130px',
                          'zIndex': '0'}),

                html.Br(),
                html.Div([
                dbc.Checklist(options=[{"label": "uniform style", "value": 0}],
                              value=[1],
                              id="uniform-switch",
                              switch=True, 
                              style={'display': 'inline-block', 
                                     'marginLeft':'-320px'}),
                dcc.Upload(id='upload-graph-tracking', 
                           children = dbc.Button([
                               html.I(
                                   className="fas fa-solid fa-upload"), " ", ".json"], 
                                   id='upload-map-btn',
                                   style={'border': 'none',
                                          'color': '#8793c9',
                                          'backgroundColor': 'lightgray', 
                                          'padding': '7px'}),
                   style={'display': 'inline-block', 
                          'marginLeft':'190px'}),
                dbc.Button([
                    html.I(
                        className="fas fa-solid fa-trash")], 
                        id='delete-tracking-map', 
                        color="danger", 
                        style={'marginLeft': '10px',
                               'border': 'none',
                               'color': '#8793c9',
                               'backgroundColor': 'lightgray', 
                               'padding': '7px'}),
                   ], style={'display': 'flex', 
                             'alignItems': 'center',
                             'marginLeft': '112px', 
                             'marginTop': '350px',
                             'zIndex': '0'}),

            ], 
            style={'flex': '1'}),
        ], 
        style={'display': 'flex', 
               'height': '470px', 
               'alignItems': 'flex-start'}),

        dbc.Modal([
            dbc.ModalHeader(
                dbc.ModalTitle("Note")),
                dbc.ModalBody("Annotation will go here...", 
                              id='modal-notes')
                              ], 
                              id="modal-annotation", 
                              is_open = False, 
                              backdrop = True, 
                              style={"display": "flex", 
                                     "gap": "5px", 
                                     'zIndex':'3000'}),
        
    ],
    style={
        "position": "fixed",
        "top": "225px",  # Adjust the top position as needed
        "left": "117px",
        "bottom": "0px",
        "zIndex": "150",  # Ensure this is higher than the top colored bar
        "width": "100%",
        "backgroundColor": "#f0f0f0",  # Ensure all background underneath the top bar is #f0f0f0
    })

def create_about(app):
    return html.Div([
        html.Div(
            [
                html.Br(),
                html.Br(),
                html.Br(),
                html.H2(
                    "Share Knowledge. Empower People.", 
                    style={"fontFamily": "Arial Black", 
                           "fontWeight": "bold",
                           "color": "white", 
                           'marginLeft':'-100px'}),
                html.Br(),
                html.Br(),
                html.P(
                    "PsySys aims to convey the concepts of the network approach to psychopathology directly to users. Thereby, it provides users with a framework to better understand their mental health. Starting as a Research Master Thesis, the PsySys Project is currently being funded by the University of Amsterdam through an Impact Grant.",
                    style={"maxWidth": "900px", 
                           "color": "white", 
                           "margin": "0 auto", 
                           'marginLeft':'180px'},
                ),
                html.Br(),
            ],
            style={
                "background-image": "linear-gradient(to right, #8793c9, #516395)",
                #614385, #516395
                #614385, #516395
                #93A5CF, #E4EfE9
                #4F86F7, #4961F7
                #2E3192, #1BFFFF
                "padding": "20px",
                "textAlign": "center",
                "margin": "0",
                "width": "100%",
                "position": "fixed",
                "top": "0",
                "left": "116.4px",
                "zIndex": "1000",  # Ensures it's above other content
            },
        ),
        html.Div(
            [
                html.Div(
                    [
                        html.Img(
                            src=app.get_asset_url('DSC_4985.JPG'), 
                            style={'width': '160px', 
                                   'height': '160px',
                                   'borderRadius': '50%', 
                                   'margin': '5px'}),
                        html.P(
                            "Emily Campos Sindermann", 
                            style={'textAlign': 'center', 
                                   'marginTop': '10px', 
                                   'color': 'black', 
                                   "fontFamily": "Arial Black"}),
                        html.P(
                            "Freelance Researcher", 
                            style={'marginTop': '-15px', 
                                   'fontStyle': 'italic', 
                                   'color': 'grey'}),
                        html.P(
                            "Developer & Project Lead", 
                            style={'marginTop': '-15px', 
                                   'fontStyle': 'italic', 
                                   'color': 'grey'}),
                    ],
                    style={'display': 'inline-block', 
                           'margin': '3px',
                           'marginTop': '190px',
                           'marginLeft': '-150px'},
                ),
                html.Div(
                    [
                        html.Img(
                            src=app.get_asset_url('profile_dennyborsboom.jpeg'), 
                            style={'width': '160px', 
                                   'height': '160px', 
                                   'borderRadius': '50%', 
                                   'margin': '5px',
                                   'marginLeft': '40px'}),
                        html.P(
                            "Denny Borsboom", 
                            style={'textAlign': 'center', 
                                   'marginTop': '10px', 
                                   'color': 'black',
                                   "fontFamily": "Arial Black", 
                                   'marginLeft': '30px'}),
                        html.P(
                            "University of Amsterdam", 
                            style={'marginTop': '-15px', 
                                   'fontStyle': 'italic', 
                                   'color': 'grey',
                                   'marginLeft': '25px'}),
                        html.P(
                            "Supervisor", 
                            style={'marginTop': '-15px', 
                                   'fontStyle': 'italic', 
                                   'color': 'grey',
                                   'marginLeft': '25px'}),
                    ],
                    style={'display': 'inline-block',
                           'margin': '3px'},
                ),
                html.Div(
                    [
                        html.Img(
                            src=app.get_asset_url('profile_tessablanken.jpeg'), 
                            style={'width': '160px', 
                                   'height': '160px', 
                                   'borderRadius': '50%', 
                                   'margin': '5px',
                                   'marginLeft': '70px'}),
                        html.P(
                            "Tessa Blanken", 
                            style={'textAlign': 'center', 
                                   'marginTop': '10px', 
                                   'color': 'black',
                                   "fontFamily": "Arial Black",
                                   'marginLeft': '70px'}),
                        html.P(
                            "University of Amsterdam", 
                            style={'marginTop': '-15px', 
                                   'fontStyle': 'italic', 
                                   'color': 'grey',
                                   'marginLeft': '60px'}),
                        html.P(
                            "Scientific Advisor", 
                            style={'marginTop': '-15px', 
                                   'fontStyle': 'italic', 
                                   'color': 'grey', 
                                   'marginLeft': '60px'}),
                    ],
                    style={'display': 'inline-block', 
                           'margin': '3px'},
                ),
                html.Div(
                    [
                        html.Img(
                            src=app.get_asset_url('profile_larsklintwall.jpeg'), 
                            style={'width': '160px', 
                                   'height': '160px', 
                                   'borderRadius': '50%', 
                                   'margin': '5px', 
                                   'marginLeft': '70px'}),
                        html.P(
                            "Lars Klintwall", 
                            style={'textAlign': 'center', 
                                   'marginTop': '10px', 
                                   'color': 'black',
                                   "fontFamily": "Arial Black", 
                                   'marginLeft': '70px'}),
                        html.P(
                            "Karolinska Institute", 
                            style={'marginTop': '-15px', 
                                   'fontStyle': 'italic', 
                                   'color': 'grey',
                                   'marginLeft': '70px'}),
                        html.P(
                            "Clinical Advisor", 
                            style={'marginTop': '-15px', 
                                   'fontStyle': 'italic', 
                                   'color': 'grey',
                                   'marginLeft': '70px'}),
                    ],
                    style={'display': 'inline-block', 
                           'margin': '3px'},
                ),
                html.Div(
                    [
                        html.Img(
                            src=app.get_asset_url('profile_julianburger.jpeg'), 
                            style={'width': '160px', 
                                   'height': '160px', 
                                   'borderRadius': '50%', 
                                   'margin': '5px', 
                                   'marginLeft': '70px'}),
                        html.P(
                            "Julian Burger", 
                            style={'textAlign': 'center', 
                                   'marginTop': '10px', 
                                   'color': 'black', 
                                   "fontFamily": "Arial Black",
                                   'marginLeft': '60px'}),
                        html.P(
                            "Yale", 
                            style={'marginTop': '-15px', 
                                   'fontStyle': 'italic', 
                                   'color': 'grey', 
                                   'marginLeft': '60px'}),
                        html.P(
                            "Scientific Advisor", 
                            style={'marginTop': '-15px', 
                                   'fontStyle': 'italic', 
                                   'color': 'grey', 
                                   'marginLeft': '60px'}),
                    ],
                    style={'display': 'inline-block', 
                           'margin': '3px'},
                ),
            ],
            style={"backgroundColor": "#f0f0f0", 
                   'position': 'fixed', 
                   'top':'200px', 
                   'bottom': '0', 
                   'left': '117px', 
                   'width': '100%',
                   'textAlign': 'center'},
        ),
    ], style={"backgroundColor": "#f0f0f0",
              "overflowY": "auto"})