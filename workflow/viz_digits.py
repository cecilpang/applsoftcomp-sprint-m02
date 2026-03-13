from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

def create_fig(data:pd.DataFrame, out_path:Path, show_fig:bool=False):
    """
    Create 2D scatter plots of digits
    """
    X = data.drop(columns="digit")
    y = data["digit"]

    X_pca_2d = PCA(n_components=2, random_state=42).fit_transform(X)
    X_pca = PCA(n_components=30, random_state=42).fit_transform(X)
    X_tsne = TSNE(
        n_components=2,
        perplexity=30,
        init="pca",
        learning_rate="auto",
        random_state=42,
    ).fit_transform(X_pca)

    sns.set_theme(style="white", context="talk")
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))

    dfs = [
        ("PCA (64 -> 2)", X_pca_2d, y),
        ("PCA + t-SNE (64 -> 30 -> 2)", X_tsne, y),
    ]

    for ax, (title, X_i, y_i) in zip(axes, dfs):
        sns.scatterplot(
            x=X_i[:, 0],
            y=X_i[:, 1],
            hue=y_i,
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

    plt.savefig(out_path)
    print("Generated figure of digits-data.")
    if show_fig:
        plt.show()


if __name__ == "__main__":
    csv_file = Path('./data/digits-data.csv')
    fig_path = Path('./figs/fig-digits.png')

    df = pd.read_csv(csv_file)
    print("-"*30, "\nLoaded digits-data.csv")
    create_fig(df, fig_path)
