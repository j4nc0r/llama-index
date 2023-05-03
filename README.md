# 🦙 llama-ui-lite 🖥️

A simple Streamlit web app for using [LlamaIndex](https://github.com/jerryjliu/llama_index), an interface to connect LLM’s with external data.
Forked from alphasecio

## 🚀 Context

- LLamaIndex lets you create a custom ChatGPT version especially for your specific data & documents 
- It doesn't provide an user interface so we create one using Steamlit
- The goal is to make it as easy as possible to create a custom ChatGPT clone and deploy it locally or on the web with a simply UI


## 💻 Installation

Clone the repo or download the files to zip 
```
git clone https://github.com/j4nc0r/llama-ui-lite.git
```
Install the required packages using PIP
```
pip install -r requirements.txt
```
(optional) If you already have created a Llama index somewhere else safe it the to JSON-files and copy them from your `./storage` folder to `./storage` in this repo.
To create JSON files from index use:
```
index.storage_context.persist()
```
### Add your documents 📄
If you don't have index files just copy your documents you want ChatGPT to learn from in the folder `./data`<br><br>
**NOTE!** Creating an index from documents can consum a lot of tokens from your API so think carefully what you out in that folder. The program automatically saves your index to JSON files in the `./storage` folder so your only charged once for the training. 

## 🔧 Configuration 
### OpenAI API Key
(optional) If you don't have an OpenAI API Key go to [OpenAI](https://platform.openai.com/account/api-keys) and create one. <br><br>

Open `index.py` and insert your API secret key
```
os.environ['OPENAI_API_KEY']= "insert-your-key-here"
```
## 🏠 Test & Deploy locally

1. Run `index.py`
2. Deploy the Streamlit app in terminal:
```
streamlit run index.py
```
A browser should open and you're ready to chat with your personal ChatGPT clone

## 🚆 Deploy to the web with Railway


To deploy on [Railway](https://railway.app/?referralCode=01QhWs), click the button below.

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template/GpZ0J4?referralCode=01QhWs)


