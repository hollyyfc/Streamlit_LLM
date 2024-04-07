import streamlit as st
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Initialize the model and tokenizer
model_name = 'gpt2'
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

st.set_page_config(page_title="AI Story Completer", page_icon="📖", layout="wide")

# Custom CSS for Morandi color aesthetics, including the site background color
st.markdown("""
<style>
    /* Main page styling */
    .streamlit-container {
        max-width: 800px;
        margin: auto;
    }
    header {visibility: hidden;}
    footer {visibility: hidden;}
    .block-container {
        padding-top: 2rem;
        padding-bottom: 5rem;
        background-color: #f5f0eb; /* Morandi-style background color for content area */
    }
    /* Input and button styling */
    .stTextInput>div>div>input, .stTextArea>div>div>textarea {
        font-family: 'Arial';
        font-size: 16px;
        color: #6e675f; /* Morandi-style font color */
        background-color: #f0ead2; /* Morandi-style background color */
    }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        border: 1px solid #a29b91; /* Morandi-style border color */
        background-color: #a29b91; /* Morandi-style button color */
        color: white;
        padding: 14px 20px;
        margin: 8px 0;
        cursor: pointer;
    }
    .stButton>button:hover {
        background-color: #b8a9a1 !important; /* Morandi-style hover color */
    }
    /* Global page background color */
    body {
        font-family: 'Arial';
        background-color: #f5f0eb; /* Morandi-style background color for the entire page */
    }
</style>
""", unsafe_allow_html=True)

st.title('AI Storyteller ✨')

# User input for the story start
story_start = st.text_area("Start a story, and the AI will continue the magic:", height=150)

# Generate story continuation button
if st.button('Continue Story'):
    if story_start:
        # Encode the story start with attention mask
        encoded_input = tokenizer.encode_plus(story_start, return_tensors='pt', add_special_tokens=True)
        input_ids = encoded_input['input_ids']
        attention_mask = encoded_input['attention_mask']
        
        # Generate a continuation of the story
        max_length = 150  # Adjusted for a longer continuation
        story_continuation_ids = model.generate(input_ids, attention_mask=attention_mask, max_length=max_length, num_beams=5, no_repeat_ngram_size=2, early_stopping=True)
        story_continuation = tokenizer.decode(story_continuation_ids[0], skip_special_tokens=True)
        
        st.write("### Story Continuation:")
        st.write(story_continuation)
    else:
        st.write("Please start a story for the AI to continue.")
