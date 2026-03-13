import marimo

__generated_with = "0.20.4"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    from sklearn.decomposition import PCA
    from sklearn.manifold import TSNE

    return mo, pd


@app.cell
def _(mo):
    mo.md(r"""
    # UCI Digits in 2D

    This notebook loads `digits-data.csv`, visualize the handwritten digit classes in 2D using t-SNE.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    # Load and explore data
    """)
    return


@app.cell
def _(pd):
    df = pd.read_csv("../../data/digits-data.csv")
    df.head()
    return (df,)


@app.cell
def _(df):
    df.shape, df.columns[-5:].tolist()
    return


@app.cell
def _(mo):
    mo.md(r"""
    # Format X and Y
    """)
    return


@app.cell
def _(df):
    feature_columns = [column for column in df.columns if column != "digit"]
    X = df[feature_columns]
    y = df["digit"]

    X.shape, y.value_counts().sort_index()
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
