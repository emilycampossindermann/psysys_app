import dash, json, base64, re
import plotly.graph_objects as go

from app import app
from dash import dcc, Input, Output, State, ALL, MATCH, callback_context
from functions.map_style import (apply_severity_size_styles, apply_uniform_style)
from functions.descriptive_plots import (current_centrality_plot, prepare_graph_data)

# from functions import (apply_severity_size_styles, current_centrality_plot, prepare_graph_data, 
#                        apply_uniform_style)

# Callback - NETWORK COMPARISON: Network comparison file upload
def upload_tracking_graph(contents, existing_marks, current_max, current_value, graph_data, map_store, track_data, stylesheet):
    new_elements = graph_data
    print("triggered_upload")
    if contents:

        content_type, content_string = contents.split(',')
        decoded = base64.b64decode(content_string)
        data = json.loads(decoded.decode('utf-8'))  # Assuming JSON file, adjust as needed

        
        new_elements = data.get('elements', [])
        style = data.get('stylesheet', [])
        #edge_strength = data.get['edge-data', []]

        severity = data.get('severity-scores', [])
        stylesheet_new = stylesheet

        # Extract filename from the contents object
        filename = data['date']
        #match = re.search(r"(\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2})", filename)
        match = re.search(r"(\d{2}/\d{2}/\d{2}-\d{2}:\d{2})", filename)
        
        if match:
            date_time = match.group(1)
            
            # Update marks if date/time not already in the timeline
            if date_time not in existing_marks.values():
                max_val = current_max + 1
                existing_marks[max_val] = date_time

                # Set the timeline slider to the new date/time position
                current_value = max_val

                # Add to map_store
                map_store[filename] = {}
                #map_store[filename] = {'elements': new_elements}

                # Update track_data
                track_data['timeline-max'] = max_val
                track_data['timeline-max'] = max_val
                track_data['timeline-marks'] = existing_marks

                map_store[filename] = {'elements': new_elements, 
                                       'stylesheet': style}


        return existing_marks, current_value, current_value, new_elements, map_store, track_data

    return existing_marks, current_max, current_value, new_elements, map_store, track_data

# Callback - NETWORK COMPARISON: Network comparison timeline navigation
# When user navigates across timeline
# Select file in dict that correspond to chosen date + time
# Feed in this file into dummy cytoscape 
def update_cytoscape_elements(selected_value, marks, comparison_data, session_data, severity_scores):
    selected_date = None
    
    if comparison_data is not None:
        label = marks.get(str(selected_value))  # Fetch label based on the slider's value

        if label in comparison_data:  # Check if the label exists in comparison_data keys
            selected_date = label

        if selected_date is not None:
            if selected_date != "PsySys":
                elements = comparison_data[selected_date]['elements']
                stylesheet = comparison_data[selected_date].get('stylesheet', [])
            else:
                elements = comparison_data[selected_date]['elements']
                stylesheet = apply_severity_size_styles("Severity", session_data['stylesheet'], severity_scores, session_data['stylesheet'])

            return elements, stylesheet

    return [], []

# Callback - NETWORK COMPARISON: Populate tracking graph with PsySys map
def update_track(session_data, track_data, map_store):
    track_data['elements'] = session_data['elements']
    track_data['stylesheet'] = session_data['stylesheet']

    map_store['PsySys'] = {'elements': session_data['elements'], 'stylesheet': session_data['stylesheet']}
    
    return track_data, map_store

# Callback - NETWORK COMPARISON: Delete current map from map store & mark & reduce max_value
def delete_current_map(n_clicks, existing_marks, current_max, current_value, graph_data, map_store, track_data):
    if n_clicks:
        selected_date = None

        existing_marks = {int(k): v for k, v in existing_marks.items()}
        current_value = int(current_value)

        for key, value in existing_marks.items():
            if key == current_value:
                selected_date = value
                break

        if selected_date and selected_date in map_store:
            del map_store[selected_date]
            existing_marks = {k: v for k, v in existing_marks.items() if v != selected_date}

            if current_value > current_max:
                current_max = current_value

            if current_value == current_max:
                current_value -= 1

            new_marks = {}
            for key, value in existing_marks.items():
                if key > current_value:
                    new_marks[key - 1] = value
                else:
                    new_marks[key] = value

            current_max -= 1

            # Set current_value to 1 if no marks are left or if PsySys was deleted
            current_value = 1 if not new_marks else current_value

            track_data['timeline-marks'] = new_marks
            track_data['timeline-max'] = current_max
            track_data['timeline-value'] = current_value

            return new_marks, current_max, current_value, map_store, track_data

        track_data['timeline-marks'] = existing_marks
        track_data['timeline-max'] = current_max
        track_data['timeline-value'] = current_value

    return existing_marks, current_max, current_value, map_store, track_data

