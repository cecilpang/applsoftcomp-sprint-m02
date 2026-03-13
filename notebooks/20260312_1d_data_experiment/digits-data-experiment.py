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

    return PCA, mo, pd


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
    return (X,)


@app.cell
def _(mo):
    mo.md(r"""
    # PCA
    """)
    return


@app.cell
def _(PCA, X):
    pca_2d = PCA(n_components=2, random_state=42)
    X_pca_2d = pca_2d.fit_transform(X)

    explained_variance_2d = pca_2d.explained_variance_ratio_.sum()
    print('64 -> 2 explained_variance: ', explained_variance_2d)
    return


@app.cell
def _(PCA, X):
    pca = PCA(n_components=30, random_state=42)
    X_pca = pca.fit_transform(X)

    explained_variance = pca.explained_variance_ratio_.sum()
    print('64 -> 30 explained_variance: ', explained_variance)
    return


@app.cell
def _():


    return


if __name__ == "__main__":
    app.run()
