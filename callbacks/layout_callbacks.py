import dash, json, time

from app import app
from dash import html, Input, Output, State, ALL, MATCH
from constants import factors, stylesheet, hidden_style, visible_style, translations, factor_translation_map
from functions.map_build import (map_add_factors, map_add_chains, map_add_cycles)
from functions.map_style import (graph_color)
from functions.page_content import (generate_step_content, create_mental_health_map_tab, create_tracking_tab, create_about)

# Translate PsySys factors 
def update_factors_based_on_language(selected_language, session_data, edit_map_data):
    # Initialize dropdowns if they don't exist in session_data or edit_map_data
    session_data['dropdowns'] = session_data.get('dropdowns', {'initial-selection': {'options': [], 'value': []}})
    edit_map_data['dropdowns'] = edit_map_data.get('dropdowns', {'initial-selection': {'options': [], 'value': []}})
    
    # Get the translation dictionary based on the selected language
    translation = translations.get(selected_language, translations['en'])
    
    reverse_translation_map = {v: k for k, v in factor_translation_map.items()}

    # Retrieve current selected factors, defaulting to an empty list if None
    selected_factors = session_data['dropdowns']['initial-selection'].get('value', [])

    # Translate the selected factors
    if selected_language == 'en':
        translated_selected_factors = [reverse_translation_map.get(factor, factor) for factor in selected_factors]
    else:
        translated_selected_factors = [factor_translation_map.get(factor, factor) for factor in selected_factors]

    # Update the dropdown options and selected values
    options = [{'label': factor, 'value': factor} for factor in translation['factors']]

    # Update session_data and edit_map_data dropdowns
    session_data['dropdowns']['initial-selection']['options'] = options
    session_data['dropdowns']['initial-selection']['value'] = translated_selected_factors

    edit_map_data['dropdowns']['initial-selection']['options'] = options
    edit_map_data['dropdowns']['initial-selection']['value'] = translated_selected_factors

    return session_data, edit_map_data

# Display the page & next/back button based on current step 
def update_page_and_buttons(pathname, edit_map_data, current_step_data, language, session_data, color, sizing, 
                            track_data, map_store, custom_color_data):
    
    step = current_step_data.get('step', 0)  # Default to step 0 if not found

    # Default button states
    content = None
    back_button_style = hidden_style
    next_button_style = visible_style
    redirect_button_style = hidden_style
    next_button_text = html.I(className="fas fa-solid fa-angle-right")

    translation = translations.get(language, translations['en'])

    # Update content and button states based on the pathname and step
    if pathname == '/':
        # Check the step and update accordingly
        if step == 0:
            content = generate_step_content(step, session_data, translation)   
        elif step == 1:
            content = generate_step_content(step, session_data, translation)
        elif 2 <= step <= 4:
            content = generate_step_content(step, session_data, translation)
            back_button_style = visible_style            
            next_button_style = visible_style         
        elif step == 5:
            content = generate_step_content(step, session_data, translation)
            back_button_style = visible_style           
            next_button_text = html.I(className="fas fa-solid fa-trash", style={'color': '#E57373'}) 
            redirect_button_style = visible_style    

    elif pathname == "/my-mental-health-map":
        content = create_mental_health_map_tab(edit_map_data, color, sizing, custom_color_data, translation)
        back_button_style = hidden_style
        next_button_style = hidden_style

    elif pathname == "/track-my-mental-health-map":
        content = create_tracking_tab(track_data, translation)
        back_button_style = hidden_style
        next_button_style = hidden_style

    elif pathname == "/about":
        content = create_about(app, translation)
        back_button_style = hidden_style
        next_button_style = hidden_style

    elif content is None:
        content = html.Div("Page not found")

    return content, back_button_style, next_button_style, next_button_text, redirect_button_style

# Update current step based on next/back button clicks
def update_step(back_clicks, next_clicks, current_step_data):
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
    try:
        return json.dumps(values)
    except TypeError:
        return json.dumps(["Serialization error with values"])

def update_session_data(n_clicks, json_values, session_data, current_step_data, severity_scores):
    step = current_step_data.get('step')
    values = json.loads(json_values) if json_values else []

    # Ensure 'dropdowns' and other keys exist in session_data
    session_data.setdefault('dropdowns', {
        'initial-selection': {'options': [], 'value': None},
        'chain1': {'options': [], 'value': None},
        'chain2': {'options': [], 'value': None},
        'cycle1': {'options': [], 'value': None},
        'cycle2': {'options': [], 'value': None},
        'target': {'options': [], 'value': None},
    })

    # Store severity scores
    session_data['severity'] = severity_scores or {}

    # Rest of your logic
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

    # Ensure session_data remains JSON-compatible
    try:
        json.dumps(session_data)
    except TypeError:
        session_data = {"error": "Session data serialization issue"}

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
                                      'value': []},
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

