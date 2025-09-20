# Knowledge Assistant – An AI-powered tool that delivers instant, context-specific answers by searching across your chosen documents.

A **Retrieval-Augmented Generation (RAG)** demo that lets you ask natural-language questions about your own PDF documents.  
It uses:

- [LangChain](https://www.langchain.com/) for embeddings + retrieval
- [Chroma](https://www.trychroma.com/) as a local vector store
- [Mistral-7B Instruct (GGUF)](https://huggingface.co/TheBloke/Mistral-7B-Instruct-GGUF) running locally via [llama.cpp](https://github.com/ggerganov/llama.cpp)


## Features
- Index any PDF and store semantic chunks locally
- Query the content using a chat-style interface
- Runs fully offline (after the model is downloaded)
- Returns answers with **page numbers** and exact source text


## Project Structure
```
knowledge_assistant/
 ├── data/ # Your PDF files
 │ └── My_Data_File.pdf
 ├── db/ # Chroma vector database (auto-generated)
 ├── llm_model/
 │ └── mistral/ # Mistral GGUF model file
 ├── src/
 │ ├── build_index.py # Parse + chunk + embed PDF
 │ ├── rag_chat.py # Interactive Q&A with sources
 │ └── query.py # (optional) simple query script
 └── README.md


```

## Setup

1️⃣ **Clone the repo & create a venv**

```bash
git clone https://github.com/tfariyah31/knowledge_assistant.git
cd knowledge_assistant
python3 -m venv .venv
source .venv/bin/activate
```
2️⃣ Install dependencies
```
pip install -r requirements.txt
```

3️⃣ Download Mistral model
Get mistral-7b-instruct.Q4_K_M.gguf from Hugging Face
Place it under: llm_model/mistral/

4️⃣ Add your PDF
Put your file in data/ (e.g. data/My_Data_File.pdf).


## Usage
1. Build the index
```
python src/build_index.py
```
Splits the PDF into chunks, embeds them, and saves to db/.

2. Start the chat
```
python src/rag_chat.py
```
Example:
```
RAG chat is ready! Type your question (or 'exit').

You: What is the main purpose of this document?
Assistant: ...
Sources:
- page 3 | data/My_Data_File.pdf
```

## Configuration
- Model path – set in rag_chat.py (MODEL_PATH).
- Chunk size / overlap – edit in build_index.py.
- Top-k retrieval – change k in similarity_search.


## Author
👤 Tasnim Fariyah
🔗 [Github](https://github.com/tfariyah31)
🔗 [LinkedIn](https://www.linkedin.com/in/tasnim-fariyah/)



