import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from langchain_tavily import TavilySearch
import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_KEY = os.getenv("GEMINI_API_KEY")
TAVILY_KEY = os.getenv("TAVILY_API_KEY")

st.set_page_config(page_title="AI Project Generator", layout="wide")
st.title("🚀 AI-Powered Project Idea Generator")
st.write("Enter any industry or technology to generate 3 creative, grounded project ideas.")

topic = st.text_input("**Enter topic / industry:**", "3D Visualization")

PROMPT = """
You are a highly creative and well-informed project generator. Your task is to provide three novel, actionable project ideas based on the user's input industry or technology.

For each idea:
1. Provide a short, catchy Title.
2. Give a brief Concept Summary.
3. List 3 key features (must be innovative).

Structure your entire response using clear markdown headings (###) for each idea, followed by bullet points for the features. Since you are using Google Search Grounding, ensure the ideas are based on current market needs, technologies, or trends.
"""

tool = TavilySearch(
    max_results=5,
    api_key=TAVILY_KEY
)

llm = ChatGoogleGenerativeAI(
    google_api_key=GEMINI_KEY,
    temperature=0,
    model="gemini-2.5-flash"
)

agent = create_agent(
    tools=[tool],
    model=llm
)

if st.button("Generate Project Ideas"):
    with st.spinner("Generating ideas..."):
        full_prompt = f"{PROMPT}\n\nUSER TOPIC: {topic}"
        response = agent.invoke({"messages": ["user", full_prompt]})

        final_output = response["messages"][-1].content[0]["text"]
        st.markdown(final_output)
