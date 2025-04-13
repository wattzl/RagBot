# 🤖 RAGBot

A Retrieval-Augmented Generation (RAG) assistant built in Python using local tools — no OpenAI key required (unless you want it).  
Ask your documents intelligent questions. Get answers. All local. All magic.

---

## 🚀 Features

- 🧠 Local Embeddings with HuggingFace (`all-MiniLM-L6-v2`)
- 📋 Document retrieval via ChromaDB
- 📄 Ingest `.txt` or `.md` files from your `/docs` folder
- 🔍 Semantic search based on actual meaning
- ⚡ CLI-based or Streamlit UI — no fluff, just answers
- 🌱 API-optional: works offline with free embeddings

---

## 📂 Project Structure

```
ragbot/
├── main.py               # CLI version of RAG bot
├── app.py                # Streamlit UI version
├── scrape_and_save.py    # Optional web scraper
├── docs/                 # Your documents go here
├── .env.example          # API key placeholder
├── .gitignore            # Keep secrets + venv out of Git
├── requirements.txt      # Clean dependency list
└── README.md             # This file!
```

---

## 🛠️ Setup Instructions

### Step 1: Clone the Repo

```bash
git clone https://github.com/YOUR_USERNAME/ragbot.git
cd ragbot
```

### Step 2: Create a virtual environment

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Add Your Documents

Put `.txt` or `.md` files inside the `/docs` folder. For example:

```
docs/
├── ai-policy.txt
├── team-notes.md
```

### Step 5A: Run the CLI Bot

```bash
python main.py
```

### Step 5B: Run the Streamlit UI

```bash
streamlit run app.py
```

Then open: [http://localhost:8501](http://localhost:8501)

---

## 💬 Sample Query

```
Ask your docbot a question (or type 'exit'): What does the AI policy say about data retention?
```

OR via Streamlit:

> Ask your question → View the most relevant document chunks instantly.

---

## 📦 Environment Variables

Only needed if you want to enable OpenAI-based features:

```env
OPENAI_API_KEY=your-key-here
```

Place that in a `.env` file. Use `.env.example` as a reference.

---

## 🧠 Roadmap

- [ ] Add PDF ingestion
- [ ] Summarization mode
- [ ] Multi-user sessions
- [ ] Streamlit dark/light mode toggle
- [ ] Optional OpenAI fallback

---

## 📜 License

MIT — Fork it, build on it, deploy it, monetize it, teach it to love.

---

## 👤 Author

Made by [YOUR NAME] (probably not a large language model).  
Inspired by the RAG community, annoyed by LangChain updates, held together by caffeine and dreams.

---

## ⭐️ Star This Repo

If it helped you, inspired you, or didn’t break your machine — smash that ⭐️.