# Callback - NETWORK COMPARISON: Store current mode
def set_editing_mode(clicks_mode1, clicks_mode2, clicks_mode3, clicks_mode4, edit_map_data, elements):
    ctx = dash.callback_context
    triggered_id = ctx.triggered[0]['prop_id'].split('.')[0]
    
    if triggered_id == 'mode-1':
        editing_mode_data = "mode-1"
    elif triggered_id == 'mode-2':
        editing_mode_data = "mode-2"
    elif triggered_id == 'mode-3':
        editing_mode_data = "mode-3"
    elif triggered_id == 'mode-4':
        editing_mode_data = "mode-4"
    
    else:
        editing_mode_data = "unknown"

    return editing_mode_data

# Callback - NODE COMPARISON: Plotting mode switch 
def update_plotting_mode(current_clicks, overall_clicks, current_mode):
    ctx = dash.callback_context

    if not ctx.triggered:
        return current_mode, True if current_mode == 'current' else False, True if current_mode == 'overall' else False  # No change if no button has been clicked
    
    button_id = ctx.triggered[0]['prop_id'].split('.')[0]
    
    if button_id == 'plot-current':
        new_mode = 'current'
    elif button_id == 'plot-overall':
        new_mode = 'overall'
    else:
        new_mode = current_mode

    return new_mode, new_mode == 'current', new_mode == 'overall'

# Callback- NETWORK COMPARISON: Create centrality plot
def update_graph(selected_map, current_mode, comparison_data, track_data, marks):
    if current_mode == "current":
        if selected_map is None or comparison_data is None or marks is None:
            return go.Figure()  # Return an empty figure if no data is available
        
        fig = current_centrality_plot(track_data, comparison_data, selected_map, marks)
        
        if fig:
            return fig
        
        return go.Figure() 
    
    else: 

        x, y = prepare_graph_data(comparison_data)

        # Check if 'PsySys' is in marks
        if 'PsySys' not in marks.values():
            # Filter out 'PsySys' related data from x and y
            if "PsySys" in x:
                index_to_remove = x.index("PsySys")

                del x[index_to_remove]
                del y[-1]
            
            else: 
                pass

        # Extract unique network elements (keys from dictionaries in y)
        all_elements = set()
        for network_dict in y:
            if isinstance(network_dict, dict):
                all_elements.update(network_dict.keys())

        fig = go.Figure()
        
        # Add a trace for each network element
        for element in all_elements:
            element_values = []
            for network_dict in y:
                element_values.append(network_dict.get(element, None))  # Use None for missing values
            
            fig.add_trace(go.Scatter(
                x=x,  # Network labels (e.g., timestamps)
                #y=adjust_duplicates(element_values),
                y=element_values,
                mode='lines+markers',
                name=element
            ))
            
        fig.update_layout(
            title='Overall Factor Influence',
            #xaxis_title='Network',
            yaxis_title='Average Connectedness',
            template='plotly_white',
        )
        return fig
    
# Callback: Open plot information modal 
def plot_info(n_clicks, is_open):
    if n_clicks:
        return not is_open
    return is_open

# Callback: Blur background when information modal is open 
def toggle_blur(is_open):
    if is_open:
        return 'blur'
    return 'no-blur'

# Callback: Populate plot information modal 
def populate_plot_modal(current_mode):
    if current_mode == 'current':
        return 'The figure shows the number of in-coming and out-going links for each factor in the map. Factors with many out-going links have a lot of influence on the map. Factors with many in-coming links are strongly influenced by the other factors in the map.'
    elif current_mode == 'overall':
        return 'The figure shows the average influence (combination of in-coming and out-gonig links) for each factor in each of the included maps. Here you can examine how the factors influence change across the maps.'

# Callback - NETWORK COMPARISON: Toggle uniform style for network maps
def update_stylesheet_02(uniform_switch, selected_value, marks, comparison_data, session_data, severity_scores):
    selected_date = None
    
    if comparison_data is not None:
        label = marks.get(str(selected_value))  # Fetch label based on the slider's value

        if label in comparison_data:  # Check if the label exists in comparison_data keys
            selected_date = label

        if selected_date is not None:
            elements = comparison_data[selected_date]['elements']
            stylesheet = comparison_data[selected_date].get('stylesheet', [])

            if uniform_switch and 0 in uniform_switch:  # Uniform switch is on
                uniform_color = '#9CD3E1'
                stylesheet = apply_uniform_style(elements, severity_scores, uniform_color, stylesheet)
            else:  # Uniform switch is off
                if selected_date == "PsySys":
                    stylesheet = apply_severity_size_styles("Severity", session_data['stylesheet'], severity_scores, session_data['stylesheet'])
                else:
                    stylesheet = comparison_data[selected_date].get('stylesheet', [])

            return stylesheet, elements

    return [], []

# Show annotations modal when clicking on edge or node
def display_annotation_modal(tapNodeData, tapEdgeData, annotation_data, is_open):
    print("triggered_annotation_show")
    ctx = callback_context
    triggered_id = ctx.triggered[0]['prop_id'].split('.')[0]  # Identify which input triggered the callback

    # Determine if a node or edge was clicked
    if tapNodeData:
        print("it's a node")
        node_id = tapNodeData['id']
        # Fetch the annotation for the clicked node from the annotation store
        # annotation = annotation_data.get('nodes', {}).get(node_id, "No annotation for this node.")
        return True, f"{annotation_data.get(node_id, {})}"  # Open modal and display annotation

    elif tapEdgeData:
        print("it's an edge")
        edge_id = tapEdgeData['id']
        # Fetch the annotation for the clicked edge from the annotation store
        annotation = annotation_data.get('edges', {}).get(edge_id, "No annotation for this edge.")
        return True, f"Edge Annotation: {annotation}"  # Open modal and display annotation

    # If no element is clicked, close the modal or keep it closed
    return False, dash.no_update


