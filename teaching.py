import streamlit as st 
from openai import OpenAI

API_KEY=st.secrets["API_KEY"]

client=OpenAI(api_key=API_KEY,base_url=
"https://api.groq.com/openai/v1")

Model="openai/gpt-oss-20b"
def gen(prompt):
    try:
        response=client.chat.completions.create(model=Model,messages=[{"role":"user","content":prompt}],temperature=0.3,max_tokens=512)
        return response.choices[0].message.content
    except Exception as e:
        return f"Error{e}"

st.set_page_config(page_title="AI learning assistant ",layout="centered")
st.title("Ai Teaching Assistant")
st.write("ask me any thing about various subjects.")
if "history" not in st.session_state:
    st.session_state.history=[]
question=st.text_input("enter your question")
if st.button("ask"):
    if question.strip():
        with st.spinner("genrating response"):
            answer=gen(question)
        st.session_state.history.insert(0,{"question":question , "answer":answer})

    else:
        st.warning("please enter a question")
if st.session_state.history:
    st.markdown("### Conversation History")
    for i,chat in enumerate(st.session_state.history,1):
        st.markdown(f"q{i}:{chat['question']}")
        st.write(chat["answer"])
        st.divider()

if st.button("clear conversation"):
    st.session_state.history=[]
    st.rerun()
