import dash, json, base64, re
import plotly.graph_objects as go
import numpy as np

from app import app
from dash import dcc, Input, Output, State, ALL, MATCH, callback_context
from functions.map_style import (apply_severity_size_styles, apply_uniform_style)
from functions.descriptive_plots import (current_centrality_plot, prepare_graph_data)

# from functions import (apply_severity_size_styles, current_centrality_plot, prepare_graph_data, 
#                        apply_uniform_style)

# Callback - NETWORK COMPARISON: Network comparison file upload
def upload_tracking_graph(contents, existing_marks, current_max, current_value, graph_data, map_store, track_data, stylesheet, edge_data):
    new_elements = graph_data
    filename = None
    if contents:

        content_type, content_string = contents.split(',')
        decoded = base64.b64decode(content_string)
        data = json.loads(decoded.decode('utf-8'))  # Assuming JSON file, adjust as needed

        
        new_elements = data.get('elements', [])
        style = data.get('stylesheet', [])
        #edge_strength = data.get['edge-data', []]

        severity = data.get('severity-scores', {})
        annotations = data.get('annotations', [])
        print(annotations)
        print("HERE")
        print(edge_data)

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
                                       'stylesheet': style,
                                       'severity': data.get('severity-scores', {}),
                                       'annotations': annotations,
                                       'edge-data': edge_data}
                
                print(filename)

        return existing_marks, current_value, current_value, new_elements, map_store, track_data, filename

    return existing_marks, current_max, current_value, new_elements, map_store, track_data, filename

# Callback - NETWORK COMPARISON: Network comparison timeline navigation
# When user navigates across timeline
# Select file in dict that correspond to chosen date + time
# Feed in this file into dummy cytoscape 
def update_cytoscape_elements(selected_value, marks, comparison_data, session_data, severity_scores):
    selected_date = None
    filename = None
    
    if comparison_data is not None:
        label = marks.get(str(selected_value))  # Fetch label based on the slider's value

        if label in comparison_data:  # Check if the label exists in comparison_data keys
            selected_date = label
            filename = label

        if selected_date is not None:
            if selected_date != "PsySys":
                elements = comparison_data[selected_date]['elements']
                stylesheet = comparison_data[selected_date].get('stylesheet', [])
            else:
                elements = comparison_data[selected_date]['elements']
                stylesheet = apply_severity_size_styles("Severity", session_data['stylesheet'], severity_scores, session_data['stylesheet'])

            return elements, stylesheet, filename

    return [], [], filename

# Callback - NETWORK COMPARISON: Populate tracking graph with PsySys map
def update_track(session_data, track_data, map_store):
    track_data['elements'] = session_data['elements']
    track_data['stylesheet'] = session_data['stylesheet']

    map_store['PsySys'] = {'elements': session_data['elements'], 
                           'stylesheet': session_data['stylesheet'],
                           'severity': session_data.get('severity', {})
                           }
    
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

# Callback - NETWORK COMPARISON: Create centrality plot
# def update_graph(selected_map, current_mode, comparison_data, track_data, marks):
#     if current_mode == "current":
#         if selected_map is None or comparison_data is None or marks is None:
#             return go.Figure()  # Return an empty figure if no data is available
        
#         fig = current_centrality_plot(track_data, comparison_data, selected_map, marks)
        
#         if fig:
#             return fig
        
#         return go.Figure()
    
#     else: 
#         x, y = prepare_graph_data(comparison_data)

#         # Check if 'PsySys' is in marks
#         if 'PsySys' not in marks.values():
#             # Filter out 'PsySys' related data from x and y
#             if "PsySys" in x:
#                 index_to_remove = x.index("PsySys")
#                 del x[index_to_remove]
#                 del y[-1]
#             else: 
#                 pass

#         # If x is empty after filtering, return an empty figure
#         new_x_labels = []
        
#         # Convert x labels to sequential 'map 1', 'map 2', ..., 'map n'
#         if x: 
#             new_x_labels = [f'map {i+1}' for i in range(len(x))]

