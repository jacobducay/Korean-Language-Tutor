# streamlit run "P:\Program Files\Python_programs\Study App\chatgpt.py" -- server.address 192.168.0.108 --server.port 8501

import os
import sys
import json

import streamlit as st
import streamlit 
import openai

from apikey import apikey
import openai
from langchain_openai import ChatOpenAI

def main():
    # Apply custom CSS
    st.markdown(
        """
        <style>
            textarea[aria-label="Conversation"] {
                color: #FFFFFF !important;  /* Make text color white */
                font-size: 24px !important; /* Increase font size */
                background-color !important: black;
             }
             input[aria-label="Type your sentence here:"] {
                font-size: 24px !important; /* Increase font size */
        </style>
        """, unsafe_allow_html=True
    )

    os.environ["OPENAI_API_KEY"] = apikey
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.9,
        max_tokens=150,
        api_key=apikey
    )

    st.title('🇰🇷 Korean Language Tutor')

    filepath = "P:/Program Files/Python_programs/Study App/Filter/cleaned_korean_text.json"
    with open(filepath, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Loading the data text into the session
    if 'data_text' not in st.session_state:
        st.session_state.data_text = str(data)
    
    initial_prompt = (
            "You will act as an expert Korean language tutor, emulating a mid-20s male from Seoul, to help me, "
            "a beginner/intermediate Korean learner, enhance my conversational Korean skills. Please begin our session by asking whether I prefer to use formal or informal speech. "
            "Immediately follow this with a unique question crafted from the specific text data I provide from my language learning app. "
            "This text should be the primary basis for our entire conversation ensuring that all topics discussed are directly relevant to what I am currently learning. "
            "Adjust the language complexity to be simpler for better comprehension. Focus our conversation on themes related to everyday life—such as hobbies, school, work, transportation, friends, and family—while incorporating relevant Korean cultural topics like food, social norms, and popular media. "
            "Utilize personal stories, native Korean exclamations, and colloquial expressions from the Seoul dialect to make our chats authentic. "
            "When correcting my mistakes, provide explanations in both English and Korean, focusing on feedback that helps me speak more naturally in Korean. If I navigate unfamiliar topics well, continue; if mistakes occur, revert to the provided text topics. "
            "Offer spontaneous, constructive feedback throughout the session and provide a comprehensive review at the end. The session should conclude when I indicate I am finished, allowing for a flexible duration. "
            "Here is the text data from my learning app, please use this to create your unique question to begin our tutoring session: " + st.session_state.data_text )

    if 'messages' not in st.session_state:
        st.session_state.messages = []

    # Starting the conversation with the custom prompt
    if st.button("Start Conversation"):
        response = llm.invoke([{"role": "system", "content": initial_prompt}])
        st.session_state.messages = [("system", response.content)]

    user_input = st.text_input("Type your sentence here:")
    if st.button('Send', key="send_button"):
        if user_input:
            st.session_state.messages.append(("human", user_input))
            response = llm.invoke([{"role": "system", "content": initial_prompt}, {"role": "human", "content": user_input}])
            st.session_state.messages.append(("system", response.content))
            # Clear input field
            st.session_state.user_input = ""

    # Display the conversation history
    if 'messages' in st.session_state:
        conversation_text = "\n".join([f"{role.title()}: {content}" for role, content in reversed(st.session_state.messages)])
        st.text_area("Conversation", value=conversation_text, height=300, disabled=True)

if __name__ == "__main__":
    main()