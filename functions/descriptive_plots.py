from functions.map_style import calculate_degree_centrality
import plotly.graph_objects as go

# Function: Create current centrality bar plot
def current_centrality_plot(track_data, comparison_data, selected_map, marks):
    # Extract elements of currently visible map by checking timeline slider & fetching from comparison_data
    if comparison_data is not None:
        label = marks.get(str(selected_map))  # Fetch label based on the slider's value

        if label in comparison_data:  # Check if the label exists in comparison_data keys
            selected_date = label

            if selected_date is not None:
                elements = comparison_data[selected_date]['elements']

                # Calculate in- and out-degree centrality for all elements & store in degrees dictionary
                degrees = {element['data']['id']: {'out': 0, 'in': 0} for element in elements 
                           if 'source' not in element['data'] and 'target' not in element['data']}

                elements, degrees = calculate_degree_centrality(elements, degrees)

                # Prepare data for the plot
                node_ids = list(degrees.keys())
                in_degrees = [degrees[node]['in'] for node in node_ids]
                out_degrees = [degrees[node]['out'] for node in node_ids]

                # Create bar plot
                # fig = go.Figure(data=[
                #     go.Bar(name='In-Coming', x=node_ids, y=in_degrees, marker_color='lightblue'),
                #     go.Bar(name='Out-Going', x=node_ids, y=out_degrees, marker_color='orange')
                # ])
                fig = go.Figure(data=[
                go.Bar(
                    name='In-Coming', 
                    x=node_ids, 
                    y=in_degrees, 
                    marker_color='rgba(156, 211, 225, 0.5)'  # Color with low opacity
                ),
                go.Bar(
                    name='Out-Going', 
                    x=node_ids, 
                    y=out_degrees, 
                    marker_color='#9CD3E1'  # Solid color
                )
                ])

                # Update layout
                fig.update_layout(
                    barmode='group',
                    title='Factor Influence',
                    #xaxis_title='Nodes',
                    yaxis_title='Connections',
                    template='plotly_white',
                    yaxis=dict(
                    tickmode='linear',
                    tick0=0,
                    dtick=1,  # Set the tick interval to 1 to show only whole numbers
                    tickformat='d'  # Ensure that the tick labels are displayed as integers
                )
                )

                # Return the figure
                return fig

    return None

# Function: Create overall centrality line plot
def calculate_degree_ratios(elements):
    degrees = {element['data']['id']: {'out': 0, 'in': 0} for element in elements 
               if 'source' not in element['data'] and 'target' not in element['data']}
    elements, degrees = calculate_degree_centrality(elements, degrees)
    degree_ratios = {node: degrees[node]['out'] / degrees[node]['in'] if degrees[node]['in'] != 0 else degrees[node]['out'] for node in degrees}
    return degree_ratios

def prepare_graph_data(comparison_data):
    x = []
    y = []
    for network, data in comparison_data.items():
        ratios = calculate_degree_ratios(data['elements'])
        x.append(network)
        y.append(ratios)

    return x, y