# Korean Language Tutor GPT

## Project Overview
The Korean Language Tutor is an interactive chat application powered by OpenAI's GPT (Generative Pre-trained Transformer) models, 
designed to assist users in practicing and enhancing their Korean language skills. This project integrates a custom-trained language model importing personal data from Ankiweb
to simulate conversations with a virtual tutor, focusing on specific vocab and grammar that is relevant to what is being learned.

## Features
- Interactive chat interface for language learning.
- Customized based on data from Ankiweb app
- Custom prompts based on user's input and learning progress.
- Integration of OpenAI's powerful GPT models for natural language understanding.
- Ability to handle both formal and informal conversation styles.

## Technologies Used
- Python
- Streamlit
- OpenAI API
- LangChain
- JSON for data management

## Screenshots
Below are screenshots illustrating different stages of interaction within the application:

### 1. Initial Page
Here is what the application looks like upon opening, before any interaction. The user is presented with a clean interface ready to start the conversation.
![Blank](https://github.com/user-attachments/assets/614de68e-45d0-4568-bace-ecafa1e465d8)

### 2. Starting the Conversation
This screenshot shows the application after the user has clicked the "Start Conversation" button. The tutor initiates the conversation by asking whether the user prefers formal or informal speech.
![start conversation](https://github.com/user-attachments/assets/1aecf162-7b44-4c7a-a61a-e69b72c871ec)

### 3. Tutor's Response
After the user responds to the initial query, this screenshot captures the tutor's follow-up, which includes a culturally relevant question designed to further the dialogue.
![Response](https://github.com/user-attachments/assets/b94747e2-33bd-4656-b9fb-65bae22c1376)

## Conversation Translations
For clarity and to assist viewers who may not understand Korean, below are translations of the conversation depicted in the screenshots:

- **Initial Tutor Question:** "Hello! I'm glad I could help you with your Korean studies. First of all, which do you prefer, honorifics (formal words) or informal speech?
And I have a question. I saw the word "college student," what subjects or activities are you interested in as a college student? Or do you have any thoughts on college life?"
- **User Response:** "informal speech. I am no longer a college student, but I enjoyed learning about Chemistry, and I miss college life sometimes."
- **Tutor Follow-Up Question:** "Oh, I see! You missed college life and enjoyed learning chemistry. Then, what topic or experiment was the most memorable in chemistry? And what are you doing now?"

## Installation and Usage
To run this application locally, follow these steps:
1. Clone this repository.
2. Ensure you have Python and Streamlit installed.
3. Navigate to the application directory and run the command:
streamlit run chatgpt.py
4. The application will open in your web browser at `localhost:8501`.

### Prerequisites
- Python 3.8 or higher
- pip
