import matplotlib.pyplot as plt
from matplotlib.figure import Figure

def plot_data(df1: dict, df2: dict, df3: dict) -> Figure:
    X1 = ["TOTAL VIEWS", "TOTAL STARS", "TOTAL FORKS", "OPEN ISSUES"]
    Y1 = [df1["total_watchers"], df1["total_stars"], df1["total_forks"], df1["open_issues"]]

    X2 = ["PUBLIC REPOS", "PRIVATE REPOS", "ACTIVE REPOS", "STALE REPOS"]
    Y2 = [df1["public_repos"], df1["private_repos"], df1["active_repos"], df1["stale_repos"]]

    X3 = list(df2.keys())
    Y3 = list(df2.values())
    
    X4 = list(df3.keys())
    Y4 = list(df3.values())

    fig, ax = plt.subplots(2, 2, figsize=(14, 8))

    ax[0, 0].barh(X1, Y1, color=["#0d5080", "#ff7f0e", "#36be36", "#d62728"], alpha=0.75)
    ax[0, 0].set_title("POPULATITY STATUS", fontsize=14, family="serif")
    ax[0, 0].grid(axis="y", linestyle="--", color="grey")

    ax[0, 1].barh(X2, Y2, color=["#1f77b4", "#1f77b4", "#2ca02c", "#2ca02c"], alpha=0.75)
    ax[0, 1].set_title("REPOSITORY STATUS", fontsize=14, family="serif")
    ax[0, 1].grid(axis="y", linestyle="--", color="grey")

    ax[1, 0].pie(Y3, 
                labels=X3, 
                radius=1.4, 
                autopct="%1.2f%%", 
                wedgeprops={"width": 0.5})
    ax[1, 0].legend(["MAJORITY LANGUAGE"], loc="upper left", bbox_to_anchor=(-0.8, 1))

    ax[1, 1].barh(X4, Y4, alpha=0.75)
    ax[1, 1].set_title("STARS PER REPOSITORY", fontsize=14, family="serif")

    fig.tight_layout()
    return fig