from datetime import datetime, timezone

def extract_account_info(acc_data: dict) -> dict:
    date = datetime.strptime(acc_data["created_at"], "%Y-%m-%dT%H:%M:%SZ")
    active_from = date.strftime("%b %Y")

    return {
        "login_id": acc_data["login"],
        "html_url": acc_data["html_url"].removeprefix("https://"),
        "name": acc_data["name"],
        "bio": acc_data["bio"],
        "followers": acc_data["followers"],
        "following": acc_data["following"],
        "active_from": active_from
        }

def is_repo_active(pushed_at: str) -> bool:
    STALE_DAYS = 90
    if not pushed_at: return False
    pushed_date = datetime.strptime(pushed_at, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
    today = datetime.now(timezone.utc)
    days_since_push = (today - pushed_date).days
    return days_since_push <= STALE_DAYS

def extract_repos_info(data: list[dict]) -> tuple[dict, dict, dict]:
    details = { "total_repos": 0,
                "active_repos": 0,
                "public_repos": 0,
                "total_watchers": 0,
                "total_stars": 0,
                "total_forks": 0,
                "open_issues": 0
              }

    majority_lang = {}
    popular_repos = {}

    for repo in data:
        details["total_repos"] += 1
        details["total_stars"] += repo["stargazers_count"]
        details["total_forks"] += repo["forks_count"]
        details["total_watchers"] += repo["watchers_count"]
        details["open_issues"] += repo["open_issues"]

        if (is_repo_active(repo["pushed_at"])): 
            details["active_repos"] += 1
        if not (repo["private"]): 
            details["public_repos"] += 1

        language = repo["language"] or "Unknown"
        majority_lang[language] = majority_lang.get(language, 0) + 1
        popular_repos[repo["name"]] = repo["stargazers_count"]

    majority_lang = dict(sorted(majority_lang.items(), key=lambda x:x[1], reverse=True)[:5])
    popular_repos = dict(sorted(popular_repos.items(), key=lambda x:x[1], reverse=True)[:5])

    return (details, majority_lang, popular_repos)