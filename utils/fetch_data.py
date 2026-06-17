import requests
import streamlit as st

def fetch_account_data(username: str) -> dict:
    url = f"https://api.github.com/users/{username}"            # Base URL
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            raise Exception("USERNAME NOT FOUND")
        else:
            raise Exception("FAILED TO RETRIVE DATA")

    except requests.exceptions.Timeout:
        raise Exception("API REQUEST TIMED OUT")
    except Exception as error:
        raise Exception(error)

def fetch_repos_data(username: str) -> list[dict]:
    TOKEN = st.secrets["TOKEN"]
    repos_data = []
    page = 1
    per_page = 100

    while True:
        if len(repos_data) == 500:
                break   # Maximum Repos Fetching Limit
        
        url = f"https://api.github.com/users/{username}/repos"      # Base URL
        params = {"per_page": per_page,                             # Pagination
                  "page": page,
                  "sort": "updated"}
        headers = {"Authorization": f"Bearer {TOKEN}",              # Authorization
                  "Accept": "application/vnd.github+json"}

        try:
            response = requests.get(url, 
                                params=params, 
                                headers=headers,
                                timeout=10)

            if response.status_code == 200:
                repo = response.json()
                if not repo: 
                    break
                repos_data.extend(repo)
                page += 1
            
            elif response.status_code == 404:
                raise Exception("USERNAME NOT FOUND")
            else:
                raise Exception("FAILED TO RETRIVE DATA")

        except requests.exceptions.Timeout:
            raise Exception("API REQUEST TIMED OUT")
        except Exception as error:
            raise Exception(error)
        
    return repos_data