import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain_text_splitters import CharacterTextSplitter
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI
# from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from htmlTemplates import css, user_template, bot_template


def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()

    return text


def get_text_chunks(raw_text):
    text_spiltter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000, 
        chunk_overlap = 200,
        length_function = len
    )

    chunks = text_spiltter.split_text(raw_text)

    return chunks


def get_vectorstore(text_chunks):
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    
    return vectorstore


def get_conversation_chain(vectorstore):
    llm = ChatOpenAI()
    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )

    return conversation_chain


def handle_userinput(user_question):
    response = st.session_state.conversation({'question': user_question})
    st.session_state.chat_history = response['chat_history']

    for i, message in enumerate(st.session_state.chat_history):
        if i % 2==0:
            st.write(user_template.replace("{{MSG}}", message.content), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace("{{MSG}}", message.content), unsafe_allow_html=True)


    # st.write(response)

def main():
    load_dotenv()
    st.set_page_config(page_title="PagePal: Chat with multiple PDFs", page_icon=":books:")

    st.write(css, unsafe_allow_html=True)

    if "conversation" not in st.session_state:
        st.session_state.conversation = None

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None


    st.header("PagePal: Chat with multiple PDFs :books:")
    user_question = st.text_input("Ask a question about your documnets(PRESS RETURN):")
    if user_question:
        handle_userinput(user_question)


    st.write(user_template.replace("{{MSG}}", "Hello, Robot!!"), unsafe_allow_html=True)
    st.write(bot_template.replace("{{MSG}}", "Hello, Human! Ask me anything related to PDF files you uploaded."), unsafe_allow_html=True)

    with st.sidebar:

           # instruction
        st.write("---INSTRUCTIONS---")
        st.write("1. Upload the documets in the side bar")
        st.write("   - Click Browse")
        st.write("   - Upload Multiple Documents")
        st.write("2. Click 'Process' Button")
        st.write("3. Ask question to the bot in the main window")
        st.write("----------------------------------------------")

        st.subheader("Your documents")
        pdf_docs = st.file_uploader("Upload your PDFs here and click on 'Process'", accept_multiple_files=True)

    
        if st.button("Process"):
            with st.spinner("Processing"):
                # get pdf
                raw_text = get_pdf_text(pdf_docs)
                # st.write(raw_text)

                # get the text chunks
                text_chunks = get_text_chunks(raw_text)
                # st.write(text_chunks)

                #create vector store
                vectorstore = get_vectorstore(text_chunks)

                #create conversation chain
                # when you chnage code streamlit runs the entire code again which deletes chat history
                # using session_state, this retains chat history
                # session state also makes a varibale global
                st.session_state.conversation = get_conversation_chain(vectorstore)
        
if __name__ =='__main__':
    main()