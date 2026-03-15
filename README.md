# 🤖 AI Chatbot using RAG + Groq + Streamlit

An intelligent AI chatbot built using **Retrieval-Augmented Generation (RAG)** that combines **document retrieval** with **Large Language Models (LLMs)** to generate accurate and contextual responses.

The chatbot is deployed using **Streamlit Cloud** and uses **Groq LLM (LLaMA models)** for fast inference.

---

# 🚀 Features

- 💬 Conversational AI interface
- 📄 Document-based knowledge retrieval
- 🔎 Retrieval-Augmented Generation (RAG)
- ⚡ Fast inference using Groq LLM
- 🌐 Optional web search integration
- 🧩 Modular and scalable architecture
- ☁️ Streamlit Cloud deployment

---

# 🏗️ Project Architecture

```
chatbot/
│
├── app.py                    # Streamlit UI application
│
├── config/
│   └── config.py             # Project configuration
│
├── data/
│   └── documents.txt         # Knowledge base documents
│
├── models/
│   ├── embeddings.py         # Embedding model loader
│   └── llm.py                # Groq LLM initialization
│
├── utils/
│   ├── rag_utils.py          # RAG retrieval pipeline
│   ├── response_mode.py      # Prompt engineering
│   └── web_search.py         # Web search integration
│
├── requirements.txt
└── README.md
```

---

# 🧠 How It Works

### 1️⃣ Document Processing
Documents are loaded and split into smaller chunks for efficient retrieval.

### 2️⃣ Embedding Generation
Each chunk is converted into vector embeddings using an embedding model.

### 3️⃣ Vector Storage
Embeddings are stored in a **FAISS vector database**.

### 4️⃣ Query Processing
When a user asks a question:

1. The query is embedded
2. Similar document chunks are retrieved from FAISS
3. Context is sent to the LLM

### 5️⃣ Response Generation
The **Groq LLM** generates a contextual response using the retrieved information.

---

# ⚙️ Tech Stack

| Technology | Purpose |
|------------|--------|
| Python | Core programming |
| Streamlit | Web interface |
| LangChain | LLM orchestration |
| FAISS | Vector database |
| Groq API | LLM inference |
| GitHub | Version control |
| Streamlit Cloud | Deployment |

---

# 📦 Installation

Clone the repository

```bash
git clone https://github.com/your-username/chatbot.git
cd chatbot
```

Create virtual environment

```bash
python -m venv venv
```

Activate environment

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file

```
GROQ_API_KEY=your_groq_api_key
```

Or for **Streamlit Cloud**, add in **Secrets**:

```
GROQ_API_KEY = "your_groq_api_key"
```

---

# ▶️ Run the Application

```bash
streamlit run app.py
```

App will run at:

```
http://localhost:8501
```

---

# ☁️ Deployment (Streamlit Cloud)

1. Push code to GitHub
2. Go to Streamlit Cloud
3. Deploy using repository
4. Add **Secrets**

```
GROQ_API_KEY = "your_groq_api_key"
```

---

# 🧪 Example Queries

```
What is Retrieval-Augmented Generation?
Explain the document content
Summarize the uploaded knowledge base
```

---

# 🧩 Future Improvements

- 📂 Multi-document upload
- 🧠 Conversation memory
- 🎤 Voice input support
- 📊 Analytics dashboard
- 🔗 Integration with external APIs

---

# 👨‍💻 Author

**Harshavardhan Korlepara**

AI Engineer | Machine Learning | LLM Applications

GitHub:
https://github.com/Harshavardhan0909

---

# 📜 License

This project is licensed under the MIT License.

---

⭐ If you like this project, consider giving it a star!
