from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def create_fig(data:pd.DataFrame, out_path:Path, show_fig:bool=False):
    """
    Create box plot overlay swarm plot with data. Save the figure.
    """
    ax = sns.boxplot(
        data=data,
        x='group',
        y='value',
        log_scale=2
    )
    sns.swarmplot(
        data=data,
        x='group',
        y='value',
        color='red',
        size=5,
        ax=ax,
        log_scale=2
    )

    plt.xlabel('Groups')
    plt.ylabel('Values (log scale)')
    plt.title('Treatment effect Cases vs Control (log scaled)')
    plt.savefig(out_path)
    print("Generated figure of 1d-data.")
    if show_fig:
        plt.show()


if __name__ == "__main__":
    csv_file = Path('./data/1d-data.csv')
    fig_path = Path('./figs/fig-1d-data.png')

    df = pd.read_csv(csv_file)
    print("-"*30, "\nLoaded 1d-data.csv")
    create_fig(df, fig_path)
