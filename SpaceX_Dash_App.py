# =============================================================
# SpaceX Launch Records Dashboard
# Built with Plotly Dash
# =============================================================
# This file is a Python SCRIPT (not a notebook).
# Run it from terminal with: python spacex_dash_app.py
# Then open browser at: http://127.0.0.1:8050
# =============================================================


# ─────────────────────────────────────────────────────────────
# PART 1: IMPORTS & SETUP
# ─────────────────────────────────────────────────────────────

# pandas  → load and filter our SpaceX CSV data
import pandas as pd

# dash    → the web framework that creates our app
import dash
from dash import html   # builds the HTML page structure
from dash import dcc    # Dash Core Components (dropdown, slider, graph)

# Input/Output → used inside callbacks to link components together
from dash.dependencies import Input, Output

# plotly express → creates beautiful charts with one line of code
import plotly.express as px


# ─────────────────────────────────────────────────────────────
# PART 2: LOAD THE DATA
# ─────────────────────────────────────────────────────────────

# Read the SpaceX launch dataset
# This CSV has columns like:
# Launch Site | class | Payload Mass (kg) | Booster Version Category
spacex_df = pd.read_csv(
    "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud"
    "/IBM-DS0321EN-SkillsNetwork/datasets/spacex_launch_dash.csv"
)

# Get the min and max payload mass for the range slider
# round() makes them clean numbers like 0 and 9600
min_payload = round(spacex_df['Payload Mass (kg)'].min())
max_payload = round(spacex_df['Payload Mass (kg)'].max())

print("✅ Data loaded successfully!")
print(f"   Rows: {len(spacex_df)}")
print(f"   Payload range: {min_payload} kg to {max_payload} kg")
print(f"   Launch sites: {spacex_df['Launch Site'].unique()}")


# ─────────────────────────────────────────────────────────────
# PART 3: CREATE THE DASH APP
# ─────────────────────────────────────────────────────────────

# dash.Dash() creates our web application
# __name__ tells Dash where to find assets (CSS, images etc.)
app = dash.Dash(__name__)


# ─────────────────────────────────────────────────────────────
# PART 4: APP LAYOUT
# ─────────────────────────────────────────────────────────────
# The layout defines WHAT appears on the page and HOW it looks.
# html.Div() = a container box (like <div> in HTML)
# html.H1()  = a heading (like <h1> in HTML)
# dcc.Graph()= a placeholder where a chart will appear
# ─────────────────────────────────────────────────────────────

