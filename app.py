#from dotenv import load_dotenv
import streamlit as st 

def main():
    #load_dotenv()
    st.set_page_config(page_title="Ask your PDF")
    st.header("Ask your PDF 💬")
    
    # upload file
    pdf = st.file_uploader("Upload your PDF", type="pdf")
    print("Hello World!")

if __name__ == '__main__':
    main()
