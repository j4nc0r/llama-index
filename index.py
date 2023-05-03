import os, streamlit as st

# Uncomment to specify your OpenAI API key here (local testing only, not in production!), or add corresponding environment variable (recommended)
os.environ['OPENAI_API_KEY']= ""

from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader, LLMPredictor, PromptHelper, StorageContext, load_index_from_storage
from langchain import OpenAI

#Try to load existing index from JSON files
# rebuild storage context
try:
    # rebuild storage context
    storage_context = StorageContext.from_defaults(persist_dir="./storage")
    # load index
    index = load_index_from_storage(storage_context)
    index = index.as_query_engine()
except:
    # load documents from folder
    documents = SimpleDirectoryReader('./sources').load_data()
    # create index
    index = GPTVectorStoreIndex.from_documents(documents)
    #Save the index to a json-file
    index.storage_context.persist()

# Define a simple Streamlit app
st.title("Ask customized ChatGPT")
query = st.text_input("What can I do for you?", "")

if st.button("Submit"):
    response = index.query(query)
    st.write(response)
