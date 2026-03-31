import plotly.express as px
from pandas import DataFrame

def validate_data(data: dict, x_val: str, y_val: str) -> DataFrame:
    return DataFrame({x_val: list(data.keys()),
                    y_val: list(data.values())})

def activity_status_plot(data: dict): # -> Figure
    data = validate_data(data, "CLASS", "FREQUENCY")
    fig = px.bar(data,
                 x="FREQUENCY",
                 y="CLASS",
                 title="ACTIVITY STATUS")
    return fig

def majority_language_plot(data: dict): # -> Figure:
    data = validate_data(data, "LANGUAGE", "NUMBER OF REPOS")
    fig = px.pie(data,
                 values="NUMBER OF REPOS",
                 names="LANGUAGE",
                 hole = 0.6,
                 title="MAJORITY LANGUAGE")
    return fig

def popular_repo_plot(data: dict): # -> Figure
    data = validate_data(data, "REPOSITORY NAME", "STARS EARNED")
    fig = px.bar(data,
                 x="STARS EARNED",
                 y="REPOSITORY NAME",
                 title="POPULAR REPOSITORY")
    return fig