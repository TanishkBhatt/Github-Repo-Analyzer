from datetime import datetime, timezone

def is_repo_active(pushed_at: str) -> bool:
        STALE_DAYS = 90
        if not pushed_at: return False

        pushed_date = datetime.strptime(
            pushed_at, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)

        today = datetime.now(timezone.utc)
        days_since_push = (today - pushed_date).days
        return days_since_push <= STALE_DAYS

def get_data(data: list[dict]) -> tuple[dict, dict, dict]:
    basic_details = {
        "owner": None,
        "total_repos": 0,
        "total_stars": 0,
        "total_forks": 0,
        "total_watchers": 0,
        "open_issues": 0,
        "active_repos": 0,
        "stale_repos": 0,
        "public_repos": 0,
        "private_repos": 0
        }

    majority_lang = {}
    stars_per_repo = {}

    for repo in data:
        basic_details["total_repos"] += 1
        basic_details["owner"] = repo["owner"]["login"]
        basic_details["total_stars"] += repo["stargazers_count"]
        basic_details["total_forks"] += repo["forks_count"]
        basic_details["total_watchers"] += repo["watchers_count"]
        basic_details["open_issues"] += repo["open_issues"]

        if (is_repo_active(repo["pushed_at"])): 
            basic_details["active_repos"] += 1
        else: 
            basic_details["stale_repos"] += 1

        if (repo["private"]): 
            basic_details["private_repos"] += 1
        else: 
            basic_details["public_repos"] += 1

        language = repo["language"] or "Unknown"
        majority_lang[language] = majority_lang.get(language, 0) + 1

        stars_per_repo[repo["name"]] = repo["stargazers_count"]

    limit = 10 if len(data) > 10 else len(data)

    majority_lang = dict(sorted(majority_lang.items(),
                                key=lambda x:x[1],
                                reverse=True))

    stars_per_repo = dict(sorted(stars_per_repo.items(),
                                key=lambda x:x[1],
                                reverse=True)[:limit])

    return (basic_details, majority_lang, stars_per_repo)