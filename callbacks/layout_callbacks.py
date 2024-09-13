import dash, json

from app import app
from dash import html, Input, Output, State, ALL, MATCH
from constants import factors, stylesheet, hidden_style, visible_style
from functions.page_content import (generate_step_content, create_mental_health_map_tab, create_tracking_tab, 
                                    create_about)
from functions.map_build import (map_add_factors, map_add_chains, map_add_cycles)
from functions.map_style import (graph_color)

# from functions import (map_add_factors, graph_color, map_add_chains, map_add_cycles, generate_step_content,
#                        create_mental_health_map_tab, create_tracking_tab, create_about)

# Display the page & next/back button based on current step 
def update_page_and_buttons(pathname, edit_map_data, current_step_data, session_data, color, sizing, 
                            track_data, map_store, custom_color_data):
    
    step = current_step_data.get('step', 0)  # Default to step 0 if not found

    # Default button states
    content = None
    back_button_style = hidden_style
    next_button_style = visible_style
    next_button_text = html.I(className="fas fa-solid fa-angle-right")

    # Update content and button states based on the pathname and step
    if pathname == '/':
        # Check the step and update accordingly
        if step == 0:
            content = generate_step_content(step, session_data)   
        elif step == 1:
            content = generate_step_content(step, session_data)
        elif 2 <= step <= 4:
            content = generate_step_content(step, session_data)
            back_button_style = visible_style            
            next_button_style = visible_style         
        elif step == 5:
            content = generate_step_content(step, session_data)
            back_button_style = visible_style           
            next_button_text = html.I(className="fas fa-solid fa-forward")      

    elif pathname == "/my-mental-health-map":
        content = create_mental_health_map_tab(edit_map_data, color, sizing, custom_color_data)
        back_button_style = hidden_style
        next_button_style = hidden_style

    elif pathname == "/track-my-mental-health-map":
        content = create_tracking_tab(track_data)
        back_button_style = hidden_style
        next_button_style = hidden_style

    elif pathname == "/about":
        content = create_about(app)
        back_button_style = hidden_style
        next_button_style = hidden_style

    # elif pathname == "/blog":
    #     content = def_blog_page()
    #     back_button_style = hidden_style
    #     next_button_style = hidden_style

    elif content is None:
        content = html.Div("Page not found")

    return content, back_button_style, next_button_style, next_button_text

# Update current step based on next/back button clicks
def update_step(back_clicks, next_clicks, current_step_data):
    # Initialize click counts to 0 if None
    back_clicks = back_clicks or 0
    next_clicks = next_clicks or 0

    # Use callback_context to determine which input has been triggered
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    if "back-button.n_clicks" in changed_id:
        # Decrement the step, ensuring it doesn't go below 0
        current_step_data['step'] = max(current_step_data['step'] - 1, 0)
    elif "next-button.n_clicks" in changed_id:
        # Increment the step, if it reaches the max step reset to 0
        if current_step_data['step'] >= 5:
            current_step_data['step'] = 0
        else:
            current_step_data['step'] += 1

    return current_step_data

# Update session data based on user input
def update_hidden_div(values):
    return json.dumps(values)

# Update session-data (dropdowns) based on hidden Div
def update_session_data(n_clicks, json_values, session_data, current_step_data, severity_scores):

    step = current_step_data.get('step')
    values = json.loads(json_values) if json_values else []

    if len(values) == 1:
        if step == 1:
            session_data = map_add_factors(session_data, values[0], severity_scores)

    if n_clicks: 
        if len(values) == 1:
            if step == 4:
                session_data['dropdowns']['target']['value'] = values[0]
                graph_color(session_data, severity_scores)

        elif len(values) == 2:
            if step == 2: 
                session_data = map_add_chains(session_data, values[0], values[1])
            elif step == 3: 
                session_data = map_add_cycles(session_data, values[0], values[1])

    return session_data

# Update session data based on initial factor selection
def dropdown_step5_init(value, session_data):
    if session_data['add-node'] == []:
        session_data['add-node'] = value
    return session_data

# Reset session data & severity data at "Redo" (step 0)
def reset(current_step_data):
    if current_step_data['step'] == 0:
        data = {
            'dropdowns': {
                'initial-selection': {'options': [{'label': factor, 'value': factor} for factor in factors], 
                                      'value': None},
                'chain1': {'options': [], 'value': None},
                'chain2': {'options': [], 'value': None},
                'cycle1': {'options': [], 'value': None},
                'cycle2': {'options': [], 'value': None},
                'target': {'options': [], 'value': None},
            },
            'elements': [],
            'edges': [],
            'add-nodes': [],
            'add-edges': [],
            'stylesheet': stylesheet,
            'annotations': []
        }
        return (data, {}) 
    else:
        return (dash.no_update, dash.no_update)

# Register the callbacks
def register_layout_callbacks(app):

    app.callback(
        [Output('page-content', 'children'),
        Output('back-button', 'style'),
        Output('next-button', 'style', allow_duplicate=True),
        Output('next-button', 'children')],
        [Input('url', 'pathname'),
        Input('edit-map-data', 'data'),  
        Input('current-step', 'data')],
        [State('session-data', 'data'),
        State('color_scheme', 'data'),
        State('sizing_scheme', 'data'),
        State('track-map-data', 'data'),
        State('comparison', 'data'), 
        State('custom-color', 'data')],
        prevent_initial_call=True
    )(update_page_and_buttons)

    app.callback(
        Output('current-step', 'data'),
        [Input('back-button', 'n_clicks'),
        Input('next-button', 'n_clicks')],
        [State('current-step', 'data')]
    )(update_step)

    app.callback(
        Output('hidden-div', 'children', allow_duplicate=True),
        Input({'type': 'dynamic-dropdown', 'step': ALL}, 'value'),
        prevent_initial_call=True
    )(update_hidden_div)

    app.callback(
        Output('session-data', 'data'),
        [Input('next-button', 'n_clicks'),
        Input('hidden-div', 'children')],
        [State('session-data', 'data'),
        State('current-step', 'data'),
        State('severity-scores', 'data')]
    )(update_session_data)

    app.callback(
        Output('session-data', 'data', allow_duplicate=True),
        Input('factor-dropdown', 'value'),
        State('session-data', 'data'),
        prevent_initial_call=True
    )(dropdown_step5_init)

    app.callback(
        [Output('session-data', 'data', allow_duplicate=True),
        Output('severity-scores', 'data', allow_duplicate=True)],
        Input('current-step', 'data'),
        prevent_initial_call=True
    )(reset)
