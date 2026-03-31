import streamlit as st
from src import *

st.set_page_config(page_title='Github Repo Analyzer')
st.title("GITHUB REPO ANALYZER")
st.divider()

st.markdown("""
**GitHub Repo Analyzer** is a Python-based Analytics Tool that Fetches Real-Time Account and Repository Data from the GitHub REST API and converts it into meaningful insights. Focusing on **API Integration**, **Data Processing**, and **Visual Analytics** to evaluate one's GitHub Activity, Popularity, and Technology usage.
""")
st.markdown("###### [ Maximum Repos Fetching Limit : 500 ]")
st.markdown("")

with st.form(key='github_repo_analyzer'):
    username: str = st.text_input("ENTER THE USERNAME YOU WANT TO FETCH DATA OF")
    get_report: bool = st.form_submit_button("GET ANALYZED REPORT")
        
if get_report:
    if not username.strip():
        st.warning("PLEASE ENTER THE USERNAME!")
    else:
        try:
            acc_data = fetch_account_data(username)
            repo_data = fetch_repos_data(username)

            acc_info = extract_account_info(acc_data)
            repo_details, majority_lang, popular_repo = extract_repos_info(repo_data)

            majority_lang_fig = majority_language_plot(majority_lang) 
            popular_repo_fig = popular_repo_plot(popular_repo)
            activity_status_fig = activity_status_plot(repo_details)

        except Exception as e:
            st.error(e)
        else:
            st.markdown("")
            st.header("ANALYZED REPORTS")
            st.divider()

            col1, col2 = st.columns(2)
            with col1:
                st.markdown("##### ACCOUNT DETAILS")
                st.dataframe(acc_info)
                st.markdown("##### MAJORITY LANGUAGE")
                st.dataframe(majority_lang)
            with col2:
                st.markdown("##### REPOSITORY ACTIVITY")
                st.dataframe(repo_details)
                st.markdown("##### POPULAR REPOSITORY")
                st.dataframe(popular_repo)

            st.divider()
            st.header("VISUAL ANALYTICS")
            st.plotly_chart(activity_status_fig)
            st.plotly_chart(majority_lang_fig)
            st.plotly_chart(popular_repo_fig)

st.divider()
st.caption("MADE BY TANISHK - A STUDENT AND A PROGRAMMER")