# AI Support Email Assistant

AI-Powered Communication Assistant to help organizations manage customer support emails efficiently.  

This project processes incoming support-related emails, categorizes them, and generates draft responses automatically. The goal is to reduce manual effort, improve response quality, and enhance customer satisfaction.

## 🚀 Features
- **Email Filtering** – Detects support-related emails (support, query, request, help).
- **Sentiment Analysis** – Classifies emails as Positive, Negative, or Neutral.
- **Urgency Detection** – Flags urgent emails using keywords like “immediately,” “asap,” or “critical.”
- **Information Extraction** – Pulls contact details (emails, phone numbers) and customer requests from the email body.
- **AI Response Generation** – Creates professional, empathetic draft replies that can be reviewed before sending.
- **Dashboard** – Interactive Streamlit dashboard to view emails, analytics, and draft responses.

## 🛠 Tech Stack
- **Backend**: Python, Pandas, Regex, TextBlob  
- **Frontend**: Streamlit (dashboard)  
- **Visualization**: Matplotlib  

## 📊 Impact
- Reduces manual workload of customer support teams  
- Improves response time and prioritization of critical queries  
- Ensures professional, empathetic communication with customers  

## ▶️ How to Run
```bash
pip install -r requirements.txt
streamlit run src/app.py
```
