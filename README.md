# GitHub Repository Analyzer - Python

## Introduction
`GitHub Repository Analyzer` is a Python-based analytics tool that fetches real-time repository data from the GitHub REST API and converts it into meaningful insights.  
The project focuses on `API integration`, `Data Processing`, and `Visual Analytics` to evaluate a GitHub user’s repository activity, popularity, and technology usage.

This project demonstrates real-world usage of:
- REST APIs
- Exception handling
- Data Aggregation
- Graphical Visualization

---

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Technical Stack Used](#technical-stack-used)
- [How to Run the Project](#how-to-run-the-project)
- [Future Scope](#-future-scope)
- [Author](#author)
- [Links](#links)

---

## Features

### GitHub API Data Fetching
- Fetches repository data using GitHub REST API
- Handles:
  - Invalid usernames
  - API rate limits
  - Request timeouts
- Uses structured exception handling

---

### Repository Statistics Analysis
Calculates:
- Total repositories
- Public and private repositories
- Active and stale repositories
- Total stars, forks, watchers, and open issues

---

### Activity Status Detection
- Determines repository activity based on last pushed date
- Uses a fixed inactivity threshold to classify stale repositories

---

### Language Usage Analysis
- Extracts programming languages used across repositories
- Identifies the majority language
- Handles missing or null language values

---

### Popularity Insights
- Identifies the most starred repository
- Calculates stars per repository
- Highlights top repositories based on popularity

---

### Graphical Visualization
Provides professional visualizations using Matplotlib:
- Popularity metrics comparison
- Repository status overview
- Language distribution (donut chart)
- Stars per repository (top repositories)

---

## Technical Stack Used
| Component | Technology |
|--------|------------|
| Programming Language | `Python3` |
| API Handling | `requests` |
| Date & Time Processing | `datetime` |
| Visualization | `matplotlib` |
| Data Source | GitHub REST API |

---

## How to Run the Project?

### Clone the Repository
```bash
git clone https://github.com/TanishkBhatt/Github-Repo-Analyzer.git
```

### Install Required Libraries
```bash
pip install requests matplotlib
```

### Run the Script
```bash
python main.py
```
#### The program will generate:

- A detailed GitHub profile analysis report
- Multiple graphical visualizations

----

## Future Scopes
- GitHub authentication using personal access tokens
- Export reports as PDF or CSV
- Support for organization accounts
- Interactive dashboard using Streamlit or Dash
- User-to-user GitHub profile comparison

---

## Author
Designed and created by `Tanishk Bhatt` a Student and a Programmer of India, as a real world working project using API Handling and Visualisation.

---

## Links
- GitHub REST API URL :
https://api.github.com/users/Username/repos

- Matplotlib Documentation :
https://matplotlib.org/stable/index.html

- Requests Library Documentation :
https://docs.python-requests.org/

- Protfolio : https://tanishkbhatt.github.io/Portfolio/

- Github : https://github.com/TanishkBhatt/

- YouTube : https://youtube.com/@TanishkBhatt-x6w/

----