def register_comparison_callbacks(app):

    app.callback(
        [Output('timeline-slider', 'marks'), 
        Output('timeline-slider', 'max'), 
        Output('timeline-slider', 'value'),
        Output('track-graph', 'elements'),
        Output('comparison', 'data'),
        Output('track-map-data', 'data')],
        Input('upload-graph-tracking', 'contents'), 
        [State('timeline-slider', 'marks'), 
        State('timeline-slider', 'max'),
        State('timeline-slider', 'value'),
        State('track-graph', 'elements'),
        State('comparison', 'data'),
        State('track-map-data', 'data'),
        State('track-graph', 'stylesheet')]
    )(upload_tracking_graph)

    app.callback(
        [Output('track-graph', 'elements', allow_duplicate=True),
        Output('track-graph', 'stylesheet')],
        [Input('timeline-slider', 'value')],
        [State('timeline-slider', 'marks'),
        State('comparison', 'data'),
        State('session-data', 'data'),
        State('severity-scores', 'data')],
        prevent_initial_call=True
    )(update_cytoscape_elements)

    app.callback(
        [Output('track-map-data', 'data', allow_duplicate=True),
        Output('comparison', 'data', allow_duplicate=True)],
        Input('session-data', 'data'),
        [State('track-map-data', 'data'),
        State('comparison', 'data')],
        prevent_initial_call=True
    )(update_track)

    app.callback(
        [Output('timeline-slider', 'marks', allow_duplicate=True),
        Output('timeline-slider', 'max', allow_duplicate=True),
        Output('timeline-slider', 'value', allow_duplicate=True),
        Output('comparison', 'data', allow_duplicate=True),
        Output('track-map-data', 'data', allow_duplicate=True)],
        Input('delete-tracking-map', 'n_clicks'),
        [State('timeline-slider', 'marks'),
        State('timeline-slider', 'max'),
        State('timeline-slider', 'value'),
        State('track-graph', 'elements'),
        State('comparison', 'data'),
        State('track-map-data', 'data')],
        prevent_initial_call=True
    )(delete_current_map)

    app.callback(
        Output('editing-mode', 'data'),
        #Output('edit-map-data', 'data', allow_duplicate=True)],
        [Input('mode-1', 'n_clicks'), Input('mode-2', 'n_clicks'), Input('mode-3', 'n_clicks'), Input('mode-4', 'n_clicks')],
        [State('edit-map-data', 'data'), 
        State('my-mental-health-map', 'elements')],
        prevent_initial_call=True
    )(set_editing_mode)

    app.callback(
        [Output('plot-mode', 'data'),
        Output('plot-current', 'active'),
        Output('plot-overall', 'active')],
        [Input('plot-current', 'n_clicks'),
        Input('plot-overall', 'n_clicks')],
        [State('plot-mode', 'data')]
    )(update_plotting_mode)

    app.callback(
        Output('centrality-plot', 'figure'),
        #Output('graph-container', 'style'),
        #Output('data-ready', 'data')],
        [Input('timeline-slider', 'value'),
        Input('plot-mode', 'data')],
        [State('comparison', 'data'),
        State('track-map-data', 'data'), 
        State('timeline-slider', 'marks')],
        # State('timeline-slider', 'value')]
    )(update_graph)

    app.callback(
        Output('modal-plot', 'is_open'),
        [Input('help-plot', 'n_clicks')],
        [State('modal-plot', 'is_open')],
    )(plot_info)

    app.callback(
        Output('tracking-wrapper', 'className'),
        [Input('modal-plot', 'is_open')],
    )(toggle_blur)

    app.callback(
        Output('modal-plot-body', 'children'),
        [Input('plot-mode', 'data')]
    )(populate_plot_modal)
    
    app.callback(
        [Output('track-graph', 'stylesheet', allow_duplicate=True),
        Output('track-graph', 'elements', allow_duplicate=True)],
        [Input('uniform-switch', 'value'),
        Input('timeline-slider', 'value')],
        [State('timeline-slider', 'marks'),
        State('comparison', 'data'),
        State('session-data', 'data'),
        State('severity-scores', 'data')],
        prevent_initial_call=True
    )(update_stylesheet_02)

    app.callback(
        [Output('modal-annotation', 'is_open'),  # Controls modal visibility
         Output('modal-notes', 'children')],  # Updates modal content with annotation
         [Input('track-graph', 'tapNodeData'), 
          Input('track-graph', 'tapEdgeData')], 
         [State('annotation-data', 'data'),  # State to access stored annotations
          State('modal-annotation', 'is_open')],  # State to check current modal status
    )(display_annotation_modal)