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
    df = pd.read_csv('../../data/1d-multi-method-data.csv')
    df
    return (df,)


@app.cell
def _(df):
    print(df.describe())
    print('\n')
    print(df.info())
    return


@app.cell
def _(df):
    df.groupby('method').describe().apply(lambda x: x.astype(float).map('{:,.2f}'.format))
    return


@app.cell
def _(mo):
    mo.md(r"""
    # Format data
    """)
    return


@app.cell
def _(df, plt, sns):
    plt.figure(figsize=(8, 6))
    sns.stripplot(data=df, x='method', y='AUCROC', jitter=True, alpha=0.7)
    plt.xticks(rotation=45)
    plt.title('AUCROC by Method (jittered)')
    plt.tight_layout()
    plt.show()
    return


@app.cell
def _(mo):
    mo.md(r"""
    # Visualization
    """)
    return


@app.cell
def _(df, plt, sns):
    order = df.groupby('method')['AUCROC'].mean().sort_values(ascending=False).index
    palette = {m: ('red' if m == 'Proposed' else 'grey') for m in order}

    plt.figure(figsize=(8, 5))
    sns.stripplot(data=df, x='method', y='AUCROC', order=order, jitter=True, alpha=0.7, hue='method', palette=palette)

    means = df.groupby('method')['AUCROC'].mean().reindex(order)
    plt.scatter(range(len(order)), means, marker='D', s=50, c=[palette[m] for m in order], edgecolor='black', zorder=5)

    plt.xticks(rotation=45)
    plt.title('AUCROC by Method (jittered)')
    plt.tight_layout()
    plt.show()
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
