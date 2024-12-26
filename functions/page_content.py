import dash_bootstrap_components as dbc
import dash_cytoscape as cyto
from dash import dcc, html
from constants import (COMMON_STYLE, HEADER_STYLE, VIDEO_STYLE, VIDEO_CONTAINER_STYLE, TEXT_BLOCK_STYLE, 
                       TEXT_STYLE, CONTENT_CONTAINER_STYLE, ABOUT_MEMBER_STYLE, ABOUT_PARTNER_STYLE, 
                       ABOUT_SECTION_STYLE, IMAGE_STYLE, TEXT_CONTAINER_STYLE, TEXT_ELEMENT_STYLE,
                       EDITING_WINDOW_STYLE, PLOT_WINDOW_STYLE)

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
        style={'width': '100%'}
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
    ],style={#'width': '50%', 
             'width': '95%',
             'margin': '0 auto'})

# Function: Generate step content based on session data
def generate_step_content(step, session_data, translation):

    # common_style = {
    #     "backgroundColor": "#f0f0f0",
    #     "position": "fixed",
    #     "left":"117px",
    #     "width":"100%",
    #     "padding": "20px",
    #     "margin": "0",
    # }

    # if step == 0:
    #     return html.Div([
    #         html.Div(
    #             [
    #                 html.Br(), 
    #                 html.Br(),
    #                 html.Div(
    #                     html.H2(
    #                         translation['welcome_01'],
    #                         #translation.get('wecome_01', ''),
    #                             style={#"fontFamily": "Gill Sans", 
    #                                 "fontFamily": "Arial Black",
    #                                 "fontWeight": "normal", 
    #                                 "color": "white",
    #                                 "marginTop": "-10px"}),
    #                     style={"display": "flex", 
    #                            "justifyContent": "flex-start", 
    #                            "width": "100%", 
    #                            "maxWidth": "500px"}
    #                 ),
    #                 html.Div(
    #                     html.H5(
    #                         translation['welcome_02'],
    #                         #translation.get('wecome_02', ''),
    #                             style={#"fontFamily": "Gill Sans",
    #                                 "fontFamily": "Arial Black", 
    #                                 "fontWeight": "normal", 
    #                                 "color": "white"}),
    #                     style={"display": "flex", 
    #                            "justifyContent": "flex-start", 
    #                            "width": "100%", 
    #                            "maxWidth": "500px"}
    #                 ),
    #                 html.Br(), 
    #                 html.Br(), 
    #                 html.Br(), 
    #                 html.Br(), 
    #                 html.Br(), 
    #                 html.Br(), 
    #                 html.Br(),
    #             ],
    #             # style={
    #             #     "background-image": "linear-gradient(to right, #8793c9, #516395)",
    #             #     "padding": "20px",
    #             #     "textAlign": "center",
    #             #     "margin": "0",
    #             #     "width": "100%",
    #             #     "position": "fixed",
    #             #     "top": "0",
    #             #     "left": "117px",
    #             #     "zIndex": "500", 
    #             # },
    #             style=HEADER_STYLE,
    #         ),
        
    #     html.Div([
    #         html.Div([
    #             html.Div([
    #                 html.Iframe(
    #                     #src="https://www.youtube.com/embed/d8ZZyuESXcU?si=CYvKNlf17wnzt4iGrel=0&modestbranding=1",
    #                     src=translation['video_link_intro'],
    #                     # src = translation.get('video_link_intro', ''),
    #                     # style={"width": "55.4%", 
    #                     #        "height": "60vh", 
    #                     #        "zIndex": "1000", 
    #                     #        "position": "relative",
    #                     #        "marginLeft": "480px", 
    #                     #        "marginTop": "-70px", 
    #                     #        "borderRadius": "15px", 
    #                     #        "boxShadow": "0px 4px 8px rgba(0, 0, 0, 0.1)",
    #                     #        "backgroundColor": "white" }
    #                     style=VIDEO_STYLE
    #                 ),
    #                 html.Br(), html.Br(),
    #             ], style=VIDEO_CONTAINER_STYLE), 
    #             html.Div([
    #                     html.Div(
    #                         style={"height": "6px"}),
    #                     html.Ol(
    #                         [
    #                             html.Li(translation['title_block_01'], 
    #                                     style=TEXT_STYLE), 
    #                             html.P(translation['description_block_01'], 
    #                                    style={"font-size":"13px",
    #                                           "color": "grey"}),
    #                             html.Li(translation['title_block_02'], 
    #                                     style=TEXT_STYLE),
    #                             html.P(translation['description_block_02'], 
    #                                    style={"font-size":"13px",
    #                                           "color": "grey"}),
    #                             html.Li(translation['title_block_03'], 
    #                                     style=TEXT_STYLE),
    #                             html.P(translation['description_block_03'], 
    #                                    style={"font-size":"13px",
    #                                           "color": "grey"}),
    #                             html.Li(translation['title_block_04'], 
    #                                    style=TEXT_STYLE),
    #                             html.P(translation['description_block_04'], 
    #                                    style={"font-size":"13px",
    #                                           "color": "grey"}),
    #                         ],
    #                         style={"maxWidth": "900px", 
    #                                "color": "grey", 
    #                                "margin": "0 auto", 
    #                                "marginLeft": "10px"}
    #                     ),
    #                 ], style=TEXT_BLOCK_STYLE
    #                 # style={"width": "46.5%",
    #                 #           "marginLeft": "20px", 
    #                 #           "marginTop":"-375px",
    #                 #           "flex": "1"}
    #                 )
    #         ]),
    #     ], style={
    #         "position": "fixed",
    #         "top": "225px",  # Adjust the top position as needed
    #         "left": "117px",
    #         "bottom": "0px",
    #         "zIndex": "1500",  # Ensure this is higher than the top colored bar
    #         "width": "100%",
    #         "backgroundColor": "#f0f0f0",  # Ensure all background underneath the top bar is #f0f0f0
    #     }),
    # ], # style=common_style
    # style=COMMON_STYLE)

    # Function content
    if step == 0:
        return html.Div(
            style=COMMON_STYLE,
            children=[
                # Header with Welcome Message
                html.Div(
                    style=HEADER_STYLE,
                    children=[
                        html.H2(
                            translation['welcome_01'],
                            style={
                                "fontFamily": "Arial Black",
                                "fontWeight": "normal",
                                "color": "white",
                            },
                        ),
                        html.H5(
                            translation['welcome_02'],
                            style={
                                "fontFamily": "Arial Black",
                                "fontWeight": "normal",
                                "color": "white",
                            },
                        ),
                    ],
                ),
                # Main content container (text and video)
                html.Div(
                    style=CONTENT_CONTAINER_STYLE,
                    children=[
                        # Text block
                        html.Div(
                            style=TEXT_BLOCK_STYLE,
                            children=[
                                html.Ol(
                                    [
                                        html.Li(translation['title_block_01'], style=TEXT_STYLE),
                                        html.P(translation['description_block_01'], style={"color": "grey"}),
                                        html.Li(translation['title_block_02'], style=TEXT_STYLE),
                                        html.P(translation['description_block_02'], style={"color": "grey"}),
                                        html.Li(translation['title_block_03'], style=TEXT_STYLE),
                                        html.P(translation['description_block_03'], style={"color": "grey"}),
                                        html.Li(translation['title_block_04'], style=TEXT_STYLE),
                                        html.P(translation['description_block_04'], style={"color": "grey"}),
                                    ],
                                )
                            ],
                        ),
                        # Video block aligned to the right
                        html.Div(
                            style=VIDEO_CONTAINER_STYLE,
                            children=[
                                html.Iframe(
                                    src=translation['video_link_intro'],
                                    style=VIDEO_STYLE,
                                ),
                            ],
                        ),
                    ],
                ),
            ],
        )

    
    # if step == 1:
    #     # options = session_data['dropdowns']['initial-selection']['options']
    #     options = session_data.get('dropdowns', {}).get('initial-selection', {}).get('options', [])
    #     # value = session_data['dropdowns']['initial-selection']['value']
    #     value = session_data.get('dropdowns', {}).get('initial-selection', {}).get('value', [])
    #     id = {'type': 'dynamic-dropdown', 
    #           'step': 1}
    #     return html.Div([
    #         html.Div(
    #             [
    #                 html.H2(
    #                     "", 
    #                     style={"fontFamily": "Arial Black", 
    #                             "fontWeight": "bold", 
    #                             "color": "white", 
    #                             "marginLeft": "-100px"}),
    #                 html.Br(),
    #                 html.P(
    #                     "",
    #                     style={"maxWidth": "900px",
    #                             "color": "white", 
    #                             "margin": "0 auto", 
    #                             "marginLeft": "180px"}),
    #                 html.Br(), 
    #                 html.Br(), 
    #                 html.Br(), 
    #                 html.Br(), 
    #                 html.Br(), 
    #                 html.Br(), 
    #                 html.Br(),
    #             ],
    #             style={
    #                 "background-image": "linear-gradient(to right, #8793c9, #516395)",
    #                 "padding": "20px",
    #                 "textAlign": "center",
    #                 "margin": "0",
    #                 "width": "100%",
    #                 "position": "fixed",
    #                 "top": "0",
    #                 "left": "117px",
    #                 "zIndex": "500",  # Ensures it's above other content
    #             },
    #         ),

    #         html.Div([
    #         html.Div([
    #             html.Div([
    #                 html.Iframe(
    #                     #src="https://www.youtube.com/embed/ttLzT4U2F2I?si=xv1ETjdc1uGROZTo",
    #                     src= translation['video_link_block_01'],
    #                     style={"width": "55.4%", 
    #                            "height": "60vh", 
    #                            "zIndex": "1000", 
    #                            "position": "relative", 
    #                            "marginLeft": "480px", 
    #                            "marginTop": "-70px", 
    #                            "borderRadius": "15px", 
    #                            "boxShadow": "0px 4px 8px rgba(0, 0, 0, 0.1)"}
    #                 ),
    #                 html.Br(), 
    #                 html.Br(),
    #            ]),

    #            html.Div(
    #                 id='suicide-prevention-hotline', 
    #                 children=[
    #                     html.P(translation['suicide-prevention'], 
    #                             style={"color": "#516395",
    #                                    #"display": "block",
    #                                    "width": "50%",
    #                                    'marginLeft': '490px'
    #                                    }),
    #                 ],
    #                 style={'marginLeft': '490px', 
    #                        'marginTop': '0px',
    #                        'color': 'red', 
    #                        'width': '47%', 
    #                        'position': 'relative',
    #                        'zIndex': '100',
    #                        'visibility': 'hidden'}
    #             ),

    #            html.Div([
    #                 create_dropdown(id=id, 
    #                                 options=options, 
    #                                 value=value, 
    #                                 placeholder=translation['placeholder_dd_01']),
    #                 html.Br(),
    #                 html.Div(
    #                     id='likert-scales-container', 
    #                     style={'overflowY': 'auto', 
    #                            'maxHeight': '290px', 
    #                             "marginLeft": "-210px", 
    #                             "zIndex": "500"}),
    #             ], style={"width": "46.5%",
    #                       "marginLeft": "20px", 
    #                       "marginTop":"-465px",
    #                       "flex": "1",
    #                       "position": "fixed"}),

    #         ]),
    #     ], style={
    #         "position": "fixed",
    #         "top": "225px",  # Adjust the top position as needed
    #         "left": "117px",
    #         "bottom": "0px",
    #         "zIndex": "1500",  # Ensure this is higher than the top colored bar
    #         "width": "100%",
    #         "backgroundColor": "#f0f0f0",  # Ensure all background underneath the top bar is #f0f0f0
    #     }),
    #     ])

    if step == 1:
        options = session_data.get('dropdowns', {}).get('initial-selection', {}).get('options', [])
        # value = session_data['dropdowns']['initial-selection']['value']
        value = session_data.get('dropdowns', {}).get('initial-selection', {}).get('value', [])
        id = {'type': 'dynamic-dropdown', 
              'step': 1}
        return html.Div(
            style=COMMON_STYLE,
            children=[
                # Header with Welcome Message
                 html.Div(
                    html.Div(
                    id='suicide-prevention-hotline', 
                    children=[
                        html.P(
                            translation['suicide-prevention'],
                            style={
                                #"color": "#516395",
                                'color': 'white', 
                                "width": "40%",
                                # 'marginLeft': '520px',
                                'marginTop': '-25px',
                            },
                        ),
                    ],
                    style={
                        'position': 'fixed',  # Keep fixed relative to screen  
                        'visibility': 'hidden',        # Center horizontally, adjust as needed
                        'zIndex': '1000'
                    }
                ),
                    style={
                        **HEADER_STYLE,
                        "height": "228px"  # Set a consistent height for the empty header
                    }
                ),
                # Main content container (text and video)
                html.Div(
                    style={**CONTENT_CONTAINER_STYLE, 'position': 'relative'},
                    children=[
                        html.Div([
                        create_dropdown(
                            id=id,
                            options=options,
                            value=value,
                            placeholder=translation['placeholder_dd_01']
                        ),
                        html.Br(),

                        # Likert scales within responsive container
                        html.Div(
                            id='likert-scales-container',
                            style={
                                'overflowY': 'auto',
                                'maxHeight': '290px',
                                'zIndex': '500',
                            }
                        ),
                    ], style=TEXT_BLOCK_STYLE),
                        # Video block aligned to the right
                        html.Div(
                            style=VIDEO_CONTAINER_STYLE,
                            children=[
                                html.Iframe(
                                    src=translation['video_link_block_01'],
                                    style=VIDEO_STYLE,
                                ),
                            ],
                        ),
                    ],
                ),

            ],
        )

    # if step == 2:
    #     # selected_factors = session_data['dropdowns']['initial-selection']['value'] or []
    #     selected_factors = session_data.get('dropdowns', {}).get('initial-selection', {}).get('value', [])
    #     options = [{'label': factor, 'value': factor} for factor in selected_factors]
    #     # value_chain1 = session_data['dropdowns']['chain1']['value']
    #     value_chain1 = session_data.get('dropdowns', {}).get('chain1', {}).get('value', [])
    #     # value_chain2 = session_data['dropdowns']['chain2']['value']
    #     value_chain2 = session_data.get('dropdowns', {}).get('chain2', {}).get('value', [])
    #     id_chain1 = {'type': 'dynamic-dropdown', 
    #                  'step': 2}
    #     id_chain2 = {'type': 'dynamic-dropdown', 
    #                  'step': 3}
    #     return html.Div([
    #         html.Div(
    #             [
    #                 html.H2("", 
    #                         style={"fontFamily": "Arial Black", 
    #                                "fontWeight": "bold", 
    #                                "color": "white", 
    #                                "marginLeft": "-100px"}),
    #                 html.Br(),
    #                 html.P("",
    #                        style={"maxWidth": "900px", 
    #                               "color": "white", 
    #                               "margin": "0 auto", 
    #                               "marginLeft": "180px"}),
    #                 html.Br(), 
    #                 html.Br(), 
    #                 html.Br(), 
    #                 html.Br(), 
    #                 html.Br(), 
    #                 html.Br(), 
    #                 html.Br(),
    #             ],
    #             style={
    #                 "background-image": "linear-gradient(to right, #8793c9, #516395)",
    #                 "padding": "20px",
    #                 "textAlign": "center",
    #                 "margin": "0",
    #                 "width": "100%",
    #                 "position": "fixed",
    #                 "top": "0",
    #                 "left": "117px",
    #                 "zIndex": "500",  # Ensures it's above other content
    #             },
    #         ),

    #         html.Div([
    #         html.Div([
    #             html.Div([
    #                 html.Iframe(
    #                     #src="https://www.youtube.com/embed/stqJRtjIPrI?si=1MI5daW_ldY3aQz3",
    #                     src= translation['video_link_block_02'],
    #                     style={"width": "55.4%", 
    #                            "height": "60vh", 
    #                            "zIndex": "1000",
    #                            "position": "relative", 
    #                            "marginLeft": "480px", 
    #                            "marginTop": "-70px", 
    #                            "borderRadius": "15px", 
    #                            "boxShadow": "0px 4px 8px rgba(0, 0, 0, 0.1)"}
    #                 ),
    #                 html.Br(), 
    #                 html.Br(),
    #            ]),
    #            html.Div([
    #                 create_dropdown(id=id_chain1, 
    #                                 options=options, 
    #                                 value=value_chain1, 
    #                                 placeholder=translation['placeholder_dd_02']),
    #                 html.Br(),
    #                 create_dropdown(id=id_chain2, 
    #                                 options=options, 
    #                                 value=value_chain2, 
    #                                 placeholder=translation['placeholder_dd_02']),
    #                 html.Br(),
    #                 html.P(translation['example_block_02'], 
    #                        style={'width': '70%', 
    #                               'font-style': 'italic', 
    #                               'color': 'grey'}),
    #             ], style={"width": "46.5%",
    #                       "marginLeft": "20px", 
    #                       "marginTop":"-375px",
    #                       "flex": "1"})
    #         ]),
    #     ], style={
    #         "position": "fixed",
    #         "top": "225px",  # Adjust the top position as needed
    #         "left": "117px",
    #         "bottom": "0px",
    #         "zIndex": "1500",  # Ensure this is higher than the top colored bar
    #         "width": "100%",
    #         "backgroundColor": "#f0f0f0",  # Ensure all background underneath the top bar is #f0f0f0
    #     }),
    #     ])
    
    if step == 2:
        selected_factors = session_data.get('dropdowns', {}).get('initial-selection', {}).get('value', [])
        options = [{'label': factor, 'value': factor} for factor in selected_factors]
        value_chain1 = session_data.get('dropdowns', {}).get('chain1', {}).get('value', [])
        value_chain2 = session_data.get('dropdowns', {}).get('chain2', {}).get('value', [])
        id_chain1 = {'type': 'dynamic-dropdown', 
                     'step': 2}
        id_chain2 = {'type': 'dynamic-dropdown', 
                     'step': 3}
        return html.Div(
            style=COMMON_STYLE,
            children=[
                # Header with Welcome Message
                 html.Div(
                    style={
                        **HEADER_STYLE,
                        "height": "228px"  # Set a consistent height for the empty header
                    }
                ),
                # Main content container (text and video)
                html.Div(
                    style=CONTENT_CONTAINER_STYLE,
                    children=[
                        html.Div([
                            create_dropdown(id=id_chain1, 
                                            options=options, 
                                            value=value_chain1, 
                                            placeholder=translation['placeholder_dd_02']),
                            html.Br(),
                            create_dropdown(id=id_chain2, 
                                            options=options, 
                                            value=value_chain2, 
                                            placeholder=translation['placeholder_dd_02']),
                            html.Br(),
                            html.P(translation['example_block_02'], 
                                style={'width': '80%', 
                                        'font-style': 'italic', 
                                        'color': 'grey'}),
                        ], style=TEXT_BLOCK_STYLE),
                        # Video block aligned to the right
                        html.Div(
                            style=VIDEO_CONTAINER_STYLE,
                            children=[
                                html.Iframe(
                                    src=translation['video_link_block_02'],
                                    style=VIDEO_STYLE,
                                ),
                            ],
                        ),
                    ],
                ),
            ],
        )

    
    # if step == 3:
    #     # selected_factors = session_data['dropdowns']['initial-selection']['value'] or []
    #     selected_factors = session_data.get('dropdowns', {}).get('initial-selection', {}).get('value', [])
    #     options = [{'label': factor, 'value': factor} for factor in selected_factors]
    #     # value_cycle1 = session_data['dropdowns']['cycle1']['value']
    #     value_cycle1 = session_data.get('dropdowns', {}).get('cycle1', {}).get('value', [])
    #     # value_cycle2 = session_data['dropdowns']['cycle2']['value']
    #     value_cycle2 = session_data.get('dropdowns', {}).get('cycle2', {}).get('value', [])
    #     id_cycle1 = {'type': 'dynamic-dropdown', 
    #                  'step': 4}
    #     id_cycle2 = {'type': 'dynamic-dropdown', 
    #                  'step': 5}
    #     return html.Div([
    #         html.Div(
    #             [
    #                 html.H2("", 
    #                         style={"fontFamily": "Arial Black", 
    #                                "fontWeight": "bold", 
    #                                "color": "white", 
    #                                "marginLeft": "-100px"}),
    #                 html.Br(),
    #                 html.P("",
    #                        style={"maxWidth": "900px", 
    #                               "color": "white", 
    #                               "margin": "0 auto", 
    #                               "marginLeft": "180px"}),
    #                 html.Br(), 
    #                 html.Br(), 
    #                 html.Br(), 
    #                 html.Br(), 
    #                 html.Br(), 
    #                 html.Br(), 
    #                 html.Br(),
    #             ],
    #             style={
    #                 "background-image": "linear-gradient(to right, #8793c9, #516395)",
    #                 "padding": "20px",
    #                 "textAlign": "center",
    #                 "margin": "0",
    #                 "width": "100%",
    #                 "position": "fixed",
    #                 "top": "0",
    #                 "left": "117px",
    #                 "zIndex": "500",  # Ensures it's above other content
    #             },
    #         ),

    #         html.Div([
    #         html.Div([
    #             html.Div([
    #                 html.Iframe(
    #                     src= translation['video_link_block_03'],
    #                     style={"width": "55.4%", 
    #                            "height": "60vh", 
    #                            "zIndex": "1000", 
    #                            "position": "relative", 
    #                            "marginLeft": "480px", 
    #                            "marginTop": "-70px", 
    #                            "borderRadius": "15px", 
    #                            "boxShadow": "0px 4px 8px rgba(0, 0, 0, 0.1)"}
    #                 ),
    #                 html.Br(), 
    #                 html.Br(),
    #            ]),
    #            html.Div([
    #                 create_dropdown(id=id_cycle1, 
    #                                 options=options, 
    #                                 value=value_cycle1, 
    #                                 placeholder=translation['placeholder_dd_03']),
    #                 html.Br(),
    #                 create_dropdown(id=id_cycle2, 
    #                                 options=options, 
    #                                 value=value_cycle2, 
    #                                 placeholder=translation['placeholder_dd_03']),
    #                 html.Br(),
    #                 html.P(translation['example_block_03'], 
    #                        style={'width': '70%', 
    #                               'font-style': 'italic', 
    #                               'color': 'grey'}),
    #             ], style={"width": "46.5%",
    #                       "marginLeft": "20px", 
    #                       "marginTop":"-375px",
    #                       "flex": "1"})
    #         ]),
    #     ], style={
    #         "position": "fixed",
    #         "top": "225px",  # Adjust the top position as needed
    #         "left": "117px",
    #         "bottom": "0px",
    #         "zIndex": "1500",  # Ensure this is higher than the top colored bar
    #         "width": "100%",
    #         "backgroundColor": "#f0f0f0",  # Ensure all background underneath the top bar is #f0f0f0
    #     }),
    #     ])
    
    if step == 3:
        selected_factors = session_data.get('dropdowns', {}).get('initial-selection', {}).get('value', [])
        options = [{'label': factor, 'value': factor} for factor in selected_factors]
        value_cycle1 = session_data.get('dropdowns', {}).get('cycle1', {}).get('value', [])
        value_cycle2 = session_data.get('dropdowns', {}).get('cycle2', {}).get('value', [])
        id_cycle1 = {'type': 'dynamic-dropdown', 
                     'step': 4}
        id_cycle2 = {'type': 'dynamic-dropdown', 
                     'step': 5}
        return html.Div(
            style=COMMON_STYLE,
            children=[
                # Header with Welcome Message
                 html.Div(
                    style={
                        **HEADER_STYLE,
                        "height": "228px"  # Set a consistent height for the empty header
                    }
                ),
                # Main content container (text and video)
                html.Div(
                    style=CONTENT_CONTAINER_STYLE,
                    children=[
                            html.Div([
                        create_dropdown(id=id_cycle1, 
                                        options=options, 
                                        value=value_cycle1, 
                                        placeholder=translation['placeholder_dd_03']),
                        html.Br(),
                        create_dropdown(id=id_cycle2, 
                                        options=options, 
                                        value=value_cycle2, 
                                        placeholder=translation['placeholder_dd_03']),
                        html.Br(),
                        html.P(translation['example_block_03'], 
                            style={'width': '80%', 
                                    'font-style': 'italic', 
                                    'color': 'grey'}),
                    ], style=TEXT_BLOCK_STYLE),
                        # Video block aligned to the right
                        html.Div(
                            style=VIDEO_CONTAINER_STYLE,
                            children=[
                                html.Iframe(
                                    src=translation['video_link_block_03'],
                                    style=VIDEO_STYLE,
                                ),
                            ],
                        ),
                    ],
                ),
            ],
        )
    
    # if step == 4:
    #     # selected_factors = session_data['dropdowns']['initial-selection']['value'] or []
    #     selected_factors = session_data.get('dropdowns', {}).get('initial-selection', {}).get('value', [])
    #     options = [{'label': factor, 'value': factor} for factor in selected_factors]
    #     # value_target = session_data['dropdowns']['target']['value']
    #     value_target = session_data.get('dropdowns', {}).get('target', {}).get('value', [])
    #     id = {'type': 'dynamic-dropdown', 
    #           'step': 6}
    #     return html.Div([
    #         html.Div(
    #             [
    #                 html.H2("", 
    #                         style={"fontFamily": "Arial Black", 
    #                                "fontWeight": "bold", 
    #                                "color": "white", 
    #                                "marginLeft": "-100px"}),
    #                 html.Br(),
    #                 html.P("",
    #                        style={"maxWidth": "900px", 
    #                               "color": "white", 
    #                               "margin": "0 auto", 
    #                               "marginLeft": "180px"}),
    #                 html.Br(), 
    #                 html.Br(), 
    #                 html.Br(), 
    #                 html.Br(), 
    #                 html.Br(), 
    #                 html.Br(), 
    #                 html.Br(),
    #             ],
    #             style={
    #                 "background-image": "linear-gradient(to right, #8793c9, #516395)",
    #                 "padding": "20px",
    #                 "textAlign": "center",
    #                 "margin": "0",
    #                 "width": "100%",
    #                 "position": "fixed",
    #                 "top": "0",
    #                 "left": "117px",
    #                 "zIndex": "500",  # Ensures it's above other content
    #             },
    #         ),

    #         html.Div([
    #         html.Div([
    #             html.Div([
    #                 html.Iframe(
    #                     src=translation['video_link_block_04'],
    #                     style={"width": "55.4%", 
    #                            "height": "60vh", 
    #                            "zIndex": "1000", 
    #                            "position": "relative", 
    #                            "marginLeft": "480px", 
    #                            "marginTop": "-70px", 
    #                            "borderRadius": "15px", 
    #                            "boxShadow": "0px 4px 8px rgba(0, 0, 0, 0.1)"}
    #                 ),
    #                 html.Br(),
    #                 html.Br(),
    #            ]),
    #            html.Div([
    #                 create_dropdown(id=id, 
    #                                 options=options, 
    #                                 value=value_target, 
    #                                 placeholder=translation['placeholder_dd_04']),
    #             ], style={"width": "46.5%",
    #                       "marginLeft": "20px", 
    #                       "marginTop":"-375px",
    #                       "flex": "1"})
    #         ]),
    #     ], style={
    #         "position": "fixed",
    #         "top": "225px",  # Adjust the top position as needed
    #         "left": "117px",
    #         "bottom": "0px",
    #         "zIndex": "1500",  # Ensure this is higher than the top colored bar
    #         "width": "100%",
    #         "backgroundColor": "#f0f0f0",  # Ensure all background underneath the top bar is #f0f0f0
    #     }),
    #     ])
    
    if step == 4:
        selected_factors = session_data.get('dropdowns', {}).get('initial-selection', {}).get('value', [])
        options = [{'label': factor, 'value': factor} for factor in selected_factors]
        value_target = session_data.get('dropdowns', {}).get('target', {}).get('value', [])
        id = {'type': 'dynamic-dropdown', 
              'step': 6}
        return html.Div(
            style=COMMON_STYLE,
            children=[
                # Header with Welcome Message
                 html.Div(
                    style={
                        **HEADER_STYLE,
                        "height": "228px"  # Set a consistent height for the empty header
                    }
                ),
                # Main content container (text and video)
                html.Div(
                    style=CONTENT_CONTAINER_STYLE,
                    children=[
                        html.Div([
                            create_dropdown(id=id, 
                                            options=options, 
                                            value=value_target, 
                                            placeholder=translation['placeholder_dd_04']),
                            html.Br(),
                            html.P(translation['example_block_04'], 
                                style={'width': '90%', 
                                        'font-style': 'italic', 
                                        'color': 'grey'}),
                        ], style=TEXT_BLOCK_STYLE),
                        # Video block aligned to the right
                        html.Div(
                            style=VIDEO_CONTAINER_STYLE,
                            children=[
                                html.Iframe(
                                    src=translation['video_link_block_04'],
                                    style=VIDEO_STYLE,
                                ),
                            ],
                        ),
                    ],
                ),
            ],
        )
    
    # if step == 5:
    #     elements = session_data.get('elements', [])
    #     # selected_factors = session_data['add-nodes'] or []
    #     selected_factors = session_data.get('add-nodes', [])
    #     options = [{'label': factor, 'value': factor} for factor in selected_factors]
    #     return html.Div([
    #         html.Div(
    #             [
    #                 html.Br(), html.Br(),
    #                 html.Div(
    #                     html.H2(translation['finish_01'],
    #                             style={#"fontFamily": "Gill Sans", 
    #                                 "fontFamily": "Arial Black",
    #                                 "fontWeight": "normal", 
    #                                 "color": "white",
    #                                 "marginTop": "-10px"}),
    #                                 style={"display": "flex", 
    #                                        "justifyContent": "flex-start", 
    #                                        "width": "100%",
    #                                        "maxWidth": "600px"}
    #                 ),
    #                 html.Div(
    #                     html.H5(translation['finish_02'],
    #                             style={#"fontFamily": "Gill Sans",
    #                                 "fontFamily": "Arial Black", 
    #                                 "fontWeight": "normal", 
    #                                 "color": "white"}),
    #                                 style={"display": "flex", 
    #                                        "justifyContent": "flex-start", 
    #                                        "width": "100%",
    #                                        "maxWidth": "500px"}
    #                 ),
    #                 html.Br(), 
    #                 html.Br(), 
    #                 html.Br(), 
    #                 html.Br(), 
    #                 html.Br(), 
    #                 html.Br(), 
    #                 html.Br(),
    #             ],
    #             style={
    #                 "background-image": "linear-gradient(to right, #8793c9, #516395)",
    #                 "padding": "20px",
    #                 "textAlign": "center",
    #                 "margin": "0",
    #                 "width": "100%",
    #                 "position": "fixed",
    #                 "top": "0",
    #                 "left": "117px",
    #                 "zIndex": "500",  # Ensures it's above other content
    #             },
    #         ),
    #         html.Div([
    #             html.Div([
    #                 cyto.Cytoscape(
    #                     id='graph-output',
    #                     #elements=session_data['elements'],
    #                     elements = elements,
    #                     layout={'name': 'cose', 
    #                             "padding": 10, 
    #                             "nodeRepulsion": 3500,
    #                             "idealEdgeLength": 10, 
    #                             "edgeElasticity": 5000,
    #                             "nestingFactor": 1.2,
    #                             "gravity": 1,
    #                             "numIter": 1000,
    #                             "initialTemp": 200,
    #                             "coolingFactor": 0.95,
    #                             "minTemp": 1.0,
    #                             'fit': True
    #                             },
    #                     zoom=1,
    #                     pan={'x': 200, 'y': 200},
    #                     # stylesheet = session_data['stylesheet'],
    #                     stylesheet = session_data.get('stylesheet', []),
    #                     style={ 'width': '55.4%',
    #                            'height': '60vh',
    #                            'borderRadius': '15px',  # Round the edges of the graph window
    #                            'zIndex': '1000',        # Bring it to the foreground
    #                            'backgroundColor': 'white',
    #                            'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.1)',  # Shadow for  foreground effect
    #                            "position": "relative", 
    #                            "marginLeft": "480px",
    #                            "marginTop": "-70px",
    #                     }
    #                 ), 
    #                 html.Div([
    #                     html.Br(),
    #                     html.P(translation['feedback_text'], 
    #                            style={'width': '70%', 
    #                                   'color': 'grey'}),
    #                     html.Ul(
    #                         [
    #                             html.Li(translation['feedback_question_01'], 
    #                                     style={"color": "grey", 
    #                                            'font-style': 'italic'}),
    #                             html.Li(translation['feedback_question_02'], 
    #                                     style={"color": "grey", 
    #                                            'font-style': 'italic'}),
    #                             html.Li(translation['feedback_question_03'], 
    #                                     style={"color": "grey", 
    #                                            'font-style': 'italic'}),
    #                             html.Li(translation['feedback_question_04'], 
    #                                     style={"color": "grey", 
    #                                            'font-style': 'italic'}),
    #                         ],
    #                         style={'width': '70%', 
    #                                'color': 'grey'}
    #                     ),
    #                 ], style={"width": "46.5%",
    #                           "marginLeft": "20px", 
    #                           "marginTop":"-375px",
    #                           "flex": "1"})
    #             ])
                
    #         ], style={
    #             "position": "fixed",
    #             "top": "225px",  # Adjust the top position as needed
    #             "left": "117px",
    #             "bottom": "0px",
    #             "zIndex": "1500",  # Ensure this is higher than the top colored bar
    #             "width": "100%",
    #             "backgroundColor": "#f0f0f0",  # Ensure all background underneath the top bar is #f0f0f0
    #         }),
    #     ])
    
    if step == 5:
        elements = session_data.get('elements', [])
        selected_factors = session_data.get('add-nodes', [])
        options = [{'label': factor, 'value': factor} for factor in selected_factors]
        return html.Div(
            style=COMMON_STYLE,
            children=[
                # Header with Welcome Message
                html.Div(
                    style=HEADER_STYLE,
                    children=[
                        html.H2(
                            translation['finish_01'],
                            style={
                                "fontFamily": "Arial Black",
                                "fontWeight": "normal",
                                "color": "white",
                            },
                        ),
                        html.H5(
                            translation['finish_02'],
                            style={
                                "fontFamily": "Arial Black",
                                "fontWeight": "normal",
                                "color": "white",
                            },
                        ),
                    ],
                ),
                # Main content container (text and video)
                html.Div(
                    style=CONTENT_CONTAINER_STYLE,
                    children=[
                        html.Div([
                            html.P(translation['feedback_text'], 
                                style={'width': '100%', 
                                        'color': 'grey'}),
                            html.Ul(
                                [
                                    html.Li(translation['feedback_question_01'], 
                                            style={"color": "grey", 
                                                'font-style': 'italic'}),
                                    html.Li(translation['feedback_question_02'], 
                                            style={"color": "grey", 
                                                'font-style': 'italic'}),
                                    html.Li(translation['feedback_question_03'], 
                                            style={"color": "grey", 
                                                'font-style': 'italic'}),
                                    html.Li(translation['feedback_question_04'], 
                                            style={"color": "grey", 
                                                'font-style': 'italic'}),
                                ],
                                style={'width': '100%', 
                                    'color': 'grey'}
                            ),
                        ], style=TEXT_BLOCK_STYLE),
                        # Video block aligned to the right
                        html.Div(
                            style=VIDEO_CONTAINER_STYLE,
                            children=[
                                cyto.Cytoscape(
                                    id='graph-output',
                                    #elements=session_data['elements'],
                                    elements = elements,
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
                                    stylesheet = session_data.get('stylesheet', []),
                                    style=VIDEO_STYLE
                                ), 
                            ],
                        ),
                    ],
                ),
            ],
        )
    
    else:
        return None