#         # Extract unique network elements (keys from dictionaries in y)
#         all_elements = set()
#         for network_dict in y:
#             if isinstance(network_dict, dict):
#                 all_elements.update(network_dict.keys())

#         fig = go.Figure()
        
#         # Add a trace for each network element
#         for element in all_elements:
#             element_values = []
#             for network_dict in y:
#                 element_values.append(network_dict.get(element, None))  # Use None for missing values
            
#             # Introduce jitter to x positions to avoid overlap
#             jitter = np.random.uniform(-0.05, 0.05, size=len(new_x_labels))  # Adjust the jitter size as needed
#             jittered_x = [i + jitter[i] for i in range(len(new_x_labels))]
            
#             fig.add_trace(go.Scatter(
#                 #x=new_x_labels,  # Use new sequential labels for x-axis
#                 x = jittered_x,
#                 y=element_values,
#                 mode='lines+markers',
#                 name=element
#             ))
            
#         # Update the layout of the plot
#         fig.update_layout(
#             title={
#                 'text': 'Severity Comparison',
#                 'y': 0.92,  # Adjust the vertical position of the title
#                 'x': 0.5,
#                 'xanchor': 'center',
#                 'yanchor': 'top'
#             },
#             yaxis_title='Severity',
#             template='plotly_white',
#             width=420,  # Set a wider width for the plot
#             height=450,  # Adjust height as needed
#             margin={'l': 20, 'r': 20, 't': 100, 'b': 5},  # Adjust margins to fit labels
#             xaxis=dict(
#                 tickmode='array',  # Specify custom tick values
#                 tickvals=list(range(len(new_x_labels))),  # Use positions as tick values
#                 ticktext=new_x_labels,  # Set the custom tick labels to be the new sequential labels
#                 tickangle=-45  # Rotate tick labels for better fit
#             ),
#             yaxis=dict(
#                 domain=[0.1, 0.75]  # Adjusts the y-axis to start at 20% of the figure height and end at 100%
#             ),
#             legend=dict(
#                 orientation='h',  # Set the legend to horizontal
#                 yanchor='bottom',  # Anchor to the bottom of the legend box
#                 y=0.8,  # Position it slightly above the plot
#                 xanchor='center',  # Center the legend horizontally
#                 x=0.5  # Set it in the middle of the plot
#             )
#         )

#         return fig

