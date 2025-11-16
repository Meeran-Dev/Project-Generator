# AI Project Idea Generator

A Streamlit-based web application that generates **novel, actionable project ideas** using **Google Gemini (via LangChain)** and **Tavily Search** for real-time grounded information.

## 🛠️ Installation & Setup

Follow these steps to run the project on your own machine.

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Meeran-Dev/Project-Generator.git
cd Project-Generator
```

### 2️⃣ Install Dependencies

Make sure you are using Python 3.9+.

```bash
pip install -r requirements.txt
```

### 3️⃣ Set Environment Variables

Create a .env file in the project root:

```bash
GEMINI_API_KEY = your_gemini_api_key_here
TAVILY_API_KEY = your_tavily_api_key_here
```

Where to get your keys:
Gemini API Key → https://aistudio.google.com  
Tavily API Key → https://tavily.com

### 4️⃣ Run the Streamlit App

```bash
streamlit run app.py
```