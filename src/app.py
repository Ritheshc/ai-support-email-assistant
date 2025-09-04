from flask import Flask, render_template_string
import pandas as pd
from textblob import TextBlob
import re

app = Flask(__name__)

# Load dataset
df = pd.read_csv("data/Sample_Support_Emails_Dataset.csv")

# --- Detect correct column for email text ---
text_col = None
for col in df.columns:
    if col.lower() in ["body", "message", "email text", "content", "text"]:
        text_col = col
        break

if text_col is None:
    raise ValueError("No valid text column found in CSV (expected: Body, Message, or Email Text).")

# --- Functions ---
def get_sentiment(text):
    try:
        return TextBlob(str(text)).sentiment.polarity
    except:
        return 0

def get_priority(text):
    urgent_keywords = ["immediately", "urgent", "critical", "asap", "cannot access", "important"]
    text_lower = str(text).lower()
    return "Urgent" if any(word in text_lower for word in urgent_keywords) else "Not Urgent"

def extract_contact(text):
    text = str(text)
    phone = re.findall(r"\b\d{10}\b", text)  # crude phone detection
    email = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text)
    return {"phone": phone, "email": email}

# --- Process dataframe ---
df["Sentiment"] = df[text_col].apply(get_sentiment)
df["Priority"] = df[text_col].apply(get_priority)
df["Contacts"] = df[text_col].apply(extract_contact)

# --- Dashboard Template ---
TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>AI Support Email Assistant</title>
    <style>
        body { font-family: Arial, sans-serif; padding: 20px; background: #f5f5f5; }
        h1 { color: #333; }
        table { width: 100%; border-collapse: collapse; background: white; margin-top: 20px; }
        th, td { padding: 10px; border: 1px solid #ddd; text-align: left; }
        th { background: #007bff; color: white; }
        tr:nth-child(even) { background: #f9f9f9; }
    </style>
</head>
<body>
    <h1>📧 AI-Powered Support Email Assistant</h1>
    <p>Showing filtered support emails with sentiment, priority, and contact extraction.</p>
    <table>
        <tr>
            <th>Sender</th>
            <th>Subject</th>
            <th>{{text_col}}</th>
            <th>Sentiment</th>
            <th>Priority</th>
            <th>Contacts</th>
        </tr>
        {% for _, row in data.iterrows() %}
        <tr>
            <td>{{row.get("Sender", "N/A")}}</td>
            <td>{{row.get("Subject", "N/A")}}</td>
            <td>{{row[text_col][:100]}}...</td>
            <td>{{"Positive" if row["Sentiment"] > 0 else ("Negative" if row["Sentiment"] < 0 else "Neutral")}}</td>
            <td>{{row["Priority"]}}</td>
            <td>{{row["Contacts"]}}</td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(TEMPLATE, data=df, text_col=text_col)

if __name__ == "__main__":
    app.run(debug=True)
