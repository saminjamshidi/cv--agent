# 💬 CV Chatbot Agent with Ollama and LangChain

This project implements a **Retrieval-Augmented Generation (RAG)** agent that acts as an **AI chatbot for your CV**.  
You can ask it questions in natural language, and it will answer based on the contents of your **PDF resume**, using **locally-run language models** via [Ollama](https://ollama.ai).

---

## 🧠 How It Works

The system consists of two main components:

### `vector.py` — *Ingestion Script*
- Reads your `cv.pdf` file.
- Splits the text into manageable chunks.
- Uses an **embedding model** to convert chunks into numerical vectors.
- Stores these vectors in a local **Chroma vector database**.  
  *(Run this only once, or when you update your CV.)*

### `my_agent.py` — *Chatbot Agent*
When you ask a question:
1. The agent embeds your question into a vector.
2. It searches the Chroma database for similar text chunks.
3. It sends those chunks as **context** to a local LLM.
4. The LLM generates an answer **based only on your CV content**.

This **RAG** approach enables the model to provide accurate, CV-specific answers without retraining.

---

## ⚙️ Technology Stack

| Component | Description |
|------------|-------------|
| **LLM Serving** | [Ollama](https://ollama.ai) |
| **Framework** | [LangChain](https://www.langchain.com) |
| **Vector Database** | [ChromaDB](https://www.trychroma.com) |
| **LLM Model** | `llama3.2` |
| **Embedding Model** | `mxbai-embed-large` |

---

## 🚀 Getting Started

### 1. Prerequisites
Make sure **Ollama** is installed and running.  
You can download it from the [official Ollama website](https://ollama.ai).

### 2. Install Ollama Models
Open a terminal and pull the required models:

```bash
ollama pull llama3.2
ollama pull mxbai-embed-large

```

### 3. Clone & Set Up the Project

```bash
git clone <your-repo-url>
cd <your-repo-name>
pip install -r requirements.txt
```

---

### 4. Add Your CV

- Place your CV in the root directory.
- Rename it to `cv.pdf`.
- (Optional) If you use a different name, update the `PDF_PATH` variable in `vector.py`.

---

### 5. Create the Vector Database

Run the ingestion script to process your CV and create the Chroma database:

```bash
python vector.py
```

> A folder named `cv_chroma_db` will be created. This only needs to be done once.

---

### 6. Run the Chatbot Agent

```bash
python my_agent.py
```

Type your questions and interact with the chatbot.  
To quit, type `q` and press **Enter**.

---

## 🔧 Configuration

You can adjust the following variables at the top of both `vector.py` and `my_agent.py`:

| Variable            | Description                                           | Default              |
|----------------------|--------------------------------------------------------|------------------------|
| `PDF_PATH`           | Path to your CV file                                   | `./cv.pdf`            |
| `DB_LOCATION`        | Directory where the Chroma database is stored          | `./cv_chroma_db`      |
| `EMBEDDING_MODEL`    | Ollama model used for creating text embeddings         | `mxbai-embed-large`   |
| `LLM_MODEL`          | Ollama model used for generating answers              | `llama3.2`            |

---

## 📝 Summary

- **Ingest your CV once** using `vector.py`.
- **Run the chatbot** using `my_agent.py`.
- **Ask questions** and receive responses directly from your CV content.
- Fully local solution — no data leaves your machine.

---

## 📚 References

- [Ollama](https://ollama.com/)
- [LangChain](https://www.langchain.com/)
- [ChromaDB](https://www.trychroma.com/)
