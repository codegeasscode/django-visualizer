import plotly.graph_objects as go
import plotly.io as pio

def create_bar_chart(item):
    """Creates a Bar Chart"""
    x_values, y_values = item["data"]
    fig = go.Figure(data=[go.Bar(x=x_values, y=y_values)])
    fig.update_layout(
        title=item["name"],
        plot_bgcolor="white",
        margin=dict(l=40, r=40, t=40, b=40),
    )
    return pio.to_html(fig, full_html=False)

def create_table(item):
    """Creates a Table"""
    keys = list(item["data"][0].keys())
    values = [[row[key] for row in item["data"]] for key in keys]    
             
    fig = go.Figure(data=[go.Table(
        header=dict(values=keys, fill_color="lightgrey", align="center"),
        cells=dict(values=values, align="center"),
    )])
    fig.update_layout(title=item["name"], margin=dict(l=40, r=40, t=40, b=40))
    return pio.to_html(fig, full_html=False)

# Mapping chart types
CHART_OPTIONS = {
    "bar": create_bar_chart,
    "table": create_table,
}

def generate_visualization(data_list):
    """Generates visualization using composition"""
    visualizations = []

    for item in data_list:
        chart_type = item.get("type")
        
        if chart_type in CHART_OPTIONS:
            viz_html = CHART_OPTIONS[chart_type](item)
            visualizations.append(viz_html)

    return visualizations