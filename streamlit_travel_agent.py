# -*- coding: utf-8 -*-
"""
Created on Thu Jul 24 14:00:22 2025

@author: rampr
"""

from agno.agent import Agent
from agno.models.google import Gemini # adjust based on your setup
from agno.tools.reasoning import ReasoningTools
#from agno.tools.yfinance import YFinanceTools
from agno.tools.duckduckgo import DuckDuckGoTools

import streamlit as st

#from agno.models.groq import Groq



import warnings
warnings.filterwarnings("ignore", category=RuntimeWarning, message=".*duckduckgo_search.*")

from dotenv import load_dotenv

load_dotenv()



# Streamlit UI
st.set_page_config(page_title="Travel Assistant", page_icon="✈️")

# Initialize the agent once
@st.cache_resource
def load_agent():
    return Agent(
        model=Gemini(id="gemini-2.0-flash"),
       # model=Groq(id="llama-3.3-70b-versatile"),
        tools=[
            ReasoningTools(add_instructions=True),
            DuckDuckGoTools(),
        ],
        instructions=[
            "You are a helpful travel assistant.",
            "Use DuckDuckGo to search for current travel information.",
            "Display results clearly using markdown or tables.",
            
        ],
        markdown=True
    )

# Load the agent
agent = load_agent()

# UI Elements
st.title("🧳 AI Travel Assistant")
st.markdown("Ask travel-related questions, and the agent will fetch up-to-date answers for you.")

# Input field
user_query = st.text_input(
    "Where do you want to go?", 
    placeholder="e.g., How to travel from Munich to Berlin?"
)

# Search button and response handling
if st.button("Search"):
    if user_query.strip():
        with st.spinner("Finding your answer..."):
            try:
                response = agent.run(user_query)
                if hasattr(response, 'contentstr'):
                    text = response.contentstr
                elif hasattr(response, 'content'):
                    text = response.content
                elif isinstance(response, dict) and 'content' in response:
                    text = response['content']
                else:
    # fallback: just convert to string
                    text = str(response)


                print("response",response)
                st.write(text)
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
                st.info("Please try rephrasing your question or check your internet connection.")
    else:
        st.warning("Please enter a travel question.")

# Optional: Add some example queries
with st.expander("💡 Example Questions"):
    st.markdown("""
    - How to travel from Munich to Berlin?
    - Best time to visit Japan?
    - Visa requirements for US citizens traveling to Europe?
    - Flight prices from New York to London?
    - Top attractions in Paris?
    - Budget travel tips for Southeast Asia?
    """)
