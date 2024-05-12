import streamlit as st



def main():
    st.set_page_config(page_title="PagePal:Chat with multiple PDFs", page_icon=":books:")

    st.header("PagePal:Chat with multiple PDFs :books:")
    st.text_input("Ask a question about your documents:")

if __name__ =='__main__':
    main()