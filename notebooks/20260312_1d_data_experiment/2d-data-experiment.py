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

    return pd, plt, sns


@app.cell
def _(mo):
    mo.md(r"""
    # Explore data
    """)
    return


@app.cell
def _(pd):
    df_2d = pd.read_csv('../../data/2d-data.csv')
    df_2d
    return (df_2d,)


@app.cell
def _(df_2d):
    print(df_2d.describe())
    print('\n')
    print(df_2d.info())
    return


@app.cell
def _(df_2d, plt, sns):
    fig, axes = plt.subplots(1, 2, figsize=(10, 4))
    sns.histplot(df_2d['x'], ax=axes[0], kde=True)
    axes[0].set_title('Histogram of x')
    sns.histplot(df_2d['y'], ax=axes[1], kde=True)
    axes[1].set_title('Histogram of y')
    plt.tight_layout()
    plt.show()
    return


@app.cell
def _(df_2d):
    corr = df_2d['x'].corr(df_2d['y'])
    print(f"Correlation between x and y: {corr:.3f}")
    return


@app.cell
def _(df_2d, plt, sns):
    sns.scatterplot(data=df_2d, x='x', y='y', size=5, alpha=0.3)
    plt.title('Scatterplot of x vs y')
    plt.tight_layout()
    plt.show()
    return


@app.cell
def _(mo):
    mo.md(r"""
    # Try Hexbin plot
    """)
    return


@app.cell
def _(df_2d, sns):
    # Hexbin plot
    sns.set_theme(style="white")

    sns.jointplot(
        data=df_2d,
        x="x",
        y="y",
        kind="hex",
        cmap="Blues",
        height=7
    )
    return


@app.cell
def _(df_2d, plt, sns):
    sns.kdeplot(
        data=df_2d,
        x="x",
        y="y",
        cmap='viridis', 
        fill=True,
        levels=10
    )
    plt.show()
    return


@app.cell
def _(mo):
    mo.md(r"""
    # Visualization
    """)
    return


@app.cell
def _(df_2d, plt, sns):
    # df has columns x and y
    sns.set_theme(style="white")

    g = sns.jointplot(
        data=df_2d,
        x="x",
        y="y",
        kind="hex",
        cmap="Blues",
        height=7
    )

    sns.kdeplot(
        data=df_2d,
        x="x",
        y="y",
        ax=g.ax_joint,
        color="red",
        levels=10,
        linewidths=1
    )

    g.set_axis_labels('Variable X', 'Variable Y')
    g.figure.suptitle('Hexbin with marginal histograms overlay contour plot')
    plt.tight_layout()
    plt.show()
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
