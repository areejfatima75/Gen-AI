import streamlit as st
from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration

# Load the model and tokenizer
@st.cache_resource
def load_model():
    model_name = "facebook/blenderbot-400M-distill"
    tokenizer = BlenderbotTokenizer.from_pretrained(model_name)
    model = BlenderbotForConditionalGeneration.from_pretrained(model_name)
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
    # Tokenize and encode the user input along with chat history
    inputs = tokenizer(user_input, return_tensors="pt")
    
    # Generate a response from the model
    reply_ids = model.generate(**inputs)
    response = tokenizer.decode(reply_ids[0], skip_special_tokens=True)

    # Display response
    st.session_state.chat_history.append(user_input)
    st.session_state.chat_history.append(response)
    
    # Display conversation history
    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.write(f"**You:** {message}")
        else:
            st.write(f"🤖 **Chatbot:** {message}")