# Re-direct user to edit tab & populate graph with PsySys map when user clicks on redirect button end of PsySys
def redirect_edit(n_clicks):
    if n_clicks:
        return "/my-mental-health-map"

# Extract likert scale severity 
def extract_severity_scores(severity_values, current_severity_scores, slider_ids, session_data):
    factor_selection = session_data['dropdowns']['initial-selection']['value']
    
    if factor_selection is None:
        return dash.no_update
    
    if current_severity_scores is None:
        current_severity_scores = {}

    # Ensure severity_values and slider_ids are not None
    if severity_values is None or slider_ids is None:
        return current_severity_scores

    # Remove any factors from current_severity_scores that are not in the Likert scales
    current_severity_scores = {factor: score for factor, score in current_severity_scores.items() if factor in factor_selection}

    # Extract factor names and update their values in the severity scores
    for value, slider_id in zip(severity_values, slider_ids):
        factor = slider_id['factor']  # Extract the factor name from the slider id
        current_severity_scores[factor] = value

    return current_severity_scores

# Show suicide hotline message if user selects suicidal thoughts 
def show_suicide_prevention_message(selected_factors):
    if 'Suicidal thoughts' in selected_factors or 'Suizidgedanken' in selected_factors:
        return {"color": "#516395", "visibility": "visible"}  # Show the message
    return {"color": "#516395", "visibility": "hidden"}  # Keep the space but hide the text

# Limit dropdown for factor selection to 10
def limit_factor_selection(selection):
    if selection and len(selection) > 15:
        return selection[:15]
    return selection

# Set loading dcc.Store to true when user navigates to different tab
# def turn_loading_true(pathname):
#     return True 

# Simulate page load (3 sec) & show loading circle
# def simulate_page_load(pathname):
#     time.sleep(3)  # Simulating delay in content load
#     content = ""
#     return False, content

# Disable/enable the navlinks based on the loading-state
# def toggle_nav_links(loading):
#     # If loading is True, disable all navlinks, else enable them
#     return [loading, loading, loading, loading]

# Register the callbacks
def register_layout_callbacks(app):

    app.callback(
        [Output('session-data', 'data', allow_duplicate=True),
        Output('edit-map-data', 'data', allow_duplicate=True)],
        [Input('language-dropdown', 'value')],
        [State('session-data', 'data'),
        State('edit-map-data', 'data')],
        prevent_initial_call=True
    )(update_factors_based_on_language)

    app.callback(
        [Output('page-content', 'children'),
        Output('back-button', 'style'),
        Output('next-button', 'style', allow_duplicate=True),
        Output('next-button', 'children'),
        Output('go-to-edit', 'style')],
        [Input('url', 'pathname'),
        Input('edit-map-data', 'data'),  
        Input('current-step', 'data'),
        Input('language-dropdown', 'value')],
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

    app.callback(
         Output('severity-scores', 'data'),  # Update the stored severity scores
        [Input({'type': 'likert-scale', 'factor': ALL}, 'value')],
        [State('severity-scores', 'data'),  # Current severity scores
        State({'type': 'likert-scale', 'factor': ALL}, 'id'), 
        State('session-data', 'data')]  # Get the IDs (factors) of all scales
    )(extract_severity_scores)

    app.callback(
        Output('suicide-prevention-hotline', 'style'),
        [Input({'type': 'dynamic-dropdown', 'step': 1}, 'value')]
    )(show_suicide_prevention_message)

    app.callback(
        Output('url', 'pathname'),
        Input('go-to-edit', 'n_clicks')
    )(redirect_edit)

    app.callback(
        Output({'type': 'dynamic-dropdown', 'step': 1}, 'value'),
        Input({'type': 'dynamic-dropdown', 'step': 1}, 'value')
    )(limit_factor_selection)

    # app.callback(
    #     Output("loading-state", "data"),
    #     [Input("url", "pathname")]
    # )(turn_loading_true)

    # app.callback(
    #     [Output("loading-state", "data", allow_duplicate=True),
    #      Output('tab-content', 'children')],
    #     [Input("url", "pathname")],
    #     prevent_initial_call=True
    # )(simulate_page_load)

    # app.callback(
    #     [Output("Psychoeducation", "disabled"),
    #     Output("Edit My Map", "disabled"),
    #     Output("Compare My Map", "disabled"),
    #     Output("About Us", "disabled")],
    #     [Input("loading-state", "data")]
    # )(toggle_nav_links)

