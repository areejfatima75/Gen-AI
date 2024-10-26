import streamlit as st
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load the model and tokenizer from Hugging Face
@st.cache_resource  # Cache the model and tokenizer for faster loading
def load_model():
    model_name = "microsoft/DialoGPT-small"  # You can use other models here
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    return tokenizer, model

tokenizer, model = load_model()

# Set up the Streamlit app title and description
st.title("🤖 Simple Chatbot App")
st.write("Ask me anything, and I’ll do my best to respond!")

# Input box for user messages
user_input = st.text_input("You:", placeholder="Type your message here...")

# Chat history for tracking conversation
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Process the user input and generate a response
if user_input:
    # Tokenize and encode user input with the model's tokenizer
    inputs = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors="pt")

    # Concatenate chat history with user input
    chat_history_ids = torch.cat([torch.tensor(st.session_state.chat_history), inputs], dim=-1) if st.session_state.chat_history else inputs

    # Generate a response from the model
    response_ids = model.generate(chat_history_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)
    response = tokenizer.decode(response_ids[:, chat_history_ids.shape[-1]:][0], skip_special_tokens=True)

    # Update chat history and display response
    st.session_state.chat_history.append(inputs)
    st.write("🤖 Chatbot:", response)
