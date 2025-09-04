import pandas as pd
import re
from textblob import TextBlob
import streamlit as st
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/Sample_Support_Emails_Dataset.csv")

# --- Utility Functions ---
def get_sentiment(text):
    blob = TextBlob(str(text))
    polarity = blob.sentiment.polarity
    if polarity > 0.1:
        return "Positive"
    elif polarity < -0.1:
        return "Negative"
    else:
        return "Neutral"

def get_priority(text):
    urgent_keywords = ["urgent", "immediately", "asap", "critical", "cannot access"]
    text_lower = str(text).lower()
    return "Urgent" if any(word in text_lower for word in urgent_keywords) else "Not Urgent"

def extract_info(text):
    text = str(text)
    phones = re.findall(r"\b\d{10}\b", text)
    emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text)
    return {"phones": phones, "emails": emails}

def generate_response(subject, body, sentiment, priority):
    if sentiment == "Negative" or priority == "Urgent":
        return f"Dear Customer,\n\nWe understand your concern regarding '{subject}'. Our team is already working to resolve this urgently. Thank you for your patience.\n\nBest Regards,\nSupport Team"
    else:
        return f"Dear Customer,\n\nThank you for reaching out regarding '{subject}'. We have received your request and will get back shortly.\n\nBest Regards,\nSupport Team"

# --- Processing ---
df["Sentiment"] = df["Body"].apply(get_sentiment)
df["Priority"] = df["Body"].apply(get_priority)
df["Extracted Info"] = df["Body"].apply(extract_info)
df["AI Response"] = df.apply(lambda x: generate_response(x["Subject"], x["Body"], x["Sentiment"], x["Priority"]), axis=1)

# --- Streamlit UI ---
st.set_page_config(page_title="AI Support Email Assistant", layout="wide")
st.title("📧 AI-Powered Communication Assistant")

st.subheader("📊 Email Analytics")
col1, col2, col3 = st.columns(3)
col1.metric("Total Emails", len(df))
col2.metric("Urgent Emails", (df["Priority"]=="Urgent").sum())
col3.metric("Negative Sentiment", (df["Sentiment"]=="Negative").sum())

# Pie chart
fig, ax = plt.subplots()
df["Priority"].value_counts().plot(kind="pie", autopct="%1.1f%%", ax=ax)
ax.set_ylabel("")
st.pyplot(fig)

st.subheader("📋 Support Emails Dashboard")
for i, row in df.iterrows():
    with st.expander(f"📌 {row['Subject']} | {row['Priority']} | {row['Sentiment']}"):
        st.write(f"**From:** {row['Sender']}")
        st.write(f"**Date:** {row['Date']}")
        st.write(f"**Body:** {row['Body']}")
        st.write(f"**Extracted Info:** {row['Extracted Info']}")
        st.write("**AI Draft Response:**")
        st.code(row["AI Response"], language="markdown")
