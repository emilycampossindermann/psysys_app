# Imports 
import dash_bootstrap_components as dbc

# Initialize factor list
factors = ["Loss of interest", "Feeling down", "Stress", "Worry", "Overthinking", "Sleep problems", 
           "Joint pain", "Changes in appetite", "Self-blame", "Trouble concentrating", "Procrastinating", 
           "Breakup", "Problems at work", "Interpersonal problems"]

# Initialize node color schemes
node_color = ["Custom", "Uniform", "Severity", "Severity (abs)", "Out-degree", "In-degree", "Out-/In-degree ratio"]

# Initialize node sizing schemes
node_size = ["Uniform", "Severity", "Severity (abs)", "Out-degree", "In-degree", "Out-/In-degree ratio"] 

# Stylesheet
stylesheet = [{'selector': 'node','style': {'background-color': '#9CD3E1', 'label': 'data(label)', 'font-family': 'Arial'}},
              {'selector': 'edge','style': {'curve-style': 'bezier', 'target-arrow-shape': 'triangle', 'control-point-step-size': '40px' }}
    ]

# Initialize styles (buttons)
hidden_style = {'display': 'none'}
visible_style = {'display': 'block', "color": "#8793c9"}