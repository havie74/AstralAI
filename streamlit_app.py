import streamlit as st
from langchain_openai.chat_models import ChatOpenAI

# Show title and description.
st.title("Astral AI")
st.write(
    "Welcome to Astral AI, One of the best Lua programmer. Best part is, its free."
  )
openai_api_key = "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"
# Ask user for their OpenAI API key via `st.text_input`.
# Alternatively, you can store the API key in `./.streamlit/secrets.toml` and access it
# via `st.secrets`, see https://docs.streamlit.io/develop/concepts/connections/secrets-management

#gen text

def generate_response(input_text):
    model = ChatOpenAI(temperature=0.7,api_key=openai_api_key)
    st.info(model.invoke(input_text))


with st.form("my_form"):
    text = st.text_area(
        "Ask Astral_AI anything."
    )
    submitted = st.form_submit_button("Submit")
