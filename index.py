import os, streamlit as st

# Uncomment to specify your OpenAI API key here (local testing only, not in production!), or add corresponding environment variable (recommended)
os.environ['OPENAI_API_KEY']= ""

from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader, LLMPredictor, PromptHelper, StorageContext, load_index_from_storage
from langchain import OpenAI

# This example uses text-davinci-003 by default; feel free to change if desired
llm_predictor = LLMPredictor(llm=OpenAI(temperature=0, model_name="text-davinci-003"))

# Configure prompt parameters and initialise helper
max_input_size = 4096
num_output = 256
max_chunk_overlap = 20

prompt_helper = PromptHelper(max_input_size, num_output, max_chunk_overlap)

# Load documents from the 'data' directory
#documents = SimpleDirectoryReader('data').load_data()
#index = GPTSimpleVectorIndex(
#    documents, llm_predictor=llm_predictor, prompt_helper=prompt_helper
#)

#Load index from JSON-files in storage folder
# rebuild storage context
storage_context = StorageContext.from_defaults(persist_dir="./storage")
# load index
index = load_index_from_storage(storage_context)
index = index.as_query_engine()


# Define a simple Streamlit app
st.title("Frag SV-Info-GPT")
query = st.text_input("Wie kann ich Ihnen helfen?", "")
query_full = 'Answer a question. Add to the response the name of the source document and the page where the response can be verified. Answer in the language of the question. The question: ' + query

if st.button("Submit"):
    response = index.query(query_full)
    st.write(response)
