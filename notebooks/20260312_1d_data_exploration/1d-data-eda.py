import marimo

__generated_with = "0.20.4"
app = marimo.App()


@app.cell
def _():
    from pathlib import Path
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns

    return (pd,)


@app.cell
def _(pd):
    # Load the data
    df_1d = pd.read_csv('../../data/1d-data.csv')
    return (df_1d,)


@app.cell
def _(df_1d):
    df_1d.head()
    return


@app.cell
def _(df_1d):
    print(df_1d.describe())
    print('\n')
    print(df_1d.info())
    print('\n')
    print(df_1d.isna().sum())
    return


@app.cell
def _(df_1d):
    df_1d['group'].value_counts()
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
