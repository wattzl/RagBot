# 🤖 RAGBot

A Retrieval-Augmented Generation (RAG) assistant built in Python using local tools — no OpenAI key required (unless you want it).  
Ask your documents intelligent questions. Get answers. All local. All magic.

---

## 🚀 Features

- 🧠 Local Embeddings with HuggingFace (`all-MiniLM-L6-v2`)
- 📚 Document retrieval via ChromaDB
- 🧾 Ingest `.txt` or `.md` files from your `/docs` folder
- 🔍 Semantic search based on actual meaning
- ⚡ CLI-based chat — no fluff, just answers
- 💸 API-optional: works offline with free embeddings

---

## 📂 Project Structure


---

## 🛠️ Setup Instructions

### Step 1: Clone the Repo

```bash
git clone https://github.com/YOUR_USERNAME/ragbot.git
cd ragbot

### Step 2 : Create a virtual environment
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

### Step 3: Install Dependencies
pip install -r requirements.txt

### Step 4: Run the bot
python main.py

