import os
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

# === Load Documents ===
docs = []
doc_path = "docs"

for filename in os.listdir(doc_path):
    if filename.endswith(".txt") or filename.endswith(".md"):
        loader = TextLoader(os.path.join(doc_path, filename))
        docs.extend(loader.load())

# === Split Text into Chunks ===
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(docs)

# === Embed Locally (No OpenAI) ===
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# === Build Local Vector Store ===
db = Chroma.from_documents(chunks, embedding=embeddings)
retriever = db.as_retriever()

# === Ask Loop (No GPT) ===
while True:
    query = input("\nAsk your docbot a question (or type 'exit'): ")
    if query.lower() in ["exit", "quit"]:
        print("✌️ Peace out, local legend.")
        break

    docs = retriever.invoke(query)
    print("\n🔍 Top Matches:\n")
    for i, doc in enumerate(docs):
        print(f"[{i+1}] {doc.page_content.strip()[:500]}")
        print("-" * 50)
