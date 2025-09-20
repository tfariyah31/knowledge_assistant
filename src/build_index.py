from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os

# --- Paths ---
PDF_PATH = os.path.join("data", "My_Data_File.pdf")  # update if renamed
DB_DIR = "db"

# --- Load the PDF ---
print("Loading PDF...")
loader = PyPDFLoader(PDF_PATH)
documents = loader.load()

# --- Split into chunks ---
print("Splitting text...")
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(documents)

# Add source info to each chunk
for c in chunks:
    c.metadata["source"] = PDF_PATH   # file path
    # PyPDFLoader already keeps "page" in metadata

# --- Create embeddings ---
print("Loading embedding model (first run may download files)...")
embedding_function = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# --- Store chunks in Chroma ---
print(f"Saving {len(chunks)} chunks to Chroma DB...")
db = Chroma.from_documents(
    documents=chunks,
    embedding=embedding_function,
    persist_directory=DB_DIR,
)
db.persist()

print("\nDone! Vector database stored in:", DB_DIR)



