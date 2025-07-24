# ✈️ Travel Assistant AI Agent

A lightweight AI-powered travel assistant built with **Streamlit** and **Gemini** using the `agno` agent framework. It answers travel-related queries using real-time search and reasoning tools.

---

## 🚀 Features

- 🌍 Natural language query interface (e.g., *"How to travel from Munich to Berlin?"*)
- 🔎 Real-time web search via **DuckDuckGo**
- 🤖 Powered by Google's **Gemini AI** (`google-generativeai`)
- 📊 Structured output with reasoning steps
- 🖼️ Built with **Streamlit** for a clean web UI

---

## 🛠️ Tech Stack

- Python 🐍
- Streamlit
- Google Generative AI (Gemini)
- Agno AI Agent Framework
- DuckDuckGo Search (via `ddgs`)
- Pydantic

---

## 🧪 How to Run

### 1. Clone the repo
```bash
git clone https://github.com/your-username/travel-ai-agent.git
cd travel-ai-agent
```

## 🛠️ Install Dependencies

To get started, install the required dependencies:

### Option 1: Using `requirements.txt`

```bash
pip install -r requirements.txt
```
## 🔐 Gemini API Setup

To use the Gemini model, you'll need to set up the API key:

1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey).
2. Click on **Get API Key** and copy your key.
3. Create a `.env` file in your project directory and add:

```env
GOOGLE_API_KEY=your_api_key_here
