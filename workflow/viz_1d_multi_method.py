from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def create_fig(data:pd.DataFrame, out_path:Path, show_fig:bool=False):
    """
    Create jittered scatter plot and highlight Proposed method
    """
    sns.set_theme(style="white")

    order = df.groupby('method')['AUCROC'].mean().sort_values(ascending=False).index
    palette = {m: ('red' if m == 'Proposed' else 'grey') for m in order}

    plt.figure(figsize=(8, 5))
    sns.stripplot(data=df, x='method', y='AUCROC', order=order, jitter=True, alpha=0.7, hue='method', palette=palette)

    means = df.groupby('method')['AUCROC'].mean().reindex(order)
    plt.scatter(range(len(order)), means, marker='D', s=50, c=[palette[m] for m in order], edgecolor='black', zorder=5)
    plt.xlabel('Methods (sorted by mean AUC-ROC)')
    plt.ylabel('AUC-ROC')
    plt.xticks(rotation=45)
    plt.title('AUC-ROC by Method: Proposed vs Baselines')
    plt.tight_layout()

    plt.savefig(out_path)
    print("Generated figure of 1d-multi-method-data.")
    if show_fig:
        plt.show()


if __name__ == "__main__":
    csv_file = Path('./data/1d-multi-method-data.csv')
    fig_path = Path('./figs/fig-1d-multi-method.png')

    df = pd.read_csv(csv_file)
    print("-"*30, "\nLoaded 1d-multi-method-data.csv")
    create_fig(df, fig_path)
