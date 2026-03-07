import requests

def fetch_data_tokenized(username: str, TOKEN: str) -> list[dict]:
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
            response = requests.get(url, 
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

        except requests.exceptions.Timeout:
            raise Exception("API Request Timed Out")
        except Exception as f:
            raise Exception(f"Request Failed : {f}")
        
    return repos

def fetch_data_untokenized(username: str) -> list[dict]:
    url = f"https://api.github.com/users/{username}/repos"

    try:
        response = requests.get(url,
                            timeout=10)

        if response.status_code == 200:
            repos = response.json()
            
        elif response.status_code == 404:
            raise Exception("Error 404 : Username Not Found")
        elif response.status_code == 403:
            raise Exception("Error 403 : Rate Limit Exceeds")
        else:
            raise Exception(f"Something Went Wrong : {response.status_code}")

    except requests.exceptions.Timeout:
        raise Exception("API Request Timed Out")
    except Exception as f:
        raise Exception(f"Request Failed : {f}")
        
    return repos