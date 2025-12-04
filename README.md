## AI Investment Agent: Stock Comparison Tool

### **About the Project**

This project is a simple **Streamlit web application** that uses an **AI Agent** powered by **Google's Gemini** model, integrated through the **Agno framework**.

The purpose of the application is to allow a user to enter two stock tickers and then generate a **detailed investment report** that compares the two stocks based on their:
  * **Stock Prices**
  * **Analyst Recommendations**
  * **Key Fundamentals**

The AI agent retrieves the real-time financial data using the `YFinanceTools` and then synthesizes this information into a structured, easy-to-read report.


### **Requirements**

To run this project, you need:

1.  **Python**
2.  A **Gemini API Key** (required to initialize the AI agent).


### **Installation & Setup**
You will need the `streamlit`, `yfinance` and `agno` libraries.

    ```bash
    pip install -r requirements.txt
    ```

### **How to Run**

1.  **Execute the Streamlit command** from your terminal in the same directory:

    ```bash
    streamlit run investment_agent.py
    ```

2.  **Open the App:**
    The application will open in your web browser (usually at `http://localhost:8501`).

3.  **Use the Interface:**

      * Enter your **Gemini API Key**.
      * Enter the symbol for the **first stock** (e.g., `NVDA`).
      * Enter the symbol for the **second stock** (e.g., `AMD`).
      * The report will generate and appear below the inputs.
