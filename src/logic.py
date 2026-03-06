import requests as req
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from datetime import datetime, timezone

def fetch_data(username: str, TOKEN: str) -> list[dict]:
    repos = []
    page = 1
    per_page = 100

    while True:
        url = f"https://api.github.com/users/{username}/repos"
        params = {"per_page": per_page,
                  "page": page,
                  "sort": "updated"}
        headers = {"Authorization": f"Bearer {TOKEN}",
                  "Accept": "application/vnd.github+json"}

        try:
            response = req.get(url, 
                                params=params, 
                                headers=headers,
                                timeout=10)

            if response.status_code == 200:
                repo = response.json()
                if not repo: break
                repos.extend(repo)
                page += 1
            
            elif response.status_code == 404:
                raise Exception("Error 404 : Username Not Found")
            elif response.status_code == 403:
                raise Exception("Error 403 : Rate Limit Exceeds")
            else:
                raise Exception(f"Something Went Wrong : {response.status_code}")

        except req.exceptions.Timeout:
            raise Exception("API Request Timed Out")
        except Exception as f:
            raise Exception(f"Request Failed : {f}")
        
    return repos

def get_data(data: list[dict]) -> dict:
    def is_repo_active(pushed_at: str) -> bool:
        STALE_DAYS = 90
        if not pushed_at: return False

        pushed_date = datetime.strptime(
            pushed_at, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)

        today = datetime.now(timezone.utc)
        days_since_push = (today - pushed_date).days
        return days_since_push <= STALE_DAYS

    df = {"owner": None,
        "total_repos": 0,
        "total_stars": 0,
        "total_forks": 0,
        "total_watchers": 0,
        "open_issues": 0,
        "active_repos": 0,
        "stale_repos": 0,
        "public_repos": 0,
        "private_repos": 0,
        "lang": {},
        "stars_per_repo": {}}

    for repo in data:
        df["total_repos"] += 1
        df["owner"] = repo["owner"]["login"]
        df["total_stars"] += repo["stargazers_count"]
        df["total_forks"] += repo["forks_count"]
        df["total_watchers"] += repo["watchers_count"]
        df["open_issues"] += repo["open_issues"]

        if (is_repo_active(repo["pushed_at"])): df["active_repos"] += 1
        else: df["stale_repos"] += 1

        if (repo["private"]): df["private_repos"] += 1
        else: df["public_repos"] += 1

        language = repo["language"] or "Unknown"
        df["lang"][language] = df["lang"].get(language, 0) + 1

        df["stars_per_repo"][repo["name"]] = repo["stargazers_count"]

    return df

def plot_data(df: dict) -> Figure:
    X1 = ["TOTAL VIEWS", "TOTAL STARS", "TOTAL FORKS", "OPEN ISSUES"]
    Y1 = [df["total_watchers"], df["total_stars"], df["total_forks"], df["open_issues"]]

    X2 = ["PUBLIC REPOS", "PRIVATE REPOS", "ACTIVE REPOS", "STALE REPOS"]
    Y2 = [df["public_repos"], df["private_repos"], df["active_repos"], df["stale_repos"]]

    X3 = list(map(lambda x: x.upper(), list(df["lang"].keys())))
    Y3 = list(df["lang"].values())

    sorted_repos = sorted(df["stars_per_repo"].items(), 
                          key=lambda x: x[1], 
                          reverse=True)
    limit = 5 if df["total_repos"] >= 8 else df["total_repos"]

    X4 = [item[0] for item in sorted_repos[:limit]]
    Y4 = [item[1] for item in sorted_repos[:limit]]

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