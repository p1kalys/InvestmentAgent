import streamlit as st
from agno.agent import Agent
from agno.run.agent import RunOutput
from agno.models.google import Gemini 
from agno.tools.yfinance import YFinanceTools

st.title("AI Investment Agent")
st.caption("This app allows you to compare the performance of two stocks and generate detailed reports.")

gemini_api_key = st.text_input("Gemini API Key", type="password")

if gemini_api_key:
    assistant = Agent(
        model=Gemini(id="gemini-2.5-flash", api_key=gemini_api_key),
        tools=[YFinanceTools()],
        debug_mode=True,
        description="You are an investment analyst that researches stock prices, analyst recommendations, and stock fundamentals.",
        instructions=["Format your response using markdown and use tables to display data where possible."],
        )
    col1, col2 = st.columns(2)
    with col1:
        stock1 = st.text_input("Enter first stock symbol (e.g. NVDA)")
    with col2:
        stock2 = st.text_input("Enter second stock symbol (e.g. AMD)")
    
    if stock1 and stock2:
        with st.spinner(f"Analyzing {stock1} and {stock2}..."):
            query = f"Compare both the stocks - {stock1} and {stock2} and make a detailed report for an investment trying to invest and compare these stocks"
            response: RunOutput = assistant.run(query, stream=False)
            st.markdown(response.content)