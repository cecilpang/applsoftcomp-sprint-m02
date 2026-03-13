import marimo

__generated_with = "0.20.4"
app = marimo.App()


@app.cell
def _():
    import marimo
    from pathlib import Path
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns

    return (pd,)


@app.cell
def _(mo):
    mo.md(r"""
    # Load and explore data
    """)
    return


@app.cell
def _(pd):
    df = pd.read_csv('../../data/digits-data.csv')
    df
    return (df,)


@app.cell
def _(df):
    df.info()
    return


@app.cell
def _(df):
    df.columns
    return


@app.cell
def _(df):
    df.digit.value_counts()
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
