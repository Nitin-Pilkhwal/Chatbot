

import streamlit as st
import json
from streamlit_chat import message
from bardapi import Bard

#setting up credentials.json file
with open('credentials.json','r') as f:
    file = json.load(f)
    token = file['token']


#function to generate the output
def generate_response(prompt):
    bard = Bard(token=token)
    response = bard.get_answer(prompt)['content']
    return response

#function to get the input
def get_text():
    input_text = st.text_input("","",key='input')
    return input_text

st.title("🤖Personal AI chatbot")

user_input = get_text()
print(st.session_state)
if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

st.sidebar.title('Chats')

if user_input:
    print(user_input)
    output = generate_response(user_input)
    print(output)
    st.session_state['past'].append(user_input)
    st.session_state['generated'].append(output)

if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1,-1,-1):
        message(st.session_state['generated'][i],key=str(i))
        message(st.session_state['past'][i], key="user"+str(i), is_user=True)

#Set up main content
changes = '''
<style>
[data-testid="stAppViewContainer"]
{
    background-image:url("https://images.unsplash.com/photo-1508739773434-c26b3d09e071?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1170&q=80");
    background-size:cover;
}
div.css-1y35n86
{
    background-color: transparent;
}

</style>
'''
st.markdown(changes,unsafe_allow_html=True)