def update_graph(selected_map, current_mode, comparison_data, track_data, marks):
    if current_mode == "current":
        if selected_map is None or comparison_data is None or marks is None:
            return go.Figure()  # Return an empty figure if no data is available
        
        fig = current_centrality_plot(track_data, comparison_data, selected_map, marks)
        
        if fig:
            return fig
        
        return go.Figure()
    
    else:
        # Check if comparison_data is empty
        if not comparison_data:
            return go.Figure()  # Return an empty figure if comparison_data is empty
        
        # Try to call prepare_graph_data and catch potential KeyError
        try:
            x, y = prepare_graph_data(comparison_data)
        except KeyError as e:
            return go.Figure()

        # Check if 'PsySys' is in marks
        if 'PsySys' not in marks.values():
            # Filter out 'PsySys' related data from x and y
            if "PsySys" in x:
                index_to_remove = x.index("PsySys")
                del x[index_to_remove]
                del y[-1]

        # If x is empty after filtering, prepare for no x labels
        if not x:
            new_x_labels = []
        else:
            # Convert x labels to sequential 'map 1', 'map 2', ..., 'map n'
            new_x_labels = [f'map {i+1}' for i in range(len(x))]

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
            
            # Introduce jitter to x positions to avoid overlap
            jitter = np.random.uniform(-0.05, 0.05, size=len(new_x_labels))
            jittered_x = [i + jitter[i] for i in range(len(new_x_labels))]
            
            fig.add_trace(go.Scatter(
                x=jittered_x if new_x_labels else [],  # Use jittered x only if labels are present
                y=element_values,
                mode='lines+markers',
                name=element
            ))

        # Update the layout of the plot
        fig.update_layout(
            title={
                'text': 'Severity Comparison',
                'y': 0.92,
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top'
            },
            yaxis_title='Severity',
            template='plotly_white',
            width=420,
            height=450,
            margin={'l': 20, 'r': 20, 't': 100, 'b': 5},
            xaxis=dict(
                showticklabels=bool(new_x_labels),  # Show ticks only if labels exist
                tickmode='array',
                tickvals=list(range(len(new_x_labels))),
                ticktext=new_x_labels,
                tickangle=-45
            ),
            yaxis=dict(
                domain=[0.1, 0.75]
            ),
            legend=dict(
                orientation='h',
                yanchor='bottom',
                y=0.8,
                xanchor='center',
                x=0.5
            )
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
        return 'The figure shows the factor severity scores over the uploaded mental-health maps.'

# Callback - NETWORK COMPARISON: Toggle uniform style for network maps
def update_stylesheet_02(uniform_switch, selected_value, marks, comparison_data, session_data, severity_scores):
    selected_date = None
    
    if comparison_data is not None:
        label = marks.get(str(selected_value))  # Fetch label based on the slider's value

        if label in comparison_data:  # Check if the label exists in comparison_data keys
            selected_date = label

        if selected_date is not None:
            elements = comparison_data[selected_date]['elements']
            severity_scores = comparison_data[selected_date].get('severity', None)
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
# def display_annotation_nodes(tapNodeData, map_store, filename, is_open):
#     print(filename)
#     ctx = callback_context
#     triggered_id = ctx.triggered[0]['prop_id'].split('.')[0]  # Identify which input triggered the callback

#     # Check if the filename exists in the map_store
#     if filename not in map_store:
#         print("Filename not found in map_store.")
#         return False, "No annotation data available."

#     # Retrieve node and edge annotations from the map_store
#     node_annotations = map_store[filename].get('annotations', {})

#     # Check what triggered the callback
#     if triggered_id == 'track-graph':
#         # Determine if an edge was clicked
#         if tapNodeData:
#             node_id = tapNodeData['id']
#             # Fetch the annotation for the clicked node from the annotations store
#             node_annotation = node_annotations.get(node_id, "No annotation for this factor.")
#             return True, f"{node_annotation}"  # Open modal and display annotation

#     # If no element is clicked, close the modal or keep it closed
#     return False, dash.no_update

def display_annotation_nodes(tapNodeData, map_store, filename, is_open):
    print(filename)
    ctx = callback_context
    triggered_id = ctx.triggered[0]['prop_id'].split('.')[0]  # Identify which input triggered the callback

    # Check if the filename exists in the map_store
    if filename not in map_store:
        print("Filename not found in map_store.")
        return False, "No annotation data available."

    # Retrieve node annotations from the map_store
    node_annotations = map_store[filename].get('annotations', {})

    # Check what triggered the callback
    if triggered_id == 'track-graph':
        # Determine if a node was clicked
        if tapNodeData:
            print("it's a node")
            node_id = tapNodeData['id']
            # Fetch the annotation for the clicked node from the annotations store
            node_annotation = node_annotations.get(node_id, "No annotation for this factor.")
            
            # If the annotation is empty or not present, use the default message
            if not node_annotation:
                node_annotation = "No annotation for this factor."
                
            return True, f"{node_annotation}"  # Open modal and display annotation

    # If no element is clicked, close the modal or keep it closed
    return False, dash.no_update

# def display_annotation_edges(tapEdgeData, map_store, filename, is_open):
#     print(filename)
#     ctx = callback_context
#     triggered_id = ctx.triggered[0]['prop_id'].split('.')[0]  # Identify which input triggered the callback

#     # Check if the filename exists in the map_store
#     if filename not in map_store:
#         print("Filename not found in map_store.")
#         return False, "No annotation data available."

#     # Retrieve node and edge annotations from the map_store
#     node_annotations = map_store[filename].get('annotations', {})
#     edge_annotations = map_store[filename].get('edge-data', {})

#     # Check what triggered the callback
#     if triggered_id == 'track-graph':
#         # Determine if an edge was clicked
#         if tapEdgeData:
#             print("it's an edge")
#             # Construct the edge ID using the 'source' and 'target' from tapEdgeData
#             source = tapEdgeData['source']
#             target = tapEdgeData['target']
#             edge_id = f"edge_{source}_{target}"
            
#             edge_id = tapEdgeData['id']

#             # Fetch the annotation for the clicked edge from the edge-data store
#             edge_annotation = edge_annotations.get(edge_id, {}).get('annotation', "No annotation for this connection.")
#             return True, f"{edge_annotation}"  # Open modal and display annotation

#     # If no element is clicked, close the modal or keep it closed
#     return False, dash.no_update

def display_annotation_edges(tapEdgeData, map_store, filename, is_open):
    print(filename)
    ctx = callback_context
    triggered_id = ctx.triggered[0]['prop_id'].split('.')[0]  # Identify which input triggered the callback

    # Check if the filename exists in the map_store
    if filename not in map_store:
        print("Filename not found in map_store.")
        return False, "No annotation data available."

    # Retrieve edge annotations from the map_store
    edge_annotations = map_store[filename].get('edge-data', {})

    # Check what triggered the callback
    if triggered_id == 'track-graph':
        # Determine if an edge was clicked
        if tapEdgeData:
            print("it's an edge")
            # Construct the edge ID using the 'source' and 'target' from tapEdgeData
            source = tapEdgeData['source']
            target = tapEdgeData['target']
            edge_id = f"edge_{source}_{target}"
            
            # If the edge ID from `tapEdgeData` is different, use that instead
            edge_id = tapEdgeData.get('id', edge_id)

            # Fetch the annotation for the clicked edge from the edge-data store
            edge_data = edge_annotations.get(edge_id, {})
            edge_annotation = edge_data.get('annotation', "No annotation for this connection.")

            # If the annotation is empty or not present, use the default message
            if not edge_annotation:
                edge_annotation = "No annotation for this connection."
                
            return True, f"{edge_annotation}"  # Open modal and display annotation

    # If no element is clicked, close the modal or keep it closed
    return False, dash.no_update

def register_comparison_callbacks(app):

    app.callback(
        [Output('timeline-slider', 'marks'), 
        Output('timeline-slider', 'max'), 
        Output('timeline-slider', 'value'),
        Output('track-graph', 'elements'),
        Output('comparison', 'data'),
        Output('track-map-data', 'data'),
        Output('current-filename-store', 'data')],
        Input('upload-graph-tracking', 'contents'), 
        [State('timeline-slider', 'marks'), 
        State('timeline-slider', 'max'),
        State('timeline-slider', 'value'),
        State('track-graph', 'elements'),
        State('comparison', 'data'),
        State('track-map-data', 'data'),
        State('track-graph', 'stylesheet'),
        State('edge-data', 'data')]
    )(upload_tracking_graph)

    app.callback(
        [Output('track-graph', 'elements', allow_duplicate=True),
        Output('track-graph', 'stylesheet'),
        Output('current-filename-store', 'data', allow_duplicate=True)],
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
         [Input('track-graph', 'tapNodeData')], 
         [State('comparison', 'data'),  # State to access stored annotations
          State('current-filename-store', 'data'),
          State('modal-annotation', 'is_open')],  # State to check current modal status
    )(display_annotation_nodes)

    app.callback(
        [Output('modal-annotation', 'is_open', allow_duplicate=True),  # Controls modal visibility
         Output('modal-notes', 'children', allow_duplicate=True)],  # Updates modal content with annotation
         [Input('track-graph', 'tapEdgeData')], 
         [State('comparison', 'data'),  # State to access stored annotations
          State('current-filename-store', 'data'),
          State('modal-annotation', 'is_open')],  # State to check current modal status
          prevent_initial_call=True
    )(display_annotation_edges)
    