import streamlit as st
from src import *

st.title("GITHUB REPO ANALYZER")
st.set_page_config(page_title='Github Repo Analyzer')

st.markdown("""
**GitHub Repo Analyzer** is a Python-based Analytics Tool that Fetches Real-Time Repository Data from the GitHub REST API and converts it into meaningful insights. Focusing on **API Integration**, **Data Processing**, and **Visual Analytics** to evaluate one's GitHub Repository Activity, Popularity, and Technology usage.
""")
st.markdown("")

mode: str = st.selectbox("SELECT MODE OF FETCHING DATA",
            ["WITH TOKENIZATION", "WITHOUT TOKENIZATION"])
st.markdown("")

if mode == "WITH TOKENIZATION":
    with st.form(key='github_repo_analyzer_tokenized'):
        TOKEN: str = st.text_input("PUT YOUR GITHUB DEV TOKEN HERE", type='password')
        username: str = st.text_input("ENTER THE USERNAME YOU WANT TO FETCH DATA OF")
        valid: bool = username.strip() and TOKEN.strip()

        col1, col2, col3 = st.columns(3)
        with col2:
            get_report: bool = st.form_submit_button("GET ANALYZED REPORT")
        
    if get_report:
        if not valid:
            st.warning("First Carefully Enter the Required Details")
        else:
            data: list[dict] = fetch_data_tokenized(username, TOKEN)
            try:
                basic_details, majority_lang, stars_per_repo = get_data(data)
                fig = plot_data(basic_details, majority_lang, stars_per_repo)

                st.markdown("")
                st.header("ANALYZED REPORTS")
                st.divider()

                col1, col2, col3 = st.columns(3)
                with col1:
                    st.markdown("##### BASIC DETAILS")
                    st.dataframe(basic_details)
                with col2:
                    st.markdown("##### REPO POPULARIRY")
                    st.dataframe(stars_per_repo)
                with col3:
                    st.markdown("##### MAJORITY LANGUAGE")
                    st.dataframe(majority_lang)
                st.divider()

                st.header("VISUAL ANALYTICS")
                st.divider()
                st.pyplot(fig)
                st.divider()

            except Exception as error:
                    st.error(error)
        
if mode == "WITHOUT TOKENIZATION":
    with st.form(key='github_repo_analyzer_untokenized'):
        username: str = st.text_input("ENTER THE USERNAME YOU WANT TO FETCH DATA OF")
        st.warning("NOTE : This Will Generate Report Of Just Recent 30 Repos")
        valid: bool = username.strip() 

        col1, col2, col3 = st.columns(3)
        with col2:
            get_report: bool = st.form_submit_button("GET ANALYZED REPORT")
        
    if get_report:
        if not valid:
            st.warning("First Carefully Enter the Required Details")
        else:
            data: list[dict] = fetch_data_untokenized(username)
            try:
                basic_details, majority_lang, stars_per_repo = get_data(data)
                fig = plot_data(basic_details, majority_lang, stars_per_repo)

                st.markdown("")
                st.header("ANALYZED REPORTS")
                st.divider()

                col1, col2, col3 = st.columns(3)
                with col1:
                    st.markdown("##### BASIC DETAILS")
                    st.dataframe(basic_details)
                with col2:
                    st.markdown("##### REPO POPULARIRY")
                    st.dataframe(stars_per_repo)
                with col3:
                    st.markdown("##### MAJORITY LANGUAGE")
                    st.dataframe(majority_lang)
                st.divider()

                st.header("VISUAL ANALYTICS")
                st.divider()
                st.pyplot(fig)
                st.divider()

            except Exception as error:
                    st.error(error)

st.caption("MADE BY TANISHK - A STUDENT AND A PROGRAMMER")