app.layout = html.Div(
    # Outer styling — full width, light background, clean font
    style={
        'fontFamily': 'Arial, sans-serif',
        'backgroundColor': '#f8f9fa',
        'padding': '20px',
        'maxWidth': '1200px',
        'margin': '0 auto'
    },
    children=[

        # ── HEADER ───────────────────────────────────────────
        html.H1(
            'SpaceX Launch Records Dashboard',
            style={
                'textAlign': 'center',
                'color': '#1a1a2e',
                'fontSize': '2rem',
                'marginBottom': '5px',
                'fontWeight': 'bold',
                'letterSpacing': '1px'
            }
        ),

        # Subtitle line under the header
        html.P(
            'Interactive analysis of Falcon 9 launch outcomes',
            style={
                'textAlign': 'center',
                'color': '#6c757d',
                'marginBottom': '30px',
                'fontSize': '1rem'
            }
        ),

        # Thin divider line
        html.Hr(style={'borderColor': '#dee2e6'}),

        # ── TASK 1: DROPDOWN ─────────────────────────────────
        # Label above the dropdown
        html.Label(
            'Select Launch Site:',
            style={
                'fontWeight': 'bold',
                'color': '#1a1a2e',
                'fontSize': '0.95rem',
                'marginBottom': '6px',
                'display': 'block'
            }
        ),

        # TASK 1 → Complete the dcc.Dropdown below
        # id='site-dropdown' connects it to the callback function
        dcc.Dropdown(
            id='site-dropdown',
            # options = the choices available in the dropdown
            # Each choice is a dict with 'label' (shown to user)
            # and 'value' (what the code receives)
            options=[
                {'label': 'All Sites', 'value': 'ALL'},
                # We build one option per unique launch site
                *[
                    {'label': site, 'value': site}
                    for site in sorted(spacex_df['Launch Site'].unique())
                ]
            ],
            value='ALL',                          # default selected value
            placeholder='Select a Launch Site',   # grey hint text
            searchable=True,                      # user can type to filter
            style={
                'marginBottom': '25px',
                'fontSize': '0.95rem',
                'borderRadius': '6px'
            }
        ),

        # ── PIE CHART CONTAINER ───────────────────────────────
        html.Div(
            style={
                'backgroundColor': 'white',
                'borderRadius': '10px',
                'padding': '20px',
                'marginBottom': '25px',
                'boxShadow': '0 2px 8px rgba(0,0,0,0.08)'
            },
            children=[
                # TASK 2 → This graph will be filled by the
                # get_pie_chart() callback function below
                dcc.Graph(id='success-pie-chart')
            ]
        ),

        # ── TASK 3: RANGE SLIDER ──────────────────────────────
        html.Label(
            'Select Payload Range (kg):',
            style={
                'fontWeight': 'bold',
                'color': '#1a1a2e',
                'fontSize': '0.95rem',
                'marginBottom': '10px',
                'display': 'block'
            }
        ),

        # Payload range slider
        # min/max come from the actual data loaded above
        dcc.RangeSlider(
            id='payload-slider',
            min=0,
            max=10000,
            step=1000,
            # marks = labels shown on the slider track
            marks={
                0:    {'label': '0 kg',     'style': {'color': '#6c757d'}},
                2500: {'label': '2,500 kg', 'style': {'color': '#6c757d'}},
                5000: {'label': '5,000 kg', 'style': {'color': '#6c757d'}},
                7500: {'label': '7,500 kg', 'style': {'color': '#6c757d'}},
                10000:{'label': '10,000 kg','style': {'color': '#6c757d'}}
            },
            # Default range = full dataset range
            value=[min_payload, max_payload]
        ),

        # Small spacing div after slider
        html.Div(style={'marginBottom': '25px'}),

        # ── SCATTER CHART CONTAINER ───────────────────────────
        html.Div(
            style={
                'backgroundColor': 'white',
                'borderRadius': '10px',
                'padding': '20px',
                'marginBottom': '25px',
                'boxShadow': '0 2px 8px rgba(0,0,0,0.08)'
            },
            children=[
                # TASK 4 → This graph will be filled by the
                # get_scatter_chart() callback function below
                dcc.Graph(id='success-payload-scatter-chart')
            ]
        ),

        # ── FOOTER ───────────────────────────────────────────
        html.Hr(style={'borderColor': '#dee2e6'}),
        html.P(
            'IBM Applied Data Science Capstone — SpaceX Dashboard',
            style={
                'textAlign': 'center',
                'color': '#adb5bd',
                'fontSize': '0.8rem',
                'marginTop': '10px'
            }
        )
    ]
)


# ─────────────────────────────────────────────────────────────
# PART 5: CALLBACKS
# ─────────────────────────────────────────────────────────────
# Callbacks are functions that run AUTOMATICALLY when the user
# interacts with a component (dropdown, slider etc.)
#
# Structure:
# @app.callback(
#     Output(...),   ← what to UPDATE (the chart)
#     Input(...)     ← what TRIGGERS the update (user action)
# )
# def function_name(input_value):
#     return updated_chart
# ─────────────────────────────────────────────────────────────


# ── TASK 2: PIE CHART CALLBACK ────────────────────────────────
# Triggered by: dropdown selection changes
# Updates     : the pie chart