# Function: Create my-mental-health-map editing tab
def create_mental_health_map_tab(edit_map_data, color_scheme_data, sizing_scheme_data, custom_color_data, translation):   
    cytoscape_elements = edit_map_data.get('elements', [])
    options_1 = [{'label': element['data'].get('label', element['data'].get('id')), 
                  'value': element['data'].get('id')} for element in cytoscape_elements if 'data' in element and 'label' in element['data'] and 'id' in element['data']]
    color_schemes = [{'label': color, 'value': color} for color in translation['schemes']]
    sizing_schemes = [{'label': size, 'value': size} for size in translation['schemes']]
    return html.Div(
        style=COMMON_STYLE,
            children=[
                # Header with Welcome Message
                html.Div(
                    style=HEADER_STYLE,
                    children=[
                        html.H2(
                            translation['edit-map-title_01'],
                            style={"fontFamily": "Arial Black", "fontWeight": "normal", "color": "white"},
                        ),
                        html.H5(
                            translation['edit-map-title_02'],
                            style={"fontFamily": "Arial Black", "fontWeight": "normal", "color": "white"},
                        ),
                    ],
                ),

                # Main content container (text and video)
                html.Div(
                    style={**CONTENT_CONTAINER_STYLE},
                    children=[
                        # Plot section with question mark button
                        
                        
                                        html.Br(),
                                        html.Br(),
                                        html.Div([
                                            html.Div([
                                                html.Div([
                                                    dbc.Input(id='edit-node',
                                                              type='text', 
                                                              placeholder=translation['placeholder_enter_factor'], 
                                                              style={'marginRight': '10px', 
                                                                     'borderRadius': '10px'}),
                                                    dbc.Button([
                                                        html.I(
                                                            className="fas fa-solid fa-plus")], 
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
                                                                         placeholder=translation['placeholder_enter_connection'], 
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
                                                                         placeholder=translation['placeholder_color_scheme'], 
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
                                                                    dbc.ModalTitle(translation['color_modal_title'])),
                                                                    dbc.ModalBody("", 
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
                                                                         placeholder=translation['placeholder_sizing_scheme'], 
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
                                                                    dbc.ModalTitle(translation['sizing_modal_title'])),
                                                                    dbc.ModalBody("", 
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
                                                                options=[{"label": html.Span(html.I(className="fas fa-magnifying-glass"),style={'color': '#8793c9'}), 
                                                                          "value": 0}],
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
                                                                    dbc.ModalTitle(translation['inspect_modal_title'])),
                                                                    dbc.ModalBody(translation['inspect_modal_text'], 
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
                                                                    style={'marginTop': '-32px',
                                                                           'marginLeft': '13px'}),
                                                            
                                                            dbc.Tooltip(
                                                                translation['hover-back-edit'],
                                                                target='back-btn',  # Matches the button id
                                                                placement="top",
                                                                autohide=True, 
                                                                delay={"show": 500, "hide": 100}
                                                            ),
                                                        ], 
                                                        style={'display': 'flex', 
                                                                  'alignItems': 'center', 
                                                                  'marginTop': '55px', 
                                                                  'marginLeft': '365px'}),
                                                        
                                                        ]), 

                                                    ], 
                                                    id = 'editing-window', 
                                                    style={'width': '450px', 
                                                           'height':"335px", 
                                                           'padding': '10px', 
                                                           'marginTop': '5px', 
                                                           'marginLeft':'-125px', 
                                                           'backgroundColor': 'white', 
                                                           'borderRadius': '15px', 
                                                           'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.1)', 
                                                           'zIndex': '2000'}),

                        # Cytoscape graph section with vertically stacked controls
                        html.Div(
                            style={**VIDEO_CONTAINER_STYLE, 'flexDirection': 'column', 'alignItems': 'center', 'marginRight': '10px'},
                            children=[
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
                                            'fit': True},
                                            zoom=1,
                                            pan={'x': 200, 'y': 200},
                                            stylesheet=edit_map_data['stylesheet'],
                                            style=VIDEO_STYLE,
                                            generateImage={'type': 'jpg', 'action': 'store'},
                                            ), 

                                html.Div(
                                    style={'display': 'flex', 'justifyContent': 'center', 'gap': '10px', 'marginTop': '30px'},
                                    children=[
                                        dbc.Button([
                                            html.I(
                                                className="fas fa-solid fa-upload"), " ","PsySys Map"], 
                                                id='load-map-btn',
                                                className="me-2", 
                                                style={'border': 'none',
                                                        'color': '#8793c9',
                                                        'backgroundColor': 'lightgray'}),
                                        
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
                                                    color="success"),

                                            # Tooltips 
                                            dbc.Tooltip(
                                                translation['hover-load-psysys'],
                                                target='load-map-btn',  # Matches the button id
                                                placement="top",
                                                autohide=True, 
                                                delay={"show": 500, "hide": 100}
                                            ),

                                            dbc.Tooltip(
                                                translation['hover-upload-map'],
                                                target='upload-map-btn',  # Matches the button id
                                                placement="top",
                                                autohide=True, 
                                                delay={"show": 500, "hide": 100}
                                            ),

                                            dbc.Tooltip(
                                                translation['hover-download-map'],
                                                target='download-file-btn',  # Matches the button id
                                                placement="top",
                                                autohide=True, 
                                                delay={"show": 500, "hide": 100}
                                            ),

                                            dbc.Tooltip(
                                                translation['hover-save-image'],
                                                target='download-image-btn',  # Matches the button id
                                                placement="top",
                                                autohide=True, 
                                                delay={"show": 500, "hide": 100}
                                            ),

                                            dbc.Tooltip(
                                                translation['hover-donate'],
                                                target='donate-btn',  # Matches the button id
                                                placement="top",
                                                autohide=True, 
                                                delay={"show": 500, "hide": 100}
                                            ),

                                            # Modals
                                            dbc.Modal([
                                                dbc.ModalHeader(
                                                dbc.ModalTitle(translation['factor_edit_title'])),
                                                    dbc.ModalBody([
                                                        html.Div(translation['factor_edit_name']),
                                                        dbc.Input(id='modal-node-name', 
                                                                type='text'),
                                                        html.Br(),
                                                        html.Div(translation['factor_edit_severity']),
                                                        dcc.Slider(id='modal-severity-score', 
                                                                min=0, 
                                                                max=10, 
                                                                step=1),
                                                        html.Br(),
                                                        #    html.Div("Color:"),
                                                        #    dcc.Dropdown(id='custom-node-color', options=["blue", "purple", "yellow", "green", "red", "orange"], value=None, placeholder='Select a custom color', multi=False, style={'width': '70%', 'borderRadius': '10px'}),
                                                        #    html.Br(),
                                                        html.Div(translation['note']),
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
                                                            dbc.Button(translation['save_changes'], 
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
                                                    dbc.ModalTitle(translation['connection_edit_title'])),
                                                    dbc.ModalBody([
                                                        html.Div(id='edge-explanation'),
                                                        html.Br(),
                                                        html.Div(translation['connection_edit_strength']),
                                                        dcc.Slider(id='edge-strength', 
                                                                min=1, 
                                                                max=5, 
                                                                step=1),
                                                        html.Br(),
                                                        html.Div(translation['connection_types']),
                                                        dcc.Dropdown(id='edge-type-dropdown', 
                                                                    options=[#{'label': 'Default', 'value': 'default'},
                                                                            {'label': translation['type_01'], 
                                                                            'value': 'amplifier'},
                                                                            {'label': translation['type_02'], 
                                                                            'value': 'reliever'}],
                                                                    placeholder='Select a custom color', 
                                                                    multi=False, 
                                                                    style={'width': '70%', 
                                                                            'borderRadius': '10px'}),
                                                        html.Br(),
                                                        html.Div(translation['note']),
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
                                                            dbc.Button(translation['save_changes'], 
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
                                                    dbc.ModalTitle(translation['donation_title'])),
                                                    dbc.ModalBody(translation['donation_info'], 
                                                                id = 'donation-info'),
                                                    dbc.ModalFooter(
                                                        dbc.Button(translation['donation_button'], 
                                                                id="donation-agree", 
                                                                className="ms-auto", 
                                                                n_clicks=0))    
                                                            ],
                                                            id='donation-modal', 
                                                            is_open=False, 
                                                            style={'zIndex': '5000'}),

                                            ]
                                        ),
                            ]
                        ),
                    ],
                ),
            ],
        )

# def create_mental_health_map_tab(edit_map_data, color_scheme_data, sizing_scheme_data, custom_color_data, translation):
#     # Assuming 'edit_map_data' contains the Cytoscape elements
#     cytoscape_elements = edit_map_data.get('elements', [])
#     options_1 = [{'label': element['data'].get('label', element['data'].get('id')), 
#                   'value': element['data'].get('id')} for element in cytoscape_elements if 'data' in element and 'label' in element['data'] and 'id' in element['data']]
#     # options = [{'label': factor, 'value': factor} for factor in factors]
#     color_schemes = [{'label': color, 'value': color} for color in translation['schemes']]
#     sizing_schemes = [{'label': size, 'value': size} for size in translation['schemes']]
#     return html.Div(id='edit-wrapper', 
#                     className='no-blur', 
#                     children=[
#                         html.Div(
#                                     [
#                                         # html.Br(), 
#                                         # html.Br(),
#                                         #html.Div(style={"height": "17px"}),
#                                         html.Br(), html.Br(),
#                                         html.Div(
#                                             html.H2(translation['edit-map-title_01'],
#                                                     style={#"fontFamily": "Gill Sans", 
#                                                         "fontFamily": "Arial Black",
#                                                         "fontWeight": "normal", 
#                                                         "color": "white",
#                                                         "marginTop": "-10px"}),
#                                                         style={"display": "flex", 
#                                                             "justifyContent": "flex-start", 
#                                                             "width": "100%",
#                                                             "maxWidth": "700px"}
#                                         ),
#                                         html.Div(
#                                             html.H5(translation['edit-map-title_02'],
#                                                     style={#"fontFamily": "Gill Sans",
#                                                         "fontFamily": "Arial Black", 
#                                                         "fontWeight": "normal", 
#                                                         "color": "white"}),
#                                                         style={"display": "flex", 
#                                                             "justifyContent": "flex-start", 
#                                                             "width": "100%",
#                                                             "maxWidth": "500px"}
#                                         ),
#                                         html.Div(style={"height": "21px"}),
#                                         html.Br(), 
#                                         html.Br(),
#                                     ],
#                                     style={
#                                         "background-image": "linear-gradient(to right, #8793c9, #516395)",
#                                         "padding": "20px",
#                                         "textAlign": "center",
#                                         "margin": "0",
#                                         "width": "100%",
#                                         "position": "fixed",
#                                         "top": "0",
#                                         "left": "117px",
#                                         "zIndex": "500",  # Ensures it's above other content
#                                     },
#                                 ), 
#                                 html.Br(),
#                                 html.Div(style={"height": "12px"}),
#                                 html.Div([
#                                     html.Div([
#                                         html.Br(),
#                                         html.Div([
#                                             html.Div([
#                                                 html.Div([
#                                                     dbc.Input(id='edit-node',
#                                                               type='text', 
#                                                               placeholder=translation['placeholder_enter_factor'], 
#                                                               style={'marginRight': '10px', 
#                                                                      'borderRadius': '10px'}),
#                                                     dbc.Button([
#                                                         html.I(
#                                                             className="fas fa-solid fa-plus")], 
#                                                             id='btn-plus-node', 
#                                                             color="primary", 
#                                                             style={'border': 'none',
#                                                                    'color': '#8793c9',
#                                                                     'backgroundColor': 'lightgray', 
#                                                                     'marginLeft':'8px'}),
#                                                     dbc.Button([
#                                                         html.I(className="fas fa-solid fa-minus")], 
#                                                                 id='btn-minus-node', 
#                                                                 color="danger", 
#                                                                 style={'border': 'none',
#                                                                         'color': '#8793c9',
#                                                                         'backgroundColor': 'lightgray', 
#                                                                         'marginLeft':'8px'})
#                                                         ], style={'display': 'flex', 
#                                                                   'alignItems': 'right', 
#                                                                   'marginBottom': '10px'}),

#                                                         html.Div([
#                                                             dcc.Dropdown(id='edit-edge', 
#                                                                          options=options_1, 
#                                                                          placeholder=translation['placeholder_enter_connection'], 
#                                                                          multi=True, 
#                                                                          style={'width': '96%', 
#                                                                                 'borderRadius': '10px'}),
#                                                             dbc.Button([
#                                                                 html.I(className="fas fa-solid fa-plus")], 
#                                                                        id='btn-plus-edge', 
#                                                                        color="primary", 
#                                                                        style={'border': 'none',
#                                                                               'color': '#8793c9',
#                                                                               'backgroundColor': 'lightgray',
#                                                                               'marginLeft':'8px'}),
#                                                             dbc.Button([
#                                                                 html.I(className="fas fa-solid fa-minus")], 
#                                                                        id='btn-minus-edge', 
#                                                                        color="danger", 
#                                                                        style={'border': 'none',
#                                                                               'color': '#8793c9',
#                                                                               'backgroundColor': 'lightgray', 
#                                                                               'marginLeft':'8px'}),
#                                                         ], style={'display': 'flex', 
#                                                                   'alignItems': 'center', 
#                                                                   'marginBottom': '10px'}),
                                                    
#                                                         html.Div([
#                                                             dcc.Dropdown(id='color-scheme', 
#                                                                          options=color_schemes, 
#                                                                          value=color_scheme_data, 
#                                                                          placeholder=translation['placeholder_color_scheme'], 
#                                                                          multi=False, 
#                                                                          style={'width': '96%', 
#                                                                                 'borderRadius': '10px'}),
#                                                             dbc.Button([
#                                                                 html.I(className="fas fa-solid fa-question")], 
#                                                                        id='help-color', 
#                                                                        color="light", 
#                                                                        style={'border': 'none',
#                                                                               'color': 'grey', 
#                                                                               'marginLeft':'8px'}),
#                                                             dbc.Modal([
#                                                                 dbc.ModalHeader(
#                                                                     dbc.ModalTitle(translation['color_modal_title'])),
#                                                                     dbc.ModalBody("", 
#                                                                                   id='modal-color-scheme-body')
#                                                                     ], 
#                                                                     id="modal-color-scheme",
#                                                                     backdrop = "False", 
#                                                                     style={"display": "flex", 
#                                                                            "gap": "5px", 
#                                                                            'zIndex':'8000'}),
#                                                         ], style={'display': 'flex', 
#                                                                   'alignItems': 'center', 
#                                                                   'marginBottom': '10px', 
#                                                                   'zIndex':'8000'}),

#                                                         html.Div([
#                                                             dcc.Dropdown(id='sizing-scheme', 
#                                                                          options=sizing_schemes, 
#                                                                          value=sizing_scheme_data, 
#                                                                          placeholder=translation['placeholder_sizing_scheme'], 
#                                                                          multi=False,
#                                                                          style={'width': '96%', 
#                                                                                 'borderRadius': '10px'}),
#                                                             dbc.Button([
#                                                                 html.I(className="fas fa-solid fa-question")], 
#                                                                        id='help-size', 
#                                                                        color="light", 
#                                                                        style={'border': 'none',
#                                                                               'color': 'grey', 
#                                                                               'marginLeft':'8px'}),
#                                                             dbc.Modal([
#                                                                 dbc.ModalHeader(
#                                                                     dbc.ModalTitle(translation['sizing_modal_title'])),
#                                                                     dbc.ModalBody("", 
#                                                                                   id='modal-sizing-scheme-body')
#                                                                     ], 
#                                                                     id="modal-sizing-scheme", 
#                                                                     style={"display": "flex", 
#                                                                            "gap": "5px", 
#                                                                            'zIndex':'8000'}),
#                                                         ], style={'display': 'flex', 
#                                                                   'alignItems': 'center', 
#                                                                   'marginBottom': '10px', 
#                                                                   'zIndex':'8000'}),
#                                                         html.Br(),

#                                                         html.Div([
#                                                             dbc.Checklist(
#                                                                 options=[{"label": html.Span(html.I(className="fas fa-magnifying-glass"),style={'color': '#8793c9'}), 
#                                                                           "value": 0}],
#                                                                 value=[1],
#                                                                 id="inspect-switch",
#                                                                 switch=True),
#                                                             dbc.Button([
#                                                                 html.I(
#                                                                     className="fas fa-solid fa-question")], 
#                                                                     id='help-inspect', 
#                                                                     color="light", 
#                                                                     style={'border': 'none',
#                                                                            'color': 'grey', 
#                                                                            'marginLeft':'8px'}),
#                                                             dbc.Modal([
#                                                                 dbc.ModalHeader(
#                                                                     dbc.ModalTitle(translation['inspect_modal_title'])),
#                                                                     dbc.ModalBody(translation['inspect_modal_text'], 
#                                                                                   id='modal-inspect-body')
#                                                                     ], 
#                                                                     id="modal-inspect", 
#                                                                     style={"display": "flex",
#                                                                            "gap": "5px", 
#                                                                            'zIndex':'8000'}
#                                                                            ),
#                                                                     ], style={'display': 'flex', 
#                                                                               'alignItems': 'center', 
#                                                                               'marginBottom': '10px', 
#                                                                               'zIndex':'8000'}),
                                                                    
#                                                         html.Div([
#                                                             dbc.Button([
#                                                                 html.I(
#                                                                     className="fas fa-solid fa-backward")], 
#                                                                     id='back-btn', 
#                                                                     color="light", 
#                                                                     style={'marginRight': '0px'}),
                                                            
#                                                             dbc.Tooltip(
#                                                                 translation['hover-back-edit'],
#                                                                 target='back-btn',  # Matches the button id
#                                                                 placement="top",
#                                                                 autohide=True, 
#                                                                 delay={"show": 500, "hide": 100}
#                                                             ),
#                                                         ], 
#                                                         style={'display': 'flex', 
#                                                                   'alignItems': 'center', 
#                                                                   'marginTop': '55px', 
#                                                                   'marginLeft': '365px'}),
                                                        
#                                                         ]), 

#                                                     ], 
#                                                     id = 'editing-window', 
#                                                     style={'width': '430px', 
#                                                            'height':"360px", 
#                                                            'padding': '10px', 
#                                                            'marginTop': '-24px', 
#                                                            'marginLeft':'25px', 
#                                                            'backgroundColor': 'white', 
#                                                            'borderRadius': '15px', 
#                                                            'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.1)', 
#                                                            'zIndex': '2000'}),

#                                         cyto.Cytoscape(
#                                                 id='my-mental-health-map',
#                                                 elements=edit_map_data['elements'],
#                                                 # elements = edit_map_data.get('elements', []),
#                                                 layout={'name': 'cose', 
#                                                         "padding": 10, 
#                                                         "nodeRepulsion": 3500,
#                                                         "idealEdgeLength": 10, 
#                                                         "edgeElasticity": 5000,
#                                                         "nestingFactor": 1.2,
#                                                         "gravity": 1,
#                                                         "numIter": 1000,
#                                                         "initialTemp": 200,
#                                                         "coolingFactor": 0.95,
#                                                         "minTemp": 1.0,
#                                                         'fit': True
#                                                         },
#                                                 zoom=1,
#                                                 pan={'x': 200, 
#                                                      'y': 200},
#                                                 stylesheet=edit_map_data['stylesheet'],
#                                                 style={
#                                                     'width': '55.4%',
#                                                     'height': '60vh',
#                                                     'borderRadius': '15px',  # Round the edges of the graph window
#                                                     'zIndex': '1000',        # Bring it to the foreground
#                                                     'backgroundColor': 'white',
#                                                     'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.1)',  # Optional: Add a shadow for better foreground effect
#                                                     "position": "fixed", 
#                                                     "marginLeft": "480px",
#                                                     "marginTop": "-441px",
#                                                 },
#                                                 generateImage={'type': 'jpg', 'action': 'store'},
#                                             ), 
                                        
#                                         html.Br(),
#                                         html.Div([
#                                             dbc.Button([
#                                                 html.I(
#                                                     className="fas fa-solid fa-upload"), " ","PsySys Map"], 
#                                                     id='load-map-btn',
#                                                     className="me-2", 
#                                                     style={'border': 'none',
#                                                            'color': '#8793c9',
#                                                            'backgroundColor': 'lightgray'}),

#                                             dbc.Tooltip(
#                                                 translation['hover-load-psysys'],
#                                                 target='load-map-btn',  # Matches the button id
#                                                 placement="top",
#                                                 autohide=True, 
#                                                 delay={"show": 500, "hide": 100}
#                                             ),
                                            
#                                             # Style the dcc.Upload component to look like a button
#                                             dcc.Upload(
#                                                 id='upload-data',
#                                                 children= dbc.Button([
#                                                     html.I(
#                                                         className="fas fa-solid fa-upload"), " ", ".json"], 
#                                                         color="secondary", 
#                                                         id='upload-map-btn',
#                                                         style={'border': 'none',
#                                                                'color': '#8793c9',
#                                                                'backgroundColor': 'lightgray', 
#                                                                'padding': '7px'}),
#                                                 style={
#                                                     'display': 'inline-block',
#                                                 },
#                                             ),

#                                             dbc.Tooltip(
#                                                 translation['hover-upload-map'],
#                                                 target='upload-map-btn',  # Matches the button id
#                                                 placement="top",
#                                                 autohide=True, 
#                                                 delay={"show": 500, "hide": 100}
#                                             ),

#                                             dbc.Button([
#                                                 html.I(
#                                                     className="fas fa-solid fa-download"), " ",".json"], 
#                                                     id='download-file-btn',
#                                                     style={'border': 'none',
#                                                            'color': '#8793c9',
#                                                            'backgroundColor': 'lightgray', 
#                                                            'marginLeft':'8px'}), 

#                                             dbc.Tooltip(
#                                                 translation['hover-download-map'],
#                                                 target='download-file-btn',  # Matches the button id
#                                                 placement="top",
#                                                 autohide=True, 
#                                                 delay={"show": 500, "hide": 100}
#                                             ),

#                                             dbc.Button([
#                                                 html.I(
#                                                     className="fas fa-solid fa-download"), " ",".jpg"], 
#                                                     id='download-image-btn',
#                                                     style={'border': 'none',
#                                                            'color': '#8793c9',
#                                                            'backgroundColor': 'lightgray', 
#                                                            'marginLeft':'8px', 
#                                                            'marginRight':'8px'}),
#                                             dbc.Tooltip(
#                                                 translation['hover-save-image'],
#                                                 target='download-image-btn',  # Matches the button id
#                                                 placement="top",
#                                                 autohide=True, 
#                                                 delay={"show": 500, "hide": 100}
#                                             ),

#                                             dbc.Button([
#                                                 html.I(
#                                                     className="fas fa-solid fa-hand-holding-medical")], 
#                                                     id="donate-btn", 
#                                                     color="success")
#                                         ], style={'marginLeft': '640px', 
#                                                   'display': 'flex', 
#                                                   'flexWrap': 'wrap', 
#                                                   'gap': '10px'}), 
#                                         dbc.Tooltip(
#                                                 translation['hover-donate'],
#                                                 target='donate-btn',  # Matches the button id
#                                                 placement="top",
#                                                 autohide=True, 
#                                                 delay={"show": 500, "hide": 100}
#                                             ),

#                                     ], style={'flex': '1'}),

#                                     # Modal for node name & severity edit
#                                     dbc.Modal([
#                                         dbc.ModalHeader(
#                                         dbc.ModalTitle(translation['factor_edit_title'])),
#                                             dbc.ModalBody([
#                                                 html.Div(translation['factor_edit_name']),
#                                                 dbc.Input(id='modal-node-name', 
#                                                           type='text'),
#                                                 html.Br(),
#                                                 html.Div(translation['factor_edit_severity']),
#                                                 dcc.Slider(id='modal-severity-score', 
#                                                            min=0, 
#                                                            max=10, 
#                                                            step=1),
#                                                 html.Br(),
#                                                 #    html.Div("Color:"),
#                                                 #    dcc.Dropdown(id='custom-node-color', options=["blue", "purple", "yellow", "green", "red", "orange"], value=None, placeholder='Select a custom color', multi=False, style={'width': '70%', 'borderRadius': '10px'}),
#                                                 #    html.Br(),
#                                                 html.Div(translation['note']),
#                                                 dcc.Textarea(
#                                                     id='note-input',
#                                                     value='',
#                                                     className='custom-textarea',
#                                                     style={
#                                                         'flex': '1',  # Flex for input to take available space 
#                                                         'fontSize': '0.9em',  # Adjust font size to make textbox smaller
#                                                         'resize': 'none',
#                                                         'width': '32em',
#                                                         'height': '10em'
#                                                         }
#                                                     )
#                                                 ]),
#                                                 dbc.ModalFooter(
#                                                     dbc.Button(translation['save_changes'], 
#                                                                id="modal-save-btn", 
#                                                                className="ms-auto", 
#                                                                n_clicks=0))    
#                                                     ],
#                                                     id='node-edit-modal',
#                                                     is_open=False,
#                                                     style = {'zIndex':'2000'}),

#                                     # Modal for edge info
#                                     dbc.Modal([
#                                         dbc.ModalHeader(
#                                             dbc.ModalTitle(translation['connection_edit_title'])),
#                                             dbc.ModalBody([
#                                                 html.Div(id='edge-explanation'),
#                                                 html.Br(),
#                                                 html.Div(translation['connection_edit_strength']),
#                                                 dcc.Slider(id='edge-strength', 
#                                                            min=1, 
#                                                            max=5, 
#                                                            step=1),
#                                                 html.Br(),
#                                                 html.Div(translation['connection_types']),
#                                                 dcc.Dropdown(id='edge-type-dropdown', 
#                                                              options=[#{'label': 'Default', 'value': 'default'},
#                                                                       {'label': translation['type_01'], 
#                                                                        'value': 'amplifier'},
#                                                                       {'label': translation['type_02'], 
#                                                                        'value': 'reliever'}],
#                                                              placeholder='Select a custom color', 
#                                                              multi=False, 
#                                                              style={'width': '70%', 
#                                                                     'borderRadius': '10px'}),
#                                                 html.Br(),
#                                                 html.Div(translation['note']),
#                                                 dcc.Textarea(
#                                                     id='edge-annotation',
#                                                     value='',
#                                                     className='custom-textarea',
#                                                     style={
#                                                         'flex': '1',  # Flex for input to take available space 
#                                                         'fontSize': '0.9em',  # Adjust font size to make textbox smaller
#                                                         'resize': 'none',
#                                                         'width': '32em',
#                                                         'height': '10em'
#                                                         }
#                                                     )
#                                                 ]),
#                                                 dbc.ModalFooter(
#                                                     dbc.Button(translation['save_changes'], 
#                                                         id="edge-save-btn", 
#                                                         className="ms-auto", 
#                                                         n_clicks=0))    
#                                                     ],
#                                                     id='edge-edit-modal',
#                                                     is_open=False,
#                                                     style = {'zIndex':'2000'}),

#                                     # Modal for Donation info
#                                     dbc.Modal([
#                                         dbc.ModalHeader(
#                                             dbc.ModalTitle(translation['donation_title'])),
#                                             dbc.ModalBody(translation['donation_info'], 
#                                                           id = 'donation-info'),
#                                             dbc.ModalFooter(
#                                                 dbc.Button(translation['donation_button'], 
#                                                            id="donation-agree", 
#                                                            className="ms-auto", 
#                                                            n_clicks=0))    
#                                                     ],
#                                                     id='donation-modal', 
#                                                     is_open=False, 
#                                                     style={'zIndex': '5000'}),
                                
#                                 ], style={'display': 'flex', 
#                                           'height': '470px', 
#                                           'alignItems': 'flex-start'}),
#     ], 
#     style={
#                 "position": "fixed",
#                 "top": "225px",  # Adjust the top position as needed
#                 "left": "117px",
#                 "bottom": "0px",
#                 "zIndex": "1000",  # Ensure this is higher than the top colored bar
#                 "width": "100%",
#                 "backgroundColor": "#f0f0f0",  # Ensure all background underneath the top bar is #f0f0f0
#             })

# Function: Create tracking tab
# def create_tracking_tab(track_data, translation):

#     return html.Div(id='tracking-wrapper', className='no-blur', children=[
#         html.Div(
#             [
#                 # html.Br(), 
#                 # html.Br(),
#                 # html.Div(style={"height": "17px"}),
#                 # html.Br(), 
#                 # html.Br(), 
#                 # html.Br(), 
#                 # html.Br(), 
#                 # html.Br(),
#                 html.Br(), html.Br(),
#                 html.Div(
#                     html.H2(translation['compare-map-title_01'],
#                             style={#"fontFamily": "Gill Sans", 
#                                 "fontFamily": "Arial Black",
#                                 "fontWeight": "normal",
#                                 "color": "white",
#                                 "marginTop": "-10px"}),
#                                 style={"display": "flex", 
#                                        "justifyContent": "flex-start", 
#                                        "width": "100%",
#                                        "maxWidth": "700px"}
#                                        ),
#                     html.Div(
#                         html.H5(translation['compare-map-title_02'],
#                                 style={#"fontFamily": "Gill Sans",
#                                      "fontFamily": "Arial Black", 
#                                      "fontWeight": "normal",
#                                      "color": "white"}),
#                                      style={"display": "flex", 
#                                             "justifyContent": "flex-start",
#                                             "width": "100%",
#                                             "maxWidth": "500px"}
#                                         ),
#                     html.Div(style={"height": "21px"}),
#                     html.Br(), 
#                     html.Br(),
#             ],
#             style={
#                 "background-image": "linear-gradient(to right, #8793c9, #516395)",
#                 "padding": "20px",
#                 "textAlign": "center",
#                 "margin": "0",
#                 "width": "100%",
#                 "position": "fixed",
#                 "top": "0",
#                 "left": "117px",
#                 "zIndex": "100",  # Ensures it's above other content
#             },
#         ),
#         html.Br(),
#         html.Div(style={"height": "12px"}),
#         html.Div([
#             html.Div([
#                 # Left: Navigation for plot modes 
#                 dbc.Navbar(
#                     dbc.Container([
#                         dbc.Nav(
#                             [
#                                 dbc.NavItem(
#                                     dbc.NavLink(
#                                         translation['plot_01'], 
#                                         id="plot-current", 
#                                         href="#", 
#                                         active='exact')),
#                                 dbc.NavItem(
#                                     dbc.NavLink(
#                                         translation['plot_02'], 
#                                         id="plot-overall", 
#                                         href="#", 
#                                         active='exact')),
#                             ],
#                             className="modes-plot", 
#                             navbar=True, 
#                             style={'width': '100%', 
#                                    'justifyContent': 'space-between'}
#                         ),
#                     ]),
#                     color="light", 
#                     className="mb-2", 
#                     style={'width':'40%', 
#                            'marginLeft':'100px', 
#                            'marginTop':'-105px', 
#                            'zIndex':'2000', 
#                            'borderRadius': '15px'}
#                 ),
#                 html.Br(),
#                 # Left: Box which displays plot (default current network centrality bar plot)
#                 html.Div([
#                     dcc.Store(id='data-ready', 
#                               data=False),
#                     html.Div([
#                         dcc.Graph(
#                             id='centrality-plot')
#                             ], 
#                             id='graph-container', 
#                             style={'display':'block',
#                                    'height':'10px', 
#                                    'width':'400px', 
#                                    'marginTop':'-10px'}),
#                     html.Div([
#                     dbc.Button([
#                         html.I(
#                             className="fas fa-solid fa-question")], 
#                             id='help-plot', 
#                             color="light", 
#                             style={'border': 'none',
#                                    'color': 'grey', 
#                                    'marginLeft':'373px', 
#                                    'marginTop': '417px',
#                                    'zIndex': '0'}),
#                     dbc.Modal([
#                         dbc.ModalHeader(
#                             dbc.ModalTitle(translation['plot_modal_title'])),
#                             dbc.ModalBody("", 
#                                           id='modal-plot-body')
#                             ], 
#                             id="modal-plot", 
#                             is_open=False, 
#                             backdrop = True, 
#                             style={'zIndex': '50000'}),

#                 ], style={'display': 'flex', 
#                           'alignItems': 'center', 
#                           'marginBottom': '10px'}),
#                 ], style={'width': '430px', 
#                           'height':"65vh", 
#                           'padding': '10px', 
#                           'marginTop': '-8px', 
#                           'marginLeft':'25px', 
#                           'backgroundColor': 'white', 
#                           'borderRadius': '15px', 
#                           'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.1)', 
#                           'zIndex': '0'}),
                

#             ], style={'flex': '1'}),

#             # Right: Box which displays networks, timespan under it & upload + delete button
#             html.Div([
#                 cyto.Cytoscape(
#                         id='track-graph',
#                         # elements=track_data['elements'],
#                         elements = track_data.get('elements', []),
#                         layout={'name': 'cose', 
#                                 "padding": 10, 
#                                 "nodeRepulsion": 3500,
#                                 "idealEdgeLength": 10, 
#                                 "edgeElasticity": 5000,
#                                 "nestingFactor": 1.2,
#                                 "gravity": 1,
#                                 "numIter": 1000,
#                                 "initialTemp": 200,
#                                 "coolingFactor": 0.95,
#                                 "minTemp": 1.0,
#                                 'fit': True
#                                 },
#                         zoom=1,
#                         pan={'x': 200, 'y': 200},
#                         stylesheet=track_data['stylesheet'],
#                         style={
#                             'width': '55.4%',
#                             'height': '60vh',
#                             'borderRadius': '15px',  # Round the edges of the graph window
#                             'zIndex': '100',        # Bring it to the foreground
#                             'backgroundColor': 'white',
#                             'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.1)',  # Optional: Add a shadow for better foreground effect
#                             "position": "fixed", 
#                             "marginLeft": "-229.5px",
#                             "marginTop": "-106px",
#                         }
#                     ),

#                 html.Br(),
#                 html.Div([
#                     dcc.Slider(id='timeline-slider',
#                        marks=track_data['timeline-marks'],
#                        min=track_data['timeline-min'],
#                        max=track_data['timeline-max'],
#                        value=track_data['timeline-value'],
#                        step=None,
#                        className='timeline-slider'),  # Apply CSS class instead of style
#                 ], style={'position': 'absolute', 
#                           'top': '50%', 
#                           'width': '55%', 
#                           'marginLeft': '-225px', 
#                           'marginTop': '130px',
#                           'zIndex': '0'}),

#                 html.Br(),
#                 html.Div([
#                 dbc.Checklist(options=[{"label": "uniform style", "value": 0}],
#                               value=[1],
#                               id="uniform-switch",
#                               switch=True, 
#                               style={'display': 'inline-block', 
#                                      'marginLeft':'-320px'}),

#                 dbc.Tooltip(
#                     translation['hover-uniform'],  # Tooltip text
#                     target="uniform-switch",  # ID of the element to show the tooltip for
#                     placement="top",
#                     autohide=True, 
#                     delay={"show": 500, "hide": 100}
#                 ),

#                 dcc.Upload(id='upload-graph-tracking', 
#                            children = dbc.Button([
#                                html.I(
#                                    className="fas fa-solid fa-upload"), " ", ".json"], 
#                                    id='upload-map-btn',
#                                    style={'border': 'none',
#                                           'color': '#8793c9',
#                                           'backgroundColor': 'lightgray', 
#                                           'padding': '7px'}),
#                    style={'display': 'inline-block', 
#                           'marginLeft':'190px'},
                          
#                           ),

#                     dbc.Tooltip(
#                         translation['hover-upload-tracking'],  # Tooltip text
#                         target="upload-map-btn",  # ID of the element to show the tooltip for
#                         placement="top",
#                         autohide=True, 
#                         delay={"show": 500, "hide": 100}
#                     ),

#                 dbc.Button([
#                     html.I(
#                         className="fas fa-solid fa-trash")], 
#                         id='delete-tracking-map', 
#                         color="danger", 
#                         style={'marginLeft': '10px',
#                                'border': 'none',
#                                'color': '#8793c9',
#                                'backgroundColor': 'lightgray', 
#                                'padding': '7px'}),

#                     dbc.Tooltip(
#                         translation['hover-delete-tracking'],  # Tooltip text
#                         target="delete-tracking-map",  # ID of the element to show the tooltip for
#                         placement="top",
#                         autohide=True, 
#                         delay={"show": 500, "hide": 100}  # Set delay for show and hide (milliseconds) # Adjust placement as needed (top, bottom, left, right)
#                     ),

#                    ], style={'display': 'flex', 
#                              'alignItems': 'center',
#                              'marginLeft': '112px', 
#                              'marginTop': '350px',
#                              'zIndex': '0'}),

#             ], 
#             style={'flex': '1'}),
#         ], 
#         style={'display': 'flex', 
#                'height': '470px', 
#                'alignItems': 'flex-start'}),

#         dbc.Modal([
#             dbc.ModalHeader(
#                 dbc.ModalTitle(translation['note'])),
#                 dbc.ModalBody(" ", 
#                               id='modal-notes')
#                               ], 
#                               id="modal-annotation", 
#                               is_open = False, 
#                               backdrop = True, 
#                               style={"display": "flex", 
#                                      "gap": "5px", 
#                                      'zIndex':'3000'}),
        
#     ],
#     style={
#         "position": "fixed",
#         "top": "225px",  # Adjust the top position as needed
#         "left": "117px",
#         "bottom": "0px",
#         "zIndex": "150",  # Ensure this is higher than the top colored bar
#         "width": "100%",
#         "backgroundColor": "#f0f0f0",  # Ensure all background underneath the top bar is #f0f0f0
#     })

def create_tracking_tab(track_data, translation):
    return html.Div(
            style=COMMON_STYLE,
            children=[
                # Header with Welcome Message
                html.Div(
                    style=HEADER_STYLE,
                    children=[
                        html.H2(
                            translation['compare-map-title_01'],
                            style={"fontFamily": "Arial Black", "fontWeight": "normal", "color": "white"},
                        ),
                        html.H5(
                            translation['compare-map-title_02'],
                            style={"fontFamily": "Arial Black", "fontWeight": "normal", "color": "white"},
                        ),
                    ],
                ),

                # Navbar above the plot, overlapping with header
                dbc.Navbar(
                    dbc.Container([
                        dbc.Nav(
                            [
                                dbc.NavItem(
                                    dbc.NavLink(
                                        translation['plot_01'], 
                                        id="plot-current", 
                                        href="#", 
                                        active='exact',
                                        style={"padding": "3px 10px"}
                                    )
                                ),
                                dbc.NavItem(
                                    dbc.NavLink(
                                        translation['plot_02'], 
                                        id="plot-overall", 
                                        href="#", 
                                        active='exact',
                                        style={"padding": "3px 10px"}
                                    )
                                ),
                            ],
                            className="modes-plot", 
                            navbar=True, 
                            style={'width': '100%', 'justifyContent': 'space-between'}
                        ),
                    ]),
                    id= 'plot-switch',
                    color="light", 
                    className="mb-2", 
                    style={
                        'width': '22%', 
                        'position': 'fixed', 
                        'top': '170px',   # Adjusted to overlap with header height
                        'left': '15%',    # Adjust for horizontal centering
                        'borderRadius': '15px',
                        'zIndex': '2000',
                    }
                ),

                dbc.Tooltip(
                    translation['hover-plots'],
                    target="plot-switch",  # ID of the element to show the tooltip for
                    placement="top",
                    autohide=True,
                    delay={"show": 500, "hide": 100}
                ),
                
                # Main content container (text and video)
                html.Div(
                    style={**CONTENT_CONTAINER_STYLE},
                    children=[
                        # Plot section with question mark button
                        html.Div(
                            style={'position': 'relative', 'width': '450px', 'height': "64vh", 'padding': '10px', 'backgroundColor': 'white',
                                   'borderRadius': '15px', 'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.1)', 'zIndex': '0', "marginLeft": "13px", "marginTop": "5px"},
                            children=[
                                dcc.Store(id='data-ready', data=False),
                                html.Div([dcc.Graph(id='centrality-plot')], 
                                         id='graph-container',
                                         style={'width': '90%', 'height': '90%', 'borderRadius': '15px'}),
                                
                                # Question Mark Button
                                dbc.Button(
                                    [html.I(className="fas fa-solid fa-question")], 
                                    id='help-plot', 
                                    color="light", 
                                    style={
                                        'border': 'none', 'color': 'grey', 
                                        'position': 'absolute', 'top': '15px', 'right': '15px', 'zIndex': '10'
                                    }
                                ),
                                dbc.Modal([
                                    dbc.ModalHeader(
                                        dbc.ModalTitle(translation['plot_modal_title'])),
                                        dbc.ModalBody("", id='modal-plot-body')], 
                                    id="modal-plot", is_open=False, backdrop=True
                                ),
                            ]
                        ),

                        # Cytoscape graph section with vertically stacked controls
                        html.Div(
                            style={**VIDEO_CONTAINER_STYLE, 'flexDirection': 'column', 'alignItems': 'center', 'marginRight': '10px'},
                            children=[
                                cyto.Cytoscape(
                                    id='track-graph',
                                    elements=track_data.get('elements', []),
                                    layout={'name': 'cose', "padding": 10, "nodeRepulsion": 3500, "idealEdgeLength": 10, "edgeElasticity": 5000, "nestingFactor": 1.2,
                                            "gravity": 1, "numIter": 1000, "initialTemp": 200, "coolingFactor": 0.95, "minTemp": 1.0, 'fit': True},
                                    zoom=1,
                                    pan={'x': 200, 'y': 200},
                                    stylesheet=track_data['stylesheet'],
                                    style=VIDEO_STYLE
                                ),

                                # Slider and Uniform Style Toggle Below Graph
                                html.Div(
                                    style={'marginTop': '20px', 'width': '100%', 'textAlign': 'center'},
                                    children=[
                                        dcc.Slider(id='timeline-slider',
                                            marks=track_data['timeline-marks'],
                                            min=track_data['timeline-min'],
                                            max=track_data['timeline-max'],
                                            value=track_data['timeline-value'],
                                            step=None,
                                            className='timeline-slider',
                                        ),
                                        html.Div(
                                            style={'display': 'flex', 'justifyContent': 'center', 'gap': '15px', 'marginTop': '25px'},
                                            children=[
                                                dbc.Checklist(
                                                    options=[{"label": "Uniform Style", "value": 0}],
                                                    value=[1],
                                                    id="uniform-switch",
                                                    switch=True,
                                                    style={'marginRight': "500px"}
                                                ),
                                                dcc.Upload(
                                                    id='upload-graph-tracking',
                                                    children=dbc.Button(
                                                        [html.I(className="fas fa-upload"), " ", ".json"], 
                                                        style={'border': 'none', 'color': '#8793c9', 'backgroundColor': 'lightgray', 'padding': '7px'}
                                                    )
                                                ),
                                                dbc.Button(
                                                    html.I(className="fas fa-trash"), 
                                                    id='delete-tracking-map', 
                                                    color="danger", 
                                                    style={'border': 'none', 'color': '#E57373', 'backgroundColor': 'lightgray', 'padding': '7px'}
                                                ),
                                            ]
                                        ),
                                        dbc.Tooltip(
                                            translation['hover-uniform'],
                                            target="uniform-switch",  # ID of the element to show the tooltip for
                                            placement="top",
                                            autohide=True,
                                            delay={"show": 500, "hide": 100}
                                        ),

                                        dbc.Tooltip(
                                            translation['hover-upload-tracking'],  # Tooltip text
                                            target='upload-graph-tracking',  # ID of the element to show the tooltip for
                                            placement="top",
                                            autohide=True, 
                                            delay={"show": 500, "hide": 100}
                                        ),

                                        dbc.Tooltip(
                                            translation['hover-delete-tracking'],  # Tooltip text
                                            target="delete-tracking-map",  # ID of the element to show the tooltip for
                                            placement="top",
                                            autohide=True, 
                                            delay={"show": 500, "hide": 100}  # Set delay for show and hide (milliseconds) # Adjust placement as needed (top, bottom, left, right)
                                        ),

                                    ]
                                )
                            ]
                        ),
                    ],
                ),
            ],
        )

# def create_about(app, translation):
#     return html.Div([
#         html.Div(
#             [
#                 html.Br(),
#                 html.Br(),
#                 #html.Br(),
#                 html.H1(
#                     "Share Knowledge. Empower People.", 
#                     style={"fontFamily": "Arial Black", 
#                            "fontWeight": "bold",
#                            "color": "white", 
#                            'marginLeft':'-100px'}),
#                 html.Br(),
#                 html.Br(),
#                 html.P(translation['psysys_mission'],
#                     style={"maxWidth": "900px", 
#                            "color": "white", 
#                            "margin": "0 auto", 
#                            'marginLeft':'180px'},
#                 ),
#                 html.Br(),
#             ],
#             style={
#                 "background-image": "linear-gradient(to right, #8793c9, #516395)",
#                 #614385, #516395
#                 #614385, #516395
#                 #93A5CF, #E4EfE9
#                 #4F86F7, #4961F7
#                 #2E3192, #1BFFFF
#                 "padding": "20px",
#                 "textAlign": "center",
#                 "margin": "0",
#                 "width": "100%",
#                 "position": "fixed",
#                 "top": "0",
#                 "left": "116.4px",
#                 "zIndex": "1000",  # Ensures it's above other content
#             },
#         ),
#         html.Div(
#             [
#                 html.Div(
#                     [
#                         html.Img(
#                             src=app.get_asset_url('DSC_4985.JPG'), 
#                             style={'width': '160px', 
#                                    'height': '160px',
#                                    'borderRadius': '50%', 
#                                    'margin': '5px'}),
#                         html.P(
#                             "Emily Campos Sindermann", 
#                             style={'textAlign': 'center', 
#                                    'marginTop': '10px', 
#                                    'color': 'black', 
#                                    "fontFamily": "Arial Black"}),
#                         html.P(
#                             translation['freelance'],
#                             style={'marginTop': '-15px', 
#                                    'fontStyle': 'italic', 
#                                    'color': 'grey'}),
#                         html.P(
#                             translation['role_01'], 
#                             style={'marginTop': '-15px', 
#                                    'fontStyle': 'italic', 
#                                    'color': 'grey'}),
#                     ],
#                     style={'display': 'inline-block', 
#                            'margin': '3px',
#                            'marginTop': '130px',
#                            'marginLeft': '-150px'},
#                 ),
#                 html.Div(
#                     [
#                         html.Img(
#                             src=app.get_asset_url('profile_dennyborsboom.jpeg'), 
#                             style={'width': '160px', 
#                                    'height': '160px', 
#                                    'borderRadius': '50%', 
#                                    'margin': '5px',
#                                    'marginLeft': '40px'}),
#                         html.P(
#                             "Denny Borsboom", 
#                             style={'textAlign': 'center', 
#                                    'marginTop': '10px', 
#                                    'color': 'black',
#                                    "fontFamily": "Arial Black", 
#                                    'marginLeft': '30px'}),
#                         html.P(
#                             "University of Amsterdam", 
#                             style={'marginTop': '-15px', 
#                                    'fontStyle': 'italic', 
#                                    'color': 'grey',
#                                    'marginLeft': '25px'}),
#                         html.P(
#                             translation['role_02'], 
#                             style={'marginTop': '-15px', 
#                                    'fontStyle': 'italic', 
#                                    'color': 'grey',
#                                    'marginLeft': '25px'}),
#                     ],
#                     style={'display': 'inline-block',
#                            'margin': '3px'},
#                 ),
#                 html.Div(
#                     [
#                         html.Img(
#                             src=app.get_asset_url('profile_tessablanken.jpeg'), 
#                             style={'width': '160px', 
#                                    'height': '160px', 
#                                    'borderRadius': '50%', 
#                                    'margin': '5px',
#                                    'marginLeft': '70px'}),
#                         html.P(
#                             "Tessa Blanken", 
#                             style={'textAlign': 'center', 
#                                    'marginTop': '10px', 
#                                    'color': 'black',
#                                    "fontFamily": "Arial Black",
#                                    'marginLeft': '70px'}),
#                         html.P(
#                             "University of Amsterdam", 
#                             style={'marginTop': '-15px', 
#                                    'fontStyle': 'italic', 
#                                    'color': 'grey',
#                                    'marginLeft': '60px'}),
#                         html.P(
#                             translation['role_03'], 
#                             style={'marginTop': '-15px', 
#                                    'fontStyle': 'italic', 
#                                    'color': 'grey', 
#                                    'marginLeft': '60px'}),
#                     ],
#                     style={'display': 'inline-block', 
#                            'margin': '3px'},
#                 ),
#                 html.Div(
#                     [
#                         html.Img(
#                             src=app.get_asset_url('profile_larsklintwall.jpeg'), 
#                             style={'width': '160px', 
#                                    'height': '160px', 
#                                    'borderRadius': '50%', 
#                                    'margin': '5px', 
#                                    'marginLeft': '70px'}),
#                         html.P(
#                             "Lars Klintwall", 
#                             style={'textAlign': 'center', 
#                                    'marginTop': '10px', 
#                                    'color': 'black',
#                                    "fontFamily": "Arial Black", 
#                                    'marginLeft': '70px'}),
#                         html.P(
#                             "Karolinska Institute", 
#                             style={'marginTop': '-15px', 
#                                    'fontStyle': 'italic', 
#                                    'color': 'grey',
#                                    'marginLeft': '70px'}),
#                         html.P(
#                             translation['role_04'], 
#                             style={'marginTop': '-15px', 
#                                    'fontStyle': 'italic', 
#                                    'color': 'grey',
#                                    'marginLeft': '70px'}),
#                     ],
#                     style={'display': 'inline-block', 
#                            'margin': '3px'},
#                 ),
#                 html.Div(
#                     [
#                         html.Img(
#                             src=app.get_asset_url('profile_julianburger.jpeg'), 
#                             style={'width': '160px', 
#                                    'height': '160px', 
#                                    'borderRadius': '50%', 
#                                    'margin': '5px', 
#                                    'marginLeft': '70px'}),
#                         html.P(
#                             "Julian Burger", 
#                             style={'textAlign': 'center', 
#                                    'marginTop': '10px', 
#                                    'color': 'black', 
#                                    "fontFamily": "Arial Black",
#                                    'marginLeft': '60px'}),
#                         html.P(
#                             "Yale University", 
#                             style={'marginTop': '-15px', 
#                                    'fontStyle': 'italic', 
#                                    'color': 'grey', 
#                                    'marginLeft': '60px'}),
#                         html.P(
#                             translation['role_03'], 
#                             style={'marginTop': '-15px', 
#                                    'fontStyle': 'italic', 
#                                    'color': 'grey', 
#                                    'marginLeft': '60px'}),
#                     ],
#                     style={'display': 'inline-block', 
#                            'margin': '3px'},
#                 ),

#                 # Birdt Health section
#                 html.Div(
#                     [
#                         html.Div(
#                             html.Img(
#                                 src=app.get_asset_url('Amsterdamuniversitylogo.svg.png'), 
#                                 style={'width': '50px', 
#                                        'height': '50px', 
#                                        'borderRadius': '50%', 
#                                        'marginRight': '15px'}),
#                             style={'flex': '0 0 auto'}
#                         ), 

#                         html.Div(
#                             html.Img(
#                                 src=app.get_asset_url('birdt-health-logo.jpeg'), 
#                                 style={'width': '50px', 
#                                        'height': '50px', 
#                                        'borderRadius': '50%', 
#                                        'marginRight': '15px'}),
#                             style={'flex': '0 0 auto'}
#                         ),
#                         html.Div(style={'height': '30px'}),
#                         html.Div(
#                             html.P(
#                                 translation['birdt'], 
#                                 style={'textAlign': 'left', 
#                                        'color': 'grey', 
#                                        'marginTop': '12px',
#                                        'maxWidth': '350px'}),
#                             style={'flex': '1'}
#                         )
#                     ],
#                     style={'display': 'flex', 
#                            'alignItems': 'center', 
#                            'marginTop': '20px',
#                            'marginLeft': '400px',
#                            'width': '35%',
#                            'padding': '10px',
#                            'borderTop': '1px solid lightgrey',
#                            'justifyContent': 'center',
#                            'textAlign': 'center'}
#                 ),
#             ],
#             style={"backgroundColor": "#f0f0f0", 
#                    'position': 'fixed', 
#                    'top':'200px', 
#                    'bottom': '0', 
#                    'left': '117px', 
#                    'width': '100%',
#                    'textAlign': 'center'},
#         ),
#     ], style={"backgroundColor": "#f0f0f0",
#               "overflowY": "auto"})

def create_about(app, translation):
    return html.Div([
        html.Div(
            style=HEADER_STYLE,
            children=[
                html.H2(
                    "Share Knowledge. Empower People.", 
                    style={"fontFamily": "Arial Black", 
                           "fontWeight": "bold",
                           "color": "white", 
                           "textAlign": 'center'}),
                        html.Div(style={"height": "20px"}),
                        html.P(translation['psysys_mission'],
                            style={"maxWidth": "900px", 
                                "color": "white", 
                                "margin": "0 auto", 
                                #'marginLeft':'180px',
                                "textAlign": 'center'},
                        ),
                    ],
                ),
        html.Div(
            style=ABOUT_SECTION_STYLE,
            children=[
                # Member 1
                html.Div(
                    style=ABOUT_MEMBER_STYLE,
                    children=[
                        html.Img(src=app.get_asset_url('DSC_4985.JPG'), style=IMAGE_STYLE),
                        html.Div(
                            style=TEXT_CONTAINER_STYLE,
                            children=[
                                html.P("Emily Campos Sindermann", style={"fontWeight": "bold", "color": "black","marginBottom": '1px', 'marginTop': '10px'}),
                                html.P(translation['freelance'], style=TEXT_ELEMENT_STYLE),
                                html.P(translation['role_01'], style=TEXT_ELEMENT_STYLE),
                            ]
                        ),
                    ]
                ),
                # Member 2
                html.Div(
                    style=ABOUT_MEMBER_STYLE,
                    children=[
                        html.Img(src=app.get_asset_url('profile_dennyborsboom.jpeg'), style=IMAGE_STYLE),
                        html.Div(
                            style=TEXT_CONTAINER_STYLE,
                            children=[
                                html.P("Denny Borsboom", style={"fontWeight": "bold", "color": "black","marginBottom": '1px', 'marginTop': '10px'}),
                                html.P("University of Amsterdam", style=TEXT_ELEMENT_STYLE),
                                html.P(translation['role_02'], style=TEXT_ELEMENT_STYLE),
                            ]
                        ),
                    ]
                ),
                # Member 3
                html.Div(
                    style=ABOUT_MEMBER_STYLE,
                    children=[
                        html.Img(src=app.get_asset_url('profile_tessablanken.jpeg'), style=IMAGE_STYLE),
                        html.Div(
                            style=TEXT_CONTAINER_STYLE,
                            children=[
                                html.P("Tessa Blanken", style={"fontWeight": "bold", "color": "black","marginBottom": '1px', 'marginTop': '10px'}),
                                html.P("University of Amsterdam", style=TEXT_ELEMENT_STYLE),
                                html.P(translation['role_03'], style=TEXT_ELEMENT_STYLE),
                            ]
                        ),
                    ]
                ),
                # Member 4
                html.Div(
                    style=ABOUT_MEMBER_STYLE,
                    children=[
                        html.Img(src=app.get_asset_url('profile_larsklintwall.jpeg'), style=IMAGE_STYLE),
                        html.Div(
                            style=TEXT_CONTAINER_STYLE,
                            children=[
                                html.P("Lars Klintwall", style={"fontWeight": "bold", "color": "black","marginBottom": '1px', 'marginTop': '10px'}),
                                html.P("Karolinska Institute", style=TEXT_ELEMENT_STYLE),
                                html.P(translation['role_04'], style=TEXT_ELEMENT_STYLE),
                            ]
                        ),
                    ]
                ),
                # Member 5
                html.Div(
                    style=ABOUT_MEMBER_STYLE,
                    children=[
                        html.Img(src=app.get_asset_url('profile_julianburger.jpeg'), style=IMAGE_STYLE),
                        html.Div(
                            style=TEXT_CONTAINER_STYLE,
                            children=[
                                html.P("Julian Burger", style={"fontWeight": "bold", "color": "black","marginBottom": '1px', 'marginTop': '10px'}),
                                html.P("Yale University", style=TEXT_ELEMENT_STYLE),
                                html.P(translation['role_03'], style=TEXT_ELEMENT_STYLE),
                            ]
                        ),
                    ]
                ),
                # Partner Section
                html.Div(
                    style=ABOUT_PARTNER_STYLE,
                    children=[
                        html.Img(src=app.get_asset_url('Amsterdamuniversitylogo.svg.png'), style={
                            'width': '50px', 'height': '50px', 'borderRadius': '50%'}),
                        html.Img(src=app.get_asset_url('birdt-health-logo.jpeg'), style={
                            'width': '50px', 'height': '50px', 'borderRadius': '50%'}),
                        html.P(translation['birdt'], style={"textAlign": "left", "color": "grey", "maxWidth": "350px"}),
                    ]
                ),
            ],
        ),
    ], style=COMMON_STYLE)