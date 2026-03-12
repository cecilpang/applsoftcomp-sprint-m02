import marimo

__generated_with = "0.20.4"
app = marimo.App()


@app.cell
def _():
    from pathlib import Path
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns

    return np, pd, plt, sns


@app.cell
def _(mo):
    mo.md(r"""
    # Explore data
    """)
    return


@app.cell
def _(pd):
    # Load the data
    df_1d = pd.read_csv('../../data/1d-data.csv')
    df_1d
    return (df_1d,)


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
    df_1d.groupby('group').describe().apply(lambda x: x.astype(float).map('{:,.2f}'.format))
    return


@app.cell
def _(mo):
    mo.md(r"""
    # Visualization
    """)
    return


@app.cell
def _():
    show_fig = True
    return


@app.cell
def _(df_1d, plt, sns):
    sns.swarmplot(data=df_1d, x='group', y='value')
    plt.xlabel('Groups')
    plt.ylabel('Values')
    plt.title('Swarm Plot: Treatment effects case vs control')
    plt.show()
    return


@app.cell
def _(mo):
    mo.md(r"""
    It seems there are two outliers in group cases. Try swarm plot with log scale, and exam statistic with log scale.
    """)
    return


@app.cell
def _(df_1d, plt, sns):
    sns.swarmplot(data=df_1d, x='group', y='value', log_scale=2)
    plt.xlabel('Groups')
    plt.ylabel('Values')
    plt.title('Swarm Plot: Treatment effects case vs control')
    plt.show()
    return


@app.cell
def _(df_1d, np):
    # transform the “value” column to log₂, then do the groupby and describe
    df_1d.assign(log2_value=lambda d: np.log2(d['value'])) \
        .groupby('group')['log2_value'] \
        .describe() \
        .apply(lambda x: x.astype(float).map('{:,.2f}'.format))
    return


@app.cell
def _(mo):
    mo.md(r"""
    The swarm plot and statistic summary under log shows the large values in "cases" group are not outliers. So no need to remove outliers under log scale.
    """)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
