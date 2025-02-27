import cohere 
import streamlit as st

#Initialize cohere client
cohere_api_key = "7Vrkkt1PwJjspHHmMUc839FxdIwbRAkrifwFxctT"
co = cohere.ClientV2(api_key=cohere_api_key)

#Streamlit UI
st.title("Text Summarization with Cohere")

st.write("This app uses Cohere's API to summarize text. Enter the text you want to summarize below:")

#text input from user
user_input = st.text_area("Enter text here:", height = 300)

if st.button("Summarize"):
    if user_input.strip():
        with st.spinner("Summarizing..."):
            try:
                #prepare the message for cohere
                message = f"Generate a concise summary of the following text\n{user_input}"

                #call cohere API
                response = co.chat(
                    model="command-r-plus", 
                    messages=[{"role": "user", "content": message}]
                )

                #display summarized text
                summary = response.message.content[0].text
                st.subheader("Summarized text:")
                st.write(summary)

            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter some text to summarize.")