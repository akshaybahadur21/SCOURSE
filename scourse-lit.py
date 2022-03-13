import streamlit as st

from scourse import SCOURSE
from src.algo.course_similarity import course_sim


@st.cache(suppress_st_warning=True)
def cache_embeddings():
    # This function will only be run the first time it's called
    scourse = SCOURSE()
    return scourse


st.set_page_config(page_title='SCOURSE',
                   layout='wide')

st.image("resources/scourse_logo.png", width=500)
st.header("SCOURSE")
st.markdown("""
This application aims to generate smart course recommendations for students. 
 - As input, it takes the job role the student wants to aim for, and any skills the student wants to gain. 
 - Top 10 courses are displayed to the user using Machine Learning and Artificial Intelligence. 
""")

st.markdown("""
##### Made with ❤️ and 🦙 by Abhinaav, Akshay, Chirag and Naman
""")

with st.sidebar.header('1. Enter the Desired Role'):
    role = st.sidebar.text_input("Desired Role", "Data Scientist")

with st.sidebar.header('1. Enter the desired Skill Set'):
    skill = st.sidebar.text_input("Desired Skill Set", "Data Science, Machine Learning, Statisics, Python")

if st.sidebar.button('Press to generate courselist'):
    st.subheader("Generating the course recommendations")
    if len(role) or len(skill) != 0:
        sorted_dict, relevantJobDict = course_sim("{} {}".format(role, skill))
        for t in sorted_dict:
            score = ((t[1] * 100) / 3.0)
            stylishScore = "{:.2f}%".format(score)
            jobListString = ' '.join(str(v) for v in relevantJobDict[t[0]])
            st.write("Course:", t[0])
            st.write("Relevance Score:", stylishScore)
            st.write('-----------------------------------------------------------\n')
    else:
        st.warning("Kindly validate the input")
