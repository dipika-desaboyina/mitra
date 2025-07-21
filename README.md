# 🧘🏽‍♀️ mITRa: Your Emotionally-Intelligent Tax Helper for India

## 🤖 What is mITRa?

**mITRa** is a smart, sensitive assistant built to help Indian taxpayers make sense of taxation — without drowning in jargon, government links, or frustration.

Stuck on which ITR form to fill?  
Wondering why your refund is delayed?  
Freelancer unsure where to start?  
Feeling overwhelmed?

Just ask mITRa — it reads official tax documentation, detects your emotional tone (confused, annoyed, calm), and gives human-like answers, fine-tuned for exactly where you are mentally. 🙃🙂😠

---

## 🔧 What This Notebook Does

This single notebook walks you through the full mITRa pipeline:

1. **Data Collection**: Scrapes useful tax guidance from India’s official IT site and ClearTax
2. **Cleaning & Formatting**: Extracts meaningful sections, preserves structure + screenshots
3. **Indexing**: Chunks & embeds documents for semantic search (LlamaIndex + Weaviate)
4. **Sentiment Detection**: Uses a lightweight RoBERTa model to “read the room”
5. **Query Understanding**: Matches answers based on your tone + intent
6. **Response Generation**: Uses Mistral 7B (via Ollama) to reply helpfully & empathetically
7. **Demo Interface**: A simple Streamlit window to chat with mITRa in real-time

All code is designed to run locally or for free in the cloud 💻☁️

---

## 🎯 Features

- 🧾 Retrieval-Augmented Generation (RAG) chatbot, fine-tuned for Indian tax FAQs  
- 🧠 Sentiment-adjusted answer generation (calm, supportive, to-the-point)  
- 🔍 Document-grounded — draws from Income Tax portal & ClearTax blog  
- 🧘🏽 Persona-aware — supports salaried users, freelancers, NRIs, first-time filers & more  
- 🛠️ Fully local (runs on CPU via Ollama)
- 💬 Tested via CLI or Streamlit interface

---

## ✅ In Scope

- Tax questions around ITR forms, refunds, PAN/Aadhaar, deadlines, etc.
- Built completely using open-source, free-tier tools
- Runs locally (CPU) or can be deployed to HuggingFace Spaces
- Document scraping & retrieval with full Markdown + screenshot retrieval
- Multiple user personas supported

---

## 🚫 Not in Scope

- No real-time integration with the Income Tax site
- Doesn’t collect personal info (no PAN, Aadhaar, etc.)
- Not a certified tax filing app
- Built in English only (no regional languages — yet!)
- No mobile app (simple CLI/Streamlit demo only)

---

## ⚙️ Tech Stack

| Piece                | Tool Used                         |
|---------------------|-----------------------------------|
| 🧠 LLM               | Mistral 7B via Ollama (local)     |
| 📚 Retrieval Engine | LlamaIndex + Weaviate             |
| 🔍 Searchable Index | Preprocessed from Income Tax docs |
| 🤗 Sentiment Model  | twitter-roberta-base-sentiment    |
| 💬 UI / Chat Demo   | Streamlit                         |
| 🔧 Backend (optional)| FastAPI                          |

---

## 📁 Notebook Sections

Each section of this notebook corresponds to one stage of the mITRa pipeline:

1. 📘 Setup & Environment
2. 🔍 Scraping & Preprocessing Tax Docs
3. 📊 Index Construction (Chunking + Embedding)
4. 🧠 Sentiment Detection Engine
5. 💬 Answer Generation via LLM
6. 🎭 User Persona Testing
7. 🖥️ Chat Interface Demo (Streamlit/CLI)
8. ✅ Wrap-Up, Thoughts & Future Work

---

## 🗓️ Project Updates

| Date       | Update                                   | Author               |
|------------|------------------------------------------|----------------------|
| 2025-07-16 | Initial design & project setup           | Dipika Desaboyina    |
| 2025-07-17 | Scraper and query modeling implemented   | Dipika Desaboyina    |

---

## 📚 References

- [Income Tax Portal](https://www.incometax.gov.in/iec/foportal/)
- [ClearTax Blog](https://cleartax.in)
- [LangChain](https://www.langchain.com/)
- [LlamaIndex](https://llamaindex.ai)
- [Mistral via Ollama](https://ollama.com)
- [Weaviate Vector DB](https://weaviate.io)
- [HuggingFace Transformers](https://huggingface.co)

---

> Let’s make tax time a little less scary, one empathetic answer at a time. 👂💸📥

