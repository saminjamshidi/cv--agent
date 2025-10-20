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
