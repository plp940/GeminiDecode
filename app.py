###Health Management APP
from dotenv import load_dotenv

load_dotenv()##load all the environtment variables
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
st.set_page_config(page_title="GeminiDecode:Multilanguage Document Extraction by Gemini Pro")

genai.configure(api_key=os.getenv("AIzaSyDWUwJHoXawbSHRexLwrCArmAdis0jNoLo"))

def get_gemini_response(input,image,prompt):
    model=genai.GenerativeModel('gemini-pro-vision')
    response=model.generate_content([input,image[0],prompt])
    return response.text

uploaded_file=st.file_uploader("choose an image of the document",type=["jpg","jpeg","png"])
image=""
if uploaded_file is not None:
    image=Image.open(uploaded_file)
    st.image(image,caption="Uploaded Image",use_column_width=True)
submit=st.button("Tel me about the document")   

input_prompt="""
You are expert in understanding invoices.
We will upload a image as invoice and you will have to answer any questions based on the uploaded invoice image.""" 

#initialize streamlit app
st.header("GeminiDecode: Multilanguage Document Extraction by Gemini Pro")
text="Utilizing Gemini Pro AI,this project effortlessly extracts vital information+ \
from diverse multilingual documents, transcending language barriers with \nprecision and + \
efficienc for enchanced  productivity and decision making."
styled_text = f"<span style='font-family:serif;'>{text}</span>"
st.markdown(styled_text,unsafe_allow_html=True)


def input_image_details(uploaded_file):
    # Process the uploaded file and return image data
    # This is a placeholder function. You need to implement the actual logic.
    return [uploaded_file]  # Replace with actual image processing logic


#if submit button is clicked
if submit:
    image_data=input_image_details(uploaded_file)
    response=get_gemini_response(input_prompt,image_data,image)
    st.subheader("The response is")
    st.write(response)
    