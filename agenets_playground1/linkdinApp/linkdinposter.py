import os

from linkdinBlogHF import linkdin_blog_free
import streamlit as st

if __name__ == "__main__":
    os.environ["HF_TOKEN"] = st.secrets["HF_TOKEN"]
    st.title("LinkdIn Post Generator")
    user_input = st.text_input("Enter your achievment:")

    placeholder = st.empty()

    if st.button("Submit"):
        if user_input:
            # placeholder.empty()
            st.empty()I 
            o = linkdin_blog_free(user_input, 3)
            st.write(o[0])
        else:
            st.warning("Please enter some text first.")
