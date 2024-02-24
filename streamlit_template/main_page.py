import streamlit as st

st.markdown("# Welcome to my Website!")
st.sidebar.markdown("# Main Page")

st.write("Click on a page to see racer stats")

link = '(To my Github Pages Site)(https://jacobnd20.github.io/GitHub_test_assign/)'
st.markdown(link, unsafe_allow_html=True)