@app.callback(
    Output(component_id='success-pie-chart', component_property='figure'),
    Input(component_id='site-dropdown',      component_property='value')
)
def get_pie_chart(entered_site):
    """
    If ALL sites selected:
        Show total successful launches for all sites combined
        (one slice per launch site)

    If specific site selected:
        Show Success vs Failed count for THAT site only
        (two slices: success=1, failed=0)
    """
    if entered_site == 'ALL':
        # Filter only successful launches (class=1) across all sites
        success_df = spacex_df[spacex_df['class'] == 1]

        # Count successes per site and build pie chart
        fig = px.pie(
            success_df,
            names='Launch Site',          # one slice per site
            title='Total Successful Launches by Site',
            color_discrete_sequence=px.colors.qualitative.Bold
        )

    else:
        # Filter dataframe to only the selected site
        site_df = spacex_df[spacex_df['Launch Site'] == entered_site]

        # Show success (1) vs failure (0) for that site
        fig = px.pie(
            site_df,
            names='class',                # 0=fail, 1=success
            title=f'Launch Outcomes for site: {entered_site}',
            color_discrete_map={
                1: '#2ecc71',             # green for success
                0: '#e74c3c'              # red for failure
            },
            labels={'class': 'Outcome'}
        )

    # Apply clean styling to the chart
    fig.update_layout(
        paper_bgcolor='white',
        plot_bgcolor='white',
        font=dict(family='Arial', size=13),
        margin=dict(t=60, b=20, l=20, r=20),
        legend=dict(
            orientation='v',
            x=1.02,
            y=0.5
        )
    )
    return fig


# ── TASK 4: SCATTER CHART CALLBACK ───────────────────────────
# Triggered by: dropdown selection OR slider range changes
# Updates     : the scatter chart
# Note: TWO inputs this time — both trigger the same function

@app.callback(
    Output(component_id='success-payload-scatter-chart', component_property='figure'),
    [
        Input(component_id='site-dropdown',   component_property='value'),
        Input(component_id='payload-slider',  component_property='value')
    ]
)
def get_scatter_chart(entered_site, payload_range):
    """
    payload_range = [low, high] from the slider
    entered_site  = 'ALL' or a specific site name

    Steps:
    1. Filter by payload range (always)
    2. Filter by site (if not ALL)
    3. Plot payload (x) vs success (y), coloured by booster version
    """
    # Step 1: Filter rows where payload is within the slider range
    low, high = payload_range
    filtered_df = spacex_df[
        (spacex_df['Payload Mass (kg)'] >= low) &
        (spacex_df['Payload Mass (kg)'] <= high)
    ]

    # Step 2: Further filter by site if a specific one was chosen
    if entered_site != 'ALL':
        filtered_df = filtered_df[
            filtered_df['Launch Site'] == entered_site
        ]
        title = f'Payload vs. Launch Outcome for site: {entered_site}'
    else:
        title = 'Payload vs. Launch Outcome for All Sites'

    # Step 3: Build scatter plot
    # x = payload mass, y = success (0 or 1), colour = booster version
    fig = px.scatter(
        filtered_df,
        x='Payload Mass (kg)',
        y='class',
        color='Booster Version Category',
        title=title,
        labels={
            'class': 'Launch Outcome (1=Success, 0=Failure)',
            'Payload Mass (kg)': 'Payload Mass (kg)'
        },
        color_discrete_sequence=px.colors.qualitative.Bold,
        opacity=0.8
    )

    # Apply clean styling to the chart
    fig.update_layout(
        paper_bgcolor='white',
        plot_bgcolor='#f8f9fa',
        font=dict(family='Arial', size=13),
        margin=dict(t=60, b=40, l=60, r=20),
        yaxis=dict(
            tickvals=[0, 1],
            ticktext=['Failure', 'Success'],
            gridcolor='#dee2e6'
        ),
        xaxis=dict(gridcolor='#dee2e6'),
        legend_title='Booster Version'
    )
    return fig


# ─────────────────────────────────────────────────────────────
# PART 6: RUN THE APP
# ─────────────────────────────────────────────────────────────
# debug=True means the app auto-reloads when you save changes
# port=8050 is the default Dash port

if __name__ == '__main__':
    app.run(debug=True, port=8050)