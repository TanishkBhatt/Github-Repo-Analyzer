# GitHub Repo Analyzer - Python
![Developer](https://img.shields.io/badge/Developed%20By%20%3A-Tanishk%20Bhatt-white)

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_white.svg)](https://githb-repo-analyzer-tanishkbhatt.streamlit.app)

## Dashboard View 
- App's User Interface

![User-Interface](img/user-interface.png)

- Analyzed Report through Github API.

![Analyzed-Report](img/analyzed-report.png)

- Complete Account Analysis using Matplotlib.

![Graphical-Repr-I](img/visual-analytics-I.png)
![Graphical-Repr-II](img/visual-analytics-II.png)
![Graphical-Repr-III](img/visual-analytics-III.png)

## Table of Contents
- [Dashboard View](#dashboard-view)
- [Introduction](#introduction)
- [Features](#features)
- [Technical Stack Used](#technical-stack-used)
- [Author and Links](#author-and-links)

## Introduction
`GitHub Repository Analyzer` is a Python-based analytics tool that fetches real-time repository data from the GitHub REST API and converts it into meaningful insights.  
The project focuses on `API integration`, `Data Processing`, and `Visual Analytics` to evaluate a GitHub user’s repository activity, popularity, and technology usage.

This project demonstrates real-world usage of:
- REST APIs
- Exception handling
- Data Aggregation
- Graphical Visualization


## Features
### GitHub API Data Fetching
- Fetches repository data using GitHub REST API
- User Account API : `https://api.github.com/users/<username>/`
- User Repositories API : `https://api.github.com/users/<username>/repos/`

- Handles:
  - Invalid usernames
  - API rate limits
  - Request timeouts
- Uses structured exception handling

### Repository Statistics Analysis
Calculates:
- Total repositories
- Public and private repositories
- Active and stale repositories
- Total stars, forks, watchers, and open issues

### Language Usage Analysis
- Extracts programming languages used across repositories
- Identifies the majority language
- Handles missing or null language values

### Popularity Insights
- Identifies the most starred repository
- Calculates stars per repository
- Highlights top repositories based on popularity

### Graphical Visualization
Provides professional visualizations using Matplotlib:
- Popularity metrics comparison
- Repository status overview
- Language distribution (donut chart)
- Stars per repository (top repositories)


## Technical Stack Used
| Component | Technology |
|--------|------------|
| Programming Language |  python3  |
| API Handling |  requests  |
| UI Integration |  streamlit  |
| Date & Time Processing |  datetime  |
| Visualization |  plotly  |
| Data Source |  GitHub APIs  |

## Author and Links
Designed and created by `Tanishk Bhatt` a Student and a Programmer of India, as a real world working project using API Handling and Visualisation.

[![Portfolio](https://img.shields.io/badge/My%20Portfolio-Visit-blue?style=for-the-badge)](https://tanishk-bhatt.vercel.app)
[![YouTube](https://img.shields.io/badge/YouTube-Subscribe-red?style=for-the-badge&logo=youtube&logoColor=white)](https://youtube.com/@Tanishk_Bhatt)

---
