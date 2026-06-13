import streamlit as st
from langchain_community.document_loaders import WebBaseLoader

from chains import Chain
from portfolio import Portfolio
from utils import clean_text


def create_streamlit_app(llm, portfolio, clean_text):
    st.title("📧 Cold Mail Generator")

    url_input = st.text_input(
        "Enter a URL:"
    )

    submit_button = st.button("Submit")

    if submit_button:
        try:
            with st.spinner("Analyzing job posting..."):

                loader = WebBaseLoader([url_input])

                page_content = loader.load().pop().page_content
                data = clean_text(page_content)

                portfolio.load_portfolio()

                jobs = llm.extract_jobs(data)

                if not jobs:
                    st.warning("No jobs found.")
                    return

                for idx, job in enumerate(jobs, start=1):

                    skills = job.get("skills", [])

                    # query_links already returns clean unique links
                    links = portfolio.query_links(skills)

                    email = llm.write_mail(job, links)

                    st.subheader(
                        f"Job #{idx}: {job.get('role', 'Unknown Role')}"
                    )

                    st.code(email, language="markdown")

                    if links:
                        with st.expander("Matched Portfolio Links"):
                            for link in links:
                                st.write(link)

        except Exception as e:
            st.error(f"An Error Occurred: {str(e)}")


if __name__ == "__main__":
    st.set_page_config(
        layout="wide",
        page_title="Cold Email Generator",
        page_icon="📧"
    )

    chain = Chain()
    portfolio = Portfolio()

    create_streamlit_app(chain, portfolio, clean_text)