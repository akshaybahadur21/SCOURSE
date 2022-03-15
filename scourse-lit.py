import streamlit as st


@st.cache(suppress_st_warning=True, allow_output_mutation=True)
def cache_embeddings():
    '''
    Generates embeddings and caches them for faster reload
    '''
    global SCOURSE
    from scourse import SCOURSE


@st.cache(suppress_st_warning=True, allow_output_mutation=True)
def cache_similarity():
    '''
    Returns a function to get course similarity metric 
    '''
    from src.algo.course_similarity import course_sim
    return course_sim


st.set_page_config(page_title='SCOURSE',
                   layout='wide')

with st.spinner('Please wait while we load up the data'):
    cache_embeddings()
    course_sim = cache_similarity()

st.image("resources/logo4.png", width=200)
st.header("SCOURSE 🔍🎓")
st.markdown("""A smart course recommender for CMU students.""")
st.warning("Disclaimer : The course recommender is assertive in nature and has been developed as part of a project.")
st.subheader("How to use Scourse")
st.markdown("""
- Select the department from the dropdown (Default : All Departments)
- Select the Desired Role from the dropdown
- Enter the Desired Skill Set
""")

st.markdown("""
##### Made with ❤️ and 🦙 by [Abhinaav Singh](https://abhinaav.com), [Akshay Bahadur](https://akshaybahadur.com), [Chirag Huria](https://linkedin.com/in/chirag-huria), and [Naman Arora](https://namanarora.me)
""")

st.markdown(
    """
    <style>
    [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
        width: 500px;
    }
    [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
        width: 500px;
        margin-left: -500px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.sidebar.info("Data Sources : Smartevals, coursicle and Carnegie Mellon University course catalogue")
with st.sidebar.header('Select Department'):
    dept = st.sidebar.multiselect(
        'Select the Department',
        ['All Departments', 'Heinz College of Information Systems and Public Policy'],
        default="All Departments")

with st.sidebar.header('Select the Desired Role'):
    role = st.sidebar.selectbox(
        'Select the Desired Role',
        ['Data Analyst', 'Data Scientist', 'Product Manager', 'Software Engineer', 'Consultant',
         'Business Intelligence Engineer', 'Business Analyst', 'System/Solutions Architect'])

with st.sidebar.header('Enter the Desired Skill Set'):
    skill = st.sidebar.text_input("eg : Data Science, Machine Learning, Statistics, Python", "")

if st.sidebar.button('Press to generate the courselist'):
    st.write('')
    st.subheader("Generating the course recommendations")
    if len(role) != 0 and len(skill) != 0 and len(dept) != 0:
        sorted_dict, relevantJobDict = course_sim("{} {}".format(role, skill))
        for t in sorted_dict:
            score = ((t[1] * 100) / 3.0)
            stylishScore = "{:.2f}%".format(score)
            jobListString = ' '.join(str(v) for v in relevantJobDict[t[0]])
            st.write("", t[0])
            st.write('Match: ', stylishScore)
            st.progress(int(score))
            st.write('-----------------------------------------------------------\n')
    else:
        st.warning("Kindly validate the input")
