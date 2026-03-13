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

    return PCA, TSNE, mo, pd, plt, sns


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
    X = df.drop(columns="digit")
    y = df["digit"]

    X.shape, y.value_counts().sort_index()
    return X, y


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
    return (X_pca_2d,)


@app.cell
def _(mo):
    mo.md(r"""
    # PCA + t-SNE
    """)
    return


@app.cell
def _(PCA, X):
    pca = PCA(n_components=30, random_state=42)
    X_pca = pca.fit_transform(X)

    explained_variance = pca.explained_variance_ratio_.sum()
    print('64 -> 30 explained_variance: ', explained_variance)
    return (X_pca,)


@app.cell
def _(TSNE, X_pca):
    # PCA: 64 -> 30 + t-SNE: 30 -> 2
    tsne = TSNE(
        n_components=2,
        perplexity=30,
        init="pca",
        learning_rate="auto",
        random_state=42,
    )
    X_tsne = tsne.fit_transform(X_pca)

    return (X_tsne,)


@app.cell
def _(mo):
    mo.md(r"""
    # Plot 2D
    """)
    return


@app.cell
def _(X_pca_2d, pd, y):
    pca_df = pd.DataFrame(
        {
            "component_1": X_pca_2d[:, 0],
            "component_2": X_pca_2d[:, 1],
            "digit": y,
        }
    )
    pca_df.head()
    return (pca_df,)


@app.cell
def _(pca_df, plt, sns):
    sns.set_theme(style="white", context="talk")

    sns.scatterplot(
        data=pca_df,
        x="component_1",
        y="component_2",
        hue="digit",
        palette="tab10",
        s=28,
        alpha=0.85,
        linewidth=0,
    )
    plt.title("PCA (64 -> 2)")
    plt.xlabel("Component 1")
    plt.ylabel("Component 2")

    plt.legend(title="Digit", bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.show()
    return


@app.cell
def _(X_tsne, pd, y):
    tsne_df = pd.DataFrame(
        {
            "component_1": X_tsne[:, 0],
            "component_2": X_tsne[:, 1],
            "digit": y,
        }
    )
    tsne_df.head()
    return (tsne_df,)


@app.cell
def _(plt, sns, tsne_df):
    sns.set_theme(style="white", context="talk")

    sns.scatterplot(
        data=tsne_df,
        x="component_1",
        y="component_2",
        hue="digit",
        palette="tab10",
        s=28,
        alpha=0.85,
        linewidth=0,
    )
    plt.title("PCA + t-SNE (64 -> 30 -> 2)")
    plt.xlabel("Component 1")
    plt.ylabel("Component 2")

    plt.legend(title="Digit", bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.show()
    return


@app.cell
def _(pca_df, plt, sns, tsne_df):
    sns.set_theme(style="white", context="talk")

    fig, axes = plt.subplots(1, 2, figsize=(10, 5))

    dfs = [
        ("PCA (64 -> 2)", pca_df),
        ("PCA + t-SNE (64 -> 30 -> 2)", tsne_df),
    ]

    for ax, (title, dfi) in zip(axes, dfs):
        sns.scatterplot(
            data=dfi,
            x="component_1",
            y="component_2",
            hue="digit",
            palette="tab10",
            s=28,
            alpha=0.85,
            linewidth=0,
            legend=ax is axes[1],
            ax=ax,
        )
        ax.set_title(title)
        ax.set_xlabel("Component 1")
        ax.set_ylabel("Component 2")

    handles, labels = axes[1].get_legend_handles_labels()
    if handles:
        axes[1].legend(
            handles,
            labels,
            title="Digit",
            bbox_to_anchor=(1.05, 1.05),
            loc="upper left",
        )

    fig.suptitle("2D plots of UCI Handwritten Digits", y=0.95)
    plt.tight_layout()
    plt.show()
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
