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
st.header("SCOURSE")
st.markdown("""
You can get smart course recommendations for your targeted job roles and skillset.  
On the left pane, provide your target job role and a comma separated list of skills you are aiming to gain.  
Top 10 courses will be displayed in the order of relevance to your input.
""")

st.markdown("""
##### Made with ❤️ and 🦙 by [Abhinaav](https://abhinaav.com), [Akshay](https://akshaybahadur.com), [Chirag](https://linkedin.com/in/chirag-huria), and [Naman](https://namanarora.me)
""")

with st.sidebar.header('1. Enter the Desired Role'):
    role = st.sidebar.text_input("Desired Role", "Data Scientist")

with st.sidebar.header('1. Enter the desired Skill Set'):
    skill = st.sidebar.text_input("Desired Skill Set", "Data Science, Machine Learning, Statisics, Python")

if st.sidebar.button('Press to generate courselist'):
    st.write('')
    st.subheader("Generating the course recommendations")
    if len(role) or len(skill) != 0:
        sorted_dict, relevantJobDict = course_sim("{} {}".format(role, skill))
        for t in sorted_dict:
            score = ((t[1] * 100) / 3.0)
            stylishScore = "{:.2f}%".format(score)
            jobListString = ' '.join(str(v) for v in relevantJobDict[t[0]])
            st.write("", t[0])
            # st.write("Relevance Score:", stylishScore)
            st.write('Match: ', stylishScore)
            st.progress(int(score))
            st.write('-----------------------------------------------------------\n')
    else:
        st.warning("Kindly validate the input")
