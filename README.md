# Dashboard📊 AI-Powered Stock Dashboard

This is an interactive Streamlit dashboard that visualizes TSLA stock data using Plotly. It includes:

✅ Real-time candlestick charts
✅ Technical indicators
✅ Interactive date range filtering
✅ AI Chatbot for stock analysis

🚀 Features
Feature	Description
📈 Candlestick Chart	Visualizes daily price movement
📊 Volume Analytics	Shows trading volume trends
🤖 AI Stock Assistant	Ask questions about TSLA stock
⏱ Live Data Fetching	Fetch latest TSLA prices
💾 Local caching	Faster reloads
🏁 How to Run the Project

1️⃣ Clone or download the repository

git clone <your_repo_url>
cd e-commerce


2️⃣ Create a virtual environment

python -m venv venv
source venv/bin/activate   # Mac / Linux
venv\Scripts\activate      # Windows


3️⃣ Install dependencies

pip install -r requirements.txt


4️⃣ Run the Streamlit App

streamlit run Dashboards.py


✅ The app will open automatically in your browser
➡ http://localhost:8501/

📦 Requirements

Make sure these packages are included in requirements.txt:

streamlit
plotly
pandas
numpy
requests
yfinance
google-generativeai

🧠 Architecture

Frontend/UI → Streamlit

Charts → Plotly candlestick

LLM Assistant → Gemini API

Data Source → Yahoo Finance (yfinance)

📝 Folder Structure
📁 project-folder
 ├── Dashboards.py
 ├── requirements.txt
 ├── README.md
 ├── data/ (auto created)

❗Troubleshooting
Issue	Fix
ModuleNotFoundError: plotly	Run: pip install plotly
Deployment fails	Ensure dependencies are inside requirements.txt
AI not responding	Check Gemini API key is set correctly
📬 Contact

For any queries, feel free to ask — Happy deploying! 🚀
