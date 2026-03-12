from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def create_fig(data:pd.DataFrame, out_path:Path, show_fig:bool=False):
    """
    Create Hexbin plot overlay with Contour Plots
    """
    sns.set_theme(style="white")

    g = sns.jointplot(
        data=data,
        x="x",
        y="y",
        kind="hex",
        cmap="Blues",
        height=7
    )
    sns.kdeplot(
        data=data,
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

    plt.savefig(out_path)
    print("Generated figure of 2d-data.")
    if show_fig:
        plt.show()


if __name__ == "__main__":
    csv_file = Path('./data/2d-data.csv')
    fig_path = Path('./figs/fig-2d-data.png')

    df = pd.read_csv(csv_file)
    print("-"*30, "\nLoaded 2d-data.csv")
    create_fig(df, fig_path)
