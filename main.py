import requests
import matplotlib.pyplot as plt
from datetime import datetime, timezone

def getData(username: str) -> list[dict]:
    """FETCHING API DATA USING GET()"""
    repos = []
    page = 1
    per_page = 100

    while True:
        url = f"https://api.github.com/users/{username}/repos"
        params = {"per_page": per_page, "page": page}

        try:
            response = requests.get(url, params=params, timeout=10)

            if response.status_code == 200:
                repo = response.json()

                if not repo: break
                repos.extend(repo)
                page += 1
            
            elif response.status_code == 404:
                print("USER NOT FOUND!"); break

            elif response.status_code == 403:
                print("RATE LIMIT EXCEEDED!"); break

            else:
                print(f"ERROR: {response.status_code}"); break

        except requests.exceptions.Timeout:
            print("REQUEST TIMED OUT"); break

        except Exception as f:
            print(f"REQUEST FAILED: {f}"); break

    return repos


username = input("\nENTER THE USERNAME TO FETCH DATA : ")
data = getData(username)

def is_repo_active(pushed_at: str) -> bool:
    """ACTIVITY STATUS CALCULATOR"""
    STALE_DAYS = 90
    if not pushed_at: return False

    pushed_date = datetime.strptime(
        pushed_at, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)

    today = datetime.now(timezone.utc)
    days_since_push = (today - pushed_date).days
    return days_since_push <= STALE_DAYS


if data:
    df = {
        "OWNER": None,
        "TOTAL REPOSITORIES": 0,
        "TOTAL STARS": 0,
        "TOTAL FORKS": 0,
        "TOTAL WATCHERS": 0,
        "TOTAL OPEN ISSUES": 0,
        "ACTIVE REPOS": 0,
        "STALE REPOS": 0,
        "PUBLIC REPOS": 0,
        "PRIVATE REPOS": 0,
        "LANGUAGES": {},
        "STARS PER REPO": {}
    }

    for idx, repo in enumerate(data, 1):
        """DATA MANUPLATION"""
        df["TOTAL REPOSITORIES"] += 1
        df["OWNER"] = repo["owner"]["login"]

        df["TOTAL STARS"] += repo["stargazers_count"]
        df["TOTAL FORKS"] += repo["forks_count"]
        df["TOTAL WATCHERS"] += repo["watchers_count"]
        df["TOTAL OPEN ISSUES"] += repo["open_issues"]

        if (is_repo_active(repo["pushed_at"])):
            df["ACTIVE REPOS"] += 1
        else:
            df["STALE REPOS"] += 1

        if (repo["private"]):
            df["PRIVATE REPOS"] += 1
        else:
            df["PUBLIC REPOS"] += 1

        language = repo["language"] or "Unknown"
        df["LANGUAGES"][language] = df["LANGUAGES"].get(language, 0) + 1

        df["STARS PER REPO"][repo["name"]] = repo["stargazers_count"]

    """DATA PRESENTATION"""
    print(f"""
------------------------GITHUB PROFILE ANALYSIS REPORT------------------------
USERNAME                    : {df['OWNER']}
TOTAL REPOSITORIES          : {df["TOTAL REPOSITORIES"]}
TOTAL WATCHERS              : {df["TOTAL WATCHERS"]}
TOTAL STARS                 : {df["TOTAL STARS"]}
TOTAL FORKS                 : {df["TOTAL FORKS"]}
TOTAL OPEN ISSUES           : {df["TOTAL OPEN ISSUES"]}
PUBLIC REPOSITORIES         : {df['PUBLIC REPOS']}
PRIVATE REPOSITORIES        : {df["PRIVATE REPOS"]}
ACTIVE REPOSITORIES         : {df["ACTIVE REPOS"]}
STALE REPOSITORIES          : {df["STALE REPOS"]}

MAJORITY LANGUAGE           : {sorted(df["LANGUAGES"].items(), key=lambda x: x[1], reverse=True)[0][0]}
MOST POPULAR REPOSITORY     : {sorted(df["STARS PER REPO"].items(), key=lambda x: x[1], reverse=True)[0][0].upper()}
-------------------------------------------------------------------------------
    """)

    """GRAPHICAL REPRESENTATION"""
    fig, ax = plt.subplots(2, 2, figsize=(12.5, 6.5))

    X1 = ["TOTAL VIEWS", "TOTAL STARS", "TOTAL FORKS", "OPEN ISSUES"]
    Y1 = [df["TOTAL WATCHERS"], df["TOTAL STARS"], df["TOTAL FORKS"], df["TOTAL OPEN ISSUES"]]

    ax[0, 0].barh(X1, Y1, color=["#0d5080", "#ff7f0e", "#36be36", "#d62728"], alpha=0.7)
    ax[0, 0].set_title("POPULATITY STATUS", fontsize=14, family="serif")
    ax[0, 0].grid(axis="y", linestyle="--", color="grey")

    X2 = ["PUBLIC REPOS", "PRIVATE REPOS", "ACTIVE REPOS", "STALE REPOS"]
    Y2 = [df["PUBLIC REPOS"], df["PRIVATE REPOS"], df["ACTIVE REPOS"], df["STALE REPOS"]]

    ax[0, 1].barh(X2, Y2, color=["#1f77b4", "#1f77b4", "#2ca02c", "#2ca02c"], alpha=0.7)
    ax[0, 1].set_title("REPOSITORY STATUS", fontsize=14, family="serif")
    ax[0, 1].grid(axis="y", linestyle="--", color="grey")

    X3 = list(map(lambda x: x.upper(), list(df["LANGUAGES"].keys())))
    Y3 = list(df["LANGUAGES"].values())

    ax[1, 0].pie(Y3, labels=X3,
                radius=1.4,
                autopct="%1.2f%%",
                wedgeprops=dict(width=0.5, edgecolor="white")
                )
    ax[1, 0].legend(["MAJORITY LANGUAGE"], loc="upper left", bbox_to_anchor=(-0.8, 1))

    sorted_repos = sorted(df["STARS PER REPO"].items(), key=lambda x: x[1], reverse=True)
    lim = 7 if df["TOTAL REPOSITORIES"] >= 8 else df["TOTAL REPOSITORIES"]
    X4 = []
    Y4 = []
    for i in range(lim):
        X4.append(sorted_repos[i][0])
        Y4.append(sorted_repos[i][1])
    X4 = list(map(lambda x: x.upper(), X4))

    ax[1, 1].barh(X4, Y4, alpha=0.7)
    ax[1, 1].set_title("STARS PER REPOSITORY", fontsize=14, family="serif")

    plt.tight_layout()
    plt.show()
    
else:
    print("NO DATA RECIEVED!")
