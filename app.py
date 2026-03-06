import streamlit as st
from src.logic import fetch_data, get_data, plot_data

st.title("GITHUB REPO ANALYZER")
st.set_page_config(page_title='Github Repo Analyzer')

st.markdown("""
**GitHub Repo Analyzer** is a Python-based Analytics Tool that Fetches Real-Time Repository Data from the GitHub REST API and converts it into meaningful insights. Focusing on **API Integration**, **Data Processing**, and **Visual Analytics** to evaluate one's GitHub Repository Activity, Popularity, and Technology usage.
""")
st.markdown("")

if "TOKEN" not in st.session_state:
    st.session_state.TOKEN = ""

with st.form(key='github_repo_analyzer'):
    TOKEN: str = st.text_input("PUT YOUR GITHUB DEV TOKEN HERE")
    username: str = st.text_input("ENTER THE USERNAME YOU WANT TO FETCH DATA OF")

    col1, col2, col3 = st.columns(3)
    with col2:
        get_report: bool = st.form_submit_button("GET ANALYZED REPORT")

if get_report:
    if not (username.strip() and TOKEN.strip()):
        st.warning("First Carefully Enter the TOKEN and the Username")
    else:
        try:
            data: list[dict] = fetch_data(username, TOKEN)

            df = get_data(data)
            st.subheader("Analyzed Report")
            st.json(df)

            fig = plot_data(df)
            st.subheader("Visual Analytics")
            st.pyplot(fig)
            st.divider()

        except Exception as error:
            st.error(error)

st.caption("MADE BY TANISHK - A STUDENT AND A PROGRAMMER")