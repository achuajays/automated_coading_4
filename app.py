
import streamlit as st
import yaml

# Load configuration from config.yaml
with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)

st.title(config['title'])
st.markdown(config['description'])

# Text input from user
user_text = st.text_area(config['input_label'], config['input_placeholder'])

# Configuration for text formatting
format_text = config['format_text']

# Button to display formatted text
if st.button(config['button_label']):
    if format_text:
        formatted_text = user_text.upper()  # Example formatting: convert to uppercase
    else:
        formatted_text = user_text
    
    st.markdown(f"**{config['output_label']}:** {formatted_text}")
