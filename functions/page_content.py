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
        style={'width': '100%', "fontFamily": "Outfit", "fontWeight": 200, "fontSize": "16px"}
    )

# Function: Generate likert scales to indicate factor severity
def create_likert_scale(factor, initial_value=0):
    return html.Div([
        html.Label([
            html.Span('Severity of ',
                      style={"fontFamily": "Outfit",  
                             "fontWeight": 200, 
                             'color': 'black'}),
            html.Span(factor, 
                      style={"fontFamily": "Outfit",  
                             "fontWeight": 500, 
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

# Function: Create progress bar
def create_progress_bar(current_step):
    # Define labels directly within the function
    labels = ["Intro", "Personal Factors", "Causal Chains", "Vicious Cycles", "Finding Targets", "Finish"]
    color = "#aaa2fc"

    # Circle elements
    progress_circles = []
    for i, label in enumerate(labels):
        i = i
        completed = i < current_step
        is_current = i == current_step

        progress_circles.append(
            html.Div(
                style={
                    "display": "flex",
                    "flexDirection": "column",
                    "alignItems": "center",
                    "zIndex": "2",  # Ensure circles are above the line
                },
                children=[
                    html.Div(
                        style={
                            "width": "30px",
                            "height": "30px",
                            "borderRadius": "50%",
                            "backgroundColor": color if completed else "#ffffff",
                            "border": "2px solid #aaa2fc" if completed or is_current else "#ccc",
                            "display": "flex",
                            "alignItems": "center",
                            "justifyContent": "center",
                            "color": "#ffffff" if completed else color,
                            "fontWeight": "300",
                            "fontFamily": "Outfit",
                        },
                        children=html.Span("✔" if completed else str(i)),
                    ),
                    html.Div(
                        style={
                            "marginTop": "5px",
                            "color": color if is_current else "#ccc",
                            "fontWeight": "300",
                            "fontFamily": "Outfit",
                        },
                        children=label,  # Use the predefined label
                    ),
                ],
            )
        )

    # Progress bar container
    return html.Div(
        style={
            "position": "relative",
            "display": "flex",
            "alignItems": "center",
            "justifyContent": "space-evenly",  # Decrease space between circles
            "marginLeft": "-120px",
            "marginRight": "0px",
            "marginBottom": "20px",
        },
        children=[
            # Line connecting the circles
            html.Div(
                style={
                    "position": "absolute",
                    "top": "15px",  # Move the line to the vertical center of the circles
                    "left": "5%",
                    "right": "5%",
                    "height": "2px",
                    "backgroundColor": "#aaa2fc" if current_step > 0 else "#ccc",
                    "zIndex": "1",  # Line is behind the circles
                }
            ),
            # Add the circles on top of the line
            *progress_circles,
        ],
    )




# Function: Generate step content based on session data
def generate_step_content(step, session_data, translation):
    # Function content
    if step == 0:
        return html.Div(
            html.Div(
                    style=COMMON_STYLE,
                    children=[
                        # Header Section
                        # html.Div(
                        #     style=HEADER_STYLE,
                        #     children=[
                        #         html.H1(
                        #             translation['welcome_01'],
                        #             className="multi-color-text",
                        #             style={
                        #                 "fontSize": "70px",
                        #                 "fontFamily": "Outfit",
                        #                 "fontWeight": 400,
                        #                 "color": "black",
                        #                 "marginLeft": "0px"
                        #             },
                        #         ),
                        #         html.H3(
                        #             translation['welcome_02'],
                        #             style={
                        #                 "fontFamily": "Outfit",
                        #                 "fontWeight": 400,
                        #                 "color": "black",
                        #                 "marginLeft": "100px"
                        #             },
                        #         ),
                        #     ],
                        # ),

                        # html.Hr(style={"marginLeft": "100px", "width": "90%", "marginTop": "-10px"}),

                        html.Div(
                            style={
                                **HEADER_STYLE,
                                "height": "228px"  # Set a consistent height for the empty header
                            }
                        ),

                        html.Div(create_progress_bar(step), style={"marginTop": "-100px"}),

                        html.Hr(style={"marginLeft": "0px", "width": "90%", "marginTop": "31px"}),

                        # Main Content Container
                        html.Div(
                            style={
                                "display": "flex",
                                "flexDirection": "row",
                                "gap": "20px",
                                "alignItems": "flex-start",
                                "padding": "20px",
                                "marginTop": "-25px"
                            },
                            children=[
                                # Left Section: Fixed Text Block and Likert Scales
                                html.Div(
                                    style={
                                        "width": "40%",
                                        "padding": "15px",
                                        #"marginLeft": "100px",
                                        "marginLeft": "0px"
                                    },
                                    children=[
                                        # Exercise Description and Dropdown
                                        html.Div(
                                            style={
                                                "position": "sticky",
                                                "top": "20px",
                                                "zIndex": "10",
                                                "padding": "15px",
                                                "boxShadow": "0 4px 6px rgba(0, 0, 0, 0.1)",
                                                "borderRadius": "8px",
                                                "backgroundColor": "#F4F3FE",
                                            },
                                            children=[
                                                html.H5("Watch the video. Then click on 'Start' to begin with the session which will guide you through the following blocks:" , style={**TEXT_STYLE, "color": "black"}),
                                                html.Div(style={"height": "10px"}),
                                                html.Ol(
                                                    [
                                                        html.Li(translation['title_block_01'], style={"color": "black", "fontFamily": "Outfit", "fontWeight": 200, "fontSize": "15px"}),
                                                        html.P(translation['description_block_01'], style={"color": "grey", "fontFamily": "Outfit", "fontWeight": 200, "fontSize": "15px"}),
                                                        html.Li(translation['title_block_02'], style={"color": "black", "fontFamily": "Outfit", "fontWeight": 200, "fontSize": "15px"}),
                                                        html.P(translation['description_block_02'], style={"color": "grey", "fontFamily": "Outfit", "fontWeight": 200, "fontSize": "15px"}),
                                                        html.Li(translation['title_block_03'], style={"color": "black", "fontFamily": "Outfit", "fontWeight": 200, "fontSize": "15px"}),
                                                        html.P(translation['description_block_03'], style={"color": "grey", "fontFamily": "Outfit", "fontWeight": 200, "fontSize": "15px"}),
                                                        html.Li(translation['title_block_04'], style={"color": "black", "fontFamily": "Outfit", "fontWeight": 200, "fontSize": "15px"}),
                                                        html.P(translation['description_block_04'], style={"color": "grey", "fontFamily": "Outfit", "fontWeight": 200, "fontSize": "15px"}),
                                                    ],
                                                )
                                            ],
                                        ),
                                    ],
                                ),

                                # Right Section: Video
                                html.Div(
                                    style={
                                        "width": "48.5%",  # Adjusted to align with the left section
                                        "padding": "15px",
                                        "position": "relative",
                                    },
                                    children=[
                                        html.Iframe(
                                            src=translation["video_link_intro"],
                                            style={
                                                **VIDEO_STYLE,
                                                "marginTop": "0px",
                                                "marginLeft": "0px",
                                            },
                                        ),
                                    ],
                                ),
                            ],
                        ),
                    ],
                ),
            )
    

    if step == 1:
        options = session_data.get('dropdowns', {}).get('initial-selection', {}).get('options', [])
        value = session_data.get('dropdowns', {}).get('initial-selection', {}).get('value', [])
        id = {'type': 'dynamic-dropdown', 'step': 1}

        return html.Div(
            html.Div(
                style=COMMON_STYLE,
                children=[
                    # Header Section
                    html.Div(
                        html.Div(
                            id="suicide-prevention-hotline",
                            children=[
                                html.P(
                                    translation['suicide-prevention'],
                                    style={
                                        'color': 'white',
                                        'width': '40%',
                                        'marginTop': '-25px',
                                    },
                                ),
                            ],
                            style={
                                'position': 'fixed',
                                'visibility': 'hidden',
                                'zIndex': '1000',
                            },
                        ),
                        style={**HEADER_STYLE, "height": "228px"},
                    ),

                    html.Div(create_progress_bar(step), style={"marginTop": "-100px"}),

                    html.Hr(style={"marginLeft": "100px", "width": "90%", "marginTop": "31px"}),

                    #html.Hr(style={"marginLeft": "100px", "width": "90%", "marginTop": "-10px"}),

                    # Main Content Container
                    html.Div(
                        style={
                            "display": "flex",
                            "flexDirection": "row",
                            "gap": "20px",
                            "alignItems": "flex-start",
                            "padding": "20px",
                            "marginTop": "-25px"
                        },
                        children=[
                            # Left Section: Fixed Text Block and Likert Scales
                            html.Div(
                                style={
                                    "width": "40%",
                                    "padding": "15px",
                                    "marginLeft": "100px",
                                },
                                children=[
                                    # Exercise Description and Dropdown
                                    html.Div(
                                        style={
                                            "position": "sticky",
                                            "top": "20px",
                                            "zIndex": "10",
                                            #"backgroundColor": "white",
                                            "padding": "15px",
                                            "boxShadow": "0 4px 6px rgba(0, 0, 0, 0.1)",
                                            "borderRadius": "8px",
                                            "backgroundColor": "#F4F3FE",
                                            # "backgroundColor": "#e8eefc",
                                            #"backgroundColor": "#f8f9fa"
                                        },
                                        children=[
                                            html.H5(
                                                "Watch the video. Then select the factors you are currently dealing with from the list below and indicate their severity.",
                                                style=TEXT_STYLE,
                                            ),
                                            html.Div(style={"height": "10px"}),
                                            html.Div(
                                                create_dropdown(
                                                id=id,
                                                options=options,
                                                value=value,
                                                placeholder=translation["placeholder_dd_01"],
                                            ),
                                            className="dynamic-dropdown",
                                            ),
                                        ],
                                    ),
                                    html.Br(),

                                    # Likert Scales Section
                                    html.Div(
                                        id="likert-scales-container",
                                        style={
                                            "marginTop": "0px",
                                            "overflowY": "auto",
                                            "maxHeight": "240px",
                                            "padding": "5px",
                                            #"backgroundColor": "#f8f9fa",
                                            "backgroundColor": "#white",
                                            #"borderRadius": "8px",
                                            #"boxShadow": "0 2px 4px rgba(0, 0, 0, 0.1)",
                                        },
                                    ),
                                ],
                            ),

                            # Right Section: Video
                            html.Div(
                                style={
                                    "width": "48.5%",  # Adjusted to align with the left section
                                    "padding": "15px",
                                    "position": "relative",
                                },
                                children=[
                                    html.Iframe(
                                        src=translation["video_link_block_01"],
                                        style={
                                            **VIDEO_STYLE,
                                            "marginTop": "0px",
                                            "marginLeft": "0px",
                                        },
                                    ),
                                ],
                            ),
                        ],
                    ),
                ],
            ),
        )


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

                html.Div(create_progress_bar(step), style={"marginTop": "-100px"}),

                html.Hr(style={"marginLeft": "100px", "width": "90%", "marginTop": "31px"}),

                # html.Hr(style={"marginLeft": "100px", "width": "90%", "marginTop": "-10px"}),

                html.Div(
                    style={
                        "display": "flex",
                        "flexDirection": "row",
                        "gap": "20px",
                        "alignItems": "flex-start",
                        "padding": "20px",
                        "marginTop": "-25px"
                    },
                    children=[
                        # Left Section: Fixed Text Block and Likert Scales
                        html.Div(
                            style={
                                "width": "40%",
                                "padding": "15px",
                                "marginLeft": "100px",
                            },
                            children=[
                                # Exercise Description and Dropdown
                                html.Div(
                                    style={
                                        "position": "sticky",
                                        "top": "20px",
                                        "zIndex": "10",
                                        #"backgroundColor": "white",
                                        "padding": "15px",
                                        "boxShadow": "0 4px 6px rgba(0, 0, 0, 0.1)",
                                        "borderRadius": "8px",
                                        "backgroundColor": "#F4F3FE",
                                        # "backgroundColor": "#e8eefc",
                                        #"backgroundColor": "#f8f9fa"
                                    },
                                    children=[
                                        html.H5( "Watch the video. Then select two causal chains you recognize from yourself. Include as many factors as you like.",
                                                style=TEXT_STYLE,
                                                ),
                                        html.Div(style={"height": "10px"}),
                                        html.Div(
                                            create_dropdown(
                                            id=id_chain1,
                                            options=options,
                                            value=value_chain1,
                                            placeholder=translation["placeholder_dd_02"],
                                        ),
                                        className="dynamic-dropdown",
                                        ),
                                        html.Div(style={"height": "10px"}),
                                        html.P("e.g. If you have trouble sleeping, which impairs your ability to concentrate, select 'Sleep problems', 'Trouble concentrating'.", 
                                            style={'width': '100%',
                                                'fontFamily': 'Outfit',
                                                "fontWeight": "200", 
                                                'color': 'grey',
                                                'fontSize': '15px'}),
                                        html.Div(style={"height": "10px"}),
                                        html.Div(
                                            create_dropdown(
                                            id=id_chain2,
                                            options=options,
                                            value=value_chain2,
                                            placeholder=translation["placeholder_dd_02"],
                                        ),
                                        className="dynamic-dropdown",
                                        ),
                                        html.Div(style={"height": "10px"}),
                                        html.P("e.g. If your fear of the future increases your feelings of hopelesness, which in turn worsens your anxiety, select 'Fear of the future', 'Hopelesness', 'Anxiety'.", 
                                            style={'width': '100%',
                                                'fontFamily': 'Outfit',
                                                "fontWeight": "200", 
                                                'color': 'grey',
                                                'fontSize': '15px'}),
                                    ],
                                ),
                            ],
                        ),

                        # Right Section: Video
                        html.Div(
                            style={
                                "width": "48.5%",  # Adjusted to align with the left section
                                "padding": "15px",
                                "position": "relative",
                            },
                            children=[
                                html.Iframe(
                                    src=translation["video_link_block_02"],
                                    style={
                                        **VIDEO_STYLE,
                                        "marginTop": "0px",
                                        "marginLeft": "0px",
                                    },
                                ),
                            ],
                        ),
                    ],
                ),
            ],
        )
    
    
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

                html.Div(create_progress_bar(step), style={"marginTop": "-100px"}),

                html.Hr(style={"marginLeft": "100px", "width": "90%", "marginTop": "31px"}),

                #html.Hr(style={"marginLeft": "100px", "width": "90%", "marginTop": "-10px"}),

                html.Div(
                    style={
                        "display": "flex",
                        "flexDirection": "row",
                        "gap": "20px",
                        "alignItems": "flex-start",
                        "padding": "20px",
                        "marginTop": "-25px"
                    },
                    children=[
                        # Left Section: Fixed Text Block and Likert Scales
                        html.Div(
                            style={
                                "width": "40%",
                                "padding": "15px",
                                "marginLeft": "100px",
                            },
                            children=[
                                # Exercise Description and Dropdown
                                html.Div(
                                    style={
                                        "position": "sticky",
                                        "top": "20px",
                                        "zIndex": "10",
                                        #"backgroundColor": "white",
                                        "padding": "15px",
                                        "boxShadow": "0 4px 6px rgba(0, 0, 0, 0.1)",
                                        "borderRadius": "8px",
                                        "backgroundColor": "#F4F3FE",
                                        # "backgroundColor": "#e8eefc",
                                        #"backgroundColor": "#f8f9fa"
                                    },
                                    children=[
                                        html.H5( "Watch the video. Then select two vicious cycles you recognize from yourself. Include as many factors as you like.",
                                                style=TEXT_STYLE,
                                                ),
                                        html.Div(style={"height": "10px"}),
                                        html.Div(
                                            create_dropdown(
                                            id=id_cycle1,
                                            options=options,
                                            value=value_cycle1,
                                            placeholder=translation["placeholder_dd_03"],
                                        ),
                                        className="dynamic-dropdown",
                                        ),
                                        html.Div(style={"height": "10px"}),
                                        html.P("e.g. If you have trouble sleeping, which increases your anxiety, which worsens your sleep, select 'Sleep problems', 'Anxiety'.", 
                                            style={'width': '100%',
                                                'fontFamily': 'Outfit',
                                                "fontWeight": "200", 
                                                'color': 'grey',
                                                'fontSize': '15px'}),
                                        html.Div(style={"height": "10px"}),
                                        html.Div(
                                            create_dropdown(
                                            id=id_cycle2,
                                            options=options,
                                            value=value_cycle2,
                                            placeholder=translation["placeholder_dd_03"],
                                        ),
                                        className="dynamic-dropdown",
                                        ),
                                        html.Div(style={"height": "10px"}),
                                        html.P("e.g. If your social isolation leads to self-neglect which increases your shame and only worsens your isolation, select 'Social isolation', 'Self-neglect', 'Shame'.", 
                                            style={'width': '100%',
                                                'fontFamily': 'Outfit',
                                                "fontWeight": "200", 
                                                'color': 'grey',
                                                'fontSize': '15px'}),
                                    ],
                                ),
                            ],
                        ),

                        # Right Section: Video
                        html.Div(
                            style={
                                "width": "48.5%",  # Adjusted to align with the left section
                                "padding": "15px",
                                "position": "relative",
                            },
                            children=[
                                html.Iframe(
                                    src=translation["video_link_block_03"],
                                    style={
                                        **VIDEO_STYLE,
                                        "marginTop": "0px",
                                        "marginLeft": "0px",
                                    },
                                ),
                            ],
                        ),
                    ],
                ),
            ],
        )
    
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

                html.Div(create_progress_bar(step), style={"marginTop": "-100px"}),

                html.Hr(style={"marginLeft": "100px", "width": "90%", "marginTop": "31px"}),

                html.Div(
                    style={
                        "display": "flex",
                        "flexDirection": "row",
                        "gap": "20px",
                        "alignItems": "flex-start",
                        "padding": "20px",
                        "marginTop": "-25px"
                    },
                    children=[
                        # Left Section: Fixed Text Block and Likert Scales
                        html.Div(
                            style={
                                "width": "40%",
                                "padding": "15px",
                                "marginLeft": "100px",
                            },
                            children=[
                                # Exercise Description and Dropdown
                                html.Div(
                                    style={
                                        "position": "sticky",
                                        "top": "20px",
                                        "zIndex": "10",
                                        #"backgroundColor": "white",
                                        "padding": "15px",
                                        "boxShadow": "0 4px 6px rgba(0, 0, 0, 0.1)",
                                        "borderRadius": "8px",
                                        "backgroundColor": "#F4F3FE",
                                        # "backgroundColor": "#e8eefc",
                                        #"backgroundColor": "#f8f9fa"
                                    },
                                    children=[
                                        html.H5( "Watch the video. Then select the factor you feel like is the most influential one in your mental-health-map.",
                                                style=TEXT_STYLE,
                                                ),
                                        html.Div(style={"height": "10px"}),
                                        html.Div(
                                            create_dropdown(
                                            id=id,
                                            options=options,
                                            value=value_target,
                                            placeholder=translation["placeholder_dd_04"],
                                        ),
                                        className="dynamic-dropdown",
                                        ),
                                        html.Div(style={"height": "10px"}),
                                        html.P(translation['example_block_04'], 
                                            style={'width': '100%',
                                                'fontFamily': 'Outfit',
                                                "fontWeight": "200", 
                                                'color': 'grey',
                                                'fontSize': '15px'}),
                                    ],
                                ),
                            ],
                        ),

                        # Right Section: Video
                        html.Div(
                            style={
                                "width": "48.5%",  # Adjusted to align with the left section
                                "padding": "15px",
                                "position": "relative",
                            },
                            children=[
                                html.Iframe(
                                    src=translation["video_link_block_04"],
                                    style={
                                        **VIDEO_STYLE,
                                        "marginTop": "0px",
                                        "marginLeft": "0px",
                                    },
                                ),
                            ],
                        ),
                    ],
                ),
            ],
        )
    
    
    if step == 5:
        elements = session_data.get('elements', [])
        selected_factors = session_data.get('add-nodes', [])
        options = [{'label': factor, 'value': factor} for factor in selected_factors]
        return html.Div(
            style=COMMON_STYLE,
            children=[
                # Header Section
                # html.Div(
                #     style=HEADER_STYLE,
                #     children=[
                #         html.H1(
                #             translation['finish_01'],
                #             className="multi-color-text",
                #             style={
                #                 "fontSize": "70px",
                #                 "fontFamily": "Outfit",
                #                 "fontWeight": 400,
                #                 "color": "black",
                #                 "marginLeft": "-65px"
                #             },
                #         ),
                #         html.H3(
                #             translation['finish_02'],
                #             style={
                #                 "fontFamily": "Outfit",
                #                 "fontWeight": 400,
                #                 "color": "black",
                #                 "marginLeft": "100px"
                #             },
                #         ),
                #     ],
                # ),

                # html.Hr(style={"marginLeft": "100px", "width": "90%", "marginTop": "-10px"}),

                html.Div(
                    style={
                        **HEADER_STYLE,
                        "height": "228px"  # Set a consistent height for the empty header
                    }
                ),

                html.Div(create_progress_bar(step), style={"marginTop": "-100px"}),

                html.Hr(style={"marginLeft": "100px", "width": "90%", "marginTop": "31px"}),

                # Main Content Container
                html.Div(
                    style={
                        "display": "flex",
                        "flexDirection": "row",
                        "gap": "20px",
                        "alignItems": "flex-start",
                        "padding": "20px",
                        "marginTop": "-25px"
                    },
                    children=[
                        # Left Section: Fixed Text Block and Likert Scales
                        html.Div(
                            style={
                                "width": "40%",
                                "padding": "15px",
                                "marginLeft": "100px",
                            },
                            children=[
                                # Exercise Description and Dropdown
                                html.Div(
                                    style={
                                        "position": "sticky",
                                        "top": "20px",
                                        "zIndex": "10",
                                        "padding": "15px",
                                        "boxShadow": "0 4px 6px rgba(0, 0, 0, 0.1)",
                                        "borderRadius": "8px",
                                        "backgroundColor": "#F4F3FE",
                                    },
                                    children=[
                                        html.H5(translation['feedback_text'] , style={**TEXT_STYLE, "color": "black"}),
                                        html.Div(style={"height": "10px"}),
                                        html.Ol(
                                            [
                                                html.Li(translation['feedback_question_01'], style={"color": "black", "fontFamily": "Outfit", "fontWeight": 200, "fontSize": "15px"}),
                                                html.Li(translation['feedback_question_02'], style={"color": "black", "fontFamily": "Outfit", "fontWeight": 200, "fontSize": "15px"}),
                                                html.Li(translation['feedback_question_03'], style={"color": "black", "fontFamily": "Outfit", "fontWeight": 200, "fontSize": "15px"}),
                                                html.Li(translation['feedback_question_04'], style={"color": "black", "fontFamily": "Outfit", "fontWeight": 200, "fontSize": "15px"}),
                                            ],
                                        )
                                    ],
                                ),
                            ],
                        ),

                        # Right Section: Video
                        html.Div(
                            style={
                                "width": "48.5%",  # Adjusted to align with the left section
                                "padding": "15px",
                                "position": "relative",
                            },
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
                                    style={**VIDEO_STYLE, "marginLeft": "0px", "marginTop": "0px"}
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

# Function: Create Team page
def create_about(app, translation):
    return html.Div([
        html.Div(
            style=HEADER_STYLE,
            children=[
                # html.H2(
                #     "Share Knowledge. Empower People.", 
                #     style={"fontFamily": "Arial Black", 
                #            "fontWeight": "bold",
                #            "color": "white", 
                #            "textAlign": 'center'}),
                        html.Div(style={"height": "20px"}),
                        # html.P(translation['psysys_mission'],
                        #     style={"maxWidth": "900px", 
                        #         "color": "white", 
                        #         "margin": "0 auto", 
                        #         #'marginLeft':'180px',
                        #         "textAlign": 'center'},
                        # ),
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

# Function: Create demo page
# def create_demo_page():
#     return html.Div(
#         style={
#             "textAlign": "center",
#             "background": "linear-gradient(to bottom, white, #f4f4f9, #d6ccff, #9b84ff, #6F4CFF)",
#             "fontFamily": "Outfit",
#             "width": "100vw",  # Use 100% to avoid horizontal overflow
#             "height": "100vh",
#             "display": "flex",
#             "flexDirection": "column",
#             "justifyContent": "center",
#             "alignItems": "center",
#             "overflowX": "hidden",  # Prevent horizontal scrolling
#             "marginLeft": "-12px"
#         },
#         children=[
#             # Header Section
#             html.Div(
#                 children=[
#                     html.Img(
#                         src="/assets/new-logo.png",
#                         style={"width": "200px", "marginBottom": "20px"},
#                     ),
#                     html.H1(
#                         #"Welcome to PsySys",
#                         "PsySys Demo",
#                         #className="multi-color-text",
#                         style={
#                             "fontSize": "55px",
#                             #"color": "black",
#                             "color": "#4A4A8D",
#                             "fontWeight": 500,
#                             "fontFamily": "Outfit",
#                         },
#                     ),
#                     html.P(
#                         "Discover insights, track your mental health, and gain actionable knowledge.",
#                         style={"fontSize": "18px", "color": "#6c757d", "fontWeight": 300},
#                     ),
#                     # Buttons Section
#                     html.Div(
#                         children=[
#                             dbc.Button(
#                                 "Get Started",
#                                 href="/psychoeducation",
#                                 className="glowing-button",
#                                 style={
#                                     "margin": "10px",
#                                     "fontSize": "18px",
#                                     "padding": "10px 20px",
#                                     "backgroundColor": "#6F4CFF",
#                                     "border": "none",
#                                     "color": "white",
#                                     "borderRadius": "50px",
#                                 },
#                             ),
#                             dbc.Button(
#                                 "Learn More",
#                                 href="/about",
#                                 style={
#                                     "margin": "10px",
#                                     "fontSize": "18px",
#                                     "padding": "10px 20px",
#                                     "backgroundColor": "transparent",
#                                     "color": "#6F4CFF",
#                                     "border": "2px solid #6F4CFF",
#                                     "borderRadius": "50px",
#                                 },
#                             ),
#                         ]
#                     ),
#                 ],
#                 style={
#                     "maxWidth": "900px",
#                     "backgroundColor": "#fff",
#                     "padding": "20px 40px",  # Adjusted padding
#                     "borderRadius": "30px",
#                     "opacity": "0.9",
#                     "boxSizing": "border-box",  # Ensures padding doesn't overflow
#                     "boxShadow": "0px 4px 10px rgba(0, 0, 0, 0.1)",
#                     "marginTop": "140px"
#                 },
#             ),
#             # Features Section
#             html.Div(
#                 style={"marginTop": "50px", "width": "100%"},  # Adjusted for responsive width
#                 children=[
#                     html.H2(
#                         "Our Features",
#                         style={
#                             "fontSize": "32px",
#                             #"color": "#4a4a8d",
#                             "color": "black", 
#                             "marginBottom": "30px",
#                             "fontWeight": 400,
#                         },
#                     ),
#                     dbc.Row(
#                         [
#                             dbc.Col(
#                                 html.Div(
#                                     children=[
#                                         html.H4(
#                                             "Psychoeducation",
#                                             style={"marginTop": "5px", "fontWeight": 500},
#                                         ),
#                                         html.P(
#                                             "Learn about your mental health dynamics.",
#                                             style={"fontSize": "17px", "color": "black", "fontWeight": 300},
#                                         ),
#                                     ],
#                                     style={"textAlign": "center", "padding": "5px"},
#                                 ),
#                                 md=3,
#                             ),
#                             dbc.Col(
#                                 html.Div(
#                                     children=[
#                                         html.H4(
#                                             "Map Editor",
#                                             style={"marginTop": "5px", "fontWeight": 500},
#                                         ),
#                                         html.P(
#                                             "Build your mental-health-map.",
#                                             style={"fontSize": "17px", "color": "black", "fontWeight": 300},
#                                         ),
#                                     ],
#                                     style={"textAlign": "center", "padding": "5px"},
#                                 ),
#                                 md=3,
#                             ),
#                             dbc.Col(
#                                 html.Div(
#                                     children=[
#                                         html.H4(
#                                             "Map Tracker",
#                                             style={"marginTop": "5px", "fontWeight": 500},
#                                         ),
#                                         html.P(
#                                             "Monitor your mental-health-maps.",
#                                             style={"fontSize": "17px", "color": "black", "fontWeight": 300},
#                                         ),
#                                     ],
#                                     style={"textAlign": "center", "padding": "5px"},
#                                 ),
#                                 md=3,
#                             ),
#                         ],
#                         justify="center",
#                         className="g-2",  # Add gap for consistency
#                     ),
#                 ],
#             ),
#         ],
#     )

def create_demo_page():
    return html.Div(
        style={
            "textAlign": "center",
            "background": "linear-gradient(to bottom, white, #f4f4f9, #d6ccff, #9b84ff, #6F4CFF)",
            "fontFamily": "Outfit",
            "width": "100vw",
            "minHeight": "100vh",
            "display": "flex",
            "flexDirection": "column",
            "justifyContent": "center",
            "alignItems": "center",
            "overflowX": "hidden",
            "marginLeft": "-12px",
        },
        children=[
            # Header Section
            html.Div(
                children=[
                    html.Img(
                        src="/assets/new-logo.png",
                        style={"width": "200px", "marginBottom": "20px"},
                    ),
                    html.H1(
                        "PsySys Demo",
                        style={
                            "fontSize": "55px",
                            "color": "#4A4A8D",
                            "fontWeight": 500,
                            "fontFamily": "Outfit",
                        },
                    ),
                    html.P(
                        "Discover insights, track your mental health, and gain actionable knowledge.",
                        style={"fontSize": "18px", "color": "#6c757d", "fontWeight": 300},
                    ),

                    html.Div(
                        children=[
                            dbc.Button(
                                "Get Started",
                                href="/psychoeducation",
                                className="glowing-button",
                                style={
                                    "margin": "10px",
                                    "fontSize": "18px",
                                    "padding": "10px 20px",
                                    "backgroundColor": "#6F4CFF",
                                    "border": "none",
                                    "color": "white",
                                    "borderRadius": "50px",
                                    "boxShadow": "0px 4px 6px rgba(0, 0, 0, 0.2)"
                                },
                            ),
                            dbc.Button(
                                "Learn More",
                                href="/about",
                                style={
                                    "margin": "10px",
                                    "fontSize": "18px",
                                    "padding": "10px 20px",
                                    "backgroundColor": "transparent",
                                    "color": "#6F4CFF",
                                    "border": "2px solid #6F4CFF",
                                    "borderRadius": "50px",
                                    "boxShadow": "0px 4px 6px rgba(0, 0, 0, 0.2)"
                                },
                            ),
                        ]
                    ),
                ],
                style={
                    "maxWidth": "900px",
                    "backgroundColor": "#fff",
                    "padding": "20px 40px",
                    "borderRadius": "30px",
                    "opacity": "0.9",
                    "boxShadow": "0px 4px 10px rgba(0, 0, 0, 0.1)",
                    "marginTop": "120px",
                },
            ),
            # Features Section
            html.Div(
                style={"marginTop": "50px", "width": "100%"},
                children=[
                    # html.H2(
                    #     "Our Features",
                    #     style={
                    #         "fontSize": "32px",
                    #         "color": "black",
                    #         "marginBottom": "30px",
                    #         "fontWeight": 400,
                    #     },
                    # ),
                    dbc.Row(
                        [
                            # Feature 1: Psychoeducation
                            dbc.Col(
                                html.A(
                                    href="/psychoeducation",  # Target URL
                                    style={"textDecoration": "none"},  # Remove underline
                                    children=html.Div(
                                        children=[
                                            html.H4(
                                                "Psychoeducation",
                                                style={
                                                    "marginTop": "10px",
                                                    "fontWeight": 600,
                                                    "color": "black",
                                                },
                                            ),
                                            html.P(
                                                "Learn about your mental dynamics.",
                                                style={
                                                    "fontSize": "17px",
                                                    "color": "black",
                                                    "fontWeight": 300,
                                                },
                                            ),
                                        ],
                                        style={
                                            #"backgroundColor": "#A5C9FF",
                                            "backgroundColor": "#C9E2FF",
                                            #"backgroundColor": "#D6E9F8",
                                            "borderRadius": "15px",
                                            "padding": "30px 20px",
                                            "textAlign": "center",
                                            "boxShadow": "0px 4px 10px rgba(0, 0, 0, 0.1)",
                                            "transition": "transform 0.2s ease-in-out",
                                        },
                                        className="feature-box",
                                    ),
                                ),
                                md=3,
                            ),
                            # Feature 2: Map Editor
                            dbc.Col(
                                html.A(
                                    href="/my-mental-health-map",  # Target URL
                                    style={"textDecoration": "none"},
                                    children=html.Div(
                                        children=[
                                            html.H4(
                                                "Map Editor",
                                                style={
                                                    "marginTop": "10px",
                                                    "fontWeight": 600,
                                                    "color": "black",
                                                },
                                            ),
                                            html.P(
                                                "Build your mental-health-map.",
                                                style={
                                                    "fontSize": "17px",
                                                    "color": "black",
                                                    "fontWeight": 300,
                                                },
                                            ),
                                        ],
                                        style={
                                            "backgroundColor": "#D6CCFF",
                                            "borderRadius": "15px",
                                            "padding": "30px 20px",
                                            "textAlign": "center",
                                            "boxShadow": "0px 4px 10px rgba(0, 0, 0, 0.1)",
                                            "transition": "transform 0.2s ease-in-out",
                                        },
                                        className="feature-box",
                                    ),
                                ),
                                md=3,
                            ),
                            # Feature 3: Map Tracker
                            dbc.Col(
                                html.A(
                                    href="/track-my-mental-health-map",  # Target URL
                                    style={"textDecoration": "none"},
                                    children=html.Div(
                                        children=[
                                            html.H4(
                                                "Map Tracker",
                                                style={
                                                    "marginTop": "10px",
                                                    "fontWeight": 600,
                                                    "color": "black",
                                                },
                                            ),
                                            html.P(
                                                "Monitor your mental-health-maps.",
                                                style={
                                                    "fontSize": "17px",
                                                    "color": "black",
                                                    "fontWeight": 300,
                                                },
                                            ),
                                        ],
                                        style={
                                            "backgroundColor": "#F4D9FF",
                                            "borderRadius": "15px",
                                            "padding": "30px 20px",
                                            "textAlign": "center",
                                            "boxShadow": "0px 4px 10px rgba(0, 0, 0, 0.1)",
                                            "transition": "transform 0.2s ease-in-out",
                                        },
                                        className="feature-box",
                                    ),
                                ),
                                md=3,
                            ),
                        ],
                        justify="center",
                        className="g-4",  # Adds spacing between columns
                    ),
                ],
            ),
        ],
    )

# Function: Create landing page
# def create_landing_page():
#     return html.Div(
#         style={
#             "height": "100vh",
#             "width": "100%",
#             "background": "linear-gradient(to right, white 190px, #f4f4f9 250px, #d6ccff 600px, #9b84ff 70%, #6F4CFF)",
#             "display": "flex",
#             "position": "relative",  # Enables absolute positioning for layers
#             "fontFamily": "Outfit",
#             "color": "white",
#             "overflow": "hidden",
            
#         },
#         children=[
#             # Layered Network Images from Bottom-Left
#             html.Div(
#                 style={
#                     "position": "absolute",
#                     "top": "50%",
#                     "left": "28%",
#                     "zIndex": "0",  # Behind all content
#                 },
#                 children=[
#                     html.Img(
#                         src="/assets/network_2.png",
#                         style={
#                             "width": "600px",
#                             "opacity": "0.7",
#                             "transform": "rotate(10deg) translate(50px, 50px)",
#                             "animation": "move-glow-1 2s infinite alternate"
#                         },
#                     ),
#                 ]
#             ), 

#             html.Div(
#                 style={
#                     "position": "absolute",
#                     "top": "40%",
#                     "left": "-5%",
#                     "zIndex": "0",  # Behind all content
#                 },
#                 children=[
#                     html.Img(
#                         src="/assets/network_3.png",
#                         style={
#                             "width": "900px",
#                             "opacity": "0.5",
#                             "transform": "rotate(35deg) translate(-100px, -50px)",
#                             "animation": "move-glow-2 2s infinite alternate"
#                         },
#                     ),
#                 ]
#             ), 

#             html.Div(
#                 style={
#                     "position": "absolute",
#                     "top": "40%",
#                     "left": "-5%",
#                     "zIndex": "0",  # Behind all content
#                 },
#                 children=[
#                     html.Img(
#                         src="/assets/network_4.png",
#                         style={
#                             "width": "1200px",
#                             "opacity": "0.3",
#                             "transform": "rotate(-10deg) translate(-200px, -100px)",
#                             "animation": "move-glow-3 5s infinite alternate"
#                         },
#                     ),
#                 ]
#             ), 

#             # Text in Bottom-Right Corner
#             html.Div(
#                 style={
#                     "position": "absolute",
#                     "bottom": "10%",
#                     "right": "5%",
#                     "textAlign": "right",
#                     "zIndex": "1",  # Above the network images
#                 },
#                 children=[
#                     html.H1(
#                         "PsySys",
#                         style={
#                             "fontSize": "60px",
#                             "fontWeight": "bold",
#                             "marginBottom": "20px",
#                             "color": "white",
#                         },
#                     ),
#                     html.P(
#                         "Leveraging the network approach to psychopathology to empower patients.",
#                         style={
#                             "fontSize": "25px",
#                             "fontWeight": "300",
#                             "maxWidth": "500px",
#                             "margin": "0 auto",
#                             "color": "white",
#                         },
#                     ),
#                     # Call-to-Action Buttons
#                     html.Div(
#                         style={"marginTop": "30px", "display": "flex", "gap": "10px", "justifyContent": "flex-end"},
#                         children=[
#                             dbc.Button(
#                                 "Get Started",
#                                 href="/get-started",
#                                 style={
#                                     "backgroundColor": "#FFFFFF",
#                                     "color": "#6F4CFF",
#                                     "padding": "15px 30px",
#                                     "borderRadius": "50px",
#                                     "fontSize": "18px",
#                                     "fontWeight": "500",
#                                     "border": "none",
#                                 },
#                             ),
#                             dbc.Button(
#                                 "Learn More",
#                                 href="/learn-more",
#                                 style={
#                                     "backgroundColor": "transparent",
#                                     "color": "white",
#                                     "padding": "15px 30px",
#                                     "borderRadius": "50px",
#                                     "fontSize": "18px",
#                                     "fontWeight": "500",
#                                     "border": "2px solid white",
#                                 },
#                             ),
#                         ],
#                     ),
#                 ],
#             ),
#         ],
#     )


def create_learn_more_page():
    return html.Div(
        style={
            "minHeight": "100vh",
            "width": "100vw",
            "background": "linear-gradient(to right, white 190px, #f4f4f9 250px, #d6ccff 600px, #9b84ff 70%, #6F4CFF)",  # Match existing gradient
            "fontFamily": "Outfit",
            "display": "flex",
            "flexDirection": "column",
            "alignItems": "center",
            "padding": "50px 20px",
            "color": "#333333",  # Dark text for readability
        },
        children=[
            # Page Title
            html.H1(
                "What is PsySys?",
                style={
                    "fontSize": "48px",
                    "fontWeight": "bold",
                    "color": "#4A4A8D",
                    "marginBottom": "30px",
                },
            ),
            # Content Container
            html.Div(
                style={
                    "maxWidth": "800px",
                    "backgroundColor": "rgba(255, 255, 255, 0.8)",  # Semi-transparent white
                    "padding": "30px",
                    "borderRadius": "15px",
                    "boxShadow": "0px 4px 10px rgba(0, 0, 0, 0.1)",
                    "textAlign": "left",
                },
                children=[
                    # Text Content
                    html.P(
                        "PsySys is an innovative mental health platform designed to empower individuals with personalized insights, "
                        "interactive tools, and actionable data. Our mission is to bridge the gap between technology and emotional well-being, "
                        "helping users understand, monitor, and improve their mental health journey.",
                        style={"fontSize": "18px", "lineHeight": "1.6", "marginBottom": "20px", "fontWeight": 300},
                    ),
                    html.P(
                        "By leveraging advanced data analysis and visualization techniques, PsySys enables users to build and track their own "
                        "mental health maps, identify key factors, and collaborate with professionals or peers. Whether you're looking to better "
                        "understand your mental health dynamics or take actionable steps toward improvement, PsySys is here to guide you.",
                        style={"fontSize": "18px", "lineHeight": "1.6", "marginBottom": "20px"},
                    ),
                    # Images for Visual Appeal
                    html.Img(
                        src="/assets/mental-health-illustration.png",
                        style={
                            "width": "100%",
                            "marginBottom": "20px",
                            "borderRadius": "10px",
                            "boxShadow": "0px 2px 6px rgba(0, 0, 0, 0.1)",
                        },
                    ),
                    # Call-to-Action Buttons
                    html.Div(
                        style={"display": "flex", "gap": "20px", "justifyContent": "center"},
                        children=[
                            dbc.Button(
                                "Get Started",
                                href="/get-started",
                                style={
                                    "backgroundColor": "#6F4CFF",
                                    "color": "white",
                                    "padding": "15px 30px",
                                    "borderRadius": "50px",
                                    "fontSize": "18px",
                                    "fontWeight": "500",
                                    "border": "none",
                                },
                            ),
                            dbc.Button(
                                "Back to Home",
                                href="/",
                                style={
                                    "backgroundColor": "transparent",
                                    "color": "#6F4CFF",
                                    "padding": "15px 30px",
                                    "borderRadius": "50px",
                                    "fontSize": "18px",
                                    "fontWeight": "500",
                                    "border": "2px solid #6F4CFF",
                                },
                            ),
                        ],
                    ),
                ],
            ),
        ],
    )

# def create_landing_page():
#     return html.Div(
#         style={
#             "height": "100vh",
#             "width": "100vw",
#             "background": "linear-gradient(to bottom, white, #f4f4f9, #d6ccff, #9b84ff, #6F4CFF)",
#             "display": "flex",
#             "alignItems": "center",
#             "justifyContent": "center",
#             "position": "relative",
#             "fontFamily": "Outfit",
#             "color": "white",
#             "overflow": "hidden",
#             "marginLeft": "-12px"
#         },
#         children=[
#             # Layered Network Images from Bottom-Left
#             html.Div(
#                 style={
#                     "position": "absolute",
#                     "bottom": "-30%",
#                     "left": "-20%",
#                     "zIndex": "0",
#                 },
#                 children=[
#                     html.Img(
#                         src="/assets/network_2.png",
#                         style={
#                             "width": "600px",
#                             "opacity": "0.7",
#                             "transform": "rotate(15deg)",
#                             "animation": "move-glow-1 4s infinite alternate",
#                         },
#                     ),
#                 ],
#             ),
#             html.Div(
#                 style={
#                     "position": "absolute",
#                     "bottom": "-50%",
#                     "left": "10%",
#                     "zIndex": "0",
#                 },
#                 children=[
#                     html.Img(
#                         src="/assets/network_3.png",
#                         style={
#                             "width": "900px",
#                             "opacity": "0.5",
#                             "transform": "rotate(-10deg)",
#                             "animation": "move-glow-2 5s infinite alternate",
#                         },
#                     ),
#                 ],
#             ),
#             html.Div(
#                 style={
#                     "position": "absolute",
#                     "bottom": "-70%",
#                     "left": "5%",
#                     "zIndex": "0",
#                 },
#                 children=[
#                     html.Img(
#                         src="/assets/network_4.png",
#                         style={
#                             "width": "1200px",
#                             "opacity": "0.3",
#                             "transform": "rotate(10deg)",
#                             "animation": "move-glow-3 6s infinite alternate",
#                         },
#                     ),
#                 ],
#             ),
            
#             # Main Content (Centered)
#             html.Div(
#                 style={
#                     "position": "relative",
#                     "zIndex": "1",
#                     "textAlign": "center",
#                     "maxWidth": "800px",
#                     "color": "white",
#                     "margin": "0 auto",
#                 },
#                 children=[
#                     html.H1(
#                         "Welcome to PsySys",
#                         style={
#                             "fontSize": "60px",
#                             "fontWeight": "bold",
#                             "marginBottom": "20px",
#                             "color": "#4A4A8D",
#                             #"color": "white",
#                         },
#                     ),
#                     html.P(
#                         "Leveraging the network approach to psychopathology to empower patients.",
#                         style={
#                             "fontSize": "23px",
#                             "fontWeight": "300",
#                             "lineHeight": "1.6",
#                             "marginBottom": "30px",
#                             "color": "#4A4A8D",
#                         },
#                     ),
#                     # Call-to-Action Buttons
#                     html.Div(
#                         style={"display": "flex", "justifyContent": "center", "gap": "15px"},
#                         children=[
#                             dbc.Button(
#                                 #"Get Started",
#                                 "View Demo",
#                                 href="/get-started",
#                                 style={
#                                     "backgroundColor": "#6F4CFF",
#                                     "color": "white",
#                                     "padding": "15px 30px",
#                                     "borderRadius": "50px",
#                                     "fontSize": "18px",
#                                     "fontWeight": "500",
#                                     "border": "none",
#                                     "boxShadow": "0px 4px 6px rgba(0, 0, 0, 0.2)",
#                                 },
#                             ),
#                             dbc.Button(
#                                 "Learn More",
#                                 href="/learn-more",
#                                 style={
#                                     "backgroundColor": "transparent",
#                                     "color": "white",
#                                     "padding": "15px 30px",
#                                     "borderRadius": "50px",
#                                     "fontSize": "18px",
#                                     "fontWeight": "500",
#                                     "border": "2px solid white",
#                                     "boxShadow": "0px 4px 6px rgba(0, 0, 0, 0.1)",
#                                 },
#                             ),
#                         ],
#                     ),
#                 ],
#             ),
#         ],
#     )

def create_landing_page():
    return html.Div(
        style={
            "height": "100vh",
            "width": "100vw",
            "background": "linear-gradient(to bottom, white, #f4f4f9, #d6ccff, #9b84ff, #6F4CFF)",
            "display": "flex",
            "alignItems": "center",
            "justifyContent": "center",
            "position": "relative",
            "fontFamily": "Outfit",
            "color": "white",
            "overflow": "hidden",
            "marginLeft": "-12px"
        },
        children=[
            # Top-left network image
            html.Div(
                style={
                    "position": "absolute",
                    "top": "5%",
                    "left": "0%",
                    "zIndex": "0",
                },
                children=[
                    html.Img(
                        src="/assets/network_2.png",
                        style={
                            "width": "500px",
                            "opacity": "0.5",
                            "transform": "rotate(15deg)",
                        },
                    ),
                ],
            ),
            # Bottom-left network image
            html.Div(
                style={
                    "position": "absolute",
                    "bottom": "0%",
                    "left": "-10%",
                    "zIndex": "0",
                },
                children=[
                    html.Img(
                        src="/assets/network_3.png",
                        style={
                            "width": "600px",
                            "opacity": "0.6",
                            "transform": "rotate(-10deg)",
                        },
                    ),
                ],
            ),
            # Bottom-right network image
            html.Div(
                style={
                    "position": "absolute",
                    "bottom": "-10%",
                    "right": "-5%",
                    "zIndex": "0",
                },
                children=[
                    html.Img(
                        src="/assets/network_4.png",
                        style={
                            "width": "900px",
                            "opacity": "0.4",
                            "transform": "rotate(10deg)",
                        },
                    ),
                ],
            ),
            # Top-right network image
            html.Div(
                style={
                    "position": "absolute",
                    "top": "0%",
                    "right": "0%",
                    "zIndex": "0",
                },
                children=[
                    html.Img(
                        src="/assets/network_2.png",
                        style={
                            "width": "600px",
                            "opacity": "0.3",
                            "transform": "rotate(-15deg)",
                        },
                    ),
                ],
            ),
            # Gradient Overlay to clear center
            html.Div(
                style={
                    "position": "absolute",
                    "top": "0",
                    "left": "0",
                    "width": "100%",
                    "height": "100%",
                    "background": "radial-gradient(circle, rgba(255,255,255,0.7) 10%, transparent 60%)",
                    "zIndex": "0",
                },
            ),
            # Main Content (Centered)
            html.Div(
                style={
                    "position": "relative",
                    "zIndex": "1",
                    "textAlign": "center",
                    "maxWidth": "800px",
                    "color": "white",
                    "margin": "0 auto",
                },
                children=[
                    html.H1(
                        "Welcome to PsySys",
                        style={
                            "fontSize": "60px",
                            "fontWeight": "bold",
                            #"fontWeight": 500,
                            "marginBottom": "20px",
                            "color": "#4A4A8D",
                        },
                    ),
                    html.P(
                        "Leveraging the network approach to psychopathology to empower patients.",
                        style={
                            "fontSize": "23px",
                            "fontWeight": "300",
                            "lineHeight": "1.6",
                            "marginBottom": "30px",
                            "color": "#4A4A8D",
                        },
                    ),
                    # Call-to-Action Buttons
                    html.Div(
                        style={"display": "flex", "justifyContent": "center", "gap": "15px"},
                        children=[
                            dbc.Button(
                                "View Demo",
                                href="/psysys-demo",
                                style={
                                    "backgroundColor": "#6F4CFF",
                                    "color": "white",
                                    "padding": "15px 30px",
                                    "borderRadius": "50px",
                                    "fontSize": "18px",
                                    "fontWeight": "500",
                                    "border": "none",
                                    "boxShadow": "0px 4px 6px rgba(0, 0, 0, 0.2)",
                                },
                            ),
                            dbc.Button(
                                "Learn More",
                                href="/about",
                                style={
                                    "backgroundColor": "transparent",
                                    "color": "#6F4CFF",
                                    "padding": "15px 30px",
                                    "borderRadius": "50px",
                                    "fontSize": "18px",
                                    "fontWeight": "500",
                                    "border": "2px solid #6F4CFF",
                                    "boxShadow": "0px 4px 6px rgba(0, 0, 0, 0.1)",
                                },
                            ),
                        ],
                    ),
                ],
            ),
        ],
    )


def create_about(app, translation):
    return html.Div(
        style={
            "minHeight": "100vh",
            "width": "100vw",
            #"background": "linear-gradient(to right, white 190px, #f4f4f9 250px, #d6ccff 600px, #9b84ff 70%, #6F4CFF)",
            "background": "linear-gradient(to bottom, white, #f4f4f9, #d6ccff, #9b84ff, #6F4CFF)",
            "fontFamily": "Outfit",
            "padding": "50px 20px",
            "overflowX": "hidden",  # Prevent horizontal scrolling
            "marginLeft": "-12px"
        },
        children=[
            # Mission Statement
            # html.Div(
            #     style={
            #         "textAlign": "center",
            #         "padding": "20px",
            #         "marginBottom": "50px",
            #         "color": "#FFFFFF",
            #     },
            #     # children=[
            #     #     html.H2(
            #     #         "Share Knowledge. Empower People.",
            #     #         style={
            #     #             "fontSize": "48px",
            #     #             "fontWeight": "bold",
            #     #         },
            #     #     ),
            #     # ],
            # ),
            html.Div(style={"height": "105px"}),

            # Team Section
            html.Div(
                children=[
                    html.H3(
                        "Our Team",
                        #className="multi-color-text",
                        style={
                            "textAlign": "center",
                            "fontSize": "36px",
                            "color": "#4A4A8D",
                            #"color": "#6F4CFF",
                            "marginBottom": "30px",
                        },
                    ),
                    dbc.Row(
                        [
                            # Team Members
                            create_team_member(
                                app,
                                "Emily Campos Sindermann",
                                "DSC_5008.JPG",
                                #translation['freelance'],
                                "PsySys Lead & Developer",
                                translation['role_01'],
                            ),
                            create_team_member(
                                app,
                                "Denny Borsboom",
                                "profile_dennyborsboom.jpeg",
                                "Professor @ Psychological Methods, University of Amsterdam",
                                translation['role_02'],
                            ),
                            create_team_member(
                                app,
                                "Tessa Blanken",
                                "profile_tessablanken.jpeg",
                                "Assistant Professor @ Psychological Methods, University of Amsterdam",  
                                translation['role_03'],
                            ),
                            create_team_member(
                                app,
                                "Lars Klintwall",
                                "profile_larsklintwall.jpeg",
                                "Clinician & Post-Doc @ Clinical Neuroscience, Karolinska Institute",
                                translation['role_04'],
                            ),
                        ],
                        justify="center",
                        style={"gap": "30px"},  # Uniform spacing between team members
                    ),
                ],
                style={"marginBottom": "50px"},
            ),
            # Collaborators Section
            html.Div(
                children=[
                    html.H3(
                        "Collaborators",
                        style={
                            "textAlign": "center",
                            "fontSize": "36px",
                            "color": "#4A4A8D",
                            "marginBottom": "30px",
                        },
                    ),
                    dbc.Row(
                        [
                            create_team_member(
                                app, 
                                "Julian Burger",
                                "profile_julianburger.jpeg", 
                                "Post-Doc @ Yale School of Public Health",
                                translation['role_04']),
                            create_team_member(
                                app, 
                                "Mark Willems",
                                "mark_willems_2.jpeg", 
                                "Founder & CEO @ Birdt Health",
                                translation['role_04'],),
                            create_team_member(
                                app, 
                                "Felix Vogel",
                                "felix_vogel.jpeg", 
                                "Interim Professor @ University of Hamburg",
                                translation['role_04'],),
                        ],
                        justify="center",
                        style={"gap": "30px"},  # Consistent spacing between collaborators
                    ),
                ],
                style={"marginBottom": "50px"},
            ),
            # Supporters Section
            # html.Div(
            #     children=[
            #         html.H3(
            #             "Supporters",
            #             style={
            #                 "textAlign": "center",
            #                 "fontSize": "36px",
            #                 "color": "#4A4A8D",
            #                 "marginBottom": "30px",
            #             },
            #         ),
            #         dbc.Row(
            #             [
            #                 html.Div(
            #                     html.Img(src=app.get_asset_url('Amsterdamuniversitylogo.svg.png'), style=SUPPORTER_LOGO_STYLE),
            #                     style={"textAlign": "center"},
            #                 ),
            #                 html.Div(
            #                     html.Img(src=app.get_asset_url('birdt-health-logo.jpeg'), style=SUPPORTER_LOGO_STYLE),
            #                     style={"textAlign": "center"},
            #                 ),
            #                 html.Div(
            #                     html.Img(src=app.get_asset_url('another-supporter-logo.png'), style=SUPPORTER_LOGO_STYLE),
            #                     style={"textAlign": "center"},
            #                 ),
            #             ],
            #             justify="center",
            #             style={"gap": "30px"},  # Horizontal layout for supporters
            #         ),
            #     ],
            #     style={"marginBottom": "50px"},
            # ),

            # Supporters Section
            html.Div(
                children=[
                    html.H3(
                        "Supporters",
                        style={
                            "textAlign": "center",
                            "fontSize": "36px",
                            "color": "#4A4A8D",
                            "marginBottom": "30px",
                        },
                    ),
                    dbc.Row(
                        [
                            create_supporter(app, 'uva-logo-3.png', "Granted the PsySys project an Impact Grant of €25.000  in April 2024."),
                            create_supporter(app, 'dptv-logo.png', "Awarded the PsySys project with the master-research award 2024 endowed with €1000."),
                            create_supporter(app, 'zü-logo.webp', "Supported the improvement of the PsySys demo with usability feedback."),
                        ],
                        justify="center",
                        style={"gap": "30px"},  # Consistent spacing between supporters
                    ),
                ],
                style={"marginBottom": "50px"},
            ),

            # Contact Us Section
            html.Div(
                style={
                    "textAlign": "center",
                    "marginTop": "50px",
                    "position": "relative",
                },
                children=[
                    dbc.Button(
                        "Contact Us",
                        href="mailto:campos.sindermann@gmail.com?subject=Inquiry%20for%20PsySys%20App&",
                        style={
                            "backgroundColor": "transparent",
                            "color": "white",
                            "padding": "15px 30px",
                            "borderRadius": "50px",
                            "fontSize": "18px",
                            "fontWeight": "500",
                            "border": "2px solid white",
                            "boxShadow": "0px 4px 6px rgba(0, 0, 0, 0.2)"
                        },
                    ),
                ],
            ),
        ],
    )


# Helper Function for Team Member
def create_team_member(app, name, img, institution, role):
    return dbc.Col(
        html.Div(
            style={
                "textAlign": "center",
                "width": "200px",  # Fixed width ensures uniform spacing
                "margin": "0 auto",
            },
            children=[
                html.Img(
                    src=app.get_asset_url(img),
                    style={
                        "width": "160px",  # Increased size
                        "height": "160px",
                        "borderRadius": "50%",  # Circle images
                        "marginBottom": "10px",
                    },
                ),
                html.P(
                    name,
                    style={"fontWeight": 500, "color": "#4A4A8D", "fontSize": "19px"},
                ),
                html.P(institution, style={"color": "#black", "fontSize": "16px", "fontWeight": 300}),
                # html.P(role, style={"color": "#6c757d", "fontSize": "14px"}),
            ],
        ),
        width="auto",  # Dynamically adjust to fit content
    )


# Helper Function for Collaborator
# Helper Function for Supporter with Logo and Text
def create_supporter(app, img, description):
    return dbc.Col(
        html.Div(
            style={
                "textAlign": "center",
                "width": "230px",  # Consistent width for each supporter
                "margin": "0 auto",
            },
            children=[
                html.Img(
                    src=app.get_asset_url(img),
                    style={
                        "width": "200px",  # Adjust logo size
                        "height": "130px",  # Maintain aspect ratio
                        "borderRadius": "15px",  # Rounded edges
                        "boxShadow": "0 2px 4px rgba(0, 0, 0, 0.1)",  # Optional shadow
                        "marginBottom": "10px",
                    },
                ),
                html.P(
                    description,
                    style={
                        "fontSize": "16px",
                        "fontWeight": 300,
                        "color": "#black",  # Subtle gray text color
                        "marginTop": "5px",
                    },
                ),
            ],
        ),
        width="auto",  # Dynamically adjust to fit content
    )


# Styles
SUPPORTER_LOGO_STYLE = {
    "width": "120px",  # Slightly larger for visual balance
    "height": "120px",
    "borderRadius": "50%",  # Circular logos
}

COLLABORATOR_STYLE = {
    "width": "140px",
    "height": "140px",
    "borderRadius": "50%",  # Circular collaborator images
}

import dash_bootstrap_components as dbc
from dash import html


def create_output_page():
    # Helper function to create a single output box
    def create_output_box(image, tag, title, action, action_link):
        return html.Div(
            style={
                "width": "400px",
                "backgroundColor": "white",
                "borderRadius": "15px",
                "boxShadow": "0px 4px 10px rgba(0, 0, 0, 0.1)",
                "overflow": "hidden",
                "display": "flex",
                "flexDirection": "column",
            },
            children=[
                # Image Section
                html.Div(
                    style={"position": "relative"},
                    children=[
                        html.Img(
                            src=image,
                            style={
                                "width": "100%",
                                "height": "200px",
                                "objectFit": "cover",
                            },
                        ),
                        # Tag
                        html.Div(
                            tag,
                            style={
                                "position": "absolute",
                                "top": "10px",
                                "right": "10px",
                                "backgroundColor": "#6F4CFF",
                                "color": "white",
                                "padding": "5px 10px",
                                "borderRadius": "20px",
                                "fontSize": "12px",
                                "fontWeight": "bold",
                            },
                        ),
                    ],
                ),
                # Content Section
                html.Div(
                    style={
                        "padding": "15px",
                        "flex": "1",  # Ensure content takes up remaining space
                        "display": "flex",
                        "flexDirection": "column",
                        "justifyContent": "space-between",
                    },
                    children=[
                        # Title
                        html.H4(
                            title,
                            style={
                                "marginBottom": "10px",
                                "color": "#4A4A8D",
                                #"color": "black",
                                "fontSize": "18px",
                                #"fontWeight": "bold",
                                "fontWeight": 400
                            },
                        ),
                        # Action Link
                        html.A(
                            action,
                            href=action_link,
                            style={
                                "fontSize": "14px",
                                "color": "#6F4CFF",
                                # "fontWeight": "bold"
                                "fontWeight": 500,
                                "textDecoration": "none",
                            },
                        ),
                    ],
                ),
            ],
        )

    # Main Page Layout
    return html.Div(
        style={
            "width": "100vw",
            "minHeight": "100vh",
            "background": "linear-gradient(to bottom, white, #f4f4f9, #d6ccff, #9b84ff, #6F4CFF)",
            "padding": "50px",
            "fontFamily": "Outfit",
            "marginLeft": "-12px"
        },
        children=[
            # Header Section
            # html.Div(style={"height": "150px"}),
            html.Div(style={"height": "100px"}),

            html.Div(
                "Output",
                style={
                    "textAlign": "center",
                    "fontSize": "36px",
                    "color": "#4A4A8D",
                    #"color":"black",
                    "marginBottom": "40px",
                    "fontWeight": "500",
                },
            ),
            # Outputs Section
            dbc.Container(
                [
                    # First Row
                    dbc.Row(
                        [
                            dbc.Col(
                                create_output_box(
                                    "/assets/master_thesis.jpg",
                                    "MASTER THESIS",
                                    #"It's All About Perspective: Introducing PsySys as a Digital Network-Informed Psychoeducation for Depression",
                                    "Master Thesis",
                                    "Download >>",
                                    "/path/to/master-thesis",
                                ),
                                width=4,
                            ),
                            dbc.Col(
                                create_output_box(
                                    "/assets/dptv_bild.jpg",
                                    "ARTICLE",
                                    "Article",
                                    "Read more >>",
                                    "/path/to/article",
                                ),
                                width=4,
                            ),
                            dbc.Col(
                                create_output_box(
                                    "/assets/blog.jpg",
                                    "BLOG",
                                    "Blog Article",
                                    "Read more >>",
                                    "/path/to/blog-article",
                                ),
                                width=4,
                            ),
                        ],
                        justify="center",
                        className="mb-4",
                    ),
                    # Second Row
                    dbc.Row(
                        [
                            dbc.Col(
                                create_output_box(
                                    "/assets/system_thinking.jpg",
                                    "BLOG",
                                    "System Thinking",
                                    "Read more >>",
                                    "/path/to/system-thinking",
                                ),
                                width=4,
                            ),
                            dbc.Col(
                                create_output_box(
                                    "/assets/complex_systems.jpg",
                                    "BLOG",
                                    "Complex Systems",
                                    "Read more >>",
                                    "/path/to/complex-systems",
                                ),
                                width=4,
                            ),
                            dbc.Col(
                                create_output_box(
                                    "/assets/paper.jpg",
                                    "PAPER",
                                    "Paper (Incoming)",
                                    "Read more >>",
                                    "/path/to/paper",
                                ),
                                width=4,
                            ),
                        ],
                        justify="center",
                    ),
                ]
            ),
        ],
